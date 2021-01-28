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
import os
from pathlib import Path
import re
import sys
import subprocess

# from colorama import Fore
# from termcolor import colored
import yaml

# define and create paths
GALLERY_DIR = os.path.abspath(os.path.dirname(__file__))
ROOT_DIR = os.path.dirname(GALLERY_DIR)
PNG_DIR = os.path.join(ROOT_DIR, "_static", "gallery")
RST_DIR = os.path.join(GALLERY_DIR, "rst")
BACKREF_DIR = os.path.join(GALLERY_DIR, "backref")
Path(PNG_DIR).mkdir(exist_ok=True)
Path(RST_DIR).mkdir(exist_ok=True)
Path(BACKREF_DIR).mkdir(exist_ok=True)


# template for example blocks/items in the main gallery page or in backreference
# use <div class="sphx-glr-thumbcontainer" tooltip="{}"> for a tooltip
ITEM_TEMPLATE = """
.. raw:: html

    <div class="sphx-glr-thumbcontainer">

.. only:: html

 .. figure:: {}
     :alt: {}

     :ref:`{}`

.. raw:: html

    </div>

"""

# template for a gallery example page
PAGE_TEMPLATE = """
:orphan:

.. only:: html

    .. note::
        :class: sphx-glr-download-link-note

        Click :download:`here <{}>` to download the full example code
    .. rst-class:: sphx-glr-example-title

    .. _{}:

{}
{}

.. image:: {}
    :alt: {}
    :class: sphx-glr-single-img

.. mv-include-code:: {}

"""

# rst code for a clear block
CLEAR_BLOCK = """

.. raw:: html

    <div class="sphx-glr-clear"></div>
"""

LINK_BACKREF = """

Most/all of the :ref:`gallery_index` examples demonstrate the use of this function.
"""

def print_red(t):
    print("\033[91m {}\033[00m".format(t))


def print_green(t):
    print("\033[92m {}\033[00m".format(t))


def to_rst_path(f):
    pos = f.find("docs/")
    return f[(pos + 4) :]


class BackReference:
    def __init__(self):
        self.func = {}
        self.skip = [
            "print",
        ]
        self.use_link = [
            "plot",
            "pdf_output",
            "setoutput",
            "exist",
            "download_gallery_data",
        ]

    def add(self, vals, item):
        if vals:
            vals = set(vals)
            for v in vals:
                if not v in self.skip:
                    if not v in self.func:
                        self.func[v] = []
                    self.func[v].append(item)

    def print(self):
        for k, v in self.func.items():
            print(k)
            for vv in v:
                print(f"  {vv.name}")

    def build(self):
        for fn_name, fn_items in self.func.items():
            output = os.path.join(BACKREF_DIR, f"{fn_name}.rst")
            with open(output, "w") as f:
                title = f"Gallery examples using ``metview.{fn_name}``"
                f.write(f"""{title}\n{"^" * (len(title)+1)}""")  
                # for some functions just a link to the gallery is inserted
                if fn_name in self.use_link:
                    f.write(LINK_BACKREF) 
                # otherwise we add a minigallery
                else:
                    for item in fn_items:
                        item.build_item(f)
                f.write(CLEAR_BLOCK)


BACKREF = BackReference()


class GalleryItem:
    def __init__(self, script):
        self.status = True
        self.script = script
        self.script_name = os.path.basename(self.script)
        self.script_dir = os.path.dirname(script)
        self.name = self.script_name.split(".py")[0]
        self.title = self.name
        self.parse()

        self.label = "gallery_" + self.name
        self.f_pdf = self.name + ".pdf"
        self.f_png = os.path.join(PNG_DIR, self.name + ".png")
        self.f_png = os.path.join(PNG_DIR, self.name + ".png")
        self.f_thumbnail = os.path.join(PNG_DIR, self.name + "_thumb.png")

        # print(f"  title={self.title}")

        do_png = True
        if os.path.isfile(self.f_png):
            src_mod_time = os.path.getmtime(self.script)
            target_mod_time = os.path.getmtime(self.f_png)
            if src_mod_time <= target_mod_time:
                do_png = False

        # generate png
        if do_png:
            print("  making PDF ...")
            try:
                r = subprocess.run(["python3", self.script_name], check=True)
            except Exception as e:
                print_red(f"  Failed to run script: {e}")
                self.status = False

            if os.path.exists(self.f_pdf):
                print("  making PNG ...")
                try:
                    cmd = f"convert -trim -border 8x8 -bordercolor white -depth 8 {self.f_pdf} {self.f_png}"
                    r = subprocess.run(cmd.split(" "), check=True)
                except Exception as e:
                    print_red(f"  Failed to convert PDF to PNG: {e}")
                    self.status = False

        if not os.path.exists(self.f_thumbnail) or do_png:
            print("  making thumbnail PNG ...")
            try:
                cmd = f"convert -trim -border 8x8 -bordercolor white -depth 8 {self.f_pdf} -resize 22% {self.f_thumbnail}"         
                r = subprocess.run(cmd.split(" "), check=True)
            except Exception as e:
                print_red(f"  Failed to resize PNG: {e}")
                self.status = False

        if self.status:
            print_green("  --> DONE")

        self.build_page()

    def parse(self):
        with open(self.script, "r") as f:
            t = f.read()
            # print(t)
            pos = t.find("#")
            # print(f"pos={pos}")
            self.title = t[:pos].strip().replace('"""', "").replace("=", "").strip()
            self.backref(t[pos:])

    def backref(self, t):
        m = re.findall(r"mv\.(\w+)\(", t)
        BACKREF.add(m, self)

    def build_item(self, f):
        f.write(
            ITEM_TEMPLATE.format(
                to_rst_path(self.f_thumbnail), self.title, self.label
            )
        )

    def build_page(self):
        output = os.path.join(RST_DIR, self.name + ".rst")
        with open(output, "w") as f:
            f.write(
                PAGE_TEMPLATE.format(
                    to_rst_path(self.script),
                    self.label,
                    self.title,
                    "=" * (len(self.title) + 2),
                    to_rst_path(self.f_png),
                    self.title,
                    to_rst_path(self.script),
                )
            )


def build_gallery(r):
    output = os.path.join(RST_DIR, "index.rst")
    with open(output, "w") as f:
        f.write(
            """
:orphan:

.. _gallery_index:

Gallery
=========================

"""
        )
        for gr in r:
            title = gr["title"]
            f.write(
                f"""
{CLEAR_BLOCK}  
{title}
{"-" * (len(title)+1)}

{gr["desc"]}

"""
            )
            for item in gr["items"]:
                item.build_item(f)


def main():
    r = []

    # generate the individual example pages
    f = open("examples.yaml", "r")
    conf = yaml.load(f, Loader=yaml.FullLoader)
    total = sum([len(conf[x]["examples"]) for x in conf])
    cnt = 1
    item_failed = []
    for group, item in conf.items():
        gr_item = {"title": item["title"], "desc": item.get("desc", ""), "items": []}
        for name in item["examples"]:
            print(f"[{cnt}/{total} {name}]")
            script = os.path.join(GALLERY_DIR, name + ".py")
            item = GalleryItem(script)
            gr_item["items"].append(item)
            cnt += 1
            if not item.status:
                item_failed.append(item)
        r.append(gr_item)

    if len(item_failed) == 0:
        print_green(f"{total}/{total} examples were generated")
    else:
        print_red(f"{total-len(item_failed)}/{total} examples were generated, {len(item_failed)}/{total} examples failed:")
        for v in item_failed:
            print_red(f"  {v.name}")

    # generate the main gallery page
    print("Build gallery index page ...")
    build_gallery(r)

    # generate the method backreference pages (mini galleries)
    print("Build backreference pages ...")
    BACKREF.build()
    # BACKREF.print()


if __name__ == "__main__":
    main()
else:
    main()
