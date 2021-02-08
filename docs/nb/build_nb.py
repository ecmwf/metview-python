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
import json
import logging
import os
from pathlib import Path
import re
import sys

logging.basicConfig(level=logging.INFO, format="%(levelname)s %(message)s")
LOG = logging.getLogger(__name__)

# define and create paths
NB_DIR = os.path.abspath(os.path.dirname(__file__))
ROOT_DIR = os.path.dirname(NB_DIR)
EXAMPLES_DIR = os.path.join(ROOT_DIR, "examples")
BACKREF_DIR = os.path.join(ROOT_DIR, "gen_files", "nb_backref")
Path(BACKREF_DIR).mkdir(parents=True, exist_ok=True)

# rst code for a clear block
CLEAR_BLOCK = """

.. raw:: html

    <div class="sphx-glr-clear"></div>
"""

GALLERY_BACKREF = """

.. nbgallery::
   :name:
   :glob:
   :reversed:

"""

LINK_BACKREF = """

Most/all of the :ref:`gallery_index` examples demonstrate the use of this function.
"""

OBJ_METHODS = ["to_dataset", "to_dataframe"]


def format_red(t):
    return "\033[91m {}\033[00m".format(t)


def format_green(t):
    return "\033[92m {}\033[00m".format(t)


def log_generated(path):
    LOG.info("  {} [{}]".format(path, format_green("generated")))


class BackReference:
    def __init__(self):
        self.func = {}
        self.skip = [
            "print",
        ]
        self.use_link = [
            "plot",
            "setoutput",
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
                title = f"Notebooks using ``metview.{fn_name}``"
                f.write(f"""{title}\n{"^" * (len(title)+1)}""")
                # for some functions just a link to the gallery is inserted
                if fn_name in self.use_link:
                    f.write(LINK_BACKREF)
                # otherwise we add a minigallery
                else:
                    f.write(GALLERY_BACKREF)
                    for item in fn_items:
                        f.write(f"   /examples/{item.name}\n")
                f.write(CLEAR_BLOCK)
            log_generated(output)


BACKREF = BackReference()


class NbItem:
    def __init__(self, script):
        self.script = script
        self.script_name = os.path.basename(self.script)
        self.name = self.script_name.split(".ipynb")[0]
        self.parse()

    def parse(self):
        t = self.to_python(self.script)
        # print(t)
        self.backref(t)

    def backref(self, t):
        m = re.findall(r"mv\.(\w+)\(", t)
        BACKREF.add(m, self)
        for fn in OBJ_METHODS:
            m = re.findall(r"\.({})\(".format(fn), t)
            BACKREF.add(m, self)

    def to_python(self, path):
        r = ""
        code = json.load(open(path))
        for cell in code["cells"]:
            if cell["cell_type"] == "code":
                for line in cell["source"]:
                    r += line + " "
                r += "\n"
        return r


def main():
    LOG.info("Generate notebook backreference pages:")
    
    items = []
    for script in glob.glob(os.path.join(EXAMPLES_DIR, "*.ipynb")):
        LOG.info(f"  processing: {script}")
        item = NbItem(script)
        items.append(item)

    # # generate the method backreference pages (mini galleries)
    BACKREF.build()
    # BACKREF.print()


if __name__ == "__main__":
    main()
else:
    main()
