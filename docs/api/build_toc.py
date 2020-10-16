import os
import sys

import yaml

groups_def = {
    "stats": "Statistics",
    "calculus": "Calculus",
    "maths": "Basic mathematics",
    "thermo": "Thermodynamics",
    "aggr": "Aggregation",
    "geo": "Geographic",
    "avg": "Average",
    "plot": "Plotting",
    "filter": "Filtering",
    "grid": "Grid",
    "vertical": "Vertical",
    "view": "Views",
    "layout": "Layout",
    "ui": "Examiners",
    "widget": "Widgets",
    "conversion": "Data conversion",
    "output": "Graphical output",
    "grib": "Grib data",
    "geopoints": "Geopoints data",
    "netcdf": "NetCDF data",
    "visdef": "Visual definitions",
    "retrieve": "Data retrieval",
}

toc_def = {
    "comp": {
        "title": "Computation functions",
        "gr": [
            "maths",
            "calculus",
            "stats",
            "thermo",
            "geo",
            "filter",
            "grid",
            "vertical",
        ],
    },
    "plot": {
        "title": "Visualisation",
        "gr": ["plot", "layout", "view", "visdef", "output"],
    },
    "ui": {"title": "User interface", "gr": ["widget", "ui"]},
    "data": {
        "title": "Data access",
        "gr": ["retrieve", "conversion", "grib", "geopoints", "netcdf"],
    },
}

groups = {}
toc = {}

dtypes = {
    "fieldset": ":class:`Fieldset`",
    "geopoints": ":class:`Geopoints`",
    "array": "ndarray",
    "number": "number",
}


class TocGroup:
    def __init__(self, name, item):
        self.name = name
        self.title = item.get("title", "")
        self.output = name + "_toc.rst"
        self.gr = []
        for gn in item.get("gr", []):
            gr = groups.get(gn, None)
            if gr:
                self.gr.append(gr)


class DocGroup:
    def __init__(self, name, title):
        self.name = name
        self.title = title
        # self.output = name + "_toc.rst"
        self.fn = []

    def sort(self):
        self.fn.sort(key=lambda x: x.name)


for k, v in groups_def.items():
    groups[k] = DocGroup(k, v)

for k, v in toc_def.items():
    toc[k] = TocGroup(k, v)

fn_list = []


class DocFunction:
    def __init__(self, name, dtype, desc):
        self.name = name
        self.dtype = dtype
        self.desc = desc
        self.dtype = {}

    def type_str(self):
        t = []
        for k, v in self.dtype.items():
            dt = dtypes.get(k, "")
            if dt:
                t.append(dt)
        return ", ".join(t)


with open("functions.yaml", "r") as f:
    for v in yaml.safe_load(f):
        name = list(v.keys())[0]
        item = v[name]
        fn = DocFunction(name, item.get("type", ""), item.get("desc", "???"))
        fn_list.append(fn)
        for gr in item.get("group", []):
            if gr in groups:
                # raise Exception("Unknown group: {}".format(gr))
                # groups[gr] = []
                groups[gr].fn.append(fn)

        fn.dtype = item.get("category", {})

    for _, gr in groups.items():
        gr.sort()

for _, t in toc.items():
    if len(t.gr) == 0:
        print("Empty toc!")
        continue

    with open(t.output, "w") as f:
        f.write(
            """
{}
===========================

""".format(
                t.title
            )
        )
        for gr in t.gr:
            if len(gr.fn) == 0:
                print("Empty group")
                continue

            f.write(
                """

{}
-------------------------------

.. list-table::
    :widths: 20 80
    :header-rows: 0

""".format(
                    gr.title
                )
            )

            for fn in gr.fn:
#                 f.write("""
#     * - :func:`{}`
#       - .. image:: {} 
#            :width: 16px
#       - {}
# """.format(fn.name, "_static/MCONT.png", fn.desc))
                f.write("""
    * - :func:`{}`
      - {}
""".format(fn.name, fn.desc))