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
from pathlib import Path
import re
import sys
import tempfile

import pandas as pd
import yaml

import metview as mv
from metview.indexer import GribIndexer, FieldsetIndexer, ExperimentIndexer
from metview.style import StyleDb, MapConf
from metview.track import Track
from metview import utils


ETC_PATH = os.path.join(os.path.dirname(__file__), "etc")

# logging.basicConfig(level=logging.INFO, format="%(levelname)s - %(message)s")
# logging.basicConfig(level=logging.DEBUG, format="%(levelname)s - %(message)s")
LOG = logging.getLogger(__name__)


class ParamInfo:
    """
    Determines the parameter properties from a user specified name
    """

    SUFFIXES = {
        "hPa": "isobaricInhPa",
        "hpa": "isobaricInhPa",
        "K": "theta",
        "ml": "hybrid",
    }
    LEVEL_TYPES = {"pl": "isobaricInhPa", "ml": "hybrid"}
    LEVEL_RE = re.compile(r"(\d+)")
    NUM_RE = re.compile(r"[0-9]+")
    SURF_RE = re.compile(r"^\d+\w+")
    # SURF_NAME_MAPPER = {"t2": "2t", "q2": "2q", "u10": "10u", "v10": "10v"}
    KNOWN_SURF_NAMES = ["2t", "2q", "10u", "10v", "msl", "wind10m"]
    VECTOR_NAMES = ["wind10m", "wind3d", "wind"]  # the longest ones first

    def __init__(self, name, level, level_type, scalar=True):
        self.name = name
        self.level = level
        self.level_type = level_type
        self.scalar = scalar

    @staticmethod
    def build(full_name, param_level_types=None):
        full_name = full_name
        # adjust surface names
        # if full_name in ParamInfo.SURF_NAME_MAPPER:
        #     full_name = ParamInfo.SURF_NAME_MAPPER[full_name]

        name = full_name
        level = None
        level_type = ""

        # the name is a known param name
        if param_level_types:
            if name in param_level_types:
                lev_t = param_level_types.get(name, [])
                if len(lev_t) == 1:
                    level_type = lev_t[0]
                scalar = not name in ParamInfo.VECTOR_NAMES
                return ParamInfo(name, level, level_type, scalar=scalar)

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
        return ParamInfo(name, level, level_type, scalar=scalar)

    @staticmethod
    def build_from_fieldset(fs):
        assert isinstance(fs, mv.Fieldset)
        f = fs[0:3] if len(fs) >= 3 else fs
        m = mv.grib_get(f, ["shortName", "level", "typeOfLevel"], "key")
        name = level = lev_type = ""
        if len(m[0]) == 3:
            if m[0] == ["u", "v", "w"] and len(set(m[1])) == 1 and len(set(m[2])) == 1:
                name = "wind3d"
                level = m[1][0]
                lev_type = m[2][0]
        if not name and len(m[0]) >= 2:
            if (
                m[0][0:2] == ["u", "v"]
                and len(set(m[1][0:2])) == 1
                and len(set(m[2][0:2])) == 1
            ):
                name = "wind"
                level = m[1][0]
                lev_type = m[2][0]
                if lev_type == "sfc":
                    name = "wind10"
        if not name:
            name = m[0][0]
            level = m[1][0]
            lev_type = m[2][0]

        if name:
            return ParamInfo(name, level, lev_type)
        else:
            return None

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

    def make_dims(self):
        dims = {}
        if self.name:
            dims["shortName"] = [self.name]
        if self.level:
            dims["level"] = [self.level]
        if self.level_type:
            dims["typeOfLevel"] = [self.level_type]
        return dims

    def __str__(self):
        return f"{self.__class__.__name__}[name={self.name}, level={self.level}, level_type={self.level_type}, scalar={self.scalar}]"


class IndexDb:
    ROOTDIR_PLACEHOLDER_TOKEN = "__ROOTDIR__"

    def __init__(
        self,
        name,
        label=None,
        desc=None,
        path=None,
        rootdir_placeholder_value=None,
        file_name_pattern=None,
        db_dir=None,
        blocks=None,
        data_files=None,
        merge_conf=None,
        mars_params=None,
        dataset=None,
    ):
        self.name = name
        self.dataset = dataset
        self.label = label
        if self.label is None or self.label == "":
            self.label = self.name
        self.desc = "" if desc is None else desc
        self.path = "" if path is None else path

        self.rootdir_placeholder_value = (
            "" if rootdir_placeholder_value is None else rootdir_placeholder_value
        )
        self.file_name_pattern = "" if file_name_pattern is None else file_name_pattern
        if self.file_name_pattern == "":
            self.path = os.path.dirname(self.path)
            self.file_name_pattern = os.path.basename(self.path)

        self.db_dir = "" if db_dir is None else db_dir
        self.mars_params = {} if mars_params is None else mars_params
        self.blocks = {} if blocks is None else blocks
        self.vector_loaded = False
        self._param_types = {}
        self.data_files = [] if data_files is None else data_files
        self.merge_conf = [] if merge_conf is None else merge_conf

    def select_with_name(self, name):
        """
        Perform a select operation where selection options are derived
        from the specified name.
        """
        p = self.get_param_info(name=name)
        # print(f"p={p}")
        if p is not None:
            fs = self._select_fs(**p.make_dims())
            # LOG.debug(f"fs={fs}")
            if fs is not None:
                fs._param_info = p
                return fs
        return None

    def select(self, **kwargs):
        return self._select_fs(**kwargs)

    def _select_fs(self, **kwargs):
        """
        Create a fieldset with the specified filter conditions. The resulting fieldset
        will contain an index db.
        """
        LOG.debug(f"kwargs={kwargs}")
        # LOG.debug(f"blocks={self.blocks}")
        dims = self._make_dims(kwargs)
        self.load(keys=list(dims.keys()), vector=("wind" in dims.get("shortName", "")))
        # fs = mv.Fieldset()
        db, fs = self._get_fields(dims)
        # for f in r:
        #     fs.append(f)
        fs._db = db
        # fs._param_info = self.get_param_info()
        # LOG.debug(f"fs={fs}")
        # LOG.debug(f"blocks={fs._db.blocks}")
        return fs

    def _get_fields(self, dims):
        res = mv.Fieldset()
        dfs = {}
        LOG.debug(f"dims={dims}")

        cnt = 0
        for key in self.blocks.keys():
            self._get_fields_for_block(key, dims, dfs, res)
        # LOG.debug(f"len_res={len(res)}")
        # LOG.debug(f"dfs={dfs}")
        # LOG.debug(f"res={res}")
        c = FieldsetDb(res, name=self.name, blocks=dfs)
        return c, res

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

    def _filter_df(self, df=None, dims={}):
        df_res = None
        if df is not None:
            q = self._build_query(dims)
            # LOG.debug("query={}".format(q))
            # print("query={}".format(q))
            # print("types={}".format(df.dtypes))
            if q != "":
                df_res = df.query(q)
                df_res.reset_index(drop=True, inplace=True)
                # print(f"df_res={df_res}")
                # LOG.debug(f"df_res={df_res}")
            else:
                return df
        return df_res

    def _get_fields_for_block(self, key, dims, dfs, res):
        # LOG.debug(f"block={self.blocks[key]}")
        if self.blocks[key] is None:
            self._load_block(key)
        df = self._filter_df(df=self.blocks[key], dims=dims)
        # LOG.debug(f"df={df}")
        if df is not None and not df.empty:
            df_fs = self._extract_fields(df, res)
            # LOG.debug(f"len_res={len(res)}")
            if df_fs is not None:
                # LOG.debug(f"df_fs={df_fs}")
                dfs[key] = df_fs

    # def _load_block(self, key):
    #     return None

    def get_param_info(self, name=""):
        if name:
            if "wind" in name and not self.vector_loaded:
                self.load(vector=True)
            return ParamInfo.build(name, param_level_types=self.param_types)
        elif self.blocks:
            df = self.blocks[list(self.blocks.keys())[0]]
            if df is not None and not df.empty:
                row = df.iloc[0]
                return ParamInfo(row.shortName, row.level, row.typeOfLevel)
        return None

    def _make_dims(self, options):
        dims = {}
        for k, v in options.items():
            name = str(k)
            vv = copy.deepcopy(v)
            name, vv = self._check_dims(name, vv)
            if vv:
                dims[name] = vv

        if dims.get("basedate", []) and (dims.get("date", []) or dims.get("time", [])):
            raise Exception("Cannot specify basedate together with date and time!")
        return dims

    def _check_dims(self, name, v):
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
        else:
            pd_type = GribIndexer.pd_types.get(name, None)
            if pd_type is not None:
                for i, t in enumerate(v):
                    v[i] = pd_type(t)
        if name is not None:
            name = name.replace(":", "_")

        return name, v

    def _check_type(self, v, name, dtypes):
        if not isinstance(v, dtypes):
            raise Exception(f"Invalid {name}={v} specified! Accepted types={dtypes}.")

    def _to_list(self, v):
        if not isinstance(v, list):
            v = [v]
        return v

    @property
    def param_types(self):
        if len(self._param_types) == 0:
            self.load()
            for k, df in self.blocks.items():
                df_u = df[["shortName", "typeOfLevel"]].drop_duplicates()
                for row in df_u.itertuples(name=None):
                    if not row[1] in self._param_types:
                        self._param_types[row[1]] = [row[2]]
                    else:
                        self._param_types[row[1]].append(row[2])
            # print(self._param_types)
        return self._param_types

    def to_df(self):
        return pd.concat([p for _, p in self.blocks.items()])

    def __str__(self):
        return "{}[name={}]".format(self.__class__.__name__, self.name)


class FieldsetDb(IndexDb):
    def __init__(self, fs, name="", **kwargs):
        super().__init__(name, **kwargs)
        self.fs = fs
        self._indexer = None

    @property
    def indexer(self):
        if self._indexer is None:
            self._indexer = FieldsetIndexer(self)
        return self._indexer

    def scan(self, vector=False):
        self.indexer.scan(vector=vector)
        self.vector_loaded = vector

    def load(self, keys=[], vector=False):
        # print(f"blocks={self.blocks}")
        if self.indexer.update_keys(keys):
            self.blocks = {}
            self._param_types = {}
            self.scan(vector=self.vector_loaded)
        elif not self.blocks:
            self._param_types = {}
            self.scan(vector=vector)
            self.vector_loaded = vector
        elif vector and not self.vector_loaded:
            self._param_types = {}
            self.indexer._scan_vector()
            self.vector_loaded = True

    def _extract_fields(self, df, fs):
        if df.empty:
            return None

        # print(f"cols={df.columns}")
        if "msgIndex3" in df.columns:
            comp_num = 3
        elif "msgIndex2" in df.columns:
            comp_num = 2
        elif "msgIndex1" in df.columns:
            comp_num = 1
        else:
            return None

        # print(f"comp_num={comp_num}")

        idx = [[] for k in range(comp_num)]
        comp_lst = list(range(comp_num))
        for row in df.itertuples():
            for comp in comp_lst:
                fs.append(self.fs[row[-1 - (comp_num - comp - 1)]])
                idx[comp].append(len(fs) - 1)
        # generate a new dataframe
        df = df.copy()
        for k, v in enumerate(idx):
            df[f"msgIndex{k+1}"] = v
        return df

    def _clone(self):
        db = FieldsetDb(
            self.name,
            label=self.label,
        )

        if self._indexer is not None:
            db.indexer.indexer.update_keys(self._indexer.keys_ecc)
        db.blocks = {k: v.copy() for k, v in self.blocks.items()}
        db.vector_loaded = self.vector_loaded
        return db

    def unique(self, key):
        r = set()
        for _, v in self.blocks.items():
            r.update(v[key].unique().tolist())
        return sorted(list(r))

    def style(self, plot_type="map"):
        return StyleDb.get_db().style(self.fs, plot_type=plot_type)

    def speed(self):
        r = mv.Fieldset()
        for i in range(len(self.fs) // 2):
            r.append(mv.sqrt(self.fs[2 * i] ** 2 + self.fs[2 * i + 1] ** 2))
        p = self.fs.param_info
        LOG.debug(f"speed p={p}")
        if p is not None:
            param_id = ""
            if p.name == "wind10":
                param_id = 207
            elif p.name == "wind":
                param_id = 10
            if param_id:
                LOG.debug("set")
                r = mv.grib_set_long(r, ["paramId", param_id])
                # r._scan()
                # LOG.debug(f"db={r._db.blocks}")
        return r

    def deacc(self):
        if len(self.fs) > 1:
            r = self.fs[0] * 0
            for i in range(1, len(self.fs)):
                f = self.fs[i] - self.fs[i - 1]
                r.append(f)
            r._db = self._clone()
            return mv.grib_set_long(r, ["generatingProcessIdentifier", 148])
        else:
            return fs


class ExperimentDb(IndexDb):
    def __init__(self, name, **kwargs):
        super().__init__(name, **kwargs)
        self.fs = {}
        self.vector_loaded = True
        LOG.debug(f"rootdir_placeholder_value={self.rootdir_placeholder_value}")

    @staticmethod
    def make_from_conf(name, conf, root_dir, db_root_dir, dataset):
        LOG.debug(f"conf={conf}")
        db = ExperimentDb(
            name,
            label=conf.get("label", ""),
            desc=conf.get("desc", ""),
            path=conf.get("dir", "").replace(
                IndexDb.ROOTDIR_PLACEHOLDER_TOKEN, root_dir
            ),
            rootdir_placeholder_value=root_dir
            if IndexDb.ROOTDIR_PLACEHOLDER_TOKEN in conf.get("dir", "")
            or "merge" in conf
            else "",
            file_name_pattern=conf.get("fname", ""),
            db_dir=os.path.join(db_root_dir, name),
            merge_conf=conf.get("merge", []),
            mars_params=conf.get("mars_params", []),
            blocks={},
            dataset=dataset,
        )
        return db

    def _clone(self):
        return ExperimentDb(
            self.name,
            label=self.label,
            db_dir=self.db_dir,
            mars_params=self.mars_params,
            dataset=self.dataset,
            data_files=self.data_files,
            rootdir_placeholder_value=self.rootdir_placeholder_value,
        )

    def scan(self, vector=True):
        print(f"Generate index for dataset component={self.name} ...")
        self.data_files = []
        # self.blocks = {}
        self.scalar = None
        self.wind = {}
        indexer = ExperimentIndexer(self)
        indexer.scan()

    def load(self, keys=[], vector=True):
        self.load_data_file_list()
        if len(self.data_files) == 0:
            self.scan(vector=True)
        if len(self.blocks) == 0:
            for key in ExperimentIndexer.get_storage_key_list(self.db_dir):
                self.blocks[key] = ExperimentIndexer.read_dataframe(key, self.db_dir)

    def load_data_file_list(self):
        if len(self.data_files) == 0:
            try:
                file_path = os.path.join(self.db_dir, "datafiles.yaml")
                with open(file_path, "rt") as f:
                    self.data_files = yaml.safe_load(f)
                if self.rootdir_placeholder_value:
                    self.data_files = [
                        x.replace(
                            IndexDb.ROOTDIR_PLACEHOLDER_TOKEN,
                            self.rootdir_placeholder_value,
                        )
                        for x in self.data_files
                    ]
                # LOG.debug(f"data_files={self.data_files}")
                for f in self.data_files:
                    assert os.path.isfile(f)
            except:
                pass

    def __getitem__(self, key):
        if isinstance(key, str):
            self.load()
            return self.select_with_name(key)
        return None

    # return a view
    def select(self, **kwargs):
        c = self._clone()
        dims = self._make_dims(kwargs)
        blocks = self._filter_blocks(dims)
        c.blocks = blocks
        # c.data_files = self.data_files
        # c.rootdir_placeholder_value = self.rootdir_placeholder_value
        return c

    def _filter_blocks(self, dims):
        self.load()
        dfs = {}
        # LOG.debug(f"data_files={self.data_files}")
        LOG.debug(f"dims={dims}")
        cnt = 0
        for key, df in self.blocks.items():
            # LOG.debug(f"key={key}")
            # df = self._load_block(key)
            # LOG.debug(f"df={df}")
            f_df = self._filter_df(df=df, dims=dims)
            # LOG.debug(f"df={df}"
            if f_df is not None and not f_df.empty:
                cnt += len(f_df)
                # LOG.debug(f" matching rows={len(df)}")
                dfs[key] = f_df

        LOG.debug(f"total matching rows={cnt}")
        return dfs

    def _extract_fields(self, df, fs):
        if df.empty:
            return None

        if "fileIndex3" in df.columns:
            comp_num = 3
        elif "fileIndex2" in df.columns:
            comp_num = 2
        elif "fileIndex1" in df.columns:
            comp_num = 1
        else:
            return None

        idx = [[] for k in range(comp_num)]
        comp_lst = list(range(comp_num))
        for row in df.itertuples():
            for comp in comp_lst:
                idx_file = row[-1 - (comp_num - comp - 1) * 2]
                idx_msg = row[-2 - (comp_num - comp - 1) * 2]
                if not idx_file in self.fs:
                    self.fs[idx_file] = mv.read(self.data_files[idx_file])
                fs.append(self.fs[idx_file][idx_msg])
                idx[comp].append(len(fs) - 1)
        # generate a new dataframe
        df = df.copy()
        for k, v in enumerate(idx):
            df[f"msgIndex{k+1}"] = v
        df.drop([f"fileIndex{x+1}" for x in range(comp_num)], axis=1, inplace=True)
        return df

    def describe(self):
        for k, v in self.param_types.items():
            print(f"{k}: {v}")


class TrackConf:
    def __init__(self, name, conf, data_dir, dataset):
        self.name = name
        self.dataset = dataset
        self.label = self.name
        self.path = conf.get("dir", "").replace(
            IndexDb.ROOTDIR_PLACEHOLDER_TOKEN, data_dir
        )
        self.file_name_pattern = conf.get("fname", "")
        # self.conf_dir = os.path.join("_conf", self.name)
        self.data_files = []

    def load_data_file_list(self):
        if len(self.data_files) == 0:
            self.data_files = mv.get_file_list(
                self.path, file_name_pattern=self.file_name_pattern
            )

    def select(self, name):
        tr = self._make(name)
        if tr is None:
            raise Exception(f"No track is available with name={name}!")
        return tr

    def _make(self, name):
        self.load_data_file_list()
        for f in self.data_files:
            if name == os.path.basename(f).split(".")[0]:
                return Track(f)
        return None


class Dataset:
    """
    Represents a Dataset
    """

    URL = "http://download.ecmwf.org/test-data/metview/dataset"
    LOCAL_ROOT = os.getenv(
        "MPY_DATASET_ROOT", os.path.join(os.getenv("HOME", ""), "dataset")
    )
    COMPRESSION = "bz2"

    def __init__(self, name, path="", load_style=True):
        self.name = name
        self.path = path
        self.field_conf = {}
        self.track_conf = {}

        assert self.name
        LOG.debug(f"name={self.name}")

        if self.path:
            # If the path does not exists, it must be a built-in dataset. Data will be
            # downloaded into path.
            if not os.path.isdir(self.path):
                if self.check_remote():
                    self.fetch(forced=True)
                else:
                    raise Exception(
                        f"Could not find dataset={self.name} on data server"
                    )
            else:
                raise Exception(
                    f"Could not find dataset={self.name} uder path={self.path}"
                )
        else:
            local_path = os.path.join(self.LOCAL_ROOT, self.name)
            # dataset exists locally
            if os.path.exists(local_path):
                self.path = local_path
            # dataset must be in the CACHE. Will be downloaded if necessary.
            else:
                self.path = os.path.join(utils.CACHE.ROOT_DIR, self.name)
                self.fetch(forced=False)

        if load_style:
            conf_dir = os.path.join(self.path, "conf")
            StyleDb.set_config(conf_dir)

        self.load()

        for _, c in self.field_conf.items():
            LOG.debug(f"{c}")

    @staticmethod
    def load_dataset(*args, **kwargs):
        return Dataset(*args, **kwargs)

    def check_remote(self):
        return not requests.get(f"{self.URL}/{self.name}") is None

    def load(self):
        data_dir = os.path.join(self.path, "data")
        index_dir = os.path.join(self.path, "_index_db")
        data_conf_file = os.path.join(self.path, "data_conf.yaml")
        with open(data_conf_file, "rt") as f:
            d = yaml.safe_load(f)
            for item in d["experiments"]:
                ((name, conf),) = item.items()
                if conf.get("type") == "track":
                    self.track_conf[name] = TrackConf(name, conf, data_dir, self)
                else:
                    c = ExperimentDb.make_from_conf(
                        name, conf, data_dir, index_dir, self
                    )
                    self.field_conf[c.name] = c

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

    def find(self, name, comp="field"):
        if comp == "all":
            f = self.field_conf.get(name, None)
            if f is not None:
                return f
            else:
                return self.track_conf.get(name, None)
        elif comp == "field":
            return self.field_conf.get(name, None)
        elif comp == "track":
            return self.track_conf.get(name, None)
        else:
            return None

    def describe(self):
        print("Dataset components:")
        t = {"name": [], "desc": []}
        for _, f in self.field_conf.items():
            t["name"].append(f.name)
            t["desc"].append(f.desc)
        df = pd.DataFrame.from_dict(t)
        df.reset_index(drop=True, inplace=True)
        print(df)

    def fetch(self, forced=False):
        if not os.path.isdir(self.path):
            Path(self.path).mkdir(0o755, parents=True, exist_ok=True)

        files = {
            "conf.tar": ["data_conf.yaml", "conf"],
            f"data.tar.{self.COMPRESSION}": ["data"],
        }

        for src, targets in files.items():
            if forced or not utils.CACHE.all_exists(targets, self.path):
                remote_file = os.path.join(self.URL, self.name, src)
                target_file = os.path.join(self.path, src)
                # LOG.debug(f"target_file={target_file}")
                try:
                    print("Download data ...")
                    utils.download(remote_file, target_file)
                    print("Unpack data ...")
                    utils.unpack(target_file, remove=True)
                    utils.CACHE.make_reference(targets, self.path)
                except:
                    # if os.exists(target_file):
                    #     os.remove(target_file)
                    raise Exception(f"Failed to download file={remote_file}")

    def __getitem__(self, key):
        if isinstance(key, str):
            return self.find(key, comp="all")
        return None
