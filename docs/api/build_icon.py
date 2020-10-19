import os
import sys
import yaml
import glob
import re
import requests
import html2text

# exclude_list = ["compute",
# "divrot_mir", "divwind_mir", "magml",
# "mboxplot", "read_mir", "retrieve_mir",
# "table","togrib", "uvwind_mir"]

# icons_pix = {"bufr_picker": "bufrpicker",
# "geo_to_kml": ,
# "grib_vectors": "gribvectors",
# "input_visialiser": "inputvisualiser",
# "maverageview": "mxaverageview",
# "cross_sect
# }

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
        self.desc = ""
        self.p_type = conf.get("type", "str")
        self.p_type = param_types.get(self.p_type, "str")


class DocFunction:
    def __init__(self, name, dtype, desc, pix, title):
        self.name = name
        self.dtype = dtype
        self.desc = desc
        self.pix = pix
        self.title = title
        if self.title == "":
            self.title = self.name.replace("_", " ")
        self.params = {}
        if self.dtype == "icon":
            if self.pix == "":
                self.pix = self.name.upper() + ".png"
            else:
                self.pix += ".png"

    def load_params(self, conf):
        d = conf.get("params", [])
        if d is None:
            d = []

        for v in d:
            assert v
            ((p_name, p_conf),) = v.items()
            p = DocParam(p_name, p_conf)
            self.params[p.name] = p

    def load_param_desc(self):
        url = "https://confluence.ecmwf.int/display/METV/{}".format(
            self.title.replace(" ", "+")
        )
        try:
            r = requests.get(url)
        except:
            print(" No URL found!")
            return

        h = r.text
        t = html2text.html2text(h)
        t = t.split("* No labels \n\nOverview")[0]
        blocks = t.split("### ")
        for name, p in self.params.items():
            print("  p={}".format(name))
            h_name = p.name.replace("_", " ").lower()
            # print("h_name={}".format(h_name))
            for b in blocks:
                if b.lower().startswith(h_name + "\n\n"):
                    # print(" raw={}".format(b))
                    b = self.remove_bold(b)
                    b = self.remove_underline(b)
                    b = self.remove_back_quote(b)

                    b = b[len(h_name) + 2 :].strip()
                    # print(" break={}".format(b.replace("\n", "<<<<<")))

                    b = b.replace("\n\n", "+++\n")
                    b = b.split("\n")
                    # print("  lines={}".format(b))
                    if len(b) > 0:
                        tt = []
                        for i, line in enumerate(b):
                            line = line.strip()
                            if line.startswith("* "):
                                if not line.endswith("+++"):
                                    line = line + "<<<"
                                line = "        " + line
                            elif i > 0 and b[i - 1].endswith("+++"):
                                line = "        " + line
                            tt.append(line)

                        tt = " ".join(tt)
                        tt = tt.replace("+++", "\n\n")
                        tt = tt.replace("<<<", "\n")

                        tt = self.resolve_arg_ref(tt)
                        tt = self.resolve_links(tt)
                        if tt.endswith("\n"):
                            tt = tt[:-1]

                        self.params[name].desc = tt

                    # print(" final={}".format(self.params[name].desc))

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

    @staticmethod
    def find(name):
        for f in fn_list:
            if f.name == name:
                return f
        return None


def add_icon_rst(name, fname):

    with open(fname, "r") as f:
        conf = yaml.safe_load(f)
        cls_name = conf.get("class", "")

        fn = DocFunction.find(cls_name)
        if fn is None:
            return

        print("class={} name={}".format(cls_name, name))
        fn.load_params(conf)
        fn.load_param_desc()

        output = "icon/{}.rst".format(cls_name)

        with open(output, "w") as f:
            f.write(
                """
{}
=========================

.. container::
    
    .. container:: leftside

        .. image:: /_static/{}
           :width: 48px

    .. container:: rightside

        This icon performs an ODB/SQL query on an ODB database (ODB-1) or file (ODB-2). The result is always an ODB file (in ODB-2 format).


.. py:function:: {}(**kwargs)
  
    Description comes here!

""".format(
                    name, fn.pix, name
                )
            )

            for _, p in fn.params.items():

                # p = conf.get("params", [])
                # if p is None:
                #     p = []

                # for v in p:
                #     assert v
                #     ((p_name, p_conf),) = v.items()
                #     print("{} {}".format(p_name, p_conf))
                #     default = p_conf.get("default", "")
                #     if default:
                #         default = " default: " + default
                #     p_val = p_conf.get("values", "")
                #     if p_val and isinstance(p_val, str):
                #         t = " values: \n\n"
                #         for pv in p_val.split("/"):
                #             # print("pv={}".format(pv))
                #             t += "        * " + pv + "\n"
                #         t += "\n"
                #         p_val = t

                f.write(
                    """
    :param {}: {}
    :type {}: {}

""".format(
                        p.name, p.desc, p.name, p.p_type
                    )
                )

            f.write(
                """
    :rtype: None


.. minigallery:: metview.{}
    :add-heading:

""".format(
                    name
                )
            )


with open("functions.yaml", "r") as f:
    for v in yaml.safe_load(f):
        name = list(v.keys())[0]
        item = v[name]
        if item.get("exclude", False) or item.get("type", "") != "icon":
            continue

        # print("pix={}".format(item.get("pix", "")))
        # print("type={}".format(item.get("type", "")))
        fn = DocFunction(
            name,
            item.get("type", ""),
            item.get("desc", "???"),
            item.get("pix", ""),
            item.get("title", ""),
        )
        # print(" -> {}".format(fn.pix))
        fn_list.append(fn)

path = os.getenv("HOME", "") + "/git/mplot_style/mplot/_util/icon_def"
for d_name in glob.glob(os.path.join(path, "*.yaml")):
    name = format(os.path.basename(d_name).split("_def.yaml")[0])
    # if name == "flexpart_run":
    # if name == "odb_visualiser":
    # if name == "cartesianview":
    if 1:
        add_icon_rst(name, d_name)
