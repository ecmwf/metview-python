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
import requests
import yaml

import metview as mv
from metview.indexer import GribIndexer, FieldsetIndexer, ExperimentIndexer
from metview.track import Track
from metview.param import ParamInfo
from metview import utils


ETC_PATH = os.path.join(os.path.dirname(__file__), "etc")

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


class ParamDesc:
    def __init__(self, name):
        self.name = name
        self.md = {}
        self.levels = {}

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

        self.md = {}
        self.levels = {}

        # print(f"par={par}")
        for b_name, b_df in db.blocks.items():
            if b_name == "scalar":
                q = f"shortName == '{self.name}'"
                dft = b_df.query(q)
            elif b_name == self.name:
                dft = b_df
            else:
                dft = None

            if dft is not None:
                for k in md.keys():
                    # print(f"{self.name}/{k}")
                    md[k].extend(dft[k].tolist())
                    # print(f"   df[{k}]={df[k]}")
            # print(df)

        if "level" in md and len(md["level"]) > 0:
            df = pd.DataFrame(md)
            for md_key in list(md.keys())[2:]:
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
            t = {
                "key": ["parameter"],
                "val": [param],
            }
            txt = ""
            v = db.param_meta.get(param, None)
            if v is not None:
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
                    t["key"].append(labels.get(kk, kk))
                    t["val"].append(ParamDesc.format_list(md_v, full=True))

            if in_jupyter:
                txt = ParamDesc._make_html_table(t, header=False)
                from IPython.display import HTML

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
        # print(f"kwargs={kwargs}")
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
        # print(f"blocks={fs._db.blocks}")
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
                if column == "basedate":
                    column = "date*10000 + time"
                else:
                    col_type = df.dtypes[column]
                    column = f"`{column}`"

                if not isinstance(v, list):
                    q += f"{column} == {self._convert_query_value(v, col_type)}"
                else:
                    v = [self._convert_query_value(x, col_type) for x in v]
                    q += f"{column} in {v}"
        return q

    def _convert_query_value(self, v, col_type):
        if isinstance(v, datetime.date):
            t = v.strftime("%Y%m%d")
            return int(t) if col_type != "object" else t
        elif isinstance(v, datetime.time):
            t = v.strftime("%H%M")
            return int(t) if col_type != "object" else t
        elif isinstance(v, datetime.datetime):
            t = v.strftime("%Y%m%d%H%M")
            return int(t) if col_type != "object" else t
        else:
            return v if col_type != "object" else str(v)

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
        valid_name = name.split(":")[0] if ":" in name else name
        if name == "basedate":
            for i, t in enumerate(v):
                self._check_type(t, name, datetime.datetime)
                v[i] = int(t.strftime("%Y%m%d%H%M"))
        elif valid_name in [
            "date",
            "dataDate",
            "validityDate",
            "mars.date",
            "marsDate",
        ]:
            for i, t in enumerate(v):
                v[i] = self._convert_date(name, t)
        elif valid_name in [
            "time",
            "dataTime",
            "validityTime",
            "mars.time",
            "marsTime",
        ]:
            for i, t in enumerate(v):
                v[i] = self._convert_time(name, t)
                # print(f"t={t} -> {v[i]}")
        else:
            pd_type = GribIndexer.pd_types.get(name, None)
            if pd_type is not None:
                for i, t in enumerate(v):
                    v[i] = pd_type(t)

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

        return name, v

    def _convert_date(self, param, v):
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

    def _convert_time(self, param, v):
        try:
            if isinstance(v, (datetime.datetime)):
                return v.time()
            elif isinstance(v, datetime.time):
                return v
            elif isinstance(v, str):
                return self._convert_str_to_time(v)
            elif isinstance(v, int):
                return self._convert_str_to_time(str(v))
            else:
                raise
        except:
            raise Exception(f"Invalid time value={v} specified for key={param}")

    def _convert_str_to_time(self, v):
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
                self._params[par] = ParamDesc(par)
                self._params[par].load(self)
        return self._params

    def describe(self, param=None):
        return ParamDesc.describe(self, param=param)

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
        for row in df.itertuples():
            for comp in comp_lst:
                fs.append(self.fs[row[-1 - (comp_num - comp - 1)]])
                idx[comp].append(len(fs) - 1)
        # generate a new dataframe
        df = df.copy()
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

    def scan(self, vector=True):
        print(f"Generate index for dataset component={self.name} ...")
        self.data_files = []
        # self.blocks = {}
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
                        f"Could not find dataset={self.name} either under path={self.path} or on data server"
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
        # df.reset_index(drop=True, inplace=True)
        # df.style.set_properties(**{'text-align': 'left'}).set_table_styles([dict(selector='th', props=[('text-align', 'left')])])
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
            if forced or not utils.CACHE.all_exists(targets, self.path):
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
