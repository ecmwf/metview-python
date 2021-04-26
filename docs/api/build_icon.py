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
import re
import sys

import yaml
from yamlinclude import YamlIncludeConstructor

logging.basicConfig(level=logging.INFO, format="%(levelname)s %(message)s")
LOG = logging.getLogger(__name__)

API_DIR = os.path.abspath(os.path.dirname(__file__))
GEN_DIR = os.path.join(os.path.dirname(API_DIR), "gen_files")
DESC_DIR = os.path.join(API_DIR, "icon_desc")
ICON_DIR = os.path.join(GEN_DIR, "icon_functions")
Path(ICON_DIR).mkdir(parents=True, exist_ok=True)


def format_red(t):
    return "\033[91m {}\033[00m".format(t)


def format_green(t):
    return "\033[92m {}\033[00m".format(t)


def log_generated(path):
    LOG.info("  {} [{}]".format(path, format_green("generated")))


# yaml loader implementing "include"
class Loader(yaml.SafeLoader):
    def __init__(self, stream):
        self._root = os.path.split(stream.name)[0]
        super(Loader, self).__init__(stream)

    def include(self, node):
        filename = os.path.join(self._root, self.construct_scalar(node))
        with open(filename, "r") as f:
            return yaml.load(f, Loader)


# registers the include directive to the yaml loader
Loader.add_constructor("!include", Loader.include)

# initialise yaml including
YamlIncludeConstructor.add_to_loader_class(
    loader_class=yaml.FullLoader, base_dir=DESC_DIR
)

ICON_HEADER_STANDARD = """
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

"""

ICON_HEADER_SIMPLE = """
{}
=========================

{}

.. py:function:: {}(**kwargs)
  
    {}

"""


class DocParam:
    """
    Class to represent an icon parameter.
    """

    def __init__(self, name, conf):
        self.name = name
        if isinstance(name, bool):
            self.name = "true" if name else "false"

        self.default = conf.get("default", "")
        self.values = conf.get("values", "")
        self.desc = conf.get("desc", "")
        self.p_type = conf.get("ptype", "str")

        # if "str" in self.p_type:
        #     self.default = self._add_double_quote(self.default)

        # reformat the description
        self._format_desc()

    def type_str(self):
        r = self.p_type
        if (
            self.p_type in ["str", "number"]
            and self.values and isinstance(self.values, str)
            and (len(self.values.split("/")) < 6 or len(self.values) < 60)
        ):
            r = self._format_list(self.values)
        if self.default:
            r += ", default: " + self._formatted_default()

        return r

    def _format_list(self, v):
        if "str" in self.p_type:
            return (
                "{" + ", ".join([self._add_double_quote(v) for v in v.split("/")]) + "}"
            )
        elif "number" in self.p_type:
            return (
                    "{" + ", ".join([v for v in v.split("/")]) + "}"
                )
        else:
            return str()

    def _add_double_quote(self, v):
        if v:
            if not v[0] in ["'", '"']:
                v = f'"{v}"'
            else:
                v = v.replace("'", '"')
        return v

    def _format_desc(self):
        self.desc = self._format_text(self.desc)
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

    def _format_text(self, txt):
        if txt:
            txt = txt.replace("<tt>", "\t\t")
            txt = txt.replace("@", "\@")
        return txt

    def _formatted_default(self):
        if self.default and isinstance(self.default, str):
            if self.default.startswith("path::"):
                t = self.default.replace("path::", "")
                return self._add_double_quote(t)
            elif "/" in self.default:
                if "str" in self.p_type and (not "number" in self.p_type or "to" in self.default.lower()):
                    return ("[" + ", ".join([self._add_double_quote(v) for v in self.default.split("/")]) + "]")
                else:
                    return (
                        "[" + ", ".join([v.strip() for v in self.default.split("/")]) + "]"
                    )
                # return (
                #     "[" + ", ".join([v.strip() for v in self.default.split("/")]) + "]"
                # )
            # print(f"  {self.default} -> {v}")
            else:
                t = self.default.replace("@", "\@")
                if "str" in self.p_type:
                    t = self._add_double_quote(t)
                return t

        else:
            if "str" in self.p_type:
                t = self._add_double_quote(t)
            else:
                t = str(self.default)
            return t


class DocFunction:
    """
    Class to represent a function.
    """

    def __init__(self, name, item):
        self.name = name
        self.dtype = item.get("type", "")
        self.desc = item.get("desc", "???")
        self.pix = item.get("pix", "")
        self.title = item.get("title", "")
        self.standard = item.get("standard", True)

        if self.title == "":
            self.title = self.name.replace("_", " ")

        self.conf_label = self.title
        if self.conf_label.lower() == self.conf_label:
            self.conf_label = " ".join(
                [w.capitalize() for w in self.conf_label.split(" ")]
            )

        if self.dtype == "icon":
            if self.pix == "":
                self.pix = self.name.upper() + ".png"
            else:
                self.pix += ".png"

        self.group = item.get("group", [])


class IconDocBuilder:
    """
    Class to build the individual icon documentation pages.
    """

    def __init__(self):
        self.functions = []
        self.ignore_group = ["widget"]
        self.init_functions()

    def init_functions(self):
        """
        Reads the icon function descriptions and create an DocFunction
        object for each entry.
        """
        path = os.path.join(API_DIR, "functions.yaml")
        with open(path, "r") as f:
            for v in yaml.safe_load(f):
                name = list(v.keys())[0]
                item = v[name]
                if item.get("exclude", False) or item.get("type", "") != "icon":
                    continue
                fn = DocFunction(name, item)
                self.functions.append(fn)

    def find(self, name):
        for f in self.functions:
            if f.name == name:
                return f
        return None

    def is_group_ignored(self, fn):
        for ig in self.ignore_group:
            if ig in fn.group:
                return True
        return False

    def parse_conf(self, conf):
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

    @staticmethod
    def indent_summary(txt):
        r = ""
        if txt:
            indent = "\t" * 2
            for t in txt.split("\n"):
                r += indent + t + "\n"
        return r

    def build(self, name, path_desc, path_summary):
        # LOG.debug(f"build name={name}")
        fn = self.find(name)
        if fn is None:
            LOG.warning(
                f"function={name}  Not listed in functions.yaml. Cannot build rst!"
            )
            return
        if self.is_group_ignored(fn):
            LOG.warning(f"funcion={name} Ignored by group! No rst will be built!")
            return

        # read yaml definition
        with open(path_desc, "r") as f_in:
            txt = ""
            conf = yaml.load(f_in, Loader=yaml.FullLoader)
            conf = self.parse_conf(conf)

            # gets summary if it is stored in a separate file
            summary = conf.get("summary", "")
            if summary == "rst":
                with open(path_summary, "r") as fs:
                    summary = fs.read()

            ret_type = conf.get("return", "None")
            one_liner = conf.get("oneliner", "")

            # generates rst
            if fn.standard:
                txt += ICON_HEADER_STANDARD.format(
                    name,
                    fn.pix,
                    self.indent_summary(summary),
                    "`{} <https://confluence.ecmwf.int/display/METV/{}>`_".format(
                        fn.conf_label, fn.title.replace(" ", "+")
                    ),
                    fn.name,
                    one_liner,
                )
            else:
                txt += ICON_HEADER_SIMPLE.format(
                    name,
                    summary,
                    fn.name,
                    one_liner,
                )

            for item in conf.get("params", []):
                ((p_name, p_conf),) = item.items()
                p = DocParam(p_name, p_conf)
                txt += f"""
    :param {p.name}: { p.desc}
    :type {p.name}: {p.type_str()}
"""
            txt += f"""
    :rtype: {ret_type}

.. mv-minigallery:: {fn.name} 
                """

            path_out = os.path.join(ICON_DIR, f"{name}.rst")
            with open(path_out, "w") as f_out:
                f_out.write(txt)
            log_generated(path_out)


def main():
    LOG.info("Generate icon documentation pages:")

    # create builder
    builder = IconDocBuilder()

    # process each yaml from icon/desc
    for f_name in glob.glob(os.path.join(DESC_DIR, "*.yaml")):
        name = format(os.path.basename(f_name).split(".yaml")[0])
        summary_file_name = os.path.join(DESC_DIR, name + ".rst")
        builder.build(name, f_name, summary_file_name)


if __name__ == "__main__":
    main()
else:
    main()
