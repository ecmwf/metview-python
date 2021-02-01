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
    "grib_access": "Grib data",
    "geopoints_access": "Geopoints data",
    "netcdf_access": "NetCDF data",
    "grib_object": "Grib methods",
    "geopoints_object": "Geopoints methods",
    "netcdf_object": "NetCDF methods",
    "grib": "Grib related functions",
    "geopoints": "Geopoints related functions",
    "netcdf": "NetCDF related functions",
    "odb": "ODB related functions",
    "bufr": "BUFR related functions",
    "visdef": "Visual definitions",
    "retrieve": "Data retrieval",
    "mask": "Masking",
    "flex": "Flextra and Flexpart",
    "table": "Table data",
    "scm": "Single Column Model",
    "rttov": "RTTOV",
    "wind": "Wind",
    "met3d": "Met3D",
    "vapor": "Vapor",
}

toc_def = {
    "comp": {
        "title": "Computation functions",
        "gr": [
            "stats",
            "geo",
            "mask",
            "wind",
            "vertical",
            "thermo",
            "calculus",
            "maths",
        ],
    },
    "plot": {
        "title": "Visualisation functions",
        "gr": ["view", "visdef", "plot", "layout", "output"],
    },
    # "ui": {"title": "User interface", "gr": ["widget", "ui"]},
    "data": {
        "title": "Data access function",
        "gr": [
            "retrieve",
            "conversion",
            "filter",
            "grib_access",
            "geopoints_access",
            "netcdf_access",
            "flex",
            "table",
            "scm",
            "rttov",
        ],
    },
    "apps": {
        "title": "External application functions",
        "gr": ["flex", "met3d", "vapor", "scm", "rttov"],
    },
    "object": {
        "title": "Object functions",
        "gr": [
            "grib_object",
            "geopoints_object",
            "netcdf_object",
        ],
    },
    "grib": {
        "title": "GRIB (Fieldset) functions",
        "desc": "This is the list of all functions related to GRIB (:class:`Fieldset`) data.",
        "gr": ["grib"],
    },
    "geopoints": {
        "title": "Geopoints functions",
        "desc": "This is the list of all functions related to :class:`Geopoints` data.",      
        "gr": ["geopoints"],
    },
    "netcdf": {
        "title": "NetCDF functions",
        "desc": "This is the list of all functions related to :class:`NetCDF` data.",
        "gr": ["netcdf"],
    },
    "odb": {
        "title": "ODB functions",
        "desc": "This is the list of all functions related to :class:`Odb` data.",
        "gr": ["odb"],
    },
    "bufr": {
        "title": "BUFR functions",
        "desc": "This is the list of all functions related to :class:`Bufr` data.",
        "gr": ["bufr"],
    },
}

groups = {}
toc = {}

dtypes = {
    "fieldsets": ":class:`Fieldset`",
    "fieldset": ":class:`Fieldset`",
    "geopoints": ":class:`Geopoints`",
    "array": "ndarray",
    "number": "number",
}


class TocGroup:
    def __init__(self, name, item):
        self.name = name
        self.title = item.get("title", "")
        self.desc = item.get("desc", "")
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
fn_orphan = []


class DocFunction:
    def __init__(self, name, dtype, desc, pix):
        self.name = name
        self.dtype = dtype
        self.category = {}
        self.desc = desc

        for k, v in dtypes.items():
            if k in self.desc:
                self.desc = self.desc.replace(k, v)

        self.groups = []
        self.pix = pix
        if self.dtype == "icon":
            if self.pix == "":
                self.pix = self.name.upper() + ".png"
            else:
                self.pix += ".png"

    def orphan(self):
        return len(self.groups) == 0

    def add_to_group(self, gr):
        gr.fn.append(self)
        self.groups.append(gr)

    # def type_str(self):
    #     t = []
    #     for k, v in self.dtype.items():
    #         dt typeses.get(k, "")
    #         if dt:
    #             t.append(dt)
    #     return ", ".join(t)


def make_group_toc(t):

    if len(t.gr) == 0:
        print("Empty toc!")
        return

    with open(t.output, "w") as f:
        title_len = len(t.title) + 2
        f.write(
            f"""
{t.title}
{"=" * title_len}
{t.desc}
""")
        for gr in t.gr:
            if len(gr.fn) == 0:
                print("Empty group")
                continue

            if len(t.gr) > 1:
                title_len = len(gr.title) + 2
                f.write(
                    f"""

{gr.title}
{"-" * title_len}

""")
            f.write(
                f"""
.. list-table::
    :widths: 20 80
    :header-rows: 0

""")
            for fn in gr.fn:
                #                 f.write("""
                #     * - :func:`{}`
                #       - .. image:: {}
                #            :width: 16px
                #       - {}
                # """.format(fn.name, "_static/MCONT.png", fn.desc))
                f.write(
                    """
    * - :func:`{}`
      - {}
""".format(
                        fn.name, fn.desc
                    )
                )


def make_icon_toc():

    with open("icon.rst", "w") as f:
        f.write(
            """
{}
===========================

""".format(
                "Icon functions"
            )
        )

        icons = {}
        for fn in fn_list:
            if fn.dtype == "icon":
                if not fn.name in icons:
                    icons[fn.name] = []
                icons[fn.name].append(fn)

        # icons.sort()

        f.write(
            """

{}
-------------------------------

.. list-table::
    :header-rows: 0

""".format(
                "Icons"
            )
        )

        for title, item in icons.items():
            fn = item[0]
            f.write(
                """
    * - .. image:: /_static/{}
            :width: 24px
      - :func:`{}`
      - {}
""".format(
                    fn.pix, fn.name, fn.desc
                )
            )


with open("functions.yaml", "r") as f:
    for v in yaml.safe_load(f):
        name = list(v.keys())[0]
        item = v[name]
        if item.get("exclude", False):
            continue

        fn = DocFunction(
            name, item.get("type", ""), item.get("desc", "???"), item.get("pix", "")
        )
        fn_list.append(fn)

        item_groups = item.get("group", [])
        for d_type in ["grib", "geopoints", "netcdf"]:
            if (not d_type in item_groups) and (
                d_type + "_access" in item_groups or d_type + "_object" in item_groups
            ):
                item_groups.append(d_type)

        for gr in item_groups:
            if gr in groups:
                # raise Exception("Unknown group: {}".format(gr))
                # groups[gr] = []
                # groups[gr].fn.append(fn)
                fn.add_to_group(groups[gr])

        fn.category = item.get("category", {})

    for _, gr in groups.items():
        gr.sort()

# make_icon_toc()

for _, t in toc.items():
    make_group_toc(t)

print("SCRIPT functions without group")
cnt = 0
for f in fn_list:
    if f.orphan() and f.dtype != "icon":
        print("[{}] {}".format(cnt, f.name))
        cnt += 1

print("\nICON functions without group")
cnt = 0
for f in fn_list:
    if f.orphan() and f.dtype == "icon":
        print("[{}] {}".format(cnt, f.name))
        cnt += 1
