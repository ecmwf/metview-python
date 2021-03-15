# (C) Copyright 2017- ECMWF.
#
# This software is licensed under the terms of the Apache Licence Version 2.0
# which can be obtained at http://www.apache.org/licenses/LICENSE-2.0.
#
# In applying this licence, ECMWF does not waive the privileges and immunities
# granted to it by virtue of its status as an intergovernmental organisation
# nor does it submit to any jurisdiction.
#

import datetime
import os

import numpy as np
import pandas as pd
import pytest

import metview as mv
from metview import bindings
from metview.dataset import ParamInfo

PATH = os.path.dirname(__file__)

DB_COLUMNS = {
    "mars.param": ("s", str, False),
    "date": ("l", np.int32, True),
    "time": ("l", np.int32, True),
    "step": ("s", str, True),
    "level": ("l", np.int32, True),
    "number": ("s", str, True),
    "experimentVersionNumber": ("s", str, False),
    "mars.class": ("s", str, False),
    "mars.stream": ("s", str, False),
    "mars.type": ("s", str, False),
    "msgIndex": ("l", np.int64),
}


def file_in_testdir(filename):
    return os.path.join(PATH, filename)


def build_index_db_dataframe(column_data):
    c = {v: column_data[i] for i, v in enumerate(list(DB_COLUMNS.keys()))}
    pd_types = {k: v[1] for k, v in DB_COLUMNS.items()}
    return pd.DataFrame(c).astype(pd_types)


def test_fieldset_select_single_file():
    f = mv.read(file_in_testdir("tuv_pl.grib"))
    assert f._db is None

    # ------------------------
    # single resulting field
    # ------------------------
    g = f.select(shortName="u", level=700)
    assert len(g) == 1
    assert mv.grib_get(g, ["shortName", "level:l"]) == [["u", 700]]

    g1 = mv.read(data=f, param="u", levelist=700)
    d = g - g1
    assert np.allclose(d.values(), np.zeros(len(d.values())))

    # check index db contents
    assert g._db is not None
    assert len(g._db.blocks) == 1
    key = ("u", "isobaricInhPa")
    assert key in g._db.blocks
    md = [
        ["131.128"],
        [20180801],
        [1200],
        [0],
        [700],
        ["0"],
        ["0001"],
        ["od"],
        ["oper"],
        ["an"],
        [0],
    ]
    df_ref = build_index_db_dataframe(md)
    df = g._db.blocks[key]
    if not df.equals(df_ref):
        print(df.compare(df_ref))
        assert False

    # -------------------------
    # multiple resulting fields
    # -------------------------
    g = f.select(shortName=["t", "u"], level=[700, 500])
    assert len(g) == 4
    assert mv.grib_get(g, ["shortName", "level:l"]) == [
        ["t", 500],
        ["t", 700],
        ["u", 500],
        ["u", 700],
    ]

    assert g._db is not None
    assert len(g._db.blocks) == 2
    key_1 = ("t", "isobaricInhPa")
    key_2 = ("u", "isobaricInhPa")
    assert key_1 in g._db.blocks
    assert key_2 in g._db.blocks
    md_1 = [
        ["130.128", "130.128"],
        [20180801, 20180801],
        [1200, 1200],
        [0, 0],
        [500, 700],
        ["0", "0"],
        ["0001", "0001"],
        ["od", "od"],
        ["oper", "oper"],
        ["an", "an"],
        [0, 1],
    ]
    md_2 = [
        ["131.128", "131.128"],
        [20180801, 20180801],
        [1200, 1200],
        [0, 0],
        [500, 700],
        ["0", "0"],
        ["0001", "0001"],
        ["od", "od"],
        ["oper", "oper"],
        ["an", "an"],
        [2, 3],
    ]
    df_1_ref = build_index_db_dataframe(md_1)
    df_1 = g._db.blocks[key_1]
    if not df_1.equals(df_1_ref):
        print(df_1.compare(df_1_ref))
        assert False

    df_2_ref = build_index_db_dataframe(md_2)
    df_2 = g._db.blocks[key_2]
    if not df_2.equals(df_2_ref):
        print(df_2.compare(df_2_ref))
        assert False

    # empty result
    g = f.select(shortName="w")
    assert isinstance(g, mv.Fieldset)
    assert len(g) == 0


def test_fieldset_select_multi_file():
    f = mv.read(file_in_testdir("tuv_pl.grib"))
    f.append(mv.read(file_in_testdir("ml_data.grib")))
    assert f._db is None

    # single resulting field
    g = f.select(shortName="t", level=61)
    assert len(g) == 1
    assert mv.grib_get(g, ["shortName", "level:l", "typeOfLevel"]) == [
        ["t", 61, "hybrid"]
    ]

    g1 = mv.read(data=f, param="t", levelist=61, levtype="ml")
    d = g - g1
    assert np.allclose(d.values(), np.zeros(len(d.values())))

    assert g._db is not None
    assert len(g._db.blocks) == 1
    key = ("t", "hybrid")
    assert key in g._db.blocks
    md = [
        ["130"],
        [20180111],
        [1200],
        [12],
        [61],
        [None],
        ["0001"],
        ["od"],
        ["oper"],
        ["fc"],
        [0],
    ]
    df_ref = build_index_db_dataframe(md)
    df = g._db.blocks[key]

    if not df.equals(df_ref):
        print(df.compare(df_ref))
        assert False


def test_param_info():
    # no exta info
    p = ParamInfo.build("2t")
    assert p.name == "2t"
    assert p.level_type == "surface"
    assert p.level is None

    p = ParamInfo.build("t2")
    assert p.name == "2t"
    assert p.level_type == "surface"
    assert p.level is None

    p = ParamInfo.build("msl")
    assert p.name == "msl"
    assert p.level_type == "surface"
    assert p.level is None

    p = ParamInfo.build("t500")
    assert p.name == "t"
    assert p.level_type == "isobaricInhPa"
    assert p.level == 500

    p = ParamInfo.build("t500hPa")
    assert p.name == "t"
    assert p.level_type == "isobaricInhPa"
    assert p.level == 500

    p = ParamInfo.build("t")
    assert p.name == "t"
    assert p.level_type == "surface"
    assert p.level is None

    p = ParamInfo.build("t320K")
    assert p.name == "t"
    assert p.level_type == "theta"
    assert p.level == 320

    p = ParamInfo.build("t72ml")
    assert p.name == "t"
    assert p.level_type == "hybrid"
    assert p.level == 72

    p = ParamInfo.build("wind10")
    assert p.name == "wind10"
    assert p.level_type == "surface"
    assert p.level is None

    p = ParamInfo.build("wind100")
    assert p.name == "wind"
    assert p.level_type == "isobaricInhPa"
    assert p.level == 100

    # exta info
    param_level_types = {
        "2t": ["surface"],
        "msl": ["surface"],
        "wind10": ["surface"],
        "t": ["isobaricInhPa", "theta"],
        "wind": ["isobaricInhPa"],
    }

    p = ParamInfo.build("2t", param_level_types=param_level_types)
    assert p.name == "2t"
    assert p.level_type == "surface"
    assert p.level is None

    try:
        p = ParamInfo.build("22t", param_level_types=param_level_types)
        assert False
    except:
        pass

    p = ParamInfo.build("t2", param_level_types=param_level_types)
    assert p.name == "2t"
    assert p.level_type == "surface"
    assert p.level is None

    p = ParamInfo.build("msl", param_level_types=param_level_types)
    assert p.name == "msl"
    assert p.level_type == "surface"
    assert p.level is None

    p = ParamInfo.build("t500", param_level_types=param_level_types)
    assert p.name == "t"
    assert p.level_type == "isobaricInhPa"
    assert p.level == 500

    p = ParamInfo.build("t500hPa", param_level_types=param_level_types)
    assert p.name == "t"
    assert p.level_type == "isobaricInhPa"
    assert p.level == 500

    p = ParamInfo.build("t", param_level_types=param_level_types)
    assert p.name == "t"
    assert p.level_type == "isobaricInhPa"
    assert p.level is None

    p = ParamInfo.build("t320K", param_level_types=param_level_types)
    assert p.name == "t"
    assert p.level_type == "theta"
    assert p.level == 320

    try:
        p = ParamInfo.build("t72ml", param_level_types=param_level_types)
        assert False
    except:
        pass

    p = ParamInfo.build("wind10", param_level_types=param_level_types)
    assert p.name == "wind10"
    assert p.level_type == "surface"
    assert p.level is None

    p = ParamInfo.build("wind100", param_level_types=param_level_types)
    assert p.name == "wind"
    assert p.level_type == "isobaricInhPa"
    assert p.level == 100

    p = ParamInfo.build("wind", param_level_types=param_level_types)
    assert p.name == "wind"
    assert p.level_type == "isobaricInhPa"
    assert p.level is None


def test_fieldset_select_operator_single_file():
    f = mv.read(file_in_testdir("tuv_pl.grib"))

    g = f["u700"]
    assert f._db is not None
    assert g._db is not None
    assert len(g) == 1
    assert mv.grib_get(g, ["shortName", "level:l"]) == [["u", 700]]

    g1 = mv.read(data=f, param="u", levelist=700)
    d = g - g1
    assert np.allclose(d.values(), np.zeros(len(d.values())))

    g = f["t"]
    assert len(g) == 6
    assert mv.grib_get(g, ["shortName", "level:l"]) == [
        ["t", 300],
        ["t", 400],
        ["t", 500],
        ["t", 700],
        ["t", 850],
        ["t", 1000],
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

    g1 = mv.read(data=f, param="t", levelist=61, levtype="ml")
    d = g - g1
    assert np.allclose(d.values(), np.zeros(len(d.values())))
