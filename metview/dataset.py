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
import logging
import os
from pathlib import Path


import pandas as pd
import requests
import yaml

import metview as mv
from metview import param
from metview.indexer import GribIndexer, FieldsetIndexer, ExperimentIndexer
from metview.track import Track
from metview.param import ParamInfo, ParamNameDesc, ParamIdDesc, init_pandas_options
from metview import utils


ETC_PATH = os.path.join(os.path.dirname(__file__), "etc")

# logging.basicConfig(level=logging.INFO, format="%(levelname)s - %(message)s")
# logging.basicConfig(level=logging.DEBUG, format="%(levelname)s - %(message)s")
LOG = logging.getLogger(__name__)


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
        mapped_params=None,
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
        self.mapped_params = {} if mapped_params is None else mapped_params
        self.blocks = {} if blocks is None else blocks
        self.vector_loaded = False
        self._param_types = {}
        self.data_files = [] if data_files is None else data_files
        self.merge_conf = [] if merge_conf is None else merge_conf
        self._params = {}

    def select_with_name(self, name):
        """
        Perform a select operation where selection options are derived
        from the specified name.
        """
        # print(f"select_with_name blocks: {self.blocks.keys()}")
        # print(f"vector_loaded: {self.vector_loaded}")

        if "wind" in name and not self.vector_loaded:
            self.load(vector=True)
        pnf = ParamInfo.build_from_name(name, param_level_types=self.param_types)
        if pnf is not None:
            fs = self._select_fs(**pnf.make_filter())
            if fs is not None:
                pnf.update_meta(fs._db._first_index_row())
                fs._param_info = pnf
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

        max_count = kwargs.pop("max_count", -1)

        # print(f"kwargs={kwargs}")
        # LOG.debug(f"blocks={self.blocks}")
        dims = self._make_dims(kwargs)
        # print(f"dims={dims}")
        self.load(keys=list(dims.keys()), vector=("wind" in dims.get("shortName", "")))
        # fs = mv.Fieldset()
        db, fs = self._get_fields(dims, max_count=max_count)
        # for f in r:
        #     fs.append(f)
        fs._db = db
        # fs._param_info = self.get_param_info()
        # LOG.debug(f"fs={fs}")
        # print(f"blocks={fs._db.blocks}")
        return fs

    def _get_fields(self, dims, max_count=None):
        res = mv.Fieldset()
        dfs = {}
        LOG.debug(f"dims={dims}")

        max_count = -1 if max_count is None else max_count
        cnt = 0
        for key in self.blocks.keys():
            self._get_fields_for_block(key, dims, dfs, res, max_count)
            if max_count != -1 and len(res) >= max_count:
                break

        # LOG.debug(f"len_res={len(res)}")
        # LOG.debug(f"dfs={dfs}")
        # LOG.debug(f"res={res}")
        c = FieldsetDb(
            res,
            name=self.name,
            blocks=dfs,
            label=self.label,
            mapped_params=self.mapped_params,
        )
        return c, res

    def _get_meta(self, dims):
        LOG.debug(f"dims={dims}")
        key = "scalar"
        if key in self.blocks:
            if self.blocks[key] is None:
                self._load_block(key)
            df = self._filter_df(df=self.blocks[key], dims=dims)
            # LOG.debug(f"df={df}")
            return df
        return None

    def _build_query(self, dims, df):
        q = ""
        for column, v in dims.items():
            # print(f"v={v}")
            if v:
                col_type = None
                if q:
                    q += " and "

                # datetime columns
                if column in GribIndexer.DATETIME_KEYS:
                    name_date = GribIndexer.DATETIME_KEYS[column][0]
                    name_time = GribIndexer.DATETIME_KEYS[column][1]
                    # here we should simply say: name_date*10000 + name_time. However,
                    # pandas cannot handle it in the query because the column types are
                    # Int64. np.int64 would work but that cannot handle missing values. So
                    # we need to break down the condition into individual logical components!
                    s = []
                    for x in v:
                        # print(f"x={x}")
                        # print(" date=" + x.strftime("%Y%m%d"))
                        # print(" time=" + x.strftime("%H%M"))
                        s.append(
                            f"(`{name_date}` == "
                            + str(int(x.strftime("%Y%m%d")))
                            + " and "
                            + f"`{name_time}` == "
                            + str(int(x.strftime("%H%M")))
                            + ")"
                        )
                    q += "(" + " or ".join(s) + " ) "
                else:
                    col_type = df.dtypes[column]
                    column = f"`{column}`"
                    if not isinstance(v, list):
                        q += f"{column} == {GribIndexer._convert_query_value(v, col_type)}"
                    else:
                        v = [GribIndexer._convert_query_value(x, col_type) for x in v]
                        q += f"{column} in {v}"
        return q

    def _filter_df(self, df=None, dims={}):
        if len(dims) == 0:
            return df
        else:
            df_res = None
            if df is not None:
                # print("types={}".format(df.dtypes))
                q = self._build_query(dims, df)
                # print("query={}".format(q))
                if q != "":
                    df_res = df.query(q, engine="python")
                    df_res.reset_index(drop=True, inplace=True)
                    # print(f"df_res={df_res}")
                    # LOG.debug(f"df_res={df_res}")
                else:
                    return df
            return df_res

    def _get_fields_for_block(self, key, dims, dfs, res, max_count):
        # LOG.debug(f"block={self.blocks[key]}")
        if self.blocks[key] is None:
            self._load_block(key)
        df = self._filter_df(df=self.blocks[key], dims=dims)
        # LOG.debug(f"df={df}")
        if df is not None and not df.empty:
            df_fs = self._extract_fields(df, res, max_count)
            # LOG.debug(f"len_res={len(res)}")
            if df_fs is not None:
                # LOG.debug(f"df_fs={df_fs}")
                dfs[key] = df_fs

    def _make_param_info(self):
        m = self._first_index_row()
        if m:
            pnf = ParamInfo(m["shortName"], meta=dict(m))
            return pnf
        return None

    def _first_index_row(self):
        if self.blocks:
            df = self.blocks[list(self.blocks.keys())[0]]
            if df is not None and not df.empty:
                row = df.iloc[0]
                return dict(row)
        return {}

    def _make_dims(self, options):
        dims = {}
        GribIndexer._check_datetime_in_filter_input(options)
        for k, v in options.items():
            name = str(k)
            vv = copy.deepcopy(v)
            r = GribIndexer._convert_filter_value(name, self._to_list(vv))
            for name, vv in r:
                if len(r) > 1 or vv:
                    dims[name] = vv
        return dims

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

    def unique(self, key, param=None):
        r = set()
        if param is not None:
            for _, v in self.blocks.items():
                df_res = v.query(f"shortName = {param}")
        else:
            for _, v in self.blocks.items():
                r.update(v[key].unique().tolist())
        return sorted(list(r))

    @property
    def param_meta(self):
        if len(self._params) == 0:
            self.load()
            for par in sorted(self.unique("shortName")):
                self._params[par] = ParamNameDesc(par)
                self._params[par].load(self)
        return self._params

    def param_id_meta(self, param_id):
        self.load()
        p = ParamIdDesc(param_id)
        p.load(self)
        return p

    def describe(self, *args):
        param = args[0] if len(args) == 1 else None
        return ParamNameDesc.describe(self, param=param)

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

    def _extract_fields(self, df, fs, max_count):
        if df.empty:
            return None

        # print(f"cols={df.columns}")
        if "_msgIndex3" in df.columns:
            comp_num = 3
        elif "_msgIndex2" in df.columns:
            comp_num = 2
        elif "_msgIndex1" in df.columns:
            comp_num = 1
        else:
            return None

        # print(f"comp_num={comp_num}")

        idx = [[] for k in range(comp_num)]
        comp_lst = list(range(comp_num))
        cnt = 0
        for row in df.itertuples():
            if max_count == -1 or len(fs) < max_count:
                for comp in comp_lst:
                    fs.append(self.fs[row[-1 - (comp_num - comp - 1)]])
                    idx[comp].append(len(fs) - 1)
                cnt += 1
            else:
                break

        # generate a new dataframe
        if max_count == -1 or cnt == df.shape[0]:
            df = df.copy()
        else:
            df = df.head(cnt).copy()

        for k, v in enumerate(idx):
            df[f"_msgIndex{k+1}"] = v
        return df

    def _clone(self):
        db = FieldsetDb(
            self.name,
            label=self.label,
        )

        if self._indexer is not None:
            db.indexer.update_keys(self._indexer.keys_ecc)
        db.blocks = {k: v.copy() for k, v in self.blocks.items()}
        db.vector_loaded = self.vector_loaded
        return db

    @staticmethod
    def make_param_info(fs):
        if fs._db is not None:
            return fs._db._make_param_info()
        else:
            return ParamInfo.build_from_fieldset(fs)

    def unique(self, key):
        r = list()
        for _, v in self.blocks.items():
            r.extend(v[key].unique().tolist())
        return list(dict.fromkeys(r))

        # r = set()
        # for _, v in self.blocks.items():
        #     r.update(v[key].unique().tolist())
        # # return sorted(list(r))
        # return r

    def ls(self, extra_keys=None, filter=None):
        default_keys = [
            "centre",
            "shortName",
            "typeOfLevel",
            "level",
            "dataDate",
            "dataTime",
            "stepRange",
            "dataType",
            "number",
            "gridType",
        ]
        ls_keys = default_keys
        extra_keys = [] if extra_keys is None else extra_keys
        if extra_keys is not None:
            [ls_keys.append(x) for x in extra_keys if x not in ls_keys]
        keys = list(ls_keys)

        # add keys appearing in the filter to the full list of keys
        dims = {} if filter is None else filter
        dims = self._make_dims(dims)
        [keys.append(k) for k, v in dims.items() if k not in keys]

        # get metadata
        self.load(keys=keys, vector=False)

        # performs filter
        df = self._get_meta(dims)

        # extract results
        keys = list(ls_keys)
        keys.append("_msgIndex1")
        df = df[keys]
        df = df.sort_values(by="_msgIndex1")
        df = df.rename(columns={"_msgIndex1": "Message"})
        df = df.set_index("Message")

        # only show the column for number in the default set of keys if
        # there are any valid values in it
        if "number" not in extra_keys:
            r = df["number"].unique()
            skip = False
            if len(r) == 1:
                skip = r[0] in ["0", None]
            if skip:
                df.drop("number", axis=1, inplace=True)

        init_pandas_options()
        try:
            import IPython

            # test whether we're in the Jupyter environment
            if IPython.get_ipython() is not None:
                return df
        except:
            pass

        print(df)

    def speed(self):
        r = mv.Fieldset()
        if len(self.fs) >= 2:
            for i in range(len(self.fs) // 2):
                r.append(mv.sqrt(self.fs[2 * i] ** 2 + self.fs[2 * i + 1] ** 2))
            pnf = self.fs.param_info
            LOG.debug(f"speed pnf={pnf}")
            param_id = 10
            if pnf is not None:
                param_ids = {"wind10m": 207, "wind": 10}
                param_id = param_ids.get(pnf.name, param_id)
            r = mv.grib_set_long(r, ["paramId", param_id])
            r._db = FieldsetDb(r, label=self.label)
            r._db.load()
        return r

    def deacc(self, skip_first=None):
        if len(self.fs) > 1:
            self.load()
            step = self.unique("step")
            if step:
                v = self.select(step=step[0])
                if skip_first is None or skip_first == False:
                    r = v * 0
                else:
                    r = mv.Fieldset()
                for i in range(1, len(step)):
                    v_next = self.select(step=step[i])
                    r.append(v_next - v)
                    v = v_next
                r = mv.grib_set_long(r, ["generatingProcessIdentifier", 148])
                r._db = FieldsetDb(
                    r, label=self.label, mapped_params=self.mapped_params
                )
                r._db.load()
                return r
        return None

    def get_longname_and_units(self, short_name, param_id):
        # The name and units keys are not included in the default set of keys for the
        # indexer. When we need them (primarily in ParamDesc) we simply get the first
        # grib message and extract them from it.
        a = {}
        if short_name:
            a["shortName"] = short_name
        if param_id:
            a["paramId"] = param_id
        if a:
            a["max_count"] = 1
            r = self.select(**a)
            if r is not None and len(r) > 0:
                md = mv.grib_get(r[0], ["name", "units"])
                if md and len(md[0]) == 2:
                    return md[0][0], md[0][1]
        return "", ""


class ExperimentDb(IndexDb):
    def __init__(self, name, **kwargs):
        super().__init__(name, **kwargs)
        self.fs = {}
        self.vector_loaded = True
        self._indexer = None
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
            mapped_params={v: k for k, v in conf.get("mapped_params", {}).items()},
            blocks={},
            dataset=dataset,
        )
        return db

    def _clone(self):
        return ExperimentDb(
            self.name,
            label=self.label,
            db_dir=self.db_dir,
            mapped_params=self.mapped_params,
            dataset=self.dataset,
            data_files=self.data_files,
            rootdir_placeholder_value=self.rootdir_placeholder_value,
        )

    @property
    def indexer(self):
        if self._indexer is None:
            self._indexer = ExperimentIndexer(self)
        return self._indexer

    def scan(self, vector=True):
        print(f"Generate index for dataset component={self.name} ...")
        self.data_files = []
        # self.blocks = {}
        self.indexer.scan()

    def load(self, keys=None, vector=True):
        keys = [] if keys is None else keys
        ivk = [x for x in keys if x not in self.indexer.allowed_keys()]
        if ivk:
            raise Exception(
                f"{self} keys={ivk} cannot be used! The allowed set of keys={self.indexer.allowed_keys()}"
            )

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

    def _filter_blocks(self, dims):
        self.load()
        dfs = {}
        # LOG.debug(f"data_files={self.data_files}")
        # LOG.debug(f"dims={dims}")
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

        # LOG.debug(f"total matching rows={cnt}")
        return dfs

    def _extract_fields(self, df, fs, max_count):
        if df.empty:
            return None

        if "_fileIndex3" in df.columns:
            comp_num = 3
        elif "_fileIndex2" in df.columns:
            comp_num = 2
        elif "_fileIndex1" in df.columns:
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
            df[f"_msgIndex{k+1}"] = v
        df.drop([f"_fileIndex{x+1}" for x in range(comp_num)], axis=1, inplace=True)
        return df

    def to_fieldset(self):
        db, fs = self._get_fields({})
        fs._db = db
        return fs

    def get_longname_and_units(self, shortName, paramId):
        return "", ""


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
        self.conf = conf

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

    def describe(self):
        self.load_data_file_list()
        init_pandas_options()
        print("Tracks:")
        t = {"Name": [], "Suffix": []}
        for f in self.data_files:
            n, s = os.path.splitext(os.path.basename(f))
            t["Name"].append(n)
            t["Suffix"].append(s)
        df = pd.DataFrame.from_dict(t)
        df.set_index("Name", inplace=True)
        return df

    def _make(self, name):
        self.load_data_file_list()
        for f in self.data_files:
            if name == os.path.basename(f).split(".")[0]:
                c = {
                    x: self.conf.get(x, None)
                    for x in [
                        "skiprows",
                        "date_index",
                        "time_index",
                        "lon_index",
                        "lat_index",
                    ]
                }
                return Track(f, **c)
        return None


class Dataset:
    """
    Represents a Dataset
    """

    URL = "https://get.ecmwf.int/repository/test-data/metview/dataset"
    LOCAL_ROOT = os.getenv(
        "MPY_DATASET_ROOT", os.path.join(os.getenv("HOME", ""), "mpy_dataset")
    )
    COMPRESSION = "bz2"

    def __init__(self, name, path=None, load_style=True):
        self.name = name
        self.path = path if path is not None else ""
        self.field_conf = {}
        self.track_conf = {}

        assert self.name
        LOG.debug(f"name={self.name}")

        # set local path
        if self.path == "":
            self.path = os.path.join(self.LOCAL_ROOT, self.name)

        # If the path does not exists, it must be a built-in dataset. Data will be
        # downloaded into path.
        if not os.path.isdir(self.path):
            if self.check_remote():
                self.fetch(forced=True)
            else:
                raise Exception(
                    f"Could not find dataset={self.name} either under path={self.path} or on data server"
                )
        # WARN: we do not store the dataset in the CACHE any more. Check code versions before
        # 09082021 to see how the CACHE was used.

        if load_style:
            self.load_style()

        self.load()

        for _, c in self.field_conf.items():
            LOG.debug(f"{c}")

    @staticmethod
    def load_dataset(*args, **kwargs):
        return Dataset(*args, **kwargs)

    def check_remote(self):
        try:
            return (
                requests.head(
                    f"{self.URL}/{self.name}/conf.tar", allow_redirects=True
                ).status_code
                == 200
            )
        except:
            return False

    def load(self):
        data_dir = os.path.join(self.path, "data")
        index_dir = os.path.join(self.path, "index")
        data_conf_file = os.path.join(self.path, "data.yaml")
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
        init_pandas_options()
        print("Dataset components:")
        t = {"Component": [], "Description": []}
        for _, f in self.field_conf.items():
            t["Component"].append(f.name)
            t["Description"].append(f.desc)
        for _, f in self.track_conf.items():
            t["Component"].append(f.name)
            t["Description"].append("Storm track data")
        df = pd.DataFrame.from_dict(t)
        df.set_index("Component", inplace=True)
        return df

    def fetch(self, forced=False):
        if not os.path.isdir(self.path):
            Path(self.path).mkdir(0o755, parents=True, exist_ok=True)

        files = {
            "conf.tar": ["data.yaml", "conf"],
            f"index.tar.{self.COMPRESSION}": ["index"],
            f"data.tar.{self.COMPRESSION}": ["data"],
        }

        checked = False
        for src, targets in files.items():
            # if forced or not utils.CACHE.all_exists(targets, self.path):
            if forced:
                if not checked and not self.check_remote():
                    raise Exception(
                        f"Could not find dataset={self.name} on data server"
                    )
                else:
                    checked = True

                remote_file = os.path.join(self.URL, self.name, src)
                target_file = os.path.join(self.path, src)
                # LOG.debug(f"target_file={target_file}")
                try:
                    # print("Download data ...")
                    utils.download(remote_file, target_file)
                    print(f"Unpack data ... {src}")
                    utils.unpack(target_file, remove=True)
                    # TODO: we skip the reference creation to make things faster. Enable it when
                    # it is needed!
                    # utils.CACHE.make_reference(targets, self.path)
                except:
                    # if os.exists(target_file):
                    #     os.remove(target_file)
                    raise Exception(f"Failed to download file={remote_file}")

    def __getitem__(self, key):
        if isinstance(key, str):
            r = self.find(key, comp="all")
            if r is None:
                raise Exception(f"No component={key} found in {self}")
            return r
        return None

    def load_style(self):
        conf_dir = os.path.join(self.path, "conf")
        mv.style.load_custom_config(conf_dir, force=True)

    def __str__(self):
        return f"{self.__class__.__name__}[name={self.name}]"
