#
# (C) Copyright 2017- ECMWF.
#
# This software is licensed under the terms of the Apache Licence Version 2.0
# which can be obtained at http://www.apache.org/licenses/LICENSE-2.0.
#
# In applying this licence, ECMWF does not waive the privileges and immunities
# granted to it by virtue of its status as an intergovernmental organisation
# nor does it submit to any jurisdiction.
#

import logging
import os

import yaml
import metview as mv

# logging.basicConfig(level=logging.DEBUG)
LOG = logging.getLogger(__name__)

_DB = {
    "param": (None, "param_style.yaml"),
    "diff": (None, "diff_style.yaml"),
    "map": (None, "map_style.yaml"),
}

ETC_PATH = os.path.join(os.path.dirname(__file__), "etc")
CUSTOM_CONF_PATH = ""
LOCAL_CONF_PATH = ""

# def get_db(name="param"):
#     global _DB
#     assert name in _DB
#     if _DB[name][0] is None:
#         _DB[name] = (StyleDb(_DB[name][1]), "")
#     return _DB[name][0]


class Visdef:
    # BUILDER = {
    #     "mcont": mv.mcont,
    #     "mwind": mv.mwind,
    #     "mcoast": mv.mcoast,
    #     "msymb": mv.msymb,
    #     "mgraph": mv.mgraph
    # }

    def __init__(self, verb, params):
        self.verb = verb
        self.params = params

        self.BUILDER = {
            "mcont": mv.mcont,
            "mwind": mv.mwind,
            "mcoast": mv.mcoast,
            "msymb": mv.msymb,
            "mgraph": mv.mgraph,
        }

    def clone(self):
        return Visdef(self.verb, dict(**self.params))

    def change(self, verb, param, value):
        if verb == self.verb:
            self.params[param] = value

    def change_symbol_text_list(self, value):
        assert self.verb == "msymb"
        if self.verb == "msymb":
            if self.params.get("symbol_type", "").lower() == "text":
                self.params["symbol_text_list"] = value

    def to_request(self):
        fn = self.BUILDER.get(self.verb, None)
        if fn is not None:
            return fn(**(self.params))
        else:
            raise Exception(f"{self} unsupported verb!")

    def __str__(self):
        return f"Visdef[verb={self.verb}, params={self.params}]"

    def __repr__(self):
        return f"Visdef(verb={self.verb}, params={self.params})"


class Style:
    def __init__(self, name, visdefs):
        self.name = name
        self.visdefs = visdefs

    def clone(self):
        return Style(self.name, [vd.clone() for vd in self.visdefs])

    def to_request(self):
        return [vd.to_request() for vd in self.visdefs]

    def __str__(self):
        t = f"{self.__class__.__name__}[name={self.name}] "
        for vd in self.visdefs:
            t += f"{vd} "
        return t


class ParamStyleGroup:
    def __init__(self, param_name, style, cond):
        self.param_name = param_name
        self.style = style
        self.cond = cond

    def match(self, param, plot_type):
        if "plot" in self.cond:
            return plot_type == self.cond["plot"]
        else:
            return param.match(
                self.param_name,
                self.cond.get("level_type", None),
                self.cond.get("level", None),
            )

    def __str__(self):
        return "{}[style={},cond={}]".format(
            self.__class__.__name__, self.style.name, self.cond
        )


class ParamStyle:
    def __init__(self, param_name, style):
        self.param_name = param_name
        self.style = style
        self.groups = []

    def find_style(self, param, plot_type):
        for gr in self.groups:
            if gr.match(param, plot_type):
                return gr.style
        return self.style

    def __str__(self):
        return "{}[param={},style={}] groups={}".format(
            self.__class__.__name__,
            self.param_name,
            self.style.name,
            [gr.__str__() for gr in self.groups],
        )


class StyleDbItem:
    def __init__(self, path, system=False):
        self.params = {}
        self.styles = {}
        self.system = system
        self._load(path)

    def get_style(self, style):
        if style in self.styles:
            return self.styles[style]
        else:
            return self.styles.get("default", None)

    def get_param_style(self, param, scalar=True, plot_type="map"):
        p = self.params.get(param.name, None)
        if p:
            return p.find_style(param, plot_type)
        else:
            if scalar:
                return self.styles.get("default_mcont", None)
            else:
                return self.styles.get("default_mwind", None)

    def _load(self, path):
        if not os.path.exists(path):
            return
        with open(path, "rt") as f:
            c = yaml.safe_load(f)
            if not "styles" in c:
                self._load_styles(c, path=path)
            else:
                self._load_styles(c["styles"], path=path)
                if "params" in c:
                    self._load_params(c["params"], path=path)

    def _load_styles(self, conf, path=""):
        for name, d in conf.items():
            vd = []
            # print(f"name={name} d={d}")
            for v in d:
                ((verb, params),) = v.items()
                vd.append(Visdef(verb, params))
            self.styles[name] = Style(name, vd)
        if self.system:
            self._make_defaults()

    def _make_defaults(self):
        for verb in ["mcont", "mwind"]:
            name = "default_" + verb
            if name not in self.styles:
                self.styles[name] = Style(name, Visdef(verb, {}))

    def _load_params(self, conf, path=""):
        for name, d in conf.items():
            # print(f"name={name} d={d}")
            if not "style" in d:
                raise Exception(
                    f"{self} No style defined for param={name}! File={path}"
                )
            style = d["style"]
            if not style in self.styles:
                raise Exception(
                    f"{self} Invalid style={style} specified for param={name}! File={path}"
                )
            style = self.styles[style]
            self.params[name] = ParamStyle(name, style)
            for gr in d.get("groups", []):
                if not "style" in gr:
                    raise Exception(
                        f"{self} No style defined for param={name} in group={gr}! File={path}"
                    )
                style = self.styles[gr.pop("style")]
                self.params[name].groups.append(ParamStyleGroup(name, style, gr))

    def visdef(self, fs, plot_type="map"):
        param = fs.param_info
        if param is not None:
            vd = self.get_param_style(param, scalar=param.scalar, plot_type=plot_type)
            LOG.debug(f"vd={vd}")
            if vd is not None:
                return vd.to_request()
        return None

    def is_empty(self):
        return len(self.params) == 0 or len(self.styles) == 0

    def __str__(self):
        return self.__class__.__name__

    def print(self):
        print(f"{self} params=")
        for k, v in self.params.items():
            print(v)
        # print(f"{self} styles=")
        # for k, v in self.styles.items():
        #     print(v)


class StyleDb:
    def __init__(self, conf_file_name):
        self.items = {"local": None, "custom": None, "system": None}
        self.items["system"] = StyleDbItem(
            os.path.join(ETC_PATH, conf_file_name), system=True
        )
        if CUSTOM_CONF_PATH:
            self.items["custom"] = StyleDbItem(
                os.path.join(CUSTOM_CONF_PATH, conf_file_name), system=False
            )
        if LOCAL_CONF_PATH:
            self.items["local"] = StyleDbItem(
                os.path.join(LOCAL_CONF_PATH, conf_file_name), system=False
            )

        for n in ["local", "custom"]:
            if self.items[n] is None or self.items[n].is_empty():
                self.items.pop(n)

        # LOG.debug(f"custom_conf_path={CUSTOM_CONF_PATH}")
        # LOG.debug(f"StyleDb items={self.items}")

    @staticmethod
    def get_db(name="param"):
        global _DB
        assert name in _DB
        if _DB[name][0] is None:
            _DB[name] = (StyleDb(_DB[name][1]), "")
        return _DB[name][0]

    def get_style(self, style):
        for _, item in self.items.items():
            vd = item.get_style(style)
            if vd is not None:
                return vd
        return None

    def visdef(self, fs, plot_type="map"):
        for _, item in self.items.items():
            vd = item.visdef(fs, plot_type=plot_type)
            if vd is not None:
                return vd
        # param = fs.param_info
        # if param is not None:
        #     vd = self.get_param_style(
        #         param, scalar=param.scalar, plot_type=plot_type
        #     ).to_request()
        #     LOG.debug(f"vd={vd}")
        #     return vd
        return None

    @staticmethod
    def set_config(conf_dir):
        global CUSTOM_CONF_PATH
        CUSTOM_CONF_PATH = conf_dir

    # def __init__(self, path):
    #     self.params = {}
    #     self.styles = {}
    #     self._load(os.path.join(PATH, path))

    # def get_style(self, style):
    #     if style in self.styles:
    #         return self.styles[style]
    #     else:
    #         return self.styles["default"]

    # def get_param_style(self, param, scalar=True, plot_type="map"):
    #     p = self.params.get(param.name, None)
    #     if p:
    #         return p.find_style(param, plot_type)
    #     else:
    #         if scalar:
    #             return self.styles["default_mcont"]
    #         else:
    #             return self.styles["default_mwind"]

    # def _load(self, path):
    #     with open(path, "rt") as f:
    #         c = yaml.safe_load(f)
    #         if not "styles" in c:
    #             self._load_styles(c, path=path)
    #         else:
    #             self._load_styles(c["styles"], path=path)
    #             if "params" in c:
    #                 self._load_params(c["params"], path=path)

    # def _load_styles(self, conf, path=""):
    #     for name, d in conf.items():
    #         vd = []
    #         # print(f"name={name} d={d}")
    #         for v in d:
    #             ((verb, params),) = v.items()
    #             vd.append(Visdef(verb, params))
    #         self.styles[name] = Style(name, vd)
    #     self._make_defaults()

    # def _make_defaults(self):
    #     for verb in ["mcont", "mwind"]:
    #         name = "default_" + verb
    #         if name not in self.styles:
    #             self.styles[name] = Style(name, Visdef(verb, {}))

    # def _load_params(self, conf, path=""):
    #     for name, d in conf.items():
    #         # print(f"name={name} d={d}")
    #         if not "style" in d:
    #             raise Exception(
    #                 f"{self} No style defined for param={name}! File={path}"
    #             )
    #         style = d["style"]
    #         if not style in self.styles:
    #             raise Exception(
    #                 f"{self} Invalid style={style} specified for param={name}! File={path}"
    #             )
    #         style = self.styles[style]
    #         self.params[name] = ParamStyle(name, style)
    #         for gr in d.get("groups", []):
    #             if not "style" in gr:
    #                 raise Exception(
    #                     f"{self} No style defined for param={name} in group={gr}! File={path}"
    #                 )
    #             style = self.styles[gr.pop("style")]
    #             self.params[name].groups.append(ParamStyleGroup(name, style, gr))

    # @staticmethod
    # def get_db(name="param"):
    #     global _DB
    #     assert name in _DB
    #     if _DB[name][0] is None:
    #         _DB[name] = (StyleDb(_DB[name][1]), "")
    #     return _DB[name][0]

    # def visdef(self, fs, plot_type="map"):
    #     param = fs.param_info
    #     if param is not None:
    #         vd = self.get_param_style(
    #             param, scalar=param.scalar, plot_type=plot_type
    #         ).to_request()
    #         LOG.debug(f"vd={vd}")
    #         return vd
    #     return None

    # @staticmethod
    # def set_config(conf_dir):
    #     StyleDB.CONFIG_PATH = conf_dir

    # def __str__(self):
    #     return self.__class__.__name__

    # def print(self):
    #     print(f"{self} params=")
    #     for k, v in self.params.items():
    #         print(v)
    #     # print(f"{self} styles=")
    #     # for k, v in self.styles.items():
    #     #     print(v)


class MapConf:
    items = []
    areas = []
    BUILTIN_AREAS = [
        "ANTARCTIC",
        "ARCTIC",
        "AUSTRALASIA",
        "CENTRAL_AMERICA",
        "CENTRAL_EUROPE",
        "EAST_TROPIC",
        "EASTERN_ASIA",
        "EQUATORIAL_PACIFIC",
        "EURASIA",
        "EUROPE",
        "GLOBAL",
        "MIDDLE_EAST_AND_INDIA",
        "NORTH_AMERICA",
        "NORTH_ATLANTIC",
        "NORTH_EAST_EUROPE",
        "NORTH_POLE",
        "NORTH_WEST_EUROPE",
        "NORTHERN_AFRICA",
        "PACIFIC",
        "SOUTH_AMERICA",
        "SOUTH_ATLANTIC_AND_INDIAN_OCEAN",
        "SOUTH_EAST_ASIA_AND_INDONESIA",
        "SOUTH_EAST_EUROPE",
        "SOUTH_POLE",
        "SOUTH_WEST_EUROPE",
        "SOUTHERN_AFRICA",
        "SOUTHERN_ASIA",
        "WEST_TROPIC",
        "WESTERN_ASIA",
    ]

    def __init__(self):
        self.areas = {}
        self.style_db = StyleDb.get_db(name="map")
        self._load(os.path.join(ETC_PATH, "maps.yaml"))
        if CUSTOM_CONF_PATH:
            self._load(os.path.join(CUSTOM_CONF_PATH, "maps.yaml"))
        if LOCAL_CONF_PATH:
            self._load(os.path.join(LOCAL_CONF_PATH, "maps.yaml"))

    def _load(self, file_path):
        with open(file_path, "rt") as f:
            for item in yaml.safe_load(f):
                ((name, conf),) = item.items()
                self.areas[name] = conf

    def find(self, area="base", style="grey_light_base"):
        a = self.areas.get(area, {})
        s = None
        if len(a) == 0 and area.upper() in self.BUILTIN_AREAS:
            a = {"area_mode": "name", "area_name": area}
        # if a is not None:
        s = self.style_db.get_style(style)
        return a, s

    def view(self, area="base"):
        a, s = self.find(area=area)
        # a["map_overlay_control"] = "by_date"
        if s is not None and s:
            a["coastlines"] = s.to_request()
        return mv.geoview(**a)


if __name__ == "__main__":
    vd = StyleConf()
    vd.print()
else:
    pass
