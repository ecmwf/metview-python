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

PATH = os.path.dirname(__file__)

DB_COLUMNS = {
    "shortName": ("s", str),
    "mars.param": ("s", str),
    "date": ("l", np.int32),
    "time": ("l", np.int32),
    "step": ("s", str),
    "level": ("l", np.int32),
    "typeOfLevel": ("s", str),
    "number": ("s", str),
    "expver": ("s", str),
    "type": ("s", str),
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

    # single resulting field
    g = f.select(shortName="u", level=700)
    assert len(g) == 1
    assert mv.grib_get(g, ["shortName", "level:l"]) == [["u", 700]]

    g1 = mv.read(data=f, param="u", levelist=700)
    d = g - g1
    assert np.allclose(d.values(), np.zeros(len(d.values())))

    assert g._db is not None
    assert len(g._db.params) == 1
    key = ("u", "isobaricInhPa")
    assert key in g._db.params
    md = [
        ["u"],
        ["131.128"],
        [20180801],
        [1200],
        [0],
        [700],
        ["isobaricInhPa"],
        ["0"],
        ["0001"],
        ["an"],
        [0],
    ]
    df_ref = build_index_db_dataframe(md)
    df = g._db.params[key]
    if not df.equals(df_ref):
        print(df.compare(df_ref))
        assert False

    # multiple resulting fields
    g = f.select(shortName=["t", "u"], level=[700, 500])
    assert len(g) == 4
    assert mv.grib_get(g, ["shortName", "level:l"]) == [
        ["t", 500],
        ["t", 700],
        ["u", 500],
        ["u", 700],
    ]

    assert g._db is not None
    assert len(g._db.params) == 2
    key_1 = ("t", "isobaricInhPa")
    key_2 = ("u", "isobaricInhPa")
    assert key_1 in g._db.params
    assert key_2 in g._db.params
    md_1 = [
        ["t", "t"],
        ["130.128", "130.128"],
        [20180801, 20180801],
        [1200, 1200],
        [0, 0],
        [500, 700],
        ["isobaricInhPa", "isobaricInhPa"],
        ["0", "0"],
        ["0001", "0001"],
        ["an", "an"],
        [0, 1],
    ]
    md_2 = [
        ["u", "u"],
        ["131.128", "131.128"],
        [20180801, 20180801],
        [1200, 1200],
        [0, 0],
        [500, 700],
        ["isobaricInhPa", "isobaricInhPa"],
        ["0", "0"],
        ["0001", "0001"],
        ["an", "an"],
        [2, 3],
    ]
    df_1_ref = build_index_db_dataframe(md_1)
    df_1 = g._db.params[key_1]
    if not df_1.equals(df_1_ref):
        print(df_1.compare(df_1_ref))
        assert False

    df_2_ref = build_index_db_dataframe(md_2)
    df_2 = g._db.params[key_2]
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
    assert len(g._db.params) == 1
    key = ("t", "hybrid")
    assert key in g._db.params
    md = [
        ["t"],
        ["130"],
        [20180111],
        [1200],
        [12],
        [61],
        ["hybrid"],
        [None],
        ["0001"],
        ["fc"],
        [0],
    ]
    df_ref = build_index_db_dataframe(md)
    df = g._db.params[key]

    if not df.equals(df_ref):
        print(df.compare(df_ref))
        assert False
