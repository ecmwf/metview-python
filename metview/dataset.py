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
from pathlib import Path
import shutil

import pandas as pd
import requests
import yaml

import metview as mv
from metview.metviewpy.indexer import ExperimentIndexer
from metview.metviewpy.indexdb import IndexDb
from metview.track import Track
from metview.metviewpy.param import init_pandas_options
from metview.metviewpy import utils


ETC_PATH = os.path.join(os.path.dirname(__file__), "etc")

# logging.basicConfig(level=logging.INFO, format="%(levelname)s - %(message)s")
# logging.basicConfig(level=logging.DEBUG, format="%(levelname)s - %(message)s")
LOG = logging.getLogger(__name__)


class ExperimentDb(IndexDb):
    def __init__(self, name, **kwargs):
        super().__init__(name, **kwargs)
        self.fs = {}
        self.vector_loaded = True
        self._indexer = None
        self.fieldset_class = mv.Fieldset
        LOG.debug(f"rootdir_placeholder_value={self.rootdir_placeholder_value}")

    @staticmethod
    def make_from_conf(name, conf, root_dir, db_root_dir, regrid_conf, dataset):
        # LOG.debug(f"conf={conf}")
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
            regrid_from=regrid_conf.get(name, []),
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
            regrid_from=self.regrid_from,
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
            self.data_files = utils.get_file_list(
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

    def __init__(self, name_or_path, load_style=True):
        self.field_conf = {}
        self.track_conf = {}

        self.path = name_or_path
        if any(x in self.path for x in ["/", "\\", "..", "./"]):
            self.name = os.path.basename(self.path)
        else:
            self.name = self.path
            self.path = ""

        assert self.name
        # print(f"name={self.name}")

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
            regrid_conf = d.get("regrid", {})
            for item in d["experiments"]:
                ((name, conf),) = item.items()
                if conf.get("type") == "track":
                    self.track_conf[name] = TrackConf(name, conf, data_dir, self)
                else:
                    c = ExperimentDb.make_from_conf(
                        name, conf, data_dir, index_dir, regrid_conf, self
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


def create_dataset_template(name_or_path):
    path = name_or_path
    if any(x in path for x in ["/", "\\", "..", "./"]):
        name = os.path.basename(path)
    else:
        name = path
        path = ""

    if path == "":
        path = os.path.join(Dataset.LOCAL_ROOT, name)

    if not os.path.exists(path):
        os.mkdir(path)
    else:
        if not os.path.isdir(path):
            raise Exception(f"path must be a directory!")
        if os.path.exists(os.path.join("path", "data.yaml")):
            raise Exception(
                f"The specified dataset directory={path} already exists and is not empty!"
            )

    # create dirs
    for dir_name in ["conf", "data", "index"]:
        os.mkdir(os.path.join(path, dir_name))

    # copy files
    files = {
        "params.yaml": ("conf", ""),
        "param_styles.yaml": ("conf", ""),
        "areas.yaml": ("conf", ""),
        "map_styles_template.yaml": ("conf", "map_styles.yaml"),
        "dataset_template.yaml": ("", "data.yaml"),
    }
    for src_name, target in files.items():
        target_dir = os.path.join(path, target[0]) if target[0] else path
        target_name = target[1] if target[1] else src_name
        shutil.copyfile(
            os.path.join(ETC_PATH, src_name), os.path.join(target_dir, target_name)
        )
