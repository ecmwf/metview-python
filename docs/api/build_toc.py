#
# (C) Copyright 2017- ECMWF.
#
# This software is licensed under the terms of the Apache Licence Version 2.0
# which can be obtained at http://www.apache.org/licenses/LICENSE-2.0.
#
# In applying this licence, ECMWF does not waive the privileges and immunities
# granted to it by virtue of its status as an intergovernmental organisation
# nor does it submit to any jurisdiction.


import glob
import logging
import os
from pathlib import Path
import sys

import yaml

logging.basicConfig(level=logging.INFO, format="%(levelname)s %(message)s")
LOG = logging.getLogger(__name__)

API_DIR = os.path.abspath(os.path.dirname(__file__))
ROOT_DIR = os.path.dirname(API_DIR)
GEN_DIR = os.path.join(ROOT_DIR, "gen_files")
TOC_DIR = os.path.join(GEN_DIR, "toc")
ICON_DIR = os.path.join(GEN_DIR, "icon_functions")
STATIC_DIR = os.path.join(ROOT_DIR, "_static")
Path(TOC_DIR).mkdir(parents=True, exist_ok=True)


def format_red(t):
    return "\033[91m {}\033[00m".format(t)


def format_green(t):
    return "\033[92m {}\033[00m".format(t)


def log_generated(path):
    LOG.info("  {} [{}]".format(path, format_green("generated")))


dtypes = {
    "fieldsets": ":class:`Fieldset`",
    "fieldset": ":class:`Fieldset`",
    "geopoints": ":class:`Geopoints`",
    "netcdf": ":class:`NetCdf`",
    "bufr": ":class:`Bufr`",
    "odb": ":class:`Odb`",
    "array": "ndarray",
    "number": "number",
}

GROUPS = {}
PAGES = {}

class TocPage:
    def __init__(self, name, item):
        self.name = name
        self.title = item.get("title", "")
        self.desc = item.get("desc", "")
        self.rst = os.path.join(TOC_DIR, name + ".rst")
        self.groups = []
        for gn in item.get("gr", []):
            gr = GROUPS.get(gn, None)
            if gr:
                self.groups.append(gr)


class TocGroup:
    def __init__(self, name, title):
        self.name = name
        self.title = title
        self.functions = []

    def sort(self):
        self.functions.sort(key=lambda x: x.name)


class DocFunction:
    def __init__(self, name, item):
        self.name = name
        self.dtype = item.get("type", "")
        self.desc = item.get("desc", "???")
        self.pix = item.get("pix", "")
        self.groups = []

        self.format_desc()

        if self.dtype == "icon":
            if self.pix == "":
                self.pix = self.name.upper() + ".png"
            else:
                self.pix += ".png"

    def format_desc(self):
        for k, v in dtypes.items():
            if k in self.desc:
                self.desc = self.desc.replace(k, v)

    def orphan(self):
        return len(self.groups) == 0

    def add_to_group(self, gr):
        gr.functions.append(self)
        self.groups.append(gr)


class TocBuilder:
    def __init__(self):
        self.functions = []
        self.init_functions()

    def init_functions(self):
        """
        Reads the function descriptions and create an DocFunction
        object for each entry.
        """
        path = os.path.join(API_DIR, "functions.yaml")
        with open(path, "r") as f:
            for v in yaml.safe_load(f):
                name = list(v.keys())[0]
                item = v[name]
                if item.get("exclude", False):
                    continue
                fn = DocFunction(name, item)
                self.functions.append(fn)

                # extend items groups
                item_groups = item.get("group", [])
                for d_type in ["grib", "geopoints", "netcdf"]:
                    if (not d_type in item_groups) and (
                        d_type + "_access" in item_groups
                        or d_type + "_object" in item_groups
                    ):
                        item_groups.append(d_type)

                # add function to groups
                for gr in item_groups:
                    if gr in GROUPS:
                        fn.add_to_group(GROUPS[gr])

            for _, gr in GROUPS.items():
                gr.sort()

    def find(self, name):
        for f in self.functions:
            if f.name == name:
                return f
        return None

    def build_page(self, page):
        if len(page.groups) == 0:
            LOG.warning("Empty toc!")
            return
        txt = ""

        title_len = len(page.title) + 2
        txt += f"""
{page.title}
{"=" * title_len}
{page.desc}
"""
        for gr in page.groups:
            if len(gr.functions) == 0:
                print("Empty group")
                continue

            if len(page.groups) > 1:
                title_len = len(gr.title) + 2
                txt += f"""

{gr.title}
{"-" * title_len}

"""

            txt += f"""
.. list-table::
    :widths: 20 80
    :header-rows: 0

"""
            for fn in gr.functions:
                txt += f"""
    * - :func:`{fn.name}`
      - {fn.desc}
"""
        with open(page.rst, "w") as f:
            f.write(txt)

        log_generated(page.rst)

    def build_icon_page(self):
        txt = ""

        txt += """
Icon functions
===========================

This is the list of the functions that are represented as an icon in Metviews' user interface.

.. list-table::
    :header-rows: 0

"""
        # process each yaml from icon/desc
        for f_name in sorted(glob.glob(os.path.join(ICON_DIR, "*.rst"))):
            name = format(os.path.basename(f_name).split(".rst")[0])
            fn = self.find(name)
            if not fn:
                continue

            if os.path.exists(os.path.join(STATIC_DIR, fn.pix)):
                txt += f"""
    * - .. image:: /_static/{fn.pix}
            :width: 24px
      - :func:`{fn.name}`
      - {fn.desc}
    """
            else:
                txt += f"""
    * - .. image:: /_static/empty.png
            :width: 24px
      - :func:`{fn.name}`
      - {fn.desc}
    """
        path = os.path.join(TOC_DIR, "icon.rst")
        with open(path, "w") as f:
            f.write(txt)

        log_generated(path)

    def print_orphan(self):
        print("SCRIPT functions without group")
        cnt = 0
        for f in self.functions:
            if f.orphan() and f.dtype != "icon":
                print("[{}] {}".format(cnt, f.name))
                cnt += 1

        print("\nICON functions without group")
        cnt = 0
        for f in self.functions:
            if f.orphan() and f.dtype == "icon":
                print("[{}] {}".format(cnt, f.name))
                cnt += 1


def load_page_conf():
    path = os.path.join(API_DIR, "toc.yaml")
    with open(path, "r") as f:
        d = yaml.safe_load(f)
        for k, v in d["groups"].items():
            GROUPS[k] = TocGroup(k, v)
        for k, v in d["pages"].items():
            PAGES[k] = TocPage(k, v)


def main():
    LOG.info("Generate function table pages:")
    load_page_conf()
    builder = TocBuilder()
    for _, t in PAGES.items():
        builder.build_page(t)
    builder.build_icon_page()
    # builder.print_orphan()


if __name__ == "__main__":
    main()
else:
    main()
