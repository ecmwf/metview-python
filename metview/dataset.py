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
import datetime
import logging
import os
import re

import pandas as pd
import yaml

import metview as mv
from metview.indexer import FieldsetIndexer, ExperimentIndexer


# logging.basicConfig(level=logging.INFO, format="%(levelname)s - %(message)s")
# logging.basicConfig(level=logging.DEBUG, format="%(levelname)s - %(message)s")
LOG = logging.getLogger(__name__)


class ParamInfo:
    """
    Determines the parameter properties from a user specified name
    """

    SUFFIXES = {"hPa": "isobaricInhPa", "hpa": "isobaricInhPa", "K": "theta", "ml": "hybrid"}
    LEVEL_TYPES = {"pl": "isobaricInhPa", "ml": "hybrid"}
    LEVEL_RE = re.compile(r"(\d+)")
    NUM_RE = re.compile(r"[0-9]+")
    SURF_NAMES = {"t2": "2t", "q2": "2q", "u10": "10u", "v10": "10v"}
    UPPER_NAMES = ["wind3d"]

    def __init__(self, name, level, level_type):
        self.name = name
        self.level = level
        self.level_type = level_type

    @staticmethod
    def build(self, full_name, param_types):
        self.full_name = full_name
        self.name = full_name
        self.level = None
        self.level_type = ""

        if self.full_name in self.SURF_NAMES:
            self.full_name = self.SURF_NAMES[self.full_name]
            self.name = self.full_name

        # LOG.debug(f"param_types={param_types}")
        lev_t = param_types.get(self.name, [])
        LOG.debug(f"lev_t={lev_t}")

        # the param full name is found in the conf
        if lev_t:
            if "isobaricInhPa" in lev_t:
                self.level_type = "isobaricInhPa"
            else:
                self.level_type = lev_t[0]
            # determine level value
            if not self.name in self.UPPER_NAMES:
                m = self.LEVEL_RE.search(self.name)
                if m and m.groups() and len(m.groups()) == 1:
                    self.level = int(m.group(1))
        elif self.name in self.UPPER_NAMES:
            raise Exception(
                f"Param={self.name} (deduced from name={full_name}) is not found in experiment!"
            )
        # the param full name has to parsed. The possible formats are:
        # t2, t, t500, t500hPa, q20m, z320K
        # If no level suffix is specified it is interpreted as
        # pressure level, unless it is a surface parameter.
        else:
            t = self.full_name
            # guess the level type from the suffix
            for k, v in self.SUFFIXES.items():
                if self.full_name.endswith(k):
                    self.level_type = v
                    t = self.full_name[: -(len(k))]
                    break

            # determine level value
            m = self.LEVEL_RE.search(t)
            if m and m.groups() and len(m.groups()) == 1:
                self.level = int(m.group(1))
                if self.level_type == "" and self.level > 10:
                    self.level_type = "isobaricInhPa"
                self.name = self.NUM_RE.sub("", t)

            # check param name in the conf
            lev_t = param_types.get(self.name, [])
            if lev_t:
                if not self.level_type:
                    self.level_type = lev_t[0]
                elif self.level_type not in lev_t:
                    raise Exception(
                        f"Level type cannot be deduced from param name={full_name}!"
                    )
            else:
                raise Exception(
                    f"Param={self.name} (deduced from name={full_name}) is not found in experiment!"
                )

        if self.level_type == "":
            self.level_type = "surface"

    @property
    def data_id(self):
        return f"{self.name}_{self.level_type}"

    def match(self, name, level_type, level):
        if self.name == name:
            if level_type:
                if level_type in self.LEVEL_TYPES:
                    level_type = self.LEVEL_TYPES[level_type]
                if level_type != self.level_type:
                    return False
                if level is not None:
                    if self.level is not None:
                        if level != self.level:
                            return False
                    else:
                        return False
            return True
        return False

    def __str__(self):
        return f"{self.__class__.__name__}[full_name={self.full_name}, name={self.name}, level={self.level}, level_type={self.level_type}]"


class IndexDb:
    DIMS = [
        "shortName",
        "mars.param",
        "basedate",
        "date",
        "time",
        "step",
        "level",
        "typeOfLevel",
        "number",
    ]

    def __init__(
        self,
        name,
        label="",
        path="",
        file_name_pattern="",
        conf_dir="",
        params={},
        data_files=[],
        merge_conf=[],
        mars_params={},
        dataset=None,
    ):
        self.name = name
        self.dataset = dataset
        self.label = label
        if self.label == "":
            self.label = self.name

        self.path = path
        self.file_name_pattern = file_name_pattern
        if self.file_name_pattern == "":
            self.path = os.path.dirname(path)
            self.file_name_pattern = os.path.basename(path)

        self.conf_dir = conf_dir
        self.mars_params = mars_params
        self.params = params
        self.wind = {}
        self._param_types = {}
        self.data_files = data_files
        self.merge_conf = merge_conf

    def scan(self):
        raise NotImplementedError

    def select(self, **kwargs):
        LOG.debug(f"kwargs={kwargs}")
        dims = {k: list() for k in IndexDb.DIMS}
        dims.update(copy.deepcopy(kwargs))
        for k, v in dims.items():
            # LOG.debug(f"dims[{k}]={v}")
            dims[k] = self._check_dim_values(v, name=k)

        if dims["basedate"] and (dims["date"] or dims["time"]):
            raise Exception("Cannot specify basedate together with date and time!")

        fs = mv.Fieldset()
        # fs.dims = {**self.dims}
        db, r = self.get_fields(dims, as_fieldset=True)
        for f in r:
            fs.append(f)
        fs._db = db
        # LOG.debug(f"params={fs.index_db.params}")
        return fs

    def _build_query(self, dims):
        q = ""
        for column, v in dims.items():
            if v:
                if q:
                    q += " and "
                if column == "basedate":
                    column = "date*10000 + time"
                if not isinstance(v, list):
                    q += f"{column} == {v}"
                else:
                    q += f"{column} in {v}"
        return q

    def filter(self, param=None, dims={}):
        # self.load_data_file_list()
        # p = self._load(param)
        df = None
        if param is not None:
            q = self._build_query(dims)
            # LOG.debug("query={}".format(q))
            if q != "":
                df = param.query(q)
                df.reset_index(drop=True, inplace=True)
                # LOG.debug(f"df={df}")
            else:
                return param
        return df

    def get_fields(self, dims, param=None, as_fieldset=False):
        # self.load_data_file_list()
        # self.load(name)
        # p = self.params.get(name + "_surface", None)
        # LOG.debug(f"df={df}")
        # fs = {}
        res = mv.Fieldset()
        dfs = {}

        # LOG.debug(f"data_files={self.data_files}")

        cnt = 0
        if len(dims["shortName"]) != 0:
            dims_tmp = {**dims}
            params = dims_tmp.pop("shortName")
            # levtypes = dims_tmp.pop("levelType")
            for par_name, par in self.params.items():
                if par_name[0] in params:
                    # LOG.debug(par_name)
                    df = self.filter(param=par, dims=dims_tmp)
                    # LOG.debug(f"df={df}")
                    if not df.empty:
                        df_fs = self._extract_fields(df, res)
                        if df_fs is not None:
                            # LOG.debug(f"df_fs={df_fs}")
                            dfs[par_name] = df_fs
        else:
            for par_name, par in self.params.items():
                # LOG.debug(f"par_name={par_name}")
                # LOG.debug(f"dtypes={par.dtypes}")
                df = self.filter(param=par, dims=dims)
                # LOG.debug(f"df={df}")
                if not df.empty:
                    df_fs = self._extract_fields(df, res)
                    if df_fs is not None:
                        # LOG.debug(f"df_fs={df_fs}")
                        dfs[par_name] = df_fs

        # LOG.debug(f"res={res}")
        c = FieldsetDb(res, params=dfs)
        return c, res

    def get_param_info(self):
        p = list(self.params.keys())
        if len(p) > 0:
            p = self.params[p[0]]
            return ParamInfo(p["shortName"][0], p["level"][0], p["typeOfLevel"][0])
        return None

    def _check_dim_values(self, v, name=None):
        v = self._to_list(v)
        if name == "basedate":
            for i, t in enumerate(v):
                self._check_type(t, name, datetime.datetime)
                v[i] = int(t.strftime("%Y%m%d%H%M"))
        elif name == "date":
            for i, t in enumerate(v):
                self._check_type(t, name, (datetime.datetime, datetime.date))
                v[i] = int(t.strftime("%Y%m%d"))
        elif name == "time":
            for i, t in enumerate(v):
                self._check_type(t, name, datetime.time)
                v[i] = int(t.strftime("%H%M"))
        return v

    def _check_type(self, v, name, dtypes):
        if not isinstance(v, dtypes):
            raise Exception(f"Invalid {name}={v} specified! Accepted types={dtypes}.")

    def _to_list(self, v):
        if not isinstance(v, list):
            v = [v]
        return v

    def to_df(self):
        return pd.concat([p for _, p in self.params.items()])

    def __str__(self):
        return "{}[name={}]".format(self.__class__.__name__, self.name)


class ExperimentDb(IndexDb):
    def __init__(self, name, **kwargs):
        super().__init__(name, **kwargs)
        self.fs = {}

    @staticmethod
    def make_from_conf(name, conf, root_dir, dataset):
        db = ExperimentDb(
            name,
            label=conf.get("label", ""),
            path=conf.get("dir", "").replace("__ROOTDIR__", root_dir),
            file_name_pattern=conf.get("fname", ""),
            conf_dir=os.path.join(root_dir, "_index", name),
            merge_conf=conf.get("merge", []),
            mars_params=conf.get("mars_params", []),
            dataset=dataset,
        )
        return db

    def _clone(self):
        return ExperimentDb(
            self.name,
            label=self.label,
            conf_dir=self.conf_dir,
            mars_params=self.mars_params,
            dataset=self.dataset,
        )

    def scan(self):
        indexer = ExperimentIndexer()
        indexer.scan(self)

    def load(self):
        self.load_data_file_list()
        for f in mv.get_file_list(os.path.join(self.conf_dir, "*_*.csv")):
            name = os.path.basename(f)
            name = name[:-4].split("_")
            assert len(name) == 2
            self.params[(name[0], name[1])] = None

    def load_data_file_list(self):
        if len(self.data_files) == 0:
            try:
                file_path = os.path.join(self.conf_dir, "datafiles.yaml")
                with open(file_path, "rt") as f:
                    self.data_files = yaml.safe_load(f)
            except:
                pass

    def _load(self, param):
        if not param in self.params or self.params[param] is None:
            f_name = os.path.join(self.conf_dir, f"{param[0]}_{param[1]}.csv")
            LOG.debug("fname={}".format(f_name))
            # self.params[param.data_id] = pd.read_csv(
            #     f_name, index_col=None, dtype={"date": str, "time": str, "expver": str}
            # )
            self.params[param] = pd.read_csv(f_name, index_col=None)
        return self.params[param]

    # return a view
    def select_view(self, **kwargs):
        c = self._clone()

        dims = {k: list() for k in IndexDb.DIMS}
        # dims = {}
        dims.update(copy.deepcopy(kwargs))
        LOG.debug(f"dims={dims}")
        for k, v in dims.items():
            # LOG.debug(f"dims[{k}]={v}")
            dims[k] = self._check_dim_values(v, name=k)

        if dims["basedate"] and (dims["date"] or dims["time"]):
            raise Exception("Cannot specify basedate together with date and time!")

        params = self._get_subset(dims)
        c.params = params
        c.data_files = self.data_files

        LOG.debug(f"kwargs={kwargs}")
        return c

    def _get_subset(self, dims):
        self.load()
        # self.load(name)
        # p = self.params.get(name + "_surface", None)
        # LOG.debug(f"df={df}")

        dfs = {}

        LOG.debug(f"data_files={self.data_files}")

        cnt = 0
        if len(dims["shortName"]) != 0:
            dims_tmp = {**dims}
            params = dims_tmp.pop("shortName")
            # levtypes = dims_tmp.pop("levelType")
            for par_name in self.params.keys():
                if par_name[0] in params:
                    LOG.debug(par_name)
                    d = self._load(par_name)
                    df = self.filter(param=d, dims=dims_tmp)
                    LOG.debug(f"df={df}")
                    if df is not None and not df.empty:
                        dfs[par_name] = df
        else:
            for par_name in self.params.keys():
                LOG.debug(f"par={par_name}")
                # LOG.debug(f"dtypes={par.dtypes}")
                d = self._load(par_name)
                df = self.filter(param=d, dims=dims)
                # LOG.debug(f"df={df}")
                if df is not None and not df.empty:
                    cnt += len(df)
                    LOG.debug(f" matching rows={len(df)}")
                    dfs[par_name] = df

        LOG.debug(f"total matching rows={cnt}")

        return dfs

    def _extract_fields(self, df, fs):
        if "fileIndex" in df.columns:
            idx = []
            for row in df.itertuples():
                # LOG.debug(f"row={row}")
                if not row.fileIndex in self.fs:
                    self.fs[row.fileIndex] = mv.read(self.data_files[row.fileIndex])
                fs.append(self.fs[row.fileIndex][row.msgIndex])
                idx.append(len(fs) - 1)
                # LOG.debug("row={}".format(row))
            # generate a new dataframe
            df = df.copy()
            # df.rename(columns={"fileIndex": "index"})
            df["msgIndex"] = idx
            df.drop(["fileIndex"], axis=1, inplace=True)
            return df
        return None


class FieldsetDb(IndexDb):
    def __init__(self, fs, extra_keys=[], **kwargs):
        super().__init__("file", **kwargs)
        self.name = "file"
        self.fs = fs
        self.extra_keys = extra_keys
        # self.scan()

    def scan(self):
        indexer = FieldsetIndexer()
        indexer.scan(self)

    def _extract_fields(self, df, fs):
        if "msgIndex" in df.columns:
            idx = []
            for row in df.itertuples():
                # LOG.debug(f"row={row}")
                fs.append(self.fs[row.msgIndex])
                idx.append(len(fs) - 1)
                # m = mv.grib_get(self.fs[row.msgIndex], ["shortName", "date", "time"])
                # LOG.debug(f"meta={m}")
                # LOG.debug("row={}".format(row))
            # generate a new dataframe
            df = df.copy()
            df["msgIndex"] = idx
            return df
        return None


class Dataset:
    """
    Represents a Dataset
    """

    def __init__(self, name="", path=""):
        self.field_conf = {}
        self.track_conf = None

        if name != "" and path != "":
            raise Exception(f"{self.__class__.__name__} cannot take both name and path!")

        if name != "":
            # root_dir = os.getnev("TMPDIR", "")
            root_dir = "/Users/sandor/metview/OpenIFS/2021"
            root_dir = os.path.join(root_dir, name)
            conf_file = os.path.join(root_dir, "config.yaml")
        elif path != "":
            if os.path.isdir(path):
                conf_file = os.path.join("path", "config.yaml")
                root_dir = path
            else:
                raise
            # path = "exp.yaml"

        with open(conf_file, "rt") as f:
            d = yaml.safe_load(f)
            for item in d["experiments"]:
                ((name, conf),) = item.items()
                if conf.get("type") == "Xtrack":
                    self.track_conf = TrackConf(name, conf, dataset=self)
                else:
                    c = ExperimentDb.make_from_conf(name, conf, root_dir, self)
                    self.field_conf[c.name] = c

        for _, c in self.field_conf.items():
            LOG.debug(f"{c}")

    def scan(self, name=None):
        # indexer = ExperimentIndexer()
        if name:
            if name in self.field_conf:
                self.field_conf[name].scan()
                # indexer.scan(self.field_conf[name], to_disk=True)
        else:
            for name, c in self.field_conf.items():
                LOG.info("-" * 40)
                c.scan()
                # indexer.scan(c, to_disk=True)

    def select(self, exp_id="", **kwargs):
        item = self.field_conf.get(exp_id, None)
        if item is None:
            raise Exception(f"No experiment found with id={exp_id}")
        # LOG.debug("date={} time={} step={}".format(date, time, step))
        # date = int(date.strftime("%Y%m%d"))
        # time = int(time.strftime("%H"))
        return item.select(**kwargs)

    def select_view(self, exp_id="", **kwargs):
        item = self.field_conf.get(exp_id, None)
        if item is None:
            raise Exception(f"No experiment found with id={exp_id}")
        return item.select_view(**kwargs)

    def find(self, name):
        return self.field_conf.get(name, None)

    def select_track(self, name):
        if self.tracks is not None:
            return self.tracks.select(name)
        else:
            raise Exception(f"No track data is available!")
