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

import pandas as pd

import metview as mv
from metview.indexer import FieldsetIndexer, ExperimentIndexer

logging.basicConfig(level=logging.DEBUG, format="%(levelname)s - %(message)s")
# logging.basicConfig(level=logging.DEBUG, format="%(levelname)s - %(message)s")
LOG = logging.getLogger(__name__)


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
        # dims = {}
        dims.update({**kwargs})
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
            df = param.query(q)
            # LOG.debug(f"df={df}")
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

    # def _extract_fields(self, df, fs):
    #     res = mv.Fieldset()
    #     fs = {}
    #     if "fileIndex" in df.columns:
    #         for row in df.itertuples():
    #             LOG.debug(f"row={row}")
    #             if not row.fileIndex in fs:
    #                 fs[row.fileIndex] = mv.read(self.data_files[row.fileIndex])
    #             res.append(fs[row.fileIndex][row.index])
    #             # LOG.debug("row={}".format(row))

    #     return res

    # def get_one_v1(self, df, fs):
    #     self.fs = {}
    #     if "fileIndex" in df.columns:
    #         idx = []
    #         for row in df.itertuples():
    #             LOG.debug(f"row={row}")
    #             if not row.fileIndex in self.fs:
    #                 fs[row.fileIndex] = mv.read(self.data_files[row.fileIndex])
    #             fs.append(fs[row.fileIndex][row.index])
    #             idx.appned(len(fs)-1)
    #             # LOG.debug("row={}".format(row))
    #             return df['fileIndex'] = idx
    #     return None

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
            conf_dir=os.path.join("_conf_index", name),
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

        dims = {k: list() for k in IndexedDb.DIMS}
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
                fs.append(self.fs[row.fileIndex][row.index])
                idx.append(len(fs) - 1)
                # LOG.debug("row={}".format(row))
            # generate a new dataframe
            df = df.copy()
            # df.rename(columns={"fileIndex": "index"})
            df["index"] = idx
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
        if "index" in df.columns:
            idx = []
            for row in df.itertuples():
                # LOG.debug(f"row={row}")
                fs.append(self.fs[row.index])
                idx.append(len(fs) - 1)
                m = mv.grib_get(self.fs[row.index], ["shortName", "date", "time"])
                # LOG.debug(f"meta={m}")
                # LOG.debug("row={}".format(row))
            # generate a new dataframe
            df = df.copy()
            df["index"] = idx
            return df
        return res


class Dataset:
    """
    Represents a Dataset
    """

    def __init__(self, path="", root_dir=""):
        self.field_conf = {}
        self.track_conf = None

        if path != "":
            path = "exp.yaml"

        with open(path, "rt") as f:
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
