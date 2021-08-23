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

import copy
import json
import logging
import os
from pathlib import Path

import yaml
import metview as mv
from metview.param import ParamInfo

# logging.basicConfig(level=logging.DEBUG)
LOG = logging.getLogger(__name__)

_DB = {
    "param": [None, "params.yaml", "param_styles.yaml"],
    "map": [None, "", "map_styles.yaml"],
}

_MAP_CONF = None
ETC_PATH = os.path.join(os.path.dirname(__file__), "etc")
CUSTOM_CONF_PATH = []
LOCAL_CONF_PATH = ""


PARAM_VISDEF_VERBS = ["mcont", "mwind", "mcoast", "msymb", "mgraph"]


# _DB = None


# def cont():
#     global _DB
#     if not _DB:
#         _DB = StyleDb()
#     return _DB


class ContourStyleDbItem:
    def __init__(self, name, db):
        self.name = name
        self.db = db
        self.keywords = []
        self.colours = []
        self.layers = []
        self.description = ""

    def list_match(self, lst, pattern):
        p = pattern.lower()
        for t in lst:
            if p in t.lower():
                return True
        return False

    def keyword_match(self, pattern):
        return self.list_match(self.keywords, pattern)

    def layer_match(self, pattern):
        return self.list_match(self.layers, pattern)

    def colour_match(self, pattern):
        return self.list_match(self.colours, pattern)

    def preview_file(self):
        if self.db.preview_path:
            return os.path.join(self.db.preview_path, self.name + ".png")
        else:
            return str()


class ContourStyleDb:
    def __init__(self):
        self.SHARE_DIR = os.path.join(
            mv.version_info()["metview_dir"], "share", "metview", "eccharts"
        )
        self.preview_path = os.path.join(self.SHARE_DIR, "style_previews")
        self.items = []
        self.keywords = []
        self.colours = []
        self.layers = []
        self._load()
        self._load_magics_def()

    def _load(self):
        file_path = os.path.join(self.SHARE_DIR, "styles.json")
        # print(f"file_path={file_path}")
        try:
            with open(file_path, "rt") as f:
                conf = json.load(f)
                col_set = set()
                key_set = set()
                layer_set = set()
                for name, c in conf.items():
                    item = ContourStyleDbItem(name, self)
                    item.colours = c.get("colours", [])
                    item.keywords = c.get("keywords", [])
                    item.layers = c.get("layers", [])
                    col_set.update(item.colours)
                    key_set.update(item.keywords)
                    layer_set.update(item.layers)
                    self.items.append(item)
            self.colours = sorted(list(col_set))
            self.keywords = sorted(list(key_set))
            self.layers = sorted(list(layer_set))
        except:
            pass
        #     LOG.exception("Failed to read eccharts styles", popup=True)

        self._load_magics_def()

    def find_by_name(self, name):
        for i, item in enumerate(self.items):
            if item.name == name:
                return i, item
        return -1, None

    def _load_magics_def(self):
        pass

    def names(self):
        return sorted([item.name for item in self.items])


class Visdef:
    # BUILDER = {
    #     "mcont": mv.mcont,
    #     "mwind": mv.mwind,
    #     "mcoast": mv.mcoast,
    #     "msymb": mv.msymb,
    #     "mgraph": mv.mgraph
    # }

    def __init__(self, verb, params):
        self.verb = verb.lower()
        self.params = params

        self.BUILDER = {
            "mcont": mv.mcont,
            "mwind": mv.mwind,
            "mcoast": mv.mcoast,
            "msymb": mv.msymb,
            "mgraph": mv.mgraph,
        }

    def clone(self):
        return Visdef(self.verb, copy.deepcopy(self.params))

    def change(self, verb, param, value):
        if verb == self.verb:
            self.params[param] = value

    def change_symbol_text_list(self, text_value, idx_value):
        assert self.verb == "msymb"
        if self.verb == "msymb":
            if self.params.get("symbol_type", "").lower() == "text":
                self.params["symbol_advanced_table_text_list"] = text_value
                self.params["symbol_advanced_table_level_list"] = idx_value

    def set_data_id(self, data_id):
        if self.verb in ["mcont", "mwind"] and data_id is not None and data_id != "":
            self.params["grib_id"] = data_id

    def set_values_list(self, values):
        if self.verb == "mcont":
            if self.params.get("contour_level_list", []):
                self.params["contour_level_list"] = values

    @staticmethod
    def from_request(req):
        params = {k: v for k, v in req.items() if not k.startswith("_")}
        vd = Visdef(req.verb.lower(), copy.deepcopy(params))
        return vd

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
        if not isinstance(visdefs, list):
            self.visdefs = [self.visdefs]

    def clone(self):
        return Style(self.name, [vd.clone() for vd in self.visdefs])

    def to_request(self):
        return [vd.to_request() for vd in self.visdefs]

    def update(self, *args, inplace=None, verb=None):
        s = self if inplace == True else self.clone()
        for i, v in enumerate(args):
            if i < len(s.visdefs):
                if isinstance(v, dict):
                    if verb is None or s.visdefs[i].verb in verb:
                        v = {v_key.lower(): v_val for v_key, v_val in v.items()}
                        s.visdefs[i].params.update(v)
        return s

    def set_data_id(self, data_id):
        allowed_verbs = ["mcont", "mwind"]
        if isinstance(data_id, str) and any(x in allowed_verbs for x in self.verbs()):
            return self.update({"grib_id": data_id}, verb=allowed_verbs)
        else:
            return self

    def verbs(self):
        return [vd.verb for vd in self.visdefs]

    def __str__(self):
        t = f"{self.__class__.__name__}[name={self.name}] "
        for vd in self.visdefs:
            t += f"{vd} "
        return t


class ParamMatchCondition:
    def __init__(self, cond):
        self.name = cond.pop("info_name", "")
        self.cond = cond
        if "levelist" in self.cond:
            if not isinstance(self.cond["levelist"], list):
                self.cond["levelist"] = [self.cond["levelist"]]
        # ParamInfo use "typeOfLevel" instead of "levtype" so we need to
        # change the key a remap values
        if "levtype" in self.cond:
            v = self.cond.pop("levtype")
            self.cond["typeOfLevel"] = v
            self.cond["typeOfLevel"] = ParamInfo.LEVEL_TYPES.get(v, v)

        for k, v in self.cond.items():
            if isinstance(v, list):
                self.cond[k] = [str(x) for x in v]
            else:
                self.cond[k] = str(v)

    def match(self, param_info):
        return param_info.match(self.name, self.cond)


class ParamStyle:
    def __init__(self, conf, db):
        self.cond = []
        for d in conf["match"]:
            if "info_name" in d:
                self.info_name = d["info_name"]
            self.cond.append(ParamMatchCondition(d))
        self.param_type = conf.get("param_type", "scalar")

        if self.param_type == "vector":
            default_style = db.VECTOR_DEFAULT_STYLE_NAME
        else:
            default_style = db.SCALAR_DEFAULT_STYLE_NAME

        s = conf.get("styles", {})
        self.style = s.get("basic", [default_style])
        self.xs_style = s.get("xs", self.style)
        self.diff_style = s.get("diff", [db.DIFF_DEFAULT_STYLE_NAME])

    def match(self, param):
        return max([d.match(param) for d in self.cond])

    def find_style(self, plot_type):
        if plot_type == "" or plot_type == "map":
            return self.style[0]
        elif plot_type == "diff":
            return self.diff_style[0]
        elif plot_type == "xs":
            return self.xs_style[0]
        else:
            return None

    def styles(self, plot_type):
        if plot_type == "" or plot_type == "map":
            return self.style
        elif plot_type == "diff":
            return self.diff_style
        elif plot_type == "xs":
            return self.xs_style
        else:
            return []

    def __str__(self):
        return "{}[name={},type={}]".format(
            self.__class__.__name__, self.info_name, self.param_type
        )


class StyleDb:
    SCALAR_DEFAULT_STYLE_NAME = "default_mcont"
    VECTOR_DEFAULT_STYLE_NAME = "default_mwind"
    DIFF_DEFAULT_STYLE_NAME = "default_diff"

    def __init__(self, param_file_name, style_file_name):
        self.params = []
        self.styles = {}
        self.param_file_name = param_file_name
        self.style_file_name = style_file_name

        self._load_system_config()
        self._load_custom_config()
        self._load_local_config()

    def _load_system_config(self):
        self._load(
            os.path.join(ETC_PATH, self.param_file_name)
            if self.param_file_name
            else "",
            os.path.join(ETC_PATH, self.style_file_name),
        )

    def _load_custom_config(self):
        if CUSTOM_CONF_PATH and CUSTOM_CONF_PATH[-1]:
            self._load(
                os.path.join(CUSTOM_CONF_PATH[-1], self.param_file_name)
                if self.param_file_name
                else "",
                os.path.join(CUSTOM_CONF_PATH[-1], self.style_file_name),
            )

    def _load_local_config(self):
        if LOCAL_CONF_PATH:
            self._load(
                os.path.join(LOCAL_CONF_PATH, self.param_file_name)
                if self.param_file_name
                else "",
                os.path.join(LOCAL_CONF_PATH, self.style_file_name),
            )

    def get_style(self, style):
        if style in self.styles:
            return self.styles[style]
        else:
            return self.styles.get("default", None)

    def _best_param_match(self, param_info):
        r = 0
        p_best = None
        for p in self.params:
            m = p.match(param_info)
            # print(f"p={p} m={m}")
            if m > r:
                r = m
                p_best = p
        return p_best

    def get_param_style_list(self, param_info, scalar=True, plot_type="map"):
        p_best = self._best_param_match(param_info)
        s = []
        # print(f"param_info={param_info}")
        if p_best is not None:
            s = p_best.styles(plot_type)
            # print(f" -> style_name={style_name}")
        if scalar:
            s.append(self.SCALAR_DEFAULT_STYLE_NAME)
        else:
            s.append(self.VECTOR_DEFAULT_STYLE_NAME)
        return s

    def get_param_style(self, param_info, scalar=True, plot_type="map", data_id=None):
        p_best = self._best_param_match(param_info)
        s = None
        # print(f"param_info={param_info}")
        if p_best is not None:
            style_name = p_best.find_style(plot_type)
            # print(f" -> style_name={style_name}")
            s = self.styles.get(style_name, None)
        else:
            if scalar:
                s = self.styles.get(self.SCALAR_DEFAULT_STYLE_NAME, None)
            else:
                s = self.styles.get(self.VECTOR_DEFAULT_STYLE_NAME, None)

        if s is not None:
            # print(f"data_id={data_id}")
            if data_id is not None:
                s = s.set_data_id(data_id)
                return s
            else:
                return s.clone()
        return None

    def style(self, fs, plot_type="map", data_id=None):
        param_info = fs.param_info
        if param_info is not None:
            vd = self.get_param_style(
                param_info,
                scalar=param_info.scalar,
                plot_type=plot_type,
                data_id=data_id,
            )
            # LOG.debug(f"vd={vd}")
            return vd
        return None

    def visdef(self, fs, plot_type="map", data_id=None):
        vd = self.style(fs, plot_type=plot_type, data_id=data_id)
        return vd.to_request() if vd is not None else None

    def style_list(self, fs, plot_type="map"):
        param_info = fs.param_info
        if param_info is not None:
            return self.get_param_style_list(
                param_info, scalar=param_info.scalar, plot_type=plot_type
            )
        return []

    def _make_defaults(self):
        d = {
            self.SCALAR_DEFAULT_STYLE_NAME: "mcont",
            self.VECTOR_DEFAULT_STYLE_NAME: "mwind",
            self.DIFF_DEFAULT_STYLE_NAME: "mcont",
        }
        for name, verb in d.items():
            if name not in self.styles:
                self.styles[name] = Style(name, Visdef(verb, {}))
        assert self.SCALAR_DEFAULT_STYLE_NAME in self.styles
        assert self.VECTOR_DEFAULT_STYLE_NAME in self.styles
        assert self.DIFF_DEFAULT_STYLE_NAME in self.styles

    def _load(self, param_path, style_path):
        if os.path.exists(style_path):
            with open(style_path, "rt") as f:
                c = yaml.safe_load(f)
                self._load_styles(c)
            if os.path.exists(param_path):
                with open(param_path, "rt") as f:
                    c = yaml.safe_load(f)
                    self._load_params(c, param_path)

    def _load_styles(self, conf):
        for name, d in conf.items():
            vd = []
            # print(f"name={name} d={d}")
            if not isinstance(d, list):
                d = [d]

            # print(f"name={name} d={d}")
            # for mcoast the verb can be missing
            if (
                len(d) == 1
                and isinstance(d[0], dict)
                and (len(d[0]) > 1 or not list(d[0].keys())[0] in PARAM_VISDEF_VERBS)
            ):
                vd.append(Visdef("mcoast", d[0]))
            else:
                for v in d:
                    ((verb, params),) = v.items()
                    vd.append(Visdef(verb, params))
            self.styles[name] = Style(name, vd)

    def _load_params(self, conf, path):
        # TODO: review defaults for maps
        self._make_defaults()

        for d in conf:
            assert isinstance(d, dict)
            # print(f"d={d}")
            p = ParamStyle(d, self)
            for v in [p.style, p.xs_style, p.diff_style]:
                # print(f"v={v}")
                for s in v:
                    if not s in self.styles:
                        raise Exception(
                            f"{self} Invalid style={s} specified in {d}! File={path}"
                        )

            self.params.append(p)

    def is_empty(self):
        return len(self.styles) == 0

    def __str__(self):
        return self.__class__.__name__

    def print(self):
        pass
        # print(f"{self} params=")
        # for k, v in self.params.items():
        #     print(v)
        # print(f"{self} styles=")
        # for k, v in self.styles.items():
        #     print(v)


class GeoView:
    def __init__(self, params, style):
        self.params = copy.deepcopy(params)
        for k in list(self.params.keys()):
            if k.lower() == "coastlines":
                self.params.pop("coastlines", None)
        self.style = style

    def to_request(self):
        v = copy.deepcopy(self.params)
        if self.style is not None and self.style:
            v["coastlines"] = self.style.to_request()
        return mv.geoview(**v)

    def __str__(self):
        t = f"{self.__class__.__name__}[params={self.params}, style={self.style}]"
        return t


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
        self.style_db = get_db(name="map")

        # load areas
        self._load_areas(os.path.join(ETC_PATH, "areas.yaml"))
        self._load_custom_config()
        self._load_local_config()

    def _load_custom_config(self):
        if CUSTOM_CONF_PATH and CUSTOM_CONF_PATH[-1]:
            self._load_areas(os.path.join(CUSTOM_CONF_PATH[-1], "areas.yaml"))

    def _load_local_config(self):
        if LOCAL_CONF_PATH:
            self._load_areas(os.path.join(LOCAL_CONF_PATH, "areas.yaml"))

    def _load_areas(self, file_path):
        if os.path.exists(file_path):
            with open(file_path, "rt") as f:
                # the file can be empty!
                d = yaml.safe_load(f)
                if isinstance(d, list):
                    for item in d:
                        ((name, conf),) = item.items()
                        self.areas[name] = conf

    def area_names(self):
        r = list(self.areas.keys())
        r.extend([a.lower() for a in self.BUILTIN_AREAS])
        return r

    def find(self, area=None, style=None):
        area_v = "base" if area is None else area
        style_v = "base" if style is None else style
        s = None
        if isinstance(area_v, list):
            if len(area_v) == 4:
                a = {
                    "area_mode": "user",
                    "map_projection": "cylindrical",
                    "map_area_definition": "corners",
                    "area": area_v,
                }
            else:
                raise Exception(
                    "Invalid list specified for area. Required format: [S,W,N,E]"
                )
        else:
            a = self.areas.get(area_v, {})
            if len(a) == 0 and area_v.upper() in self.BUILTIN_AREAS:
                a = {"area_mode": "name", "area_name": area}
        s = self.style_db.get_style(style_v)
        return a, s

    def make_geo_view(self, area=None, style=None, plot_type=None):
        if style is None and plot_type == "diff":
            style = "base_diff"

        a, s = self.find(area=area, style=style)
        if s is not None:
            s = s.clone()

        if plot_type == "stamp":
            s = s.update({"map_grid": "off", "map_label": "off"})

        if a is not None and a:
            a = copy.deepcopy(a)
        else:
            a = {}

        if s is not None and s:
            a["coastlines"] = s.to_request()

        return mv.geoview(**a)
        # return GeoView(a, s)


class StyleGallery:
    def __init__(self):
        pass

    def to_base64(self, image_path):
        import base64

        with open(image_path, "rb") as img_file:
            return base64.b64encode(img_file.read()).decode("utf-8")

    def build_gallery(self, names, images, row_height=None):
        figures = []
        # print(len(names))
        # print(len(images))
        row_height = "150px" if row_height is None else row_height
        for name, image in zip(names, images):
            src = f"data:image/png;base64,{image}"
            caption = f'<figcaption style="text-align: center; font-size: 0.8em">{name}</figcaption>'
            figures.append(
                f"""
                <figure style="margin: 2px !important;">
                <img src="{src}" style="height: {row_height}">
                {caption}
                </figure>
            """
            )
        return f"""
            <div style="display: flex; flex-flow: row wrap; text-align: center;">
            {''.join(figures)}
            </div>
        """

    def build(self):
        try:
            import IPython

            # test whether we're in the Jupyter environment
            if IPython.get_ipython() is None:
                return
        except:
            return

        img_size = 120
        img, names = self._build(img_size)

        # reset jupyter output settings
        mv.setoutput("jupyter", **mv.plot.jupyter_args)

        if len(img) > 0:
            from IPython.display import HTML

            return HTML(self.build_gallery(names, img, row_height=f"{img_size}px"))


class MapStyleGallery(StyleGallery):
    def _build(self, img_size):
        img = []
        names = []
        # img_size = 120
        tmp_dir = os.path.join(os.getenv("METVIEW_TMPDIR", ""), "_mapstyle_")
        Path(tmp_dir).mkdir(exist_ok=True)
        for name, d in map_styles().items():
            f_name = os.path.join(tmp_dir, name + ".png")
            if not os.path.exists(f_name):
                view = map(area=[30, -30, 75, 45], style=name)
                view.style.update({"MAP_COASTLINE_RESOLUTION": "low"}, inplace=True)
                mv.setoutput(
                    mv.png_output(
                        output_name=f_name[:-4],
                        output_width=300,
                        output_name_first_page_number="off",
                    )
                )
                mv.plot(view.to_request())
            if os.path.exists(f_name):
                names.append(name)
                img.append(self.to_base64(f_name))

        return (img, names)


class MapAreaGallery(StyleGallery):
    def _build(self, img_size):
        img = []
        names = []
        # img_size = 120
        tmp_dir = os.path.join(os.getenv("METVIEW_TMPDIR", ""), "_maparea_")
        Path(tmp_dir).mkdir(exist_ok=True)
        for name in map_area_names():
            f_name = os.path.join(tmp_dir, name + ".png")
            if not os.path.exists(f_name):
                view = map(area=name, style="grey_1")
                mv.setoutput(
                    mv.png_output(
                        output_name=f_name[:-4],
                        output_width=300,
                        output_name_first_page_number="off",
                    )
                )
                mv.plot(view.to_request())
            if os.path.exists(f_name):
                names.append(name)
                img.append(self.to_base64(f_name))

        return (img, names)


def MAP_CONF():
    global _MAP_CONF
    if _MAP_CONF is None:
        _MAP_CONF = MapConf()
    assert not _MAP_CONF is None
    return _MAP_CONF


def map_styles():
    return MAP_CONF().style_db.styles


def map_style_gallery():
    g = MapStyleGallery()
    return g.build()


def map_area_names():
    return MAP_CONF().area_names()


def map_area_gallery():
    g = MapAreaGallery()
    return g.build()


def make_geoview(**argv):
    return MAP_CONF().make_geo_view(**argv)


def get_db(name=None):
    global _DB
    name = "param" if name is None else name
    assert name in _DB
    if _DB[name][0] is None:
        _DB[name][0] = StyleDb(_DB[name][1], _DB[name][2])
    return _DB[name][0]


def find(name):
    db = get_db()
    s = db.styles.get(name, None)
    if s is not None:
        return s.clone()
    else:
        return None


def load_custom_config(conf_dir, force=None):
    global CUSTOM_CONF_PATH
    global _MAP_CONF
    force = False if force is None else force
    if CUSTOM_CONF_PATH:
        if CUSTOM_CONF_PATH[-1] == conf_dir:
            if force:
                CUSTOM_CONF_PATH.pop()
            else:
                return

    CUSTOM_CONF_PATH.append(conf_dir)
    for k, v in _DB.items():
        if v[0] is not None:
            v[0]._load_custom_config()
    if _MAP_CONF is not None:
        _MAP_CONF = None
        _MAP_CONF = MapConf()


def reset_config():
    global CUSTOM_CONF_PATH
    if CUSTOM_CONF_PATH:
        CUSTOM_CONF_PATH = []
        global _DB
        global _MAP_CONF
        for name, v in _DB.items():
            if v[0] is not None:
                v[0] = None
                get_db(name=name)
        if _MAP_CONF is not None:
            _MAP_CONF = None
            _MAP_CONF = MapConf()


if __name__ == "__main__":
    vd = StyleConf()
    vd.print()
else:
    pass
