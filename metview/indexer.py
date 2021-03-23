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

import glob
import logging
import os
from pathlib import Path
import re
import sys

import metview as mv
import numpy as np
import pandas as pd
import yaml

# logging.basicConfig(level=logging.DEBUG)
# logging.basicConfig(level=logging.INFO)
LOG = logging.getLogger(__name__)


class GribIndexer:
    VECTOR_PARAMS = {
        "wind10": ["10u", "10v"],
        "wind": ["u", "v"],
        "wind3d": ["u", "v", "w"],
    }

    # 0: ecCodes type, 1: pandas type, 2: use in duplicate check
    DEFAULT_KEYS = {
        "shortName": ("s", str, False),
        "mars.param": ("s", str, False),
        "date": ("l", np.int64, True),
        "time": ("l", np.int64, True),
        "step": ("s", str, True),
        "level": ("l", np.int32, True),
        "typeOfLevel": ("s", str, False),
        "number": ("s", str, True),
        "experimentVersionNumber": ("s", str, False),
        "mars.class": ("s", str, False),
        "mars.stream": ("s", str, False),
        "mars.type": ("s", str, False),
    }

    BLOCK_KEYS = ["shortName", "typeOfLevel"]

    pd_types = {k: v[1] for k, v in DEFAULT_KEYS.items()}

    def __init__(self, extra_keys=[]):
        self.ref_column_count = None
        self.keys = []
        self.keys_for_ecc = []
        for k, v in GribIndexer.DEFAULT_KEYS.items():
            name = k
            self.keys.append(name)
            if v[0]:
                name = f"{k}:{v[0]}"
            self.keys_for_ecc.append(name)

        self.keys_duplicate_check = [
            k for k, v in GribIndexer.DEFAULT_KEYS.items() if v[2] == True
        ]

        self.shortname_index = self.keys.index("shortName")
        self.levtype_index = self.keys.index("typeOfLevel")
        self.type_index = self.keys.index("mars.type")
        self.number_index = self.keys.index("number")
        self.mars_param_index = self.keys.index("mars.param")

        self.wind_check_index = []
        for v in [
            "date",
            "time",
            "step",
            "level",
            "typeOfLevel",
            "level",
            "number",
            "experimentVersionNumber",
            "mars.class",
            "mars.stream",
            "mars.type",
        ]:
            self.wind_check_index.append(self.keys.index(v))

        self.block_key_index = [self.keys.index(v) for v in GribIndexer.BLOCK_KEYS]

        self.pd_types = {k: v[1] for k, v in GribIndexer.DEFAULT_KEYS.items()}

        for k in extra_keys:
            name = k
            name_ecc = k
            if ":" in k:
                name = k.split(":")[0]
            if name not in self.keys:
                self.keys.append(name)
            if name_ecc not in self.keys_for_ecc:
                self.keys_for_ecc.append(name_ecc)

    def scan(self, db):
        raise NotImplementedError

    def _check_duplicates(self, name, df):
        dup = df.duplicated(subset=self.keys_duplicate_check)
        first_dup = True
        cnt = 0
        for i, v in dup.items():
            if v:
                if first_dup:
                    LOG.error(
                        f"{name}: has duplicates for key group: {self.keys_duplicate_check}!"
                    )
                    first_dup = False
                    LOG.error(f" first duplicate: {df.iloc[i]}")
                cnt += 1

        if cnt > 1:
            LOG.error(f"  + {cnt-1} more duplicate(s)!")

    def _build_vector_index(self, params, v_name, v_comp):
        # LOG.debug(f"v_name={v_name} v_comp={v_comp}")
        comp_num = len(v_comp)

        # collect components belonging together
        v_params = {}
        comp_params = {}
        for i, comp_name in enumerate(v_comp):
            for k, v in params.items():
                if k[0] == comp_name:
                    # LOG.debug(f"k={k}")
                    name = (v_name, k[1])
                    # LOG.debug(f"name={name}")
                    # name = k.replace(comp_name, v_name)
                    if name in comp_params and len(comp_params[name]) == i:
                        comp_params[name].append(v)
                    elif i == 0:
                        comp_params[name] = [v]

        if len(comp_params) == 0:
            LOG.debug(" No component params found!")
            return {}, {}

        # LOG.debug(f"comp_params={comp_params}")

        # pair up components within a vector field
        # LOG.debug(" pair up collected components:")
        for name in list(comp_params.keys()):
            v = comp_params[name]
            # LOG.debug(f" name={name}")
            if len(v) != comp_num:
                del comp_params[name]
                LOG.debug(f" -> skip (collected={len(v)} != expected={comp_num})")
            # 2D fields
            elif len(v) == 2:
                for v0 in v[0]:
                    for v1 in v[1]:
                        if [v0[x] for x in self.wind_check_index] == [
                            v1[x] for x in self.wind_check_index
                        ]:
                            d = v0.copy()
                            d.extend(v1[-self.ref_column_count :])
                            # LOG.debug("   d={}".format(d))
                            if name not in v_params:
                                v_params[name] = []
                            v_params[name].append(d)
                            break
            # 3D fields
            elif len(v) == 3:
                for v0 in v[0]:
                    # LOG.debug(" v0={}".format(v0[1:8]))
                    for v1 in v[1]:
                        # LOG.debug("   -> v1={}".format(v1[1:8]))
                        if [v0[x] for x in self.wind_check_index] == [
                            v1[x] for x in self.wind_check_index
                        ]:
                            for v2 in v[2]:
                                # LOG.debug("   -> v3={}".format(v3[1:8]))
                                if [v0[x] for x in self.wind_check_index] == [
                                    v2[x] for x in self.wind_check_index
                                ]:
                                    d = v0.copy()
                                    d.extend(v1[-self.ref_column_count :])
                                    d.extend(v2[-self.ref_column_count :])
                                    # LOG.debug("   d={}".format(d))
                                    if name not in v_params:
                                        v_params[name] = []
                                    v_params[name].append(d)
                                    break

        # LOG.debug(f"v_prams={v_params}")
        return comp_params, v_params

    def make_key(self, v):
        return tuple(v[x] for x in self.block_key_index)
        # return (v[self.shortname_index], v[self.levtype_index])

    def _build_dataframe(self, key, data, columns):
        df = pd.DataFrame(data, columns=columns).astype(self.pd_types)
        df.drop(self.BLOCK_KEYS, axis=1, inplace=True)
        df.sort_values(by=list(df.columns), inplace=True)
        # self._check_duplicates(key, df)
        return df

    def _write_dataframe(self, df, key, out_dir):
        assert len(key) == len(self.BLOCK_KEYS)
        name = "_".join(key)
        f_name = os.path.join(out_dir, f"{name}.csv.gz")
        # df.to_csv(path_or_buf=f_name, header=True, index=False)
        # df = df.transpose()
        df.to_csv(path_or_buf=f_name, header=True, index=False, compression="gzip")
        # df.to_csv(path_or_buf=f_name, header=False, index=True, compression="gzip")
        # df.to_csv(path_or_buf=f_name, header=True, index=False, compression="bz2")

    @staticmethod
    def read_dataframe(key, dir_name):
        assert len(key) == len(GribIndexer.BLOCK_KEYS)
        name = "_".join(key)
        f_name = os.path.join(dir_name, f"{name}.csv.gz")
        # LOG.debug("f_name={}".format(f_name))
        return pd.read_csv(f_name, index_col=None, dtype=GribIndexer.pd_types)

    @staticmethod
    def get_storage_key_list(dir_name):
        r = []
        # LOG.debug(f"dir_name={dir_name}")
        suffix = ".csv.gz"
        for f in mv.get_file_list(os.path.join(dir_name, f"*{suffix}")):
            name = os.path.basename(f)
            # LOG.debug(f"name={name}")
            name = name[: -len(suffix)].split("_")
            if len(name) == len(GribIndexer.BLOCK_KEYS):
                r.append(tuple(name))
        return r


class FieldsetIndexer(GribIndexer):
    def __init__(self):
        super().__init__()
        self.ref_column_count = 1

    def scan(self, db):
        blocks = self._scan(db.fs, mars_params=db.mars_params)

        # scalar fields
        LOG.info(f" generate scalar fields index ...")
        cols = [*self.keys]
        cols.extend(["msgIndex"])
        field_stat = {}
        for key, md in blocks.items():
            LOG.debug(self.pd_types)
            df = self._build_dataframe(key, md, cols)
            db.blocks[key] = df
            field_stat[key] = len(df)
            self._check_duplicates(key, df)

        LOG.info(f" scalar fields count: {field_stat}")

        # vector fields
        LOG.info(f" generates vector fields index ...")
        field_stat = {}
        for v_name, v_comp in GribIndexer.VECTOR_PARAMS.items():
            comp_blocks, v_blocks = self._build_vector_index(blocks, v_name, v_comp)
            LOG.debug(f"comp_blocks={comp_blocks}")
            LOG.debug(f"v_blocks={v_blocks}")
            comp_num = len(v_comp)
            for key, md in v_blocks.items():
                # LOG.debug(f" key={key}")
                cols = [*self.keys]
                assert key in comp_blocks
                for i in range(comp_num):
                    cols.extend([f"msgIndex{i+1}"])
                # LOG.debug(md)
                df = self._build_dataframe(key, md, cols)
                db.wind[key] = df
                field_stat[key] = len(df)
                self._check_duplicates(key, df)

        LOG.info(f" vector fields count: {field_stat}")

    def _scan(self, fs, mars_params={}):
        LOG.info(f" scan fields ...")
        blocks = {}
        md_vals = mv.grib_get(fs, self.keys_for_ecc)
        for i, v in enumerate(md_vals):
            # short_name = v[self.shortname_index]
            if v[self.mars_param_index] in mars_params:
                short_name = mars_params[v[self.mars_param_index]]
                md_vals[i][self.shortname_index] = short_name
            # name = "{}_{}".format(short_name, v[self.levtype_index])
            key = self.make_key(md_vals[i])
            if not key in blocks:
                blocks[key] = []
            # name = (short_name, v[self.levtype_index])
            # if not name in params:
            # params[name] = []
            v.append(i)
            blocks[key].append(v)
            # params[name].append(v)
        LOG.info(f" {len(fs)} GRIB messages processed")
        return blocks


class ExperimentIndexer(GribIndexer):
    def __init__(self):
        super().__init__()
        self.ref_column_count = 2

    def scan(self, db):
        out_dir = db.db_dir
        Path(out_dir).mkdir(exist_ok=True, parents=True)
        LOG.info(f"scan {db} out_dir={out_dir} ...")

        blocks = {}
        input_files = []

        # merge existing experiment objects
        if db.merge_conf:
            ds = []
            # simple merge
            if isinstance(db.merge_conf, list):
                for c_name in db.merge_conf:
                    ds.append(
                        {"data": db.dataset.find(c_name), "name": c_name, "ens": {}}
                    )
            # explicit ENS merge
            else:
                assert "pf" in db.merge_conf
                # control forecast
                c_name = db.merge_conf.get("cf", "")
                if c_name != "":
                    ds.append(
                        {
                            "data": db.dataset.find(c_name, comp="field"),
                            "name": c_name,
                            "ens": {"type": "cf", "number": 0},
                        }
                    )
                for i, c_name in enumerate(db.merge_conf.get("pf", [])):
                    ds.append(
                        {
                            "data": db.dataset.find(c_name, comp="field"),
                            "name": c_name,
                            "ens": {"type": "pf", "number": i + 1},
                        }
                    )

            for c in ds:
                if c["data"] is None:
                    c_name = d["name"]
                    raise Exception(
                        f"Cannot merge experiments as {db}! Experiment {c_name} is not found!"
                    )
                else:
                    params, input_files = self._scan_one(
                        input_dir=c["data"].path,
                        file_name_pattern=c["data"].file_name_pattern,
                        blocks=blocks,
                        input_files=input_files,
                        mars_params=db.mars_params,
                        ens=c["ens"],
                        rootdir_placeholder_value=c["data"].rootdir_placeholder_value,
                        rootdir_placeholder_token=db.ROOTDIR_PLACEHOLDER_TOKEN,
                    )
        # index a single experiment
        else:
            blocks, input_files = self._scan_one(
                input_dir=db.path,
                file_name_pattern=db.file_name_pattern,
                blocks={},
                input_files=[],
                mars_params=db.mars_params,
                ens={},
                rootdir_placeholder_value=db.rootdir_placeholder_value,
                rootdir_placeholder_token=db.ROOTDIR_PLACEHOLDER_TOKEN,
            )

        # write config file for input file list
        LOG.info(f"generate datafiles.yaml ...")
        f_name = os.path.join(out_dir, "datafiles.yaml")
        r = yaml.dump(input_files, default_flow_style=False)
        with open(f_name, "w") as f:
            f.write(r)
        db.input_files = input_files

        # generate and write index for scalar fields
        LOG.info(f"generate scalar fields index ...")
        cols = [*self.keys]
        cols.extend(["msgIndex", "fileIndex"])
        field_stat = {}
        for key, md in blocks.items():
            # LOG.debug(f"key={key}")
            df = self._build_dataframe(key, md, cols)
            self._write_dataframe(df, key, out_dir)
            db.blocks[key] = df
            field_stat[key] = len(df)
        LOG.info(f" scalar fields count: {field_stat}")

        # generate and write index for vector fields
        LOG.info(f"generate vector fields index ...")
        field_stat = {}
        for v_name, v_comp in GribIndexer.VECTOR_PARAMS.items():
            comp_blocks, v_blocks = self._build_vector_index(blocks, v_name, v_comp)
            comp_num = len(v_comp)

            if len(comp_blocks) == 0:
                LOG.debug(" No paired fields found!")
                continue

            # write config for vector fields
            for key, md in v_blocks.items():
                # LOG.debug(f" name={name}")
                cols = [*self.keys]
                assert key in comp_blocks
                for i in range(comp_num):
                    cols.extend([f"msgIndex{i+1}", f"fileIndex{i+1}"])
                # LOG.debug(p)
                df = self._build_dataframe(key, md, cols)
                self._write_dataframe(df, key, out_dir)
                db.wind[key] = df
                field_stat[key] = len(df)

        LOG.info(f" vector fields count: {field_stat}")

    def _scan_one(
        self,
        input_dir="",
        file_name_pattern="",
        blocks={},
        input_files=[],
        mars_params={},
        ens={},
        rootdir_placeholder_value="",
        rootdir_placeholder_token=None,
    ):
        LOG.info("scan fields ...")
        LOG.info(f" input_dir={input_dir} file_name_pattern={file_name_pattern}")

        # for f_path in glob.glob(f_pattern):
        cnt = 0
        input_files_tmp = []
        for f_path in mv.get_file_list(input_dir, file_name_pattern=file_name_pattern):
            # LOG.debug(f"  f_path={f_path}")
            fs = mv.read(f_path)
            if isinstance(fs, mv.Fieldset) and len(fs) > 0:
                input_files_tmp.append(f_path)
                file_index = len(input_files) + len(input_files_tmp) - 1
                # get metadata keys
                md_vals = mv.grib_get(fs, self.keys_for_ecc)
                for i, v in enumerate(md_vals):
                    # short_name = v[self.shortname_index]
                    if v[self.mars_param_index] in mars_params:
                        short_name = mars_params[v[self.mars_param_index]]
                        md_vals[i][self.shortname_index] = short_name
                    if ens:
                        md_vals[i][self.type_index] = ens["type"]
                        md_vals[i][self.number_index] = ens["number"]
                    key = self.make_key(md_vals[i])

                    # name = "{}_{}".format(short_name, v[self.levtype_index])
                    # name = (short_name, v[self.levtype_index])
                    if not key in blocks:
                        blocks[key] = []
                    # if not name in params:
                    #     params[name] = []
                    v.extend([i, file_index])
                    blocks[key].append(v)
                    # params[name].append(v)
                cnt += 1

        if rootdir_placeholder_value:
            input_files_tmp = [
                x.replace(rootdir_placeholder_value, rootdir_placeholder_token)
                for x in input_files_tmp
            ]

        input_files.extend(input_files_tmp)

        LOG.info(f" {cnt} GRIB files processed")
        return blocks, input_files
