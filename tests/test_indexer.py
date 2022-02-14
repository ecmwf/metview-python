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
import os
from black import assert_equivalent

import numpy as np
import pandas as pd


if "METVIEW_PYTHON_ONLY" not in os.environ:
    import metview as mv
else:
    import metview.metviewpy as mv

from metview.metviewpy.param import ParamInfo
from metview.metviewpy.indexer import GribIndexer

PATH = os.path.dirname(__file__)

DB_COLUMNS = copy.deepcopy(GribIndexer.DEFAULT_KEYS)
DB_COLUMNS["_msgIndex1"] = ("l", np.int64, False)
DB_COLUMNS_WIND2 = copy.deepcopy(DB_COLUMNS)
DB_COLUMNS_WIND2["_msgIndex2"] = ("l", np.int64, False)
DB_DEFAULT_COLUMN_NAMES = list(GribIndexer.DEFAULT_KEYS.keys())


def file_in_testdir(filename):
    return os.path.join(PATH, filename)


def build_index_db_dataframe(column_data, key_def=None):
    c = {v: column_data[i] for i, v in enumerate(list(key_def.keys()))}
    pd_types = {k: v[1] for k, v in key_def.items()}
    return pd.DataFrame(c).astype(pd_types)


def file_in_sort_dir(filename):
    return os.path.join(PATH, "sort", filename)


def build_metadata_dataframe(fs, keys):
    val = fs.grib_get(keys, "key")
    md = {k: v for k, v in zip(keys, val)}
    return pd.DataFrame.from_dict(md)


def read_sort_meta_from_csv(name):
    f_name = file_in_sort_dir(f"{name}.csv.gz")
    return pd.read_csv(f_name, index_col=None, dtype=str)


def write_sort_meta_to_csv(name, md):
    f_name = file_in_sort_dir(f"{name}.csv.gz")
    md.to_csv(path_or_buf=f_name, header=True, index=False, compression="gzip")


def test_fieldset_select_single_file():
    f = mv.read(file_in_testdir("tuv_pl.grib"))
    assert f._db is None

    # ------------------------
    # single resulting field
    # ------------------------
    g = f.select(shortName="u", level=700)
    assert len(g) == 1
    assert mv.grib_get(g, ["shortName", "level:l"]) == [["u", 700]]
    g1 = f[7]
    d = g - g1
    assert np.allclose(d.values(), np.zeros(len(d.values())))

    # check index db contents
    assert g._db is not None
    assert "scalar" in g._db.blocks
    assert len(g._db.blocks) == 1
    md = [
        ["u"],
        [131],
        [20180801],
        [1200],
        [0],
        [700],
        ["isobaricInhPa"],
        ["0"],
        ["0001"],
        ["od"],
        ["oper"],
        ["an"],
        [0],
    ]
    df_ref = build_index_db_dataframe(md, key_def=DB_COLUMNS)
    # print(df_ref.dtypes)
    # print(g._db.blocks)
    df = g._db.blocks["scalar"]
    # print(df.dtypes)
    if not df.equals(df_ref):
        print(df.compare(df_ref))
        assert False

    # ------------------------------------
    # single resulting field - paramId
    # ------------------------------------
    g = f.select(paramId=131, level=700)
    assert len(g) == 1
    assert mv.grib_get(g, ["paramId:l", "level:l"]) == [[131, 700]]
    g1 = f[7]
    d = g - g1
    assert np.allclose(d.values(), np.zeros(len(d.values())))

    # check index db contents
    assert g._db is not None
    assert "scalar" in g._db.blocks
    assert len(g._db.blocks) == 1
    md = [
        ["u"],
        [131],
        [20180801],
        [1200],
        [0],
        [700],
        ["isobaricInhPa"],
        ["0"],
        ["0001"],
        ["od"],
        ["oper"],
        ["an"],
        [0],
    ]
    df_ref = build_index_db_dataframe(md, key_def=DB_COLUMNS)
    df = g._db.blocks["scalar"]
    if not df.equals(df_ref):
        print(df.compare(df_ref))
        assert False

    # -------------------------
    # multiple resulting fields
    # -------------------------
    f = mv.read(file_in_testdir("tuv_pl.grib"))
    assert f._db is None

    g = f.select(shortName=["t", "u"], level=[700, 500])
    assert len(g) == 4
    assert mv.grib_get(g, ["shortName", "level:l"]) == [
        ["t", 700],
        ["u", 700],
        ["t", 500],
        ["u", 500],
    ]

    assert g._db is not None
    assert len(g._db.blocks) == 1
    assert "scalar" in g._db.blocks
    md = [
        ["t", "u", "t", "u"],
        [130, 131, 130, 131],
        [20180801] * 4,
        [1200] * 4,
        [0] * 4,
        [700, 700, 500, 500],
        ["isobaricInhPa"] * 4,
        ["0"] * 4,
        ["0001"] * 4,
        ["od"] * 4,
        ["oper"] * 4,
        ["an"] * 4,
        [0, 1, 2, 3],
    ]

    df_ref = build_index_db_dataframe(md, key_def=DB_COLUMNS)
    df = g._db.blocks["scalar"]
    if not df.equals(df_ref):
        print(df.compare(df_ref))
        assert False

    # -------------------------
    # empty result
    # -------------------------
    f = mv.read(file_in_testdir("tuv_pl.grib"))
    g = f.select(shortName="w")
    assert isinstance(g, mv.Fieldset)
    assert len(g) == 0

    # -------------------------
    # invalid key
    # -------------------------
    f = mv.read(file_in_testdir("tuv_pl.grib"))
    g = f.select(INVALIDKEY="w")
    assert isinstance(g, mv.Fieldset)
    assert len(g) == 0

    # -------------------------
    # str or int values
    # -------------------------
    f = mv.read(file_in_testdir("tuv_pl.grib"))
    assert f._db is None

    g = f.select(shortName=["t"], level=["500", 700], marsType="an")
    assert len(g) == 2
    assert mv.grib_get(g, ["shortName", "level:l", "marsType"]) == [
        ["t", 700, "an"],
        ["t", 500, "an"],
    ]

    f = mv.read(file_in_testdir("t_time_series.grib"))
    assert f._db is None

    g = f.select(shortName=["t"], step=[3, 6])
    assert len(g) == 2
    assert mv.grib_get(g, ["shortName", "level:l", "step:l"]) == [
        ["t", 1000, 3],
        ["t", 1000, 6],
    ]

    g = f.select(shortName=["t"], step=["3", "06"])
    assert len(g) == 2
    assert mv.grib_get(g, ["shortName", "level:l", "step:l"]) == [
        ["t", 1000, 3],
        ["t", 1000, 6],
    ]

    # -------------------------
    # repeated use
    # -------------------------
    f = mv.read(file_in_testdir("tuv_pl.grib"))
    assert f._db is None

    g = f.select(shortName=["t"], level=[500, 700], marsType="an")
    assert len(g) == 2
    assert mv.grib_get(g, ["shortName", "level:l", "marsType"]) == [
        ["t", 700, "an"],
        ["t", 500, "an"],
    ]

    g = f.select(shortName=["t"], level=[500], marsType="an")
    assert len(g) == 1
    assert mv.grib_get(g, ["shortName", "level:l", "marsType"]) == [
        ["t", 500, "an"],
    ]

    # -------------------------
    # mars keys
    # -------------------------
    f = mv.read(file_in_testdir("tuv_pl.grib"))
    assert f._db is None

    g = f.select(shortName=["t"], level=[500, 700], marsType="an")
    assert len(g) == 2
    assert mv.grib_get(g, ["shortName", "level:l", "marsType"]) == [
        ["t", 700, "an"],
        ["t", 500, "an"],
    ]

    g = f.select(shortName=["t"], level=[500, 700], type="an")
    assert len(g) == 2
    assert mv.grib_get(g, ["shortName", "level:l", "type"]) == [
        ["t", 700, "an"],
        ["t", 500, "an"],
    ]
    # check the index db contents. "type" must be mapped to the "marsType" column of the
    # db so no rescanning should happen. The db should only contain the default set of columns.
    assert g._db is not None
    assert "scalar" in g._db.blocks
    assert len(g._db.blocks) == 1
    assert list(g._db.blocks["scalar"].keys())[:-1] == DB_DEFAULT_COLUMN_NAMES

    g = f.select(shortName=["t"], level=[500, 700], type="fc")
    assert len(g) == 0

    g = f.select({"shortName": "t", "level": [500, 700], "mars.type": "an"})
    assert len(g) == 2
    assert mv.grib_get(g, ["shortName", "level:l", "mars.type"]) == [
        ["t", 700, "an"],
        ["t", 500, "an"],
    ]

    # -------------------------
    # custom keys
    # -------------------------
    f = mv.read(file_in_testdir("tuv_pl.grib"))
    assert f._db is None

    g = f.select(shortName=["t"], level=[500, 700], gridType="regular_ll")
    assert len(g) == 2
    assert mv.grib_get(g, ["shortName", "level:l", "gridType"]) == [
        ["t", 700, "regular_ll"],
        ["t", 500, "regular_ll"],
    ]

    g = f.select({"shortName": ["t"], "level": [500, 700], "mars.param:s": "130.128"})
    assert len(g) == 2
    assert mv.grib_get(g, ["shortName", "level:l", "mars.param"]) == [
        ["t", 700, "130.128"],
        ["t", 500, "130.128"],
    ]

    assert g._db is not None
    assert "scalar" in g._db.blocks
    assert len(g._db.blocks) == 1
    assert list(g._db.blocks["scalar"].keys())[:-1] == [
        *DB_DEFAULT_COLUMN_NAMES,
        "gridType",
        "mars.param:s",
    ]


def test_fieldset_select_date():
    # date and time
    f = mv.read(file_in_testdir("t_time_series.grib"))
    assert f._db is None

    g = f.select(date="20201221", time="12", step="9")
    assert len(g) == 2

    ref_keys = ["shortName", "date", "time", "step"]
    ref = [
        ["t", "20201221", "1200", "9"],
        ["z", "20201221", "1200", "9"],
    ]

    assert mv.grib_get(g, ref_keys) == ref

    g = f.select(date=20201221, time="1200", step=9)
    assert len(g) == 2
    assert mv.grib_get(g, ref_keys) == ref

    g = f.select(date=20201221, time="12:00", step=9)
    assert len(g) == 2
    assert mv.grib_get(g, ref_keys) == ref

    g = f.select(date=20201221, time=12, step=9)
    assert len(g) == 2
    assert mv.grib_get(g, ref_keys) == ref

    g = f.select(date="2020-12-21", time=1200, step=9)
    assert len(g) == 2
    assert mv.grib_get(g, ref_keys) == ref

    g = f.select(
        date=datetime.datetime(2020, 12, 21),
        time=datetime.time(hour=12, minute=0),
        step=9,
    )
    assert len(g) == 2
    assert mv.grib_get(g, ref_keys) == ref

    # dataDate and dataTime
    g = f.select(dataDate="20201221", dataTime="12", step=9)
    assert len(g) == 2
    assert mv.grib_get(g, ref_keys) == ref

    g = f.select(dataDate="2020-12-21", dataTime="12:00", step=9)
    assert len(g) == 2
    assert mv.grib_get(g, ref_keys) == ref

    # validityDate and validityTime
    g = f.select(validityDate="20201221", validityTime="21")
    assert len(g) == 2
    assert mv.grib_get(g, ref_keys) == ref

    g = f.select(validityDate="2020-12-21", validityTime="21:00")
    assert len(g) == 2
    assert mv.grib_get(g, ref_keys) == ref

    # dateTime
    g = f.select(dateTime="2020-12-21 12:00", step=9)
    assert len(g) == 2
    assert mv.grib_get(g, ref_keys) == ref

    # dataDateTime
    g = f.select(dataDateTime="2020-12-21 12:00", step=9)
    assert len(g) == 2
    assert mv.grib_get(g, ref_keys) == ref

    # validityDateTime
    g = f.select(validityDateTime="2020-12-21 21:00")
    assert len(g) == 2
    assert mv.grib_get(g, ref_keys) == ref

    # ------------------------------------
    # check multiple dates/times
    # ------------------------------------

    ref = [
        ["t", "20201221", "1200", "3"],
        ["z", "20201221", "1200", "3"],
        ["t", "20201221", "1200", "9"],
        ["z", "20201221", "1200", "9"],
    ]

    # date and time
    g = f.select(date="2020-12-21", time=12, step=[3, 9])
    assert len(g) == 4
    assert mv.grib_get(g, ref_keys) == ref

    # dateTime
    g = f.select(dateTime="2020-12-21 12:00", step=[3, 9])
    assert len(g) == 4
    assert mv.grib_get(g, ref_keys) == ref

    # validityDate and validityTime
    g = f.select(validityDate="2020-12-21", validityTime=[15, 21])
    assert len(g) == 4
    assert mv.grib_get(g, ref_keys) == ref

    # validityDateTime
    g = f.select(validityDateTime=["2020-12-21 15:00", "2020-12-21 21:00"])
    assert len(g) == 4
    assert mv.grib_get(g, ref_keys) == ref

    # ------------------------------------
    # check times with 1 digit hours
    # ------------------------------------

    # we create a new fieldset
    f = mv.merge(f[0], mv.grib_set_long(f[2:4], ["time", 600]))

    ref = [
        ["t", "20201221", "0600", "3"],
        ["z", "20201221", "0600", "3"],
    ]

    g = f.select(date="20201221", time="6", step="3")
    assert len(g) == 2
    assert mv.grib_get(g, ref_keys) == ref

    g = f.select(date=20201221, time="06", step=3)
    assert len(g) == 2
    assert mv.grib_get(g, ref_keys) == ref

    g = f.select(date=20201221, time="0600", step=3)
    assert len(g) == 2
    assert mv.grib_get(g, ref_keys) == ref

    g = f.select(date=20201221, time="06:00", step=3)
    assert len(g) == 2
    assert mv.grib_get(g, ref_keys) == ref

    g = f.select(validityDate="2020-12-21", validityTime=9)
    assert len(g) == 2
    assert mv.grib_get(g, ref_keys) == ref

    g = f.select(validityDate="2020-12-21", validityTime="09")
    assert len(g) == 2
    assert mv.grib_get(g, ref_keys) == ref

    g = f.select(validityDate="2020-12-21", validityTime=18)
    assert len(g) == 0

    # ------------------------------------
    # daily climatology dates (no year)
    # ------------------------------------

    f = mv.read(file_in_testdir("daily_clims.grib"))

    g = f.select(date="apr-01")
    assert len(g) == 1
    assert int(mv.grib_get_long(g, "date")) == 401

    g = f.select(date="Apr-02")
    assert len(g) == 1
    assert int(mv.grib_get_long(g, "date")) == 402

    g = f.select(date="402")
    assert len(g) == 1
    assert int(mv.grib_get_long(g, "date")) == 402

    g = f.select(date="0402")
    assert len(g) == 1
    assert int(mv.grib_get_long(g, "date")) == 402

    g = f.select(date=401)
    assert len(g) == 1
    assert int(mv.grib_get_long(g, "date")) == 401

    g = f.select(date=[401, 402])
    assert len(g) == 2
    assert [int(v) for v in mv.grib_get_long(g, "date")] == [402, 401]

    g = f.select(dataDate="apr-01")
    assert len(g) == 1
    assert int(mv.grib_get_long(g, "dataDate")) == 401


def test_fieldset_select_multi_file():
    f = mv.read(file_in_testdir("tuv_pl.grib"))
    f.append(mv.read(file_in_testdir("ml_data.grib")))
    assert f._db is None

    # single resulting field
    g = f.select(shortName="t", level=61)
    # print(f._db.blocks)
    assert len(g) == 1
    assert mv.grib_get(g, ["shortName", "level:l", "typeOfLevel"]) == [
        ["t", 61, "hybrid"]
    ]

    g1 = f[34]
    d = g - g1
    assert np.allclose(d.values(), np.zeros(len(d.values())))

    assert g._db is not None
    assert len(g._db.blocks) == 1
    assert "scalar" in g._db.blocks
    md = [
        ["t"],
        [130],
        [20180111],
        [1200],
        [12],
        [61],
        ["hybrid"],
        [None],
        ["0001"],
        ["od"],
        ["oper"],
        ["fc"],
        [0],
    ]
    df_ref = build_index_db_dataframe(md, key_def=DB_COLUMNS)
    df = g._db.blocks["scalar"]

    if not df.equals(df_ref):
        print(df.compare(df_ref))
        assert False


def test_param_info():
    # no extra info
    p = ParamInfo.build_from_name("2t")
    assert p.name == "2t"
    assert p.scalar == True
    assert p.meta["typeOfLevel"] == "surface"
    assert p.meta["level"] is None

    p = ParamInfo.build_from_name("msl")
    assert p.name == "msl"
    assert p.scalar == True
    assert p.meta["typeOfLevel"] == "surface"
    assert p.meta["level"] is None

    p = ParamInfo.build_from_name("t500")
    assert p.name == "t"
    assert p.scalar == True
    assert p.meta["typeOfLevel"] == "isobaricInhPa"
    assert p.meta["level"] == 500

    p = ParamInfo.build_from_name("t500hPa")
    assert p.name == "t"
    assert p.scalar == True
    assert p.meta["typeOfLevel"] == "isobaricInhPa"
    assert p.meta["level"] == 500

    p = ParamInfo.build_from_name("t")
    assert p.name == "t"
    assert p.scalar == True
    assert p.meta["typeOfLevel"] == ""
    assert p.meta["level"] is None

    p = ParamInfo.build_from_name("t320K")
    assert p.name == "t"
    assert p.scalar == True
    assert p.meta["typeOfLevel"] == "theta"
    assert p.meta["level"] == 320

    p = ParamInfo.build_from_name("t72ml")
    assert p.name == "t"
    assert p.scalar == True
    assert p.meta["typeOfLevel"] == "hybrid"
    assert p.meta["level"] == 72

    p = ParamInfo.build_from_name("wind10m")
    assert p.name == "wind10m"
    assert p.scalar == False
    assert p.meta["typeOfLevel"] == "surface"
    assert p.meta["level"] is None

    p = ParamInfo.build_from_name("wind100")
    assert p.name == "wind"
    assert p.scalar == False
    assert p.meta["typeOfLevel"] == "isobaricInhPa"
    assert p.meta["level"] == 100

    p = ParamInfo.build_from_name("wind700")
    assert p.name == "wind"
    assert p.scalar == False
    assert p.meta["typeOfLevel"] == "isobaricInhPa"
    assert p.meta["level"] == 700

    p = ParamInfo.build_from_name("wind")
    assert p.name == "wind"
    assert p.scalar == False
    assert p.meta["typeOfLevel"] == ""
    assert p.meta["level"] == None

    p = ParamInfo.build_from_name("wind3d")
    assert p.name == "wind3d"
    assert p.scalar == False
    assert p.meta["typeOfLevel"] == ""
    assert p.meta["level"] == None

    p = ParamInfo.build_from_name("wind3d500")
    assert p.name == "wind3d"
    assert p.scalar == False
    assert p.meta["typeOfLevel"] == "isobaricInhPa"
    assert p.meta["level"] == 500

    # exta info
    param_level_types = {
        "2t": ["surface"],
        "msl": ["surface"],
        "wind10m": ["surface"],
        "t": ["isobaricInhPa", "theta"],
        "wind": ["isobaricInhPa"],
    }

    p = ParamInfo.build_from_name("2t", param_level_types=param_level_types)
    assert p.name == "2t"
    assert p.scalar == True
    assert p.meta["typeOfLevel"] == "surface"
    assert p.meta["level"] == None

    try:
        p = ParamInfo.build_from_name("22t", param_level_types=param_level_types)
        assert False
    except:
        pass

    # p = ParamInfo.build_from_name("t2", param_level_types=param_level_types)
    # assert p.name == "2t"
    # assert p.level_type == "surface"
    # assert p.level is None

    p = ParamInfo.build_from_name("msl", param_level_types=param_level_types)
    assert p.name == "msl"
    assert p.scalar == True
    assert p.meta["typeOfLevel"] == "surface"
    assert p.meta["level"] == None

    p = ParamInfo.build_from_name("t500", param_level_types=param_level_types)
    assert p.name == "t"
    assert p.scalar == True
    assert p.meta["typeOfLevel"] == "isobaricInhPa"
    assert p.meta["level"] == 500

    p = ParamInfo.build_from_name("t500hPa", param_level_types=param_level_types)
    assert p.name == "t"
    assert p.scalar == True
    assert p.meta["typeOfLevel"] == "isobaricInhPa"
    assert p.meta["level"] == 500

    p = ParamInfo.build_from_name("t", param_level_types=param_level_types)
    assert p.name == "t"
    assert p.scalar == True
    assert "typeOfLevel" not in p.meta
    assert "level" not in p.meta

    p = ParamInfo.build_from_name("t320K", param_level_types=param_level_types)
    assert p.name == "t"
    assert p.scalar == True
    assert p.meta["typeOfLevel"] == "theta"
    assert p.meta["level"] == 320

    try:
        p = ParamInfo.build_from_name("t72ml", param_level_types=param_level_types)
        assert False
    except:
        pass

    p = ParamInfo.build_from_name("wind10m", param_level_types=param_level_types)
    assert p.name == "wind10m"
    assert p.scalar == False
    assert p.meta["typeOfLevel"] == "surface"
    assert p.meta["level"] is None

    p = ParamInfo.build_from_name("wind100", param_level_types=param_level_types)
    assert p.name == "wind"
    assert p.scalar == False
    assert p.meta["typeOfLevel"] == "isobaricInhPa"
    assert p.meta["level"] == 100

    p = ParamInfo.build_from_name("wind700", param_level_types=param_level_types)
    assert p.name == "wind"
    assert p.scalar == False
    assert p.meta["typeOfLevel"] == "isobaricInhPa"
    assert p.meta["level"] == 700

    p = ParamInfo.build_from_name("wind", param_level_types=param_level_types)
    assert p.name == "wind"
    assert p.scalar == False
    assert p.meta["typeOfLevel"] == "isobaricInhPa"
    assert p.meta["level"] is None

    try:
        p = ParamInfo.build_from_name("wind3d", param_level_types=param_level_types)
        assert False
    except:
        pass

    param_level_types["wind3d"] = ["isobaricInhPa"]
    p = ParamInfo.build_from_name("wind3d", param_level_types=param_level_types)
    assert p.name == "wind3d"
    assert p.scalar == False
    assert p.meta["typeOfLevel"] == "isobaricInhPa"
    assert p.meta["level"] is None

    p = ParamInfo.build_from_name("wind3d500", param_level_types=param_level_types)
    assert p.name == "wind3d"
    assert p.scalar == False
    assert p.meta["typeOfLevel"] == "isobaricInhPa"
    assert p.meta["level"] == 500


def test_param_info_from_fs_single_file():
    if "METVIEW_PYTHON_ONLY" in os.environ:
        return

    f = mv.read(file_in_testdir("tuv_pl.grib"))
    g = f["u700"]
    p = g.ds_param_info
    assert len(g) == 1
    assert p.name == "u"
    assert p.scalar == True
    md = {
        "shortName": "u",
        "paramId": 131,
        "date": 20180801,
        "time": 1200,
        "step": 0,
        "level": 700,
        "typeOfLevel": "isobaricInhPa",
        "number": "0",
        "experimentVersionNumber": "0001",
        "marsClass": "od",
        "marsStream": "oper",
        "marsType": "an",
        "_msgIndex1": 0,
    }
    assert md == p.meta

    g = f["wind500"]
    p = g.ds_param_info
    assert len(g) == 2
    assert p.name == "wind"
    assert p.scalar == False
    md = {
        "shortName": "wind",
        "paramId": 131,
        "date": 20180801,
        "time": 1200,
        "step": 0,
        "level": 500,
        "typeOfLevel": "isobaricInhPa",
        "number": "0",
        "experimentVersionNumber": "0001",
        "marsClass": "od",
        "marsStream": "oper",
        "marsType": "an",
        "_msgIndex1": 0,
        "_msgIndex2": 1,
    }
    assert md == p.meta

    # we lose the db
    g = g + 0
    p = g.ds_param_info
    assert len(g) == 2
    assert p.name == "wind"
    assert p.scalar == False
    md = {
        "shortName": "u",
        "paramId": 131,
        "date": 20180801,
        "time": 1200,
        "step": 0,
        "level": 500,
        "typeOfLevel": "isobaricInhPa",
        "number": "0",
        "experimentVersionNumber": "0001",
        "marsClass": "od",
        "marsStream": "oper",
        "marsType": "an",
    }
    assert md == p.meta

    g = f["t"]
    p = g.ds_param_info
    assert len(g) == 6
    assert p.name == "t"
    assert p.scalar == True
    md = {
        "shortName": "t",
        "paramId": 130,
        "date": 20180801,
        "time": 1200,
        "step": 0,
        "level": None,
        "typeOfLevel": "isobaricInhPa",
        "number": "0",
        "experimentVersionNumber": "0001",
        "marsClass": "od",
        "marsStream": "oper",
        "marsType": "an",
        "_msgIndex1": 0,
    }
    assert md == p.meta

    # we lose the db
    g = g + 0
    p = g.ds_param_info
    assert len(g) == 6
    assert p.name == "t"
    assert p.scalar == True
    md = {
        "shortName": "t",
        "paramId": 130,
        "date": 20180801,
        "time": 1200,
        "step": 0,
        "level": 1000,
        "typeOfLevel": "isobaricInhPa",
        "number": "0",
        "experimentVersionNumber": "0001",
        "marsClass": "od",
        "marsStream": "oper",
        "marsType": "an",
    }
    assert md == p.meta


def test_fieldset_select_operator_single_file():
    f = mv.read(file_in_testdir("tuv_pl.grib"))

    g = f["u700"]
    assert f._db is not None
    assert g._db is not None
    assert len(g) == 1
    assert mv.grib_get(g, ["shortName", "level:l"]) == [["u", 700]]

    g1 = f[7]
    d = g - g1
    assert np.allclose(d.values(), np.zeros(len(d.values())))

    g = f["t"]
    assert len(g) == 6
    assert mv.grib_get(g, ["shortName", "level:l"]) == [
        ["t", 1000],
        ["t", 850],
        ["t", 700],
        ["t", 500],
        ["t", 400],
        ["t", 300],
    ]

    try:
        g = f["w"]
        assert False
    except:
        pass


def test_fieldset_select_operator_multi_file():
    f = mv.read(file_in_testdir("tuv_pl.grib"))
    f.append(mv.read(file_in_testdir("ml_data.grib")))
    assert f._db is None

    # single resulting field
    g = f["t61ml"]
    assert f._db is not None
    assert g._db is not None
    assert len(g) == 1
    assert mv.grib_get(g, ["shortName", "level:l", "typeOfLevel"]) == [
        ["t", 61, "hybrid"]
    ]

    g1 = f[34]
    d = g - g1
    assert np.allclose(d.values(), np.zeros(len(d.values())))


def test_indexer_dataframe_sort_value_with_key():

    md = {
        "paramId": [1, 2, 1, 2, 3],
        "level": [925, 850, 925, 850, 850],
        "step": [12, 110, 1, 3, 1],
        "rest": ["1", "2", "aa", "b1", "1b"],
    }

    md_ref = {
        "paramId": [1, 1, 2, 2, 3],
        "level": [925, 925, 850, 850, 850],
        "step": [1, 12, 3, 110, 1],
        "rest": ["aa", "1", "b1", "2", "1b"],
    }

    df = pd.DataFrame(md)
    df = GribIndexer._sort_dataframe(df)
    df_ref = pd.DataFrame(md_ref)

    if not df.equals(df_ref):
        print(df.compare(df_ref))
        assert False


def test_describe():

    f = mv.read(file_in_testdir("tuv_pl.grib"))

    # full contents
    df = f.describe(no_print=True)

    ref = {
        "typeOfLevel": {
            "t": "isobaricInhPa",
            "u": "isobaricInhPa",
            "v": "isobaricInhPa",
        },
        "level": {"t": "300,400,...", "u": "300,400,...", "v": "300,400,..."},
        "date": {"t": 20180801, "u": 20180801, "v": 20180801},
        "time": {"t": 1200, "u": 1200, "v": 1200},
        "step": {"t": 0, "u": 0, "v": 0},
        "paramId": {"t": 130, "u": 131, "v": 132},
        "class": {"t": "od", "u": "od", "v": "od"},
        "stream": {"t": "oper", "u": "oper", "v": "oper"},
        "type": {"t": "an", "u": "an", "v": "an"},
        "experimentVersionNumber": {"t": "0001", "u": "0001", "v": "0001"},
    }
    ref_full = ref

    assert ref == df.to_dict()

    df = f.describe()
    assert ref == df.to_dict()

    # single param by shortName
    df = f.describe("t", no_print=True)

    ref = {
        "val": {
            "shortName": "t",
            "name": "Temperature",
            "paramId": 130,
            "units": "K",
            "typeOfLevel": "isobaricInhPa",
            "level": "300,400,500,700,850,1000",
            "date": "20180801",
            "time": "1200",
            "step": "0",
            "class": "od",
            "stream": "oper",
            "type": "an",
            "experimentVersionNumber": "0001",
        }
    }

    assert ref["val"] == df["val"].to_dict()

    df = f.describe(param="t", no_print=True)
    assert ref == df.to_dict()
    df = f.describe("t")
    assert ref == df.to_dict()
    df = f.describe(param="t")
    assert ref == df.to_dict()

    # single param by paramId
    df = f.describe(130, no_print=True)

    ref = {
        "val": {
            "shortName": "t",
            "name": "Temperature",
            "paramId": 130,
            "units": "K",
            "typeOfLevel": "isobaricInhPa",
            "level": "300,400,500,700,850,1000",
            "date": "20180801",
            "time": "1200",
            "step": "0",
            "class": "od",
            "stream": "oper",
            "type": "an",
            "experimentVersionNumber": "0001",
        }
    }

    assert ref == df.to_dict()

    df = f.describe(param=130, no_print=True)
    assert ref == df.to_dict()
    df = f.describe(130)
    assert ref == df.to_dict()
    df = f.describe(param=130)
    assert ref == df.to_dict()

    # append
    g = f + 0
    df = g.describe(no_print=True)
    assert ref_full == df.to_dict()

    g.append(f[0].grib_set_long(["level", 25]))
    df = g.describe(no_print=True)

    ref = {
        "typeOfLevel": {
            "t": "isobaricInhPa",
            "u": "isobaricInhPa",
            "v": "isobaricInhPa",
        },
        "level": {"t": "25,300,...", "u": "300,400,...", "v": "300,400,..."},
        "date": {"t": 20180801, "u": 20180801, "v": 20180801},
        "time": {"t": 1200, "u": 1200, "v": 1200},
        "step": {"t": 0, "u": 0, "v": 0},
        "paramId": {"t": 130, "u": 131, "v": 132},
        "class": {"t": "od", "u": "od", "v": "od"},
        "stream": {"t": "oper", "u": "oper", "v": "oper"},
        "type": {"t": "an", "u": "an", "v": "an"},
        "experimentVersionNumber": {"t": "0001", "u": "0001", "v": "0001"},
    }

    assert ref == df.to_dict()


def test_ls():

    f = mv.read(file_in_testdir("tuv_pl.grib"))

    # default keys
    df = f[:4].ls(no_print=True)

    ref = {
        "centre": {0: "ecmf", 1: "ecmf", 2: "ecmf", 3: "ecmf"},
        "shortName": {0: "t", 1: "u", 2: "v", 3: "t"},
        "typeOfLevel": {
            0: "isobaricInhPa",
            1: "isobaricInhPa",
            2: "isobaricInhPa",
            3: "isobaricInhPa",
        },
        "level": {0: 1000, 1: 1000, 2: 1000, 3: 850},
        "dataDate": {0: 20180801, 1: 20180801, 2: 20180801, 3: 20180801},
        "dataTime": {0: 1200, 1: 1200, 2: 1200, 3: 1200},
        "stepRange": {0: "0", 1: "0", 2: "0", 3: "0"},
        "dataType": {0: "an", 1: "an", 2: "an", 3: "an"},
        "gridType": {
            0: "regular_ll",
            1: "regular_ll",
            2: "regular_ll",
            3: "regular_ll",
        },
    }

    assert ref == df.to_dict()

    # extra keys
    df = f[:2].ls(extra_keys=["paramId"], no_print=True)

    ref = {
        "centre": {0: "ecmf", 1: "ecmf"},
        "shortName": {0: "t", 1: "u"},
        "typeOfLevel": {0: "isobaricInhPa", 1: "isobaricInhPa"},
        "level": {0: 1000, 1: 1000},
        "dataDate": {0: 20180801, 1: 20180801},
        "dataTime": {0: 1200, 1: 1200},
        "stepRange": {0: "0", 1: "0"},
        "dataType": {0: "an", 1: "an"},
        "gridType": {0: "regular_ll", 1: "regular_ll"},
        "paramId": {0: 130, 1: 131},
    }

    assert ref == df.to_dict()

    # filter
    df = f.ls(filter={"shortName": ["t", "v"], "level": 850}, no_print=True)

    ref = {
        "centre": {3: "ecmf", 5: "ecmf"},
        "shortName": {3: "t", 5: "v"},
        "typeOfLevel": {3: "isobaricInhPa", 5: "isobaricInhPa"},
        "level": {3: 850, 5: 850},
        "dataDate": {3: 20180801, 5: 20180801},
        "dataTime": {3: 1200, 5: 1200},
        "stepRange": {3: "0", 5: "0"},
        "dataType": {3: "an", 5: "an"},
        "gridType": {3: "regular_ll", 5: "regular_ll"},
    }

    assert ref == df.to_dict()

    # append
    g = f[:2]
    df = g.ls(no_print=True)

    ref = {
        "centre": {0: "ecmf", 1: "ecmf"},
        "shortName": {0: "t", 1: "u"},
        "typeOfLevel": {
            0: "isobaricInhPa",
            1: "isobaricInhPa",
        },
        "level": {0: 1000, 1: 1000},
        "dataDate": {0: 20180801, 1: 20180801},
        "dataTime": {0: 1200, 1: 1200},
        "stepRange": {0: "0", 1: "0"},
        "dataType": {0: "an", 1: "an"},
        "gridType": {
            0: "regular_ll",
            1: "regular_ll",
        },
    }

    assert ref == df.to_dict()

    g.append(f[2].grib_set_long(["level", 500]))
    df = g.ls(no_print=True)
    ref = {
        "centre": {0: "ecmf", 1: "ecmf", 2: "ecmf"},
        "shortName": {0: "t", 1: "u", 2: "v"},
        "typeOfLevel": {
            0: "isobaricInhPa",
            1: "isobaricInhPa",
            2: "isobaricInhPa",
        },
        "level": {0: 1000, 1: 1000, 2: 500},
        "dataDate": {0: 20180801, 1: 20180801, 2: 20180801},
        "dataTime": {0: 1200, 1: 1200, 2: 1200},
        "stepRange": {0: "0", 1: "0", 2: "0"},
        "dataType": {0: "an", 1: "an", 2: "an"},
        "gridType": {
            0: "regular_ll",
            1: "regular_ll",
            2: "regular_ll",
        },
    }

    assert ref == df.to_dict()


def test_sort():

    # In each message the message index (1 based) is encoded
    # into latitudeOfLastGridPoint!
    fs = mv.read(file_in_sort_dir("sort_data.grib"))

    default_sort_keys = ["date", "time", "step", "number", "level", "paramId"]
    assert GribIndexer.DEFAULT_SORT_KEYS == default_sort_keys

    # Note: shortName, units and latitudeOfLastGridPoint are non-default sort keys!
    keys = [
        "date",
        "time",
        "step",
        "number",
        "level",
        "paramId",
        "shortName",
        "units",
        "latitudeOfLastGridPoint",
    ]

    # the reference csv files were generated like this:
    #   write_sort_meta_to_csv(f_name, md)
    #
    # the correctness of the reference was tested by generating md_ref using
    # the GribIndexer and comparing it to md. E.g.:
    #   md_ori = build_metadata_dataframe(fs, keys)
    #   md_ref = GribIndexer._sort_dataframe(md_ori, columns=default_sort_keys)
    #   assert md.equals(md_ref)

    # default sorting
    f_name = "default"
    r = fs.sort()
    assert len(fs) == len(r)
    md = build_metadata_dataframe(r, keys)
    md_ref = read_sort_meta_from_csv(f_name)
    if not md.equals(md_ref):
        print(md.compare(md_ref))
        assert False

    # -----------------------------
    # default sorting direction
    # -----------------------------

    sort_keys = {
        k: k
        for k in [
            "date",
            "time",
            "step",
            "number",
            "level",
            "paramId",
            "shortName",
            "units",
        ]
    }
    sort_keys["date_level"] = ["date", "level"]
    sort_keys["level_units"] = ["level", "units"]
    sort_keys["keys"] = keys

    for f_name, key in sort_keys.items():
        r = fs.sort(key)
        assert len(fs) == len(r)
        md = build_metadata_dataframe(r, keys)
        md_ref = read_sort_meta_from_csv(f_name)
        if not md.equals(md_ref):
            print(md.compare(md_ref))
            assert False, f"key={key}"

    # single key as list
    key = f_name = "level"
    r = fs.sort([key])
    assert len(fs) == len(r)
    md = build_metadata_dataframe(r, keys)
    md_ref = read_sort_meta_from_csv(f_name)
    if not md.equals(md_ref):
        print(md.compare(md_ref))
        assert False, f"key={key}"

    # -----------------------------
    # custom sorting direction
    # -----------------------------

    # default keys

    # ascending
    f_name = "default"
    r = fs.sort(ascending=True)
    assert len(fs) == len(r)
    md = build_metadata_dataframe(r, keys)
    md_ref = read_sort_meta_from_csv(f_name)
    if not md.equals(md_ref):
        print(md.compare(md_ref))
        assert False, "default ascending"

    # descending
    f_name = "default_desc"
    r = fs.sort(ascending=False)
    assert len(fs) == len(r)
    md = build_metadata_dataframe(r, keys)
    md_ref = read_sort_meta_from_csv(f_name)
    if not md.equals(md_ref):
        print(md.compare(md_ref))
        assert False, "default descending"

    # single key
    key = "level"

    # ascending
    f_name = f"{key}_asc"
    r = fs.sort(key, "<")
    assert len(fs) == len(r)
    md = build_metadata_dataframe(r, keys)
    md_ref = read_sort_meta_from_csv(f_name)
    if not md.equals(md_ref):
        print(md.compare(md_ref))
        assert False, f"key={key}"

    r = fs.sort(key, ["<"])
    assert len(fs) == len(r)
    md = build_metadata_dataframe(r, keys)
    if not md.equals(md_ref):
        print(md.compare(md_ref))
        assert False, f"key={key}"

    r = fs.sort(key, ascending=True)
    assert len(fs) == len(r)
    md = build_metadata_dataframe(r, keys)
    if not md.equals(md_ref):
        print(md.compare(md_ref))
        assert False, f"key={key}"

    # descending
    f_name = f"{key}_desc"
    r = fs.sort(key, ">")
    assert len(fs) == len(r)
    md = build_metadata_dataframe(r, keys)
    md_ref = read_sort_meta_from_csv(f_name)
    if not md.equals(md_ref):
        print(md.compare(md_ref))
        assert False, f"key={key}"

    r = fs.sort(key, [">"])
    assert len(fs) == len(r)
    md = build_metadata_dataframe(r, keys)
    if not md.equals(md_ref):
        print(md.compare(md_ref))
        assert False, f"key={key}"

    r = fs.sort(key, ascending=False)
    assert len(fs) == len(r)
    md = build_metadata_dataframe(r, keys)
    if not md.equals(md_ref):
        print(md.compare(md_ref))
        assert False, f"key={key}"

    # multiple keys
    key = ["level", "paramId", "date"]

    f_name = "multi_asc"
    r = fs.sort(key, "<")
    assert len(fs) == len(r)
    md = build_metadata_dataframe(r, keys)
    md_ref = read_sort_meta_from_csv(f_name)
    if not md.equals(md_ref):
        print(md.compare(md_ref))
        assert False, f"key={key}"

    r = fs.sort(key, ascending=True)
    assert len(fs) == len(r)
    md = build_metadata_dataframe(r, keys)
    if not md.equals(md_ref):
        print(md.compare(md_ref))
        assert False, f"key={key}"

    f_name = "multi_desc"
    r = fs.sort(key, ">")
    assert len(fs) == len(r)
    md = build_metadata_dataframe(r, keys)
    md_ref = read_sort_meta_from_csv(f_name)
    if not md.equals(md_ref):
        print(md.compare(md_ref))
        assert False, f"key={key}"

    r = fs.sort(key, ascending=False)
    assert len(fs) == len(r)
    md = build_metadata_dataframe(r, keys)
    if not md.equals(md_ref):
        print(md.compare(md_ref))
        assert False, f"key={key}"

    f_name = "multi_mixed"
    r = fs.sort(key, ["<", ">", "<"])
    assert len(fs) == len(r)
    md = build_metadata_dataframe(r, keys)
    md_ref = read_sort_meta_from_csv(f_name)
    if not md.equals(md_ref):
        print(md.compare(md_ref))
        assert False, f"key={key}"

    r = fs.sort(key, ascending=[True, False, True])
    assert len(fs) == len(r)
    md = build_metadata_dataframe(r, keys)
    if not md.equals(md_ref):
        print(md.compare(md_ref))
        assert False, f"key={key}"

    # invalid arguments
    try:
        r = fs.sort(key, [">", "<"])
        assert False
    except ValueError:
        pass

    try:
        r = fs.sort(key, "1")
        assert False
    except ValueError:
        pass

    try:
        r = fs.sort(key, ascending=["True", "False"])
        assert False
    except ValueError:
        pass

    try:
        r = fs.sort(key, ">", ascending="True")
        assert False
    except ValueError:
        pass

    try:
        r = fs.sort(key, ">", ascending=["True", "False"])
        assert False
    except ValueError:
        pass


def test_speed():
    # test with grib written with write() function
    fs = mv.Fieldset(path=os.path.join(PATH, "tuv_pl.grib"))

    fs_u = fs.select(shortName="u")
    fs_v = fs.select(shortName="v")

    # single field
    u = fs_u[0]
    v = fs_v[0]
    r = mv.speed(u, v)
    assert len(r) == 1
    np.testing.assert_allclose(
        r.values(), np.sqrt(np.square(u.values()) + np.square(v.values())), rtol=1e-05
    )
    assert r.grib_get_long("paramId") == 10

    # multi fields
    u = fs_u[:2]
    v = fs_v[:2]
    r = mv.speed(u, v)
    assert len(r) == 2
    for i in range(len(r)):
        np.testing.assert_allclose(
            r[i].values(),
            np.sqrt(np.square(u[i].values()) + np.square(v[i].values())),
            rtol=1e-05,
        )
    assert r.grib_get_long("paramId") == [10, 10]

    # no arguments
    u = fs_u
    v = fs_v
    r = fs["wind"].speed()
    assert len(r) == 6
    for i in range(len(r)):
        np.testing.assert_allclose(
            r[i].values(),
            np.sqrt(np.square(u[i].values()) + np.square(v[i].values())),
            rtol=1e-05,
        )
    assert r.grib_get_long("paramId") == [10] * 6


def test_deacc():
    f = mv.Fieldset(path=os.path.join(PATH, "t_time_series.grib"))[:3]

    r = f.deacc()
    assert len(r) == len(f)
    assert r.grib_get_long("generatingProcessIdentifier") == [148] * len(r)
    for i in range(len(f)):
        v_ref = f[0].values() * 0 if i == 0 else f[i].values() - f[i - 1].values()
        np.testing.assert_allclose(r[i].values(), v_ref, rtol=1e-03)

    r = f.deacc(key="")
    assert len(r) == len(f)
    assert r.grib_get_long("generatingProcessIdentifier") == [148] * len(r)
    for i in range(len(f)):
        v_ref = f[0].values() * 0 if i == 0 else f[i].values() - f[i - 1].values()
        np.testing.assert_allclose(r[i].values(), v_ref, rtol=1e-03)

    r = f.deacc(skip_first=True)
    assert len(r) == len(f) - 1
    assert r.grib_get_long("generatingProcessIdentifier") == [148] * len(r)
    for i in range(len(r)):
        v_ref = f[i + 1].values() - f[i].values()
        np.testing.assert_allclose(r[i].values(), v_ref, rtol=1e-03)

    r = f.deacc(skip_first=True, mark_derived=True)
    assert len(r) == len(f) - 1
    # assert r.grib_get_long("generatingProcessIdentifier") == [254] * len(r)
    for i in range(len(r)):
        v_ref = f[i + 1].values() - f[i].values()
        np.testing.assert_allclose(r[i].values(), v_ref, rtol=1e-03)

    # use grouping by step
    f = mv.Fieldset(path=os.path.join(PATH, "t_time_series.grib"))[:6]

    # only "step" is part of the default indexing keys!
    keys = ["step", "startStep", "stepRange"]
    for key in keys:
        r = f.deacc(key=key)
        assert len(r) == 6
        assert r.grib_get_long("generatingProcessIdentifier") == [148] * len(r)

        v_ref = f[0].values() * 0
        np.testing.assert_allclose(r[0].values(), v_ref, rtol=1e-03)
        v_ref = f[1].values() * 0
        np.testing.assert_allclose(r[1].values(), v_ref, rtol=1e-03)

        steps = {2: (2, 0), 3: (3, 1), 4: (4, 2), 5: (5, 3)}

        for idx, steps in steps.items():
            v_ref = f[steps[0]].values() - f[steps[1]].values()
            np.testing.assert_allclose(r[idx].values(), v_ref, rtol=1e-03)
