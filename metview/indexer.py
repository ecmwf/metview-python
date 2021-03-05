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
        "date": ("l", np.int32, True),
        "time": ("l", np.int32, True),
        "step": ("s", str, True),
        "level": ("l", np.int32, True),
        "typeOfLevel": ("s", str, True),
        "number": ("s", str, True),
        "expver": ("s", str, False),
        "type": ("s", str, False),
    }

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
        self.type_index = self.keys.index("type")
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
            "expver",
        ]:
            self.wind_check_index.append(self.keys.index(v))

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
                    name = (v_name, k[1])
                    # name = k.replace(comp_name, v_name)
                    if name in comp_params and len(comp_params[name]) == i:
                        comp_params[name].append(v)
                    elif i == 0:
                        comp_params[name] = [v]

        if len(comp_params) == 0:
            LOG.debug(" No component params found!")
            return {}, {}

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

        return comp_params, v_params


class FieldsetIndexer(GribIndexer):
    def __init__(self):
        super().__init__()
        self.ref_column_count = 1

    def scan(self, db):
        params = self._scan(db.fs, mars_params=db.mars_params)

        # scalar fields
        LOG.info(f" generate scalar fields index ...")
        cols = [*self.keys]
        cols.extend(["msgIndex"])
        field_stat = {}
        for name, p in params.items():
            LOG.debug(self.pd_types)
            df = pd.DataFrame(p, columns=cols).astype(self.pd_types)
            df.sort_values(by=list(df.columns), inplace=True)
            db.params[name] = df
            field_stat[name] = len(df)
            self._check_duplicates(name, df)

        LOG.info(f" scalar fields count: {field_stat}")

        # vector fields
        LOG.info(f" generates vector fields index ...")
        field_stat = {}
        for v_name, v_comp in GribIndexer.VECTOR_PARAMS.items():
            comp_params, v_params = self._build_vector_index(params, v_name, v_comp)
            comp_num = len(v_comp)
            for name, p in v_params.items():
                # LOG.debug(f" name={name}")
                cols = [*self.keys]  # self.DEFAULT_KEYS.copy()
                assert name in comp_params
                for i in range(comp_num):
                    cols.extend([f"msgIndex{i+1}"])
                # LOG.debug(p)
                df = pd.DataFrame(p, columns=cols).astype(self.pd_types)
                # df.sort_values(by=list(df.columns), inplace=True)
                db.wind[name] = df
                field_stat[name] = len(df)
                self._check_duplicates(name, df)

        LOG.info(f" vector fields count: {field_stat}")

    def _scan(self, fs, mars_params={}):
        LOG.info(f" scan fields ...")
        params = {}
        md_vals = mv.grib_get(fs, self.keys_for_ecc)
        for i, v in enumerate(md_vals):
            short_name = v[self.shortname_index]
            if v[self.mars_param_index] in mars_params:
                short_name = mars_params[v[self.mars_param_index]]
                md_vals[i][self.shortname_index] = short_name
            # name = "{}_{}".format(short_name, v[self.levtype_index])
            name = (short_name, v[self.levtype_index])
            if not name in params:
                params[name] = []
            v.append(i)
            params[name].append(v)
        LOG.info(f" {len(fs)} GRIB messages processed")
        return params


class ExperimentIndexer(GribIndexer):
    def __init__(self):
        super().__init__()
        self.ref_column_count = 2

    def scan(self, db):
        out_dir = db.conf_dir
        Path(out_dir).mkdir(exist_ok=True, parents=True)
        LOG.info(f"scan {db} out_dir={out_dir} ...")

        params = {}
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
                            "data": db.dataset.find(c_name),
                            "name": c_name,
                            "ens": {"type": "cf", "number": 0},
                        }
                    )
                for i, c_name in enumerate(db.merge_conf.get("pf", [])):
                    ds.append(
                        {
                            "data": db.dataset.find(c_name),
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
                        params=params,
                        input_files=input_files,
                        mars_params=db.mars_params,
                        ens=c["ens"],
                    )
        # index a single experiment
        else:
            params, input_files = self._scan_one(
                input_dir=db.path,
                file_name_pattern=db.file_name_pattern,
                params={},
                input_files=[],
                mars_params=db.mars_params,
                ens={},
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
        for name, p in params.items():
            # df = pd.DataFrame(p, columns=cols).astype({"expver": str})
            df = pd.DataFrame(p, columns=cols).astype(self.pd_types)
            df.sort_values(by=list(df.columns), inplace=True)
            # write indexing info to disk
            f_name = os.path.join(out_dir, f"{name[0]}_{name[1]}.csv")
            df.to_csv(path_or_buf=f_name, header=True, index=False)
            db.params[name] = df
            field_stat[name] = len(df)
            self._check_duplicates(name, df)
        LOG.info(f" scalar fields count: {field_stat}")

        # generate and write index for vector fields
        LOG.info(f"generate vector fields index ...")
        field_stat = {}
        for v_name, v_comp in GribIndexer.VECTOR_PARAMS.items():
            comp_params, v_params = self._build_vector_index(params, v_name, v_comp)
            comp_num = len(v_comp)

            if len(comp_params) == 0:
                LOG.debug(" No paired fields found!")
                continue

            # write config for vector fields
            for name, p in v_params.items():
                # LOG.debug(f" name={name}")
                cols = [*self.keys]
                assert name in comp_params
                for i in range(comp_num):
                    cols.extend([f"msgIndex{i+1}", f"fileIndex{i+1}"])
                # LOG.debug(p)
                df = pd.DataFrame(p, columns=cols).astype(self.pd_types)
                df.sort_values(by=list(df.columns), inplace=True)
                f_name = os.path.join(out_dir, f"{name[0]}_{name[1]}.csv")
                df.to_csv(path_or_buf=f_name, header=True, index=False)
                db.wind[name] = df
                field_stat[name] = len(df)
                self._check_duplicates(name, df)

        LOG.info(f" vector fields count: {field_stat}")

    def _scan_one(
        self,
        input_dir="",
        file_name_pattern="",
        params={},
        input_files=[],
        mars_params={},
        ens={},
    ):
        LOG.info("scan fields ...")
        LOG.info(f" input_dir={input_dir} file_name_pattern={file_name_pattern}")

        # for f_path in glob.glob(f_pattern):
        cnt = 0
        for f_path in mv.get_file_list(input_dir, file_name_pattern=file_name_pattern):
            # LOG.debug(f"  f_path={f_path}")
            fs = mv.read(f_path)
            if isinstance(fs, mv.Fieldset) and len(fs) > 0:
                input_files.append(f_path)
                file_index = len(input_files) - 1
                # get metadata keys
                md_vals = mv.grib_get(fs, self.keys_for_ecc)
                for i, v in enumerate(md_vals):
                    short_name = v[self.shortname_index]
                    if v[self.mars_param_index] in mars_params:
                        short_name = mars_params[v[self.mars_param_index]]
                        md_vals[i][self.shortname_index] = short_name
                    if ens:
                        md_vals[i][self.type_index] = ens["type"]
                        md_vals[i][self.number_index] = ens["number"]
                    # name = "{}_{}".format(short_name, v[self.levtype_index])
                    name = (short_name, v[self.levtype_index])
                    if not name in params:
                        params[name] = []
                    v.extend([i, file_index])
                    params[name].append(v)
                cnt += 1
        LOG.info(f" {cnt} GRIB files processed")
        return params, input_files
