import os
import sys
import yaml
import glob
import re
import requests
import html2text
from yamlinclude import YamlIncludeConstructor

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

ignore_group = ["widget"]

family = {"hovm_data": ["mhovmoeller_area", 
            "mhovmoeller_expand", 
            "mhovmoeller_line", "mhovmoeller_vertical"]}

class Loader(yaml.SafeLoader):
    def __init__(self, stream):
        self._root = os.path.split(stream.name)[0]
        super(Loader, self).__init__(stream)

    def include(self, node):
        filename = os.path.join(self._root, self.construct_scalar(node))
        with open(filename, 'r') as f:
            return yaml.load(f, Loader)

Loader.add_constructor('!include', Loader.include)

def indent_summary(txt):
    r = ""
    if txt:
        indent = "\t" * 2
        for t in txt.split("\n"):
            r += indent + t + "\n"
    return r


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

        # print(f"  {conf}")
        self.format_desc()

    def type_str(self):
        r = ""
        if self.p_type == "str":
            if self.values:
                r = self.format_list(self.values)
                if len(self.values.split("/")) >= 6 and len(self.values) > 60:
                   r = self.p_type 
            else:
                r = self.p_type
        else:
            r = self.p_type

        if self.default:
            r += ", default: " + self.formatted_default()
        
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

    def format_desc(self):
        self.desc = self.format_text(self.desc)
        if self.desc:
            r = ""
            indent = "\t" * 2
            for t in self.desc.split("\n"):
                if r:
                    r += indent
                r += t + "\n"
            if r and r[-1] == "\n":
                r = r[:-1]
            self.desc = r

    @staticmethod
    def format_text(txt):
        if txt:
            txt = txt.replace("<tt>", "\t\t")
            txt = txt.replace("@","\@")
        return txt

    def formatted_default(self):
        if self.default and isinstance(self.default, str):
            if "/" in self.default:
                return "[" + ", ".join([v.strip() for v in self.default.split("/")]) + "]"
            # print(f"  {self.default} -> {v}")
            else:
                return self.default.replace("@","\@")
        else:
            return str(self.default)

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

def parse_conf(conf):
    d = []
    # print(f"conf={conf}")
    for item in conf["params"]:
        ((p, v),) = item.items()
        # print(f" p={p}")
        if p.startswith("_include"):
            # print(f" --> p {p} {v}")
            d.extend(v)           
        else:
            d.append(item)
    conf["params"] = d
    return conf


def add_icon_rst(name, fname, summary_file_name):
    with open(fname, "r") as f:
        conf = yaml.load(f, Loader=yaml.FullLoader)
        # conf = yaml.safe_load(f)
        # print(conf)
        cls_name = name # conf.get("name", "")
        print("class={} name={}".format(cls_name, name))
        
        conf = parse_conf(conf)
        summary = conf.get("summary","")
        # print(f"summary_file_name={summary_file_name}")
        if summary == "rst":    
            with open(summary_file_name, "r") as fs:
                summary = fs.read()

        # summary = DocParam.format_text(summary)
        ret_type = conf.get("return","None")
        one_liner = conf.get("oneliner","")

        # print(conf)

        fn = DocFunction.find(cls_name)
        if fn is None or fn.is_group_ignored():
            print(" -> ignored")
            return

        # print("class={} name={}".format(cls_name, name))
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

{}

\t\t.. note:: This function performs the same task as the {} icon in Metview’s user interface. It accepts its parameters as keyword arguments, described below.


.. py:function:: {}(**kwargs)
  
    {}

""".format(
                        name,
                        fn.pix,
                        indent_summary(summary),
                        "`{} <https://confluence.ecmwf.int/display/METV/{}>`_".format(
                            fn.conf_label, fn.title.replace(" ", "+")
                        ),
                        fn.name,
                        one_liner,
                    )
                )

            else:
                f.write(
                    """
{}
=========================

{}

.. py:function:: {}(**kwargs)
  
    {}

""".format(
                        name,
                        summary,
                        fn.name,
                        one_liner,
                    )
                )

            for item in conf.get("params", []):
                ((p_name, p_conf),) = item.items()
                p = DocParam(p_name, p_conf)
                # print("  " + p_name)
                # print(f"  {p_conf}")
                f.write(
                    """
    :param {}: {}
    :type {}: {}
""".format(
                        p.name, p.desc, p.name, p.type_str()
                    )
                )

            f.write(
                f"""
    :rtype: {ret_type}
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

This is the list of the functions that are represented as an icon in Metviews' user interface.

.. list-table::
    :header-rows: 0

""")

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
    * - .. image:: /_static/empty.png
            :width: 24px
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

# initialise yaml including
path = os.getenv("HOME", "") + "/icon_desc"
YamlIncludeConstructor.add_to_loader_class(
    loader_class=yaml.FullLoader, 
    base_dir=path)

path = os.getenv("HOME", "") + "/icon_desc"
for f_name in glob.glob(os.path.join(path, "*.yaml")):
    name = format(os.path.basename(f_name).split(".yaml")[0])
    summary_file_name = os.path.join(path, name + ".rst")
    # if name == "annotationview":
    # if name == "maverageview":
    # if name == "cartesianview":
    # if name == "mcont":
    # if name == "flexpart_prepare":
    if 1:
        add_icon_rst(name, f_name, summary_file_name)

make_icon_toc()