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

ignore_group = ["widget"]


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
        if self.name.endswith("_thickness") and self.p_type == "str":
            self.values = ""
            self.p_type = "int"

        if "colour" in self.name and self.p_type == "str" and self.values == "background":
            self.values = ""


    def formatted_desc(self):
        t = self.desc
        if t and "str" in self.p_type:
            vals = []
            if self.values:
                vals = [v.strip() for v in self.values.split("/")]
            if self.default:
                v = self.default.strip()
                if not v in vals:
                    vals.append(v)
            # print(f"name={name} vals={vals} t={t}") 
            for v in vals:
                if v:
                    try:
                        r = re.compile(r"\b{}\b".format(v), re.IGNORECASE)
                        t = r.sub("\"{}\"".format(v), t)
                    except:
                        pass
        
            # print(f" -> {t}")
        return t

    #  def add_double_quote(self, v):
    #     if v:
    #         if not v[0] in ["\'", "\""]:
    #             v = f"\"{v}\""
    #         else:
    #             v = v.replace("\'", "\"")
    #     return v        

    def as_dict(self):
        d = {
            # "name": self.name,
            "default": self.default,
            "values": self.values,
            "desc": self.formatted_desc(),
            "ptype": self.p_type
        }
        return d

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
            self.params[p.name] = p

    def load_param_desc(self):
        url = "https://confluence.ecmwf.int/display/METV/{}".format(
            self.title.replace(" ", "+")
        )
        print(url)
        try:
            r = requests.get(url)
        except:
            print(" No URL found!")
            return

        h = r.text
        if h == "":
            return

        t = html2text.html2text(h)
        # print(t)
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

    def load_param_desc_magics_ori(self):
        if self.mag:

            fname = os.getenv("HOME", "") + "/magics_defs/metview_files/{}.yaml".format(
                self.name.upper()
            )
            if not os.path.exists(fname):
                return

            with open(fname, "r") as f:
                doc = yaml.safe_load(f)
                for name, p in self.params.items():
                    # print("  p={}".format(name))
                    h_name = p.name
                    v = doc.get(h_name, "")
                    if v:
                        v = v.strip()
                        if v.startswith("'"):
                            v = v[1:]
                        if v.endswith("'"):
                            v = v[:-1]

                        v = v.replace("\t", "")
                        v = v.replace("\n", "")
                        v = self.resolve_arg_ref_magics(v)

                        if p.values:
                            if not v.endswith("."):
                                v += ". "
                            else:
                                v += " "
                            v += "The possible values:\n\n"
                            for vv in p.values.split("/"):
                                v += "        * {}\n".format(vv)

                        if p.default is not None and not (
                            isinstance(p.default, str) and p.default == ""
                        ):
                            if v.endswith("\n"):
                                v += "        "
                            elif not v.endswith("."):
                                v += ". "
                            else:
                                v += " "

                            v += "The default is: {}.".format(p.default)

                        self.params[name].desc += v

    def load_param_desc_magics(self):
        if self.mag:

            fname = os.getenv("HOME", "") + "/magics_defs/metview_files/{}.yaml".format(
                self.name.upper()
            )
            if not os.path.exists(fname):
                return

            with open(fname, "r") as f:
                doc = yaml.safe_load(f)
                for name, p in self.params.items():
                    # print("  p={}".format(name))
                    h_name = p.name
                    v = doc.get(h_name, "")
                    if v:
                        v = v.strip()
                        if v.startswith("'"):
                            v = v[1:]
                        if v.endswith("'"):
                            v = v[:-1]

                        v = v.replace("\t", "")
                        v = v.replace("\n", "")
                        v = self.resolve_arg_ref_magics(v)

                        # if p.values:
                        #     if not v.endswith("."):
                        #         v += ". "
                        #     else:
                        #         v += " "
                        #     v += "The possible values:\n\n"
                        #     for vv in p.values.split("/"):
                        #         v += "        * {}\n".format(vv)

                        # if p.default is not None and not (
                        #     isinstance(p.default, str) and p.default == ""
                        # ):
                        #     if v.endswith("\n"):
                        #         v += "        "
                        #     elif not v.endswith("."):
                        #         v += ". "
                        #     else:
                        #         v += " "

                        #     v += "The default is: {}.".format(p.default)

                        self.params[name].desc += v

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
            d.append({item.name: item.as_dict()}) 
        return {"params": d}

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

def add_icon_yaml(name, fname):

    with open(fname, "r") as f:
        conf = yaml.safe_load(f)
        cls_name = conf.get("class", "")

        fn = DocFunction.find(cls_name)
        if fn is None or fn.is_group_ignored():
            return
            
        # if not "output" in fn.group:
        #     return

        print("class={} name={}".format(cls_name, name))
        fn.load_params(conf)
        fn.load_param_desc()
        fn.load_param_desc_magics()
 
        output = os.path.join(os.getenv("HOME", ""), "icon_desc_1/{}.yaml".format(cls_name))
        if not os.path.exists(output):
        # if "output" in fn.group:
            print(f" -> {output}")
            r = yaml.dump(fn.as_dict(), default_flow_style=False)
            with open(output, "w") as ff:
                ff.write(r)

with open("../functions.yaml", "r") as f:
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

path = os.getenv("HOME", "") + "/git/metzoom_style/metzoom/_util/icon_def"
for d_name in glob.glob(os.path.join(path, "*.yaml")):
    name = format(os.path.basename(d_name).split("_def.yaml")[0])
    # if name == "annotationview":
    # if name == "odb_visualiser":
    # if name == "cartesianview":
    # if name == "mcont":
    # if name  == "mhovmoellerview":
    if name == "regrid":
    # if 1:
        # add_icon_rst(name, d_name)
        add_icon_yaml(name, d_name)
