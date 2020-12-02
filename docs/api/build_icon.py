import os
import sys
import yaml
import glob
import re
import requests
import html2text

fn_list = []

param_types = {
    "string": "str",
    "text": "str",
    "list": "str or list[str]",
    "number": "number",
    "number_list": "float or list[float]",
    "int_list": "int or list[int]",
    "on_off": "str",
    "combo": "str",
    "combo_delayed": "str",
    "line_style": "str",
    "line_width": "int",
    "arrow_shape": "int",
    "colour": "str",
    "colour_list": "str or list[str]",
    "style": "str",
    "palette": "str",
    "symbol_index": "int",
    "symbol_name": "str",
}

ignore_group = ["widget", "output"]


class DocParam:
    def __init__(self, name, conf):
        self.name = name
        if isinstance(name, bool):
            if name:
                self.name = "true"
            else:
                self.name = "false"

        self.default = conf.get("default", "")
        self.values = conf.get("values", "")
        self.desc = conf.get("desc", "")
        self.p_type = conf.get("ptype", "str")

        if "str" in self.p_type:
            self.default = self.add_double_quote(self.default)

    def type_str(self):
        r = ""
        if self.p_type == "str":
            if self.values:
                r = self.format_list(self.values)
            else:
                r = self.p_type
        else:
            r = self.p_type

        if self.default:
            r += ", default: " + self.default
        
        return r

    def format_list(self, v):
        if "str" in self.p_type:
            return "{" + ", ".join([self.add_double_quote(v) for v in v.split("/")]) + "}"

    def add_double_quote(self, v):
        if v:
            if not v[0] in ["\'", "\""]:
                v = f"\"{v}\""
            else:
                v = v.replace("\'", "\"")
        return v

class DocFunction:
    def __init__(self, name, conf):
        self.name = name
        self.dtype = item.get("type", "")
        self.desc = item.get("desc", "???")
        self.pix = item.get("pix", "")
        self.title = item.get("title", "")
        self.mag = item.get("mag", False)
        self.standard = item.get("standard", True)

        if self.title == "":
            self.title = self.name.replace("_", " ")

        self.conf_label = self.title
        if self.conf_label.lower() == self.conf_label:
            self.conf_label = " ".join(
                [w.capitalize() for w in self.conf_label.split(" ")]
            )

        self.params = {}
        if self.dtype == "icon":
            if self.pix == "":
                self.pix = self.name.upper() + ".png"
            else:
                self.pix += ".png"

        self.group = conf.get("group", [])

    def load_params(self, conf):
        d = conf.get("params", [])
        if d is None:
            d = []

        for v in d:
            assert v
            ((p_name, p_conf),) = v.items()
            p = DocParam(p_name, p_conf)

    def remove_bold(self, t):
        return t.replace("**", "")

    def remove_underline(self, t):
        t = t.replace(" `_", " ")
        t = t.replace("_` ", " ")
        t = t.replace(" _", " ")
        t = t.replace("_ ", " ")
        return t

    def remove_back_quote(self, t):
        t = t.replace(" `", " ")
        t = t.replace("` ", " ")
        return t

    def resolve_arg_ref(self, t):
        # print("text={}".format(t))
        for name in self.params.keys():
            p = name.replace("_", " ")
            # print("  p={}".format(p))
            r = re.compile("{}".format(p), re.IGNORECASE)
            t = r.sub("``{}``".format(name), t)
        return t

    def resolve_arg_ref_magics(self, t):
        # print("text={}".format(t))
        for name in self.params.keys():
            # print("  p={}".format(p))
            if "_" in name:
                r = re.compile("{}".format(name), re.IGNORECASE)
                t = r.sub("``{}``".format(name), t)
        return t

    def resolve_links(self, t):
        for f in fn_list:
            r = re.compile("\[{}\]\(\S+\)".format(f.title), re.IGNORECASE)
            t = r.sub(":func:`{}`".format(f.name), t)

        r = re.compile(r"\[([^\]]+)\]\(\/display\/METV\/(\S+)\)")
        for m in r.finditer(t):
            if m and m.groups and len(m.groups()) == 2:
                s1 = m.group(1)
                s2 = m.group(2)
                t = t.replace(
                    m.group(0),
                    "`{} <https://confluence.ecmwf.int/display/METV/{}>`_".format(
                        s1, s2
                    ),
                )

        return t

    def need_mini_gallery(self):
        return os.path.exists(
            "../gen_modules/backreferences/metview.{}.examples".format(self.name)
        )

    def as_dict(self):
        d = []
        for _, item in self.params.items():
            d.append(item.as_dict())    
        return d

    @staticmethod
    def find(name):
        for f in fn_list:
            if f.name == name:
                return f
        return None

    def is_group_ignored(self):
        for ig in ignore_group:
            if ig in self.group:
                return True
        return False


def add_icon_rst(name, fname):

    with open(fname, "r") as f:
        conf = yaml.safe_load(f)
        cls_name = name # conf.get("name", "")

        fn = DocFunction.find(cls_name)
        if fn is None or fn.is_group_ignored():
            return

        print("class={} name={}".format(cls_name, name))
        output = "icon/{}.rst".format(cls_name)

        with open(output, "w") as f:

            if fn.standard:

                f.write(
                    """
{}
=========================

.. container::
    
    .. container:: leftside

        .. image:: /_static/{}
           :width: 48px

    .. container:: rightside

        This function performs the same task as the {} icon in Metview’s user interface. It accepts its parameters as keyword arguments, described below.


.. py:function:: {}(**kwargs)
  
    Description comes here!

""".format(
                        name,
                        fn.pix,
                        "`{} <https://confluence.ecmwf.int/display/METV/{}>`_".format(
                            fn.conf_label, fn.title.replace(" ", "+")
                        ),
                        fn.name,
                    )
                )

            else:
                f.write(
                    """
{}
=========================

.. py:function:: {}(**kwargs)
  
    Description comes here!

""".format(
                        name,
                        fn.name,
                    )
                )

            for item in conf.get("params", {}):
                ((p_name, p_conf),) = item.items()
                p = DocParam(p_name, p_conf)
                f.write(
                    """
    :param {}: {}
    :type {}: {}

""".format(
                        p.name, p.desc, p.name, p.type_str()
                    )
                )

            f.write(
                """
    :rtype: None
"""
            )

            if fn.need_mini_gallery():
                f.write(
                    """

.. minigallery:: metview.{}
    :add-heading:

""".format(
                        name
                    )
                )

def make_icon_toc():

    with open("icon.rst", "w") as f:
        f.write(
            """
Icon functions
===========================

"""
        )
        # icons = {}
        # for fn in fn_list:
        #         if not fn.name in icons:
        #             icons[fn.name] = []
        #         icons[fn.name].append(fn)

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

        for fn in fn_list:
            if not fn.is_group_ignored():
                # print(f"../_static/{fn.pix}")
                if os.path.exists(f"../_static/{fn.pix}"):
                    f.write(
                        f"""
    * - .. image:: /_static/{fn.pix}
            :width: 24px
      - :func:`{fn.name}`
      - {fn.desc}
    """
                    )
                else:
                    f.write(
                        f"""
    * - A
      - :func:`{fn.name}`
      - {fn.desc}
    """
                    )


with open("functions.yaml", "r") as f:
    for v in yaml.safe_load(f):
        name = list(v.keys())[0]
        item = v[name]

        if item.get("exclude", False) or item.get("type", "") != "icon":
            continue

        # print("pix={}".format(item.get("pix", "")))
        # print("type={}".format(item.get("type", "")))
        fn = DocFunction(name, item)
        # print(" -> {}".format(fn.pix))
        fn_list.append(fn)

# make_icon_toc()
# sys.exit(0)

# path = os.getenv("HOME", "") + "/git/mplot_style/mplot/_util/icon_def"
# for d_name in glob.glob(os.path.join(path, "*.yaml")):
#     name = format(os.path.basename(d_name).split("_def.yaml")[0])
#     # if name == "flexpart_run":
#     # if name == "odb_visualiser":
#     # if name == "cartesianview":
#     # if name == "mcont":
#     if 1:
#         add_icon_rst(name, d_name)


path = os.getenv("HOME", "") + "/icon_desc"
for d_name in glob.glob(os.path.join(path, "*.yaml")):
    name = format(os.path.basename(d_name).split(".yaml")[0])
    # if name == "annotationview":
    # if name == "odb_visualiser":
    # if name == "cartesianview":
    # if name == "mcont":
    if 1:
        add_icon_rst(name, d_name)

make_icon_toc()