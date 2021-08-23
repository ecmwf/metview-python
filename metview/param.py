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
from metview import dataset
import re
import pandas as pd

import metview as mv
from metview.indexer import GribIndexer

# logging.basicConfig(level=logging.INFO, format="%(levelname)s - %(message)s")
# logging.basicConfig(level=logging.DEBUG, format="%(levelname)s - %(message)s")
LOG = logging.getLogger(__name__)

PANDAS_ORI_OPTIONS = {}


def init_pandas_options():
    global PANDAS_ORI_OPTIONS
    if len(PANDAS_ORI_OPTIONS) == 0:
        opt = {
            "display.max_colwidth": 300,
            "display.colheader_justify": "center",
            "display.max_columns": 100,
            "display.max_rows": 500,
            "display.width": None,
        }
        for k, _ in opt.items():
            PANDAS_ORI_OPTIONS[k] = pd.get_option(k)
        for k, v in opt.items():
            pd.set_option(k, v)


def reset_pandas_options():
    global PANDAS_ORI_OPTIONS
    if len(PANDAS_ORI_OPTIONS) > 0:
        for k, v in PANDAS_ORI_OPTIONS.items():
            pd.set_option(k, v)
        PANDAS_ORI_OPTIONS = {}


class ParamInfo:
    SUFFIXES = {
        "hPa": "isobaricInhPa",
        "hpa": "isobaricInhPa",
        "K": "theta",
        "ml": "hybrid",
    }
    LEVEL_TYPES = {"sfc": "surface", "pl": "isobaricInhPa", "ml": "hybrid"}
    LEVEL_RE = re.compile(r"(\d+)")
    NUM_RE = re.compile(r"[0-9]+")
    SURF_RE = re.compile(r"^\d+\w+")
    # SURF_NAME_MAPPER = {"t2": "2t", "q2": "2q", "u10": "10u", "v10": "10v"}
    KNOWN_SURF_NAMES = ["2t", "2q", "10u", "10v", "msl", "wind10m"]
    VECTOR_NAMES = ["wind10m", "wind3d", "wind"]  # the longest ones first

    def __init__(self, name, meta=None, scalar=None):
        self.name = name
        self.scalar = scalar if scalar is not None else True
        self.meta = {} if meta is None else meta
        if len(self.meta) == 0:
            self.meta["shortName"] = name

    def make_filter(self):
        dims = {}
        if self.name:
            dims["shortName"] = [self.name]
        for n in ["level", "typeOfLevel"]:
            v = self.meta.get(n, None)
            if v is not None:
                dims[n] = [v]
        return dims

    @staticmethod
    def build_from_name(full_name, param_level_types=None):
        full_name = full_name
        name = full_name
        level = None
        level_type = ""

        # the name is a known param name
        if param_level_types:
            if name in param_level_types:
                lev_t = param_level_types.get(name, [])
                meta = {}
                if len(lev_t) == 1:
                    meta = {"typeOfLevel": lev_t[0], "level": None}
                scalar = not name in ParamInfo.VECTOR_NAMES
                return ParamInfo(name, meta=meta, scalar=scalar)

        t = full_name
        # surface fields
        if t in ParamInfo.KNOWN_SURF_NAMES or ParamInfo.SURF_RE.match(t) is not None:
            level_type = "surface"

        else:
            # guess the level type from the suffix
            for k, v in ParamInfo.SUFFIXES.items():
                if full_name.endswith(k):
                    level_type = v
                    t = full_name[: -(len(k))]
                    break

            # recognise vector params
            for v in ParamInfo.VECTOR_NAMES:
                if t.startswith(v):
                    name = v
                    t = t[len(v) :]
                    break

            # determine level value
            m = ParamInfo.LEVEL_RE.search(t)
            if m and m.groups() and len(m.groups()) == 1:
                level = int(m.group(1))
                if level_type == "" and level > 10:
                    level_type = "isobaricInhPa"
                if name == full_name:
                    name = ParamInfo.NUM_RE.sub("", t)

        # check param name in the conf
        if param_level_types:
            if not name in param_level_types:
                raise Exception(
                    f"Param={name} (guessed from name={full_name}) is not found in dataset!"
                )

            lev_t = param_level_types.get(name, [])
            if lev_t:
                if not level_type and len(lev_t) == 1:
                    level_type = lev_t[0]
                elif level_type and level_type not in lev_t:
                    raise Exception(
                        f"Level type cannot be guessed from param name={full_name}!"
                    )

        if level_type == "":
            level = None
        scalar = not name in ParamInfo.VECTOR_NAMES

        LOG.debug(f"scalar={scalar}")
        meta = {"level": level, "typeOfLevel": level_type}
        return ParamInfo(name, meta=meta, scalar=scalar)

    @staticmethod
    def build_from_fieldset(fs):
        assert isinstance(fs, mv.Fieldset)
        f = fs[0:3] if len(fs) >= 3 else fs
        m = ParamInfo._grib_get(f, GribIndexer.DEFAULT_ECC_KEYS)
        name = level = lev_type = ""
        scalar = True

        meta_same = True
        for x in m.keys():
            if x != "shortName" and m[x].count(m[x][0]) != len(m[x]):
                same = False
                break
        if meta_same:
            if len(m["shortName"]) == 3 and m["shortName"] == ["u", "v", "w"]:
                name = "wind3d"
                scalar = False
            elif len(m["shortName"]) >= 2:
                if m["shortName"][0:2] == ["u", "v"]:
                    name = "wind"
                    scalar = False
                elif m["shortName"][0:2] == ["10u", "10v"]:
                    name = "wind10m"
                    m["level"][0] = 0
                    m["typeOfLevel"][0] = "sfc"
                    scalar = False
        if not name:
            name = m["shortName"][0]

        if name:
            return ParamInfo(name, meta={k: v[0] for k, v in m.items()}, scalar=scalar)
        else:
            return None

    def _meta_match(self, meta, key):
        local_key = key if key != "levelist" else "level"
        if (
            key in meta
            and meta[key] is not None
            and meta[key]
            and local_key in self.meta
        ):
            # print(f"local={self.meta[local_key]} other={meta[key]}")
            if isinstance(meta[key], list):
                return str(self.meta[local_key]) in meta[key]
            else:
                return meta[key] == str(self.meta[local_key])
        else:
            return False

    def match(self, name, meta):
        # print(f"{self}, name={name}, meta={meta}")
        r = 0
        if self.name == name:
            r += 3
        for n in ["shortName", "paramId"]:
            if self._meta_match(meta, n):
                r += 1
        # we only check the rest if the param is ok
        if r > 0:
            if self._meta_match(meta, "typeOfLevel"):
                r += 1
                if self._meta_match(meta, "levelist"):
                    r += 1

        return r

    def update_meta(self, meta):
        self.meta = {**meta, **self.meta}

    @staticmethod
    def _grib_get(f, keys):
        md = mv.grib_get(f, keys, "key")
        m = {}
        for k, v in zip(keys, md):
            key_val = k.split(":")[0]
            val = v
            if k.endswith(":l"):
                val = []
                for x in v:
                    try:
                        val.append(int(x))
                    except:
                        val.append(None)
            m[key_val] = val
        return m

    def __str__(self):
        return "{}[name={}, scalar={}, meta={}]".format(
            self.__class__.__name__, self.name, self.scalar, self.meta
        )


class ParamDesc:
    def __init__(self, name):
        self.db = None
        # self.name = name
        self.md = {}
        self.levels = {}
        self._short_name = None
        self._param_id = None
        self._long_name = None
        self._units = None

    def load(self, db):
        raise NotImplementedError

    def _parse(self, md):
        if "level" in md and len(md["level"]) > 0:
            df = pd.DataFrame(md)
            md.pop("typeOfLevel")
            md.pop("level")
            for md_key in list(md.keys()):
                d = df[md_key].unique().tolist()
                self.md[md_key] = d

            lev_types = df["typeOfLevel"].unique().tolist()
            for t in lev_types:
                # print(f" t={t}")
                self.levels[t] = []
                q = f"typeOfLevel == '{t}'"
                # print(q)
                dft = df.query(q)
                if dft is not None:
                    self.levels[t] = dft["level"].unique().tolist()

    @property
    def short_name(self):
        if self._short_name is None:
            self._short_name = ""
            if self.md["shortName"]:
                self._short_name = self.md["shortName"][0]
        return self._short_name

    @property
    def param_id(self):
        if self._param_id is None:
            self._param_id = ""
            if self.md["paramId"]:
                self._param_id = self.md["paramId"][0]
        return self._param_id

    @property
    def long_name(self):
        if self._long_name is None:
            self._long_name = ""
            if self.db is not None:
                self._long_name, self._units = self.db.get_longname_and_units(
                    self.short_name, self.param_id
                )
        return self._long_name

    @property
    def units(self):
        if self._units is None:
            self._units = ""
            if self.db:
                self._long_name, self._units = self.db.get_longname_and_units(
                    self.short_name, self.param_id
                )
        return self._units

    @staticmethod
    def describe(db, param=None):
        in_jupyter = False
        labels = {"marsClass": "class", "marsStream": "stream", "marsType": "type"}
        try:
            import IPython

            # test whether we're in the Jupyter environment
            if IPython.get_ipython() is not None:
                in_jupyter = True
        except:
            pass

        # describe all the params
        if param is None:
            t = {"parameter": [], "typeOfLevel": [], "level": []}
            need_number = False
            for k, v in db.param_meta.items():
                if not v.md.get("number", None) in [["0"], [None]]:
                    need_number = True
                    break

            for k, v in db.param_meta.items():
                t["parameter"].append(k)
                if len(v.levels) > 1:
                    lev_type = ""
                    level = ""
                    cnt = 0
                    for md_k, md in v.levels.items():
                        if in_jupyter:
                            lev_type += md_k + "<br>"
                            level += str(ParamDesc.format_list(md)) + "<br>"
                        else:
                            prefix = " " if cnt > 0 else ""
                            lev_type += prefix + f"[{cnt+1}]:" + md_k
                            level += (
                                prefix + f"[{cnt+1}]:" + str(ParamDesc.format_list(md))
                            )
                        cnt += 1
                    t["typeOfLevel"].append(lev_type)
                    t["level"].append(level)
                else:
                    for md_k, md in v.levels.items():
                        t["typeOfLevel"].append(md_k)
                        t["level"].append(ParamDesc.format_list(md))

                for md_k, md in v.md.items():
                    if md_k != "number" or need_number:
                        md_k = labels.get(md_k, md_k)
                        if not md_k in t:
                            t[md_k] = []
                        t[md_k].append(ParamDesc.format_list(md))

            if in_jupyter:
                txt = ParamDesc._make_html_table(t)
                from IPython.display import HTML

                return HTML(txt)
            else:
                df = pd.DataFrame.from_dict(t)
                df = df.set_index(["parameter"])
                init_pandas_options()
                print(df)

        # specific param
        else:
            v = None
            if isinstance(param, str):
                v = db.param_meta.get(param, None)
            elif isinstance(param, int):
                v = db.param_id_meta(param)

            if v is None:
                print(f"No shortName/paramId={param} found in data!")
                return

            #  if v is not None:
            t = {
                "key": ["shortName"],
                "val": [v.short_name],
            }

            if v.long_name != "" or v.units != "":
                t["key"].append("name")
                t["val"].append(v.long_name)

            t["key"].append("paramId")
            t["val"].append(v.param_id)
            # ParamDesc.format_list(v.md["shortName"], full=True),

            if v.long_name != "" or v.units != "":
                t["key"].append("units")
                t["val"].append(v.units)

            add_cnt = len(v.levels) > 1
            cnt = 0
            for md_k, md in v.levels.items():
                t["key"].append("typeOfLevel" + (f"[{cnt+1}]" if add_cnt else ""))
                t["val"].append(md_k)
                t["key"].append("level" + (f"[{cnt+1}]" if add_cnt else ""))
                t["val"].append(ParamDesc.format_list(md, full=True))
                cnt += 1

            for kk, md_v in v.md.items():
                if kk == "number" and md_v == ["0"]:
                    continue
                if not kk in ["shortName", "paramId"]:
                    t["key"].append(labels.get(kk, kk))
                    t["val"].append(ParamDesc.format_list(md_v, full=True))

            if in_jupyter:
                from IPython.display import HTML

                txt = ParamDesc._make_html_table(t, header=False)
                return HTML(txt)
            else:
                df = pd.DataFrame.from_dict(t)
                df = df.set_index("key")
                init_pandas_options()
                print(df)

    @staticmethod
    def _make_html_table(d, header=None):
        header = header if header is not None else True
        if len(d) > 1:
            first_column_name = list(d.keys())[0]
            txt = """  
                <table>
                <tr>{}</tr>
                {}
                </table>""".format(
                "" if not header else "".join([f"<th>{k}</th>" for k in d.keys()]),
                "".join(
                    [
                        "<tr><th style='text-align: right;'>"
                        + d[first_column_name][i]
                        + "</th>"
                        + "".join(
                            [
                                f"<td style='text-align: left;'>{ParamDesc.format_list(d[k][i], full=True)}</td>"
                                for k in list(d.keys())[1:]
                            ]
                        )
                        + "</tr>"
                        for i in range(len(d[first_column_name]))
                    ]
                ),
            )
            return txt
        else:
            return ""

    @staticmethod
    def format_list(v, full=None):
        if isinstance(v, list):
            if full is True:
                return ",".join([str(x) for x in v])
            else:
                if len(v) == 1:
                    return v[0]
                if len(v) > 2:
                    return ",".join([str(x) for x in [v[0], v[1], "..."]])
                else:
                    return ",".join([str(x) for x in v])
        else:
            return v


class ParamNameDesc(ParamDesc):
    def __init__(self, name):
        super().__init__(name)
        self._short_name = name

    def load(self, db):
        md = {
            "typeOfLevel": [],
            "level": [],
            "date": [],
            "time": [],
            "step": [],
            "number": [],
            "paramId": [],
            "marsClass": [],
            "marsStream": [],
            "marsType": [],
            "experimentVersionNumber": [],
        }

        self.db = db
        self.md = {}
        self.levels = {}

        # print(f"par={par}")
        for b_name, b_df in db.blocks.items():
            if b_name == "scalar":
                q = f"shortName == '{self.short_name}'"
                dft = b_df.query(q)
            elif b_name == self.short_name:
                dft = b_df
            else:
                dft = None

            if dft is not None:
                for k in md.keys():
                    # print(f"{self.name}/{k}")
                    md[k].extend(dft[k].tolist())
                    # print(f"   df[{k}]={df[k]}")
            # print(df)

        self._parse(md)


class ParamIdDesc(ParamDesc):
    def __init__(self, param_id):
        super().__init__("")
        self._param_id = param_id

    def load(self, db):
        md = {
            "shortName": [],
            "typeOfLevel": [],
            "level": [],
            "date": [],
            "time": [],
            "step": [],
            "number": [],
            "paramId": [],
            "marsClass": [],
            "marsStream": [],
            "marsType": [],
            "experimentVersionNumber": [],
        }

        self.db = db
        self.md = {}
        self.levels = {}

        # print(f"par={par}")
        b_df = db.blocks.get("scalar", None)
        if b_df is not None:
            q = f"paramId == '{self._param_id}'"
            dft = b_df.query(q)
            if dft is not None:
                for k in md.keys():
                    md[k].extend(dft[k].tolist())
                self._parse(md)
