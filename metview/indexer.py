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
import datetime
from distutils.version import StrictVersion
import logging
import os
from pathlib import Path

import metview as mv
import numpy as np
import pandas as pd
import yaml

# logging.basicConfig(level=logging.DEBUG)
# logging.basicConfig(level=logging.INFO)
LOG = logging.getLogger(__name__)

NEWER = True


class GribIndexer:
    VECTOR_PARAMS = {
        "wind10m": ["10u", "10v"],
        "wind": ["u", "v"],
        "wind3d": ["u", "v", "w"],
    }

    # 0: ecCodes type, 1: pandas type, 2: use in duplicate check
    DEFAULT_KEYS = {
        "shortName": ("s", str, str, False),
        "paramId": ("l", "Int32", int, False),
        "date": ("l", "Int64", int, True),
        "time": ("l", "Int64", int, True),
        "step": ("s", str, str, True),
        "level": ("l", "Int32", int, True),
        "typeOfLevel": ("s", str, str, False),
        "number": ("s", str, str, True),
        "experimentVersionNumber": ("s", str, str, False),
        "marsClass": ("s", str, str, False),
        "marsStream": ("s", str, str, False),
        "marsType": ("s", str, str, False),
    }

    DEFAULT_ECC_KEYS = [f"{k}:{v[0]}" for k, v in DEFAULT_KEYS.items()]
    BLOCK_KEYS = ["shortName", "typeOfLevel"]

    DATE_KEYS = {
        k: ("l", "Int64", int)
        for k in ["date", "dataDate", "validityDate", "mars.date", "marsDate"]
    }
    TIME_KEYS = {
        k: ("l", "Int64", int)
        for k in ["time", "dataTime", "validityTime", "mars.time", "marsTime"]
    }

    DATETIME_KEYS = {
        "_dateTime": ("date", "time"),
        "_dataDateTime": ("dataDate", "dataTime"),
        "_validityDateTime": ("validityDate", "validityTime"),
    }

    PREDEF_KEYS = copy.deepcopy(DEFAULT_KEYS)
    PREDEF_KEYS.update(DATE_KEYS)
    PREDEF_KEYS.update(TIME_KEYS)

    PREDEF_PD_TYPES = {k: v[1] for k, v in PREDEF_KEYS.items()}
    PREDEF_PT_TYPES = {k: v[2] for k, v in PREDEF_KEYS.items()}

    def __init__(self, db):
        self.db = db
        assert self.db is not None
        self.ref_column_count = None
        self.keys = []
        self.keys_ecc = []
        for k, v in GribIndexer.DEFAULT_KEYS.items():
            name = k
            self.keys.append(name)
            if v[0]:
                name = f"{k}:{v[0]}"
            self.keys_ecc.append(name)

        self.keys_duplicate_check = [
            k for k, v in GribIndexer.DEFAULT_KEYS.items() if v[3] == True
        ]

        self.shortname_index = self.keys.index("shortName")
        self.levtype_index = self.keys.index("typeOfLevel")
        self.type_index = self.keys.index("marsType")
        self.number_index = self.keys.index("number")
        self.param_id_index = self.keys.index("paramId")

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
            "marsClass",
            "marsStream",
            "marsType",
        ]:
            self.wind_check_index.append(self.keys.index(v) + 1)

        # self.block_key_index = [self.keys.index(v) for v in GribIndexer.BLOCK_KEYS]

        self.pd_types = {k: v[1] for k, v in GribIndexer.DEFAULT_KEYS.items()}
        self.pt_types = {k: v[2] for k, v in GribIndexer.DEFAULT_KEYS.items()}

    def update_keys(self, keys):
        ret = False
        for k in keys:
            name = k
            # we do not add datetime keys (they are pseudo keys, and their value
            # is always generated on the fly)
            if name not in self.keys and name not in GribIndexer.DATETIME_KEYS:
                self.keys.append(name)
                p = GribIndexer.PREDEF_KEYS.get(name, ("", str, str))
                ecc_name = name if p[0] == "" else name + ":" + p[0]
                self.keys_ecc.append(ecc_name)
                self.pd_types[name] = p[1]
                self.pt_types[name] = p[2]
                ret = True
        return ret

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

    def _build_vector_index(self, df, v_name, v_comp):
        # LOG.debug(f"v_name={v_name} v_comp={v_comp}")
        comp_num = len(v_comp)

        # filter components belonging together
        comp_df = []
        for i, comp_name in enumerate(v_comp):
            query = f"shortName == '{comp_name}'"
            r = df.query(query)
            # if we do not use copy, the assignment below as:
            # comp_df[0].loc[...
            # generates the SettingWithCopyWarning warning!!!
            if i == 0:
                r = df.query(query).copy()
            else:
                r = df.query(query)
            if r.empty:
                return []
            else:
                comp_df.append(r)

        assert comp_num == len(comp_df)

        # pair up components within a 2D vector field. This
        # version proved to be the fastest!
        # LOG.debug(" pair up collected components:")

        # print(f"v_name={v_name} {len(comp_df[1].index)}")
        # print("view=", comp_df[0]._is_view)
        r = []
        used1 = np.full(len(comp_df[1].index), False, dtype="?")
        comp_df[0].loc[:, "shortName"] = v_name
        # 2D
        if comp_num == 2:
            for row0 in comp_df[0].itertuples(name=None):
                i = 0
                for row1 in comp_df[1].itertuples(name=None):
                    if not used1[i]:
                        b = True
                        for x in self.wind_check_index:
                            if row0[x] != row1[x]:
                                b = False
                                break
                        if b:
                            d = list(row0[1:])
                            d.extend(row1[-self.ref_column_count :])
                            r.append(d)
                            used1[i] = True
                            break
                    i += 1
        # 3D
        elif comp_num == 3:
            used2 = np.full(len(comp_df[2].index), False, dtype="?")
            for row0 in comp_df[0].itertuples(name=None):
                i = 0
                for row1 in comp_df[1].itertuples(name=None):
                    if not used1[i]:
                        b = True
                        for x in self.wind_check_index:
                            if row0[x] != row1[x]:
                                b = False
                                break
                        if b:
                            j = 0
                            for row2 in comp_df[2].itertuples(name=None):
                                if not used2[j]:
                                    b = True
                                    for x in self.wind_check_index:
                                        if row0[x] != row2[x]:
                                            b = False
                                            break
                                    if b:
                                        d = list(row0[1:])
                                        d.extend(row1[-self.ref_column_count :])
                                        d.extend(row2[-self.ref_column_count :])
                                        r.append(d)
                                        used1[i] = True
                                        used2[j] = True
                                        j = -1
                                        break
                                j += 1
                            if j == -1:
                                break
                    i += 1
        return r

    def _make_dataframe(self, data, columns=None):
        if columns is not None:
            df = pd.DataFrame(data, columns=columns)
        else:
            df = pd.DataFrame(data)

        for c in df.columns:
            if self.pd_types.get(c, "") in ["Int32", "Int64"]:
                df[c].fillna(value=np.nan, inplace=True)
            df = df.astype(self.pd_types)
        df = GribIndexer._sort_dataframe(df)

        return df

    @staticmethod
    def _sort_dataframe(df):
        # the key argument is available from pandas 1.1.0
        if StrictVersion(pd.__version__) >= StrictVersion("1.1.0"):
            df = df.sort_values(
                by=list(df.columns),
                key=lambda col: col.str.pad(7, side="left", fillchar="0")
                if col.name == "step"
                else col,
            )
        # for an older pandas version we use this ad hoc method
        else:
            step_ori = []
            if "step" in list(df.columns):
                step_ori = list(df.step)
                df.step = df.step.str.pad(7, side="left", fillchar="0")
            df = df.sort_values(by=list(df.columns))
            if step_ori:
                df.step = [step_ori[idx] for idx in df.index]

        df = df.reset_index(drop=True)
        return df

    def _write_dataframe(self, df, name, out_dir):
        f_name = os.path.join(out_dir, f"{name}.csv.gz")
        df.to_csv(path_or_buf=f_name, header=True, index=False, compression="gzip")

    @staticmethod
    def read_dataframe(key, dir_name):
        # assert len(key) == len(GribIndexer.BLOCK_KEYS)
        # name = "_".join(key)
        name = key
        f_name = os.path.join(dir_name, f"{name}.csv.gz")
        # LOG.debug("f_name={}".format(f_name))
        return pd.read_csv(f_name, index_col=None, dtype=GribIndexer.PREDEF_PD_TYPES)

    @staticmethod
    def get_storage_key_list(dir_name):
        r = []
        # LOG.debug(f"dir_name={dir_name}")
        suffix = ".csv.gz"
        for f in mv.get_file_list(os.path.join(dir_name, f"*{suffix}")):
            name = os.path.basename(f)
            # LOG.debug(f"name={name}")
            r.append(name[: -len(suffix)])
        return r

    @staticmethod
    def is_key_wind(key):
        return key in GribIndexer.VECTOR_PARAMS

    @staticmethod
    def _convert_query_value(v, col_type):
        # print(f"v={v} {type(v)} {col_type}")
        return v if col_type != "object" else str(v)
        # if isinstance(v, datetime.datetime):
        #     t = v.strftime("%Y%m%d%H%M")
        #     # print(f"  -> {t}")
        #     return int(t) if col_type != "object" else t
        # elif isinstance(v, datetime.date):
        #     t = v.strftime("%Y%m%d")
        #     return int(t) if col_type != "object" else t
        # elif isinstance(v, datetime.time):
        #     t = v.strftime("%H%M")
        #     return int(t) if col_type != "object" else t
        # else:
        #     return v if col_type != "object" else str(v)

    @staticmethod
    def _check_datetime_in_filter_input(keys):
        for k, v in GribIndexer.DATETIME_KEYS.items():
            name = k[1:]
            name_date = v[0]
            name_time = v[1]
            if keys.get(name, []) and (
                keys.get(name_date, []) or keys.get(name_time, [])
            ):
                raise Exception(
                    "Cannot specify {name} together with {name_date} and {name_time}!"
                )

    @staticmethod
    def _convert_filter_value(name, v):
        """
        Analyse the filter key-value pairs and perform the necessary conversions
        """
        valid_name = name.split(":")[0] if ":" in name else name

        # datetime keys are pseudo keys, they start with _. Their value is converted to
        # datetime. The key itself is not added to the scan!
        if ("_" + valid_name) in GribIndexer.DATETIME_KEYS:
            valid_name = "_" + valid_name
            name_date = GribIndexer.DATETIME_KEYS[valid_name][0]
            name_time = GribIndexer.DATETIME_KEYS[valid_name][1]
            for i, t in enumerate(v):
                v[i] = GribIndexer._to_datetime(name, t)
                # print(f"t={t} -> {v[i]}")
            # We add the date and time components with an empty value. So they will be
            # added to the scan, but they will be ignored by the query. Conversely,
            # the datetime key itself will be ignored in the scan, but will be used
            # in the query.
            return [("_" + name, v), (name_date, []), (name_time, [])]
        # we convert dates to int
        elif valid_name in GribIndexer.DATE_KEYS:
            for i, t in enumerate(v):
                v[i] = int(GribIndexer._to_date(name, t).strftime("%Y%m%d"))
        # we convert times to int
        elif valid_name in GribIndexer.TIME_KEYS:
            for i, t in enumerate(v):
                v[i] = int(GribIndexer._to_time(name, t).strftime("%H%M"))
                # print(f"t={t} -> {v[i]}")
        else:
            pt_type = GribIndexer.PREDEF_PT_TYPES.get(name, None)
            # print(f"name={name} {pt_type}")
            if pt_type is not None:
                for i, t in enumerate(v):
                    v[i] = pt_type(t)
                    # print(f" t={t} -> {v[i]}")

        # remap some names to ones already in the default set of indexer keys
        if name in ["type", "mars.type"]:
            name = "marsType"
        elif name in ["stream", "mars.stream"]:
            name = "marsStream"
        elif name in ["class", "mars.class", "class_"]:
            name = "marsClass"
        elif name in ["perturbationNumber"]:
            name = "number"
        elif name in ["mars.date", "marsDate"]:
            name = "date"
        elif name in ["mars.time", "marsTime"]:
            name = "time"

        return [(name, v)]

    @staticmethod
    def _to_datetime(param, v):
        try:
            if isinstance(v, datetime.datetime):
                return v
            elif isinstance(v, str):
                return mv.date(v)
            elif isinstance(v, (int, float)):
                return mv.date(str(v))
            else:
                raise
        except:
            raise Exception(f"Invalid datetime value={v} specified for key={param}")

    @staticmethod
    def _to_date(param, v):
        try:
            if isinstance(v, datetime.datetime):
                return v.date()
            elif isinstance(v, datetime.date):
                return v
            elif isinstance(v, str):
                return mv.date(v).date()
            elif isinstance(v, (int, float)):
                return mv.date(str(v)).date()
            else:
                raise
        except:
            raise Exception(f"Invalid date value={v} specified for key={param}")

    @staticmethod
    def _to_time(param, v):
        try:
            if isinstance(v, (datetime.datetime)):
                return v.time()
            elif isinstance(v, datetime.time):
                return v
            elif isinstance(v, str):
                return GribIndexer._str_to_time(v)
            elif isinstance(v, int):
                return GribIndexer._str_to_time(str(v))
            else:
                raise
        except:
            raise Exception(f"Invalid time value={v} specified for key={param}")

    @staticmethod
    def _str_to_time(v):
        h = m = 0
        if not ":" in v:
            # formats: h[mm], hh[mm]
            if len(v) in [1, 2]:
                h = int(v)
            elif len(v) in [3, 4]:
                r = int(v)
                h = int(r / 100)
                m = int(r - h * 100)
            else:
                raise Exception(f"Invalid time={v}")
        else:
            # formats: h:mm, hh:mm
            lst = v.split(":")
            if len(lst) >= 2:
                h = int(lst[0])
                m = int(lst[1])
            else:
                raise Exception(f"Invalid time={v}")

        return datetime.time(hour=h, minute=m)


class FieldsetIndexer(GribIndexer):
    def __init__(self, *args):
        super().__init__(*args)
        self.ref_column_count = 1

    def scan(self, vector=False):
        data = self._scan(self.db.fs, mapped_params=self.db.mapped_params)
        if data:
            df = self._make_dataframe(data)
            self.db.blocks["scalar"] = df
            if vector:
                self._scan_vector()

    def _scan(self, fs, mapped_params={}):
        LOG.info(f" scan fields ...")
        data = {}
        # print(f"fs_len={len(fs)}")
        if isinstance(fs, mv.Fieldset) and len(fs) > 0:
            md_vals = mv.grib_get(fs, self.keys_ecc, "key")
            if mapped_params:
                for i in range(len(fs)):
                    v = md_vals[self.param_id_index][i]
                    if v in mapped_params:
                        short_name = mapped_params[v]
                        md_vals[self.shortname_index][i] = short_name

            assert len(self.keys) == len(self.keys_ecc)
            data = {k: md_vals[i] for i, k in enumerate(self.keys)}
            data["_msgIndex1"] = list(range(len(fs)))
            LOG.info(f" {len(fs)} GRIB messages processed")
        return data

    def _scan_vector(self):
        df = self.db.blocks["scalar"]
        if df is not None and not df.empty:
            for v_name, v_comp in GribIndexer.VECTOR_PARAMS.items():
                r = self._build_vector_index(df, v_name, v_comp)
                comp_num = len(v_comp)
                if r:
                    cols = [*self.keys]
                    for i in range(comp_num):
                        cols.extend([f"_msgIndex{i+1}"])
                    w_df = self._make_dataframe(r, columns=cols)
                    self.db.blocks[v_name] = w_df
                    # self._write_dataframe(w_df, v_name, out_dir)
                else:
                    LOG.debug(" No paired fields found!")
                    continue


class ExperimentIndexer(GribIndexer):
    def __init__(self, *args):
        super().__init__(*args)
        self.ref_column_count = 2

    def scan(self):
        out_dir = self.db.db_dir
        Path(out_dir).mkdir(exist_ok=True, parents=True)
        LOG.info(f"scan {self.db} out_dir={out_dir} ...")

        data = {k: [] for k in [*self.keys, "_msgIndex1", "_fileIndex1"]}
        input_files = []

        # print(f"out_dir={out_dir}")
        # merge existing experiment objects
        if self.db.merge_conf:
            ds = []
            # simple merge
            if isinstance(self.db.merge_conf, list):
                for c_name in self.db.merge_conf:
                    ds.append(
                        {"data": db.dataset.find(c_name), "name": c_name, "ens": {}}
                    )
            # explicit ENS merge
            else:
                assert "pf" in self.db.merge_conf
                # control forecast
                c_name = self.db.merge_conf.get("cf", "")
                if c_name != "":
                    ds.append(
                        {
                            "data": self.db.dataset.find(c_name, comp="field"),
                            "name": c_name,
                            "ens": {"type": "cf", "number": 0},
                        }
                    )
                for i, c_name in enumerate(self.db.merge_conf.get("pf", [])):
                    ds.append(
                        {
                            "data": self.db.dataset.find(c_name, comp="field"),
                            "name": c_name,
                            "ens": {"type": "pf", "number": i + 1},
                        }
                    )

            for c in ds:
                if c["data"] is None:
                    c_name = d["name"]
                    raise Exception(
                        f"Cannot merge experiments as {self.db}! Experiment {c_name} is not found!"
                    )
                else:
                    input_files = self._scan_one(
                        input_dir=c["data"].path,
                        file_name_pattern=c["data"].file_name_pattern,
                        input_files=input_files,
                        mapped_params=self.db.mapped_params,
                        ens=c["ens"],
                        data=data,
                        rootdir_placeholder_value=c["data"].rootdir_placeholder_value,
                        rootdir_placeholder_token=self.db.ROOTDIR_PLACEHOLDER_TOKEN,
                    )
        # index a single experiment
        else:
            input_files = self._scan_one(
                input_dir=self.db.path,
                file_name_pattern=self.db.file_name_pattern,
                input_files=[],
                mapped_params=self.db.mapped_params,
                ens={},
                data=data,
                rootdir_placeholder_value=self.db.rootdir_placeholder_value,
                rootdir_placeholder_token=self.db.ROOTDIR_PLACEHOLDER_TOKEN,
            )

        # print(f"input_files={input_files}")
        if len(input_files) > 0 and len(data["shortName"]) > 0:
            # write config file for input file list
            LOG.info(f"generate datafiles.yaml ...")
            f_name = os.path.join(out_dir, "datafiles.yaml")
            r = yaml.dump(input_files, default_flow_style=False)
            with open(f_name, "w") as f:
                f.write(r)
            self.db.input_files = input_files

            # scalar
            LOG.info(f"generate scalar fields index ...")
            df = self._make_dataframe(data)
            self.db.blocks["scalar"] = df
            self._write_dataframe(df, "scalar", out_dir)

            # vector (2D)
            LOG.info(f"generate vector fields index ...")
            for v_name, v_comp in GribIndexer.VECTOR_PARAMS.items():
                r = self._build_vector_index(df, v_name, v_comp)
                comp_num = len(v_comp)
                if r:
                    cols = [*self.keys]
                    for i in range(comp_num):
                        cols.extend([f"_msgIndex{i+1}", f"_fileIndex{i+1}"])
                    w_df = self._make_dataframe(r, columns=cols)
                    # print(f"wind_len={len(w_df.index)}")
                    self.db.blocks[v_name] = w_df
                    self._write_dataframe(w_df, v_name, out_dir)
                else:
                    LOG.debug(" No paired fields found!")
                    continue

    def _scan_one(
        self,
        input_dir="",
        file_name_pattern="",
        input_files=[],
        mapped_params={},
        ens={},
        data={},
        rootdir_placeholder_value="",
        rootdir_placeholder_token=None,
    ):
        LOG.info("scan fields ...")
        LOG.info(f" input_dir={input_dir} file_name_pattern={file_name_pattern}")
        # print(f" input_dir={input_dir} file_name_pattern={file_name_pattern}")

        # for f_path in glob.glob(f_pattern):
        cnt = 0
        input_files_tmp = []
        for f_path in mv.get_file_list(input_dir, file_name_pattern=file_name_pattern):
            # LOG.debug(f"  f_path={f_path}")
            fs = mv.read(f_path)
            if isinstance(fs, mv.Fieldset) and len(fs) > 0:
                cnt += 1
                input_files_tmp.append(f_path)
                file_index = len(input_files) + len(input_files_tmp) - 1
                md_vals = mv.grib_get(fs, self.keys_ecc, "key")

                if mapped_params:
                    for i in range(len(fs)):
                        v = md_vals[self.param_id_index][i]
                        if v in mapped_params:
                            short_name = mapped_params[v]
                            md_vals[self.shortname_index][i] = short_name
                if ens:
                    for i in range(len(fs)):
                        md_vals[self.type_index][i] = ens["type"]
                        md_vals[self.number_index][i] = ens["number"]

                assert len(self.keys) == len(self.keys_ecc)
                for i, c in enumerate(self.keys):
                    data[c].extend(md_vals[i])
                data["_msgIndex1"].extend(list(range(len(fs))))
                data["_fileIndex1"].extend([file_index] * len(fs))

                # print({k: len(v) for k, v in data.items()})

        if rootdir_placeholder_value:
            input_files_tmp = [
                x.replace(rootdir_placeholder_value, rootdir_placeholder_token)
                for x in input_files_tmp
            ]

        input_files.extend(input_files_tmp)

        LOG.info(f" {cnt} GRIB files processed")
        return input_files

    def allowed_keys(self):
        r = list(self.keys)
        r.extend(GribIndexer.DATE_KEYS)
        r.extend(GribIndexer.TIME_KEYS)
        r.extend(list(GribIndexer.DATETIME_KEYS.keys()))
        return set(r)
