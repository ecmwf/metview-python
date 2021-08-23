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
import shutil
import tempfile

import numpy as np
import pandas as pd
import pytest

import metview as mv
from metview import bindings
from metview.indexer import GribIndexer

PATH = os.path.dirname(__file__)
DS_DIR = ""


def build_dataset():
    # make conf file
    global DS_DIR
    DS_DIR = tempfile.mkdtemp()
    # DS_DIR = "/var/folders/ng/g0zkhc2s42xbslpsywwp_26m0000gn/T/tmpa_i2t_y6"
    # print(f"DS_DIR={DS_DIR}")
    data_dir = os.path.join(DS_DIR, "data")
    an_dir = os.path.join("__ROOTDIR__", "an")
    oper_dir = os.path.join("__ROOTDIR__", "oper")

    ds_def = fr"""
experiments:
    - an:
        label: "an"
        dir: {an_dir}
        fname : re"[A-Za-z0-9]+_[A-z]+\.grib"
    - oper:
        label: "oper"
        dir: {oper_dir}
        fname : re"[A-Za-z0-9]+_[A-z]+\.grib"
"""
    with open(os.path.join(DS_DIR, "data.yaml"), "w") as f:
        f.write(ds_def)

    shutil.copytree(os.path.join(PATH, "ds"), os.path.join(DS_DIR, "data"))
    conf_dir = os.path.join(DS_DIR, "conf")
    if not os.path.exists(conf_dir):
        os.mkdir(conf_dir)


def remove_dataset():
    global DS_DIR
    if DS_DIR and os.path.exists(DS_DIR) and not DS_DIR in ["/", "."]:
        shutil.rmtree(DS_DIR)
    DS_DIR = ""


def test_dataset():
    build_dataset()

    ds = mv.load_dataset("test", path=DS_DIR)
    assert list(ds.field_conf.keys()) == ["an", "oper"]

    # indexing
    ds.scan()
    index_dir = os.path.join(DS_DIR, "index")
    assert os.path.exists(index_dir)
    for comp in ["an", "oper"]:
        for f in [
            "datafiles.yaml",
            "scalar.csv.gz",
            "wind10m.csv.gz",
            "wind.csv.gz",
            "wind3d.csv.gz",
        ]:
            assert os.path.exists(os.path.join(index_dir, comp, f))

    # reload ds
    ds = mv.load_dataset("test", path=DS_DIR)

    # Analysis
    d = ds["an"].select(
        dateTime=[mv.date("2016-09-25 00:00"), mv.date("2016-09-26 00:00")]
    )

    assert isinstance(d, mv.Fieldset)
    assert set(ds["an"].blocks.keys()) == set(["scalar", "wind10m", "wind", "wind3d"])
    assert set(d._db.blocks.keys()) == set(["scalar", "wind10m", "wind", "wind3d"])

    v = d["msl"]
    assert isinstance(v, mv.Fieldset)
    assert len(v) == 2
    assert mv.grib_get(v, ["shortName", "date:l", "time:l"]) == [
        ["msl", 20160925, 0],
        ["msl", 20160926, 0],
    ]

    v = d["t500"]
    assert isinstance(v, mv.Fieldset)
    assert len(v) == 2
    assert mv.grib_get(v, ["shortName", "date:l", "time:l", "level:l"]) == [
        ["t", 20160925, 0, 500],
        ["t", 20160926, 0, 500],
    ]

    v = d["pv320K"]
    assert isinstance(v, mv.Fieldset)
    assert len(v) == 2
    assert mv.grib_get(
        v, ["shortName", "date:l", "time:l", "level:l", "typeOfLevel"]
    ) == [["pv", 20160925, 0, 320, "theta"], ["pv", 20160926, 0, 320, "theta"]]

    v = d["wind850"]
    assert isinstance(v, mv.Fieldset)
    assert len(v) == 4
    assert mv.grib_get(
        v, ["shortName", "date:l", "time:l", "level:l", "typeOfLevel"]
    ) == [
        ["u", 20160925, 0, 850, "isobaricInhPa"],
        ["v", 20160925, 0, 850, "isobaricInhPa"],
        ["u", 20160926, 0, 850, "isobaricInhPa"],
        ["v", 20160926, 0, 850, "isobaricInhPa"],
    ]

    v = d["wind10m"]
    assert isinstance(v, mv.Fieldset)
    assert len(v) == 4
    assert mv.grib_get(v, ["shortName", "date:l", "time:l", "typeOfLevel"]) == [
        ["10u", 20160925, 0, "surface"],
        ["10v", 20160925, 0, "surface"],
        ["10u", 20160926, 0, "surface"],
        ["10v", 20160926, 0, "surface"],
    ]

    v = d["wind"]
    assert isinstance(v, mv.Fieldset)
    assert len(v) == 8
    assert mv.grib_get(
        v, ["shortName", "date:l", "time:l", "level:l", "typeOfLevel"]
    ) == [
        ["u", 20160925, 0, 500, "isobaricInhPa"],
        ["v", 20160925, 0, 500, "isobaricInhPa"],
        ["u", 20160925, 0, 850, "isobaricInhPa"],
        ["v", 20160925, 0, 850, "isobaricInhPa"],
        ["u", 20160926, 0, 500, "isobaricInhPa"],
        ["v", 20160926, 0, 500, "isobaricInhPa"],
        ["u", 20160926, 0, 850, "isobaricInhPa"],
        ["v", 20160926, 0, 850, "isobaricInhPa"],
    ]

    v = d["wind3d"]
    assert isinstance(v, mv.Fieldset)
    assert len(v) == 12
    assert mv.grib_get(
        v, ["shortName", "date:l", "time:l", "level:l", "typeOfLevel"]
    ) == [
        ["u", 20160925, 0, 500, "isobaricInhPa"],
        ["v", 20160925, 0, 500, "isobaricInhPa"],
        ["w", 20160925, 0, 500, "isobaricInhPa"],
        ["u", 20160925, 0, 850, "isobaricInhPa"],
        ["v", 20160925, 0, 850, "isobaricInhPa"],
        ["w", 20160925, 0, 850, "isobaricInhPa"],
        ["u", 20160926, 0, 500, "isobaricInhPa"],
        ["v", 20160926, 0, 500, "isobaricInhPa"],
        ["w", 20160926, 0, 500, "isobaricInhPa"],
        ["u", 20160926, 0, 850, "isobaricInhPa"],
        ["v", 20160926, 0, 850, "isobaricInhPa"],
        ["w", 20160926, 0, 850, "isobaricInhPa"],
    ]

    # Oper
    run = mv.date("2016-09-25 00:00")
    d = ds["oper"].select(date=run.date(), time=run.time(), step=[120])

    assert isinstance(d, mv.Fieldset)
    assert set(ds["oper"].blocks.keys()) == set(["scalar", "wind10m", "wind", "wind3d"])
    assert set(d._db.blocks.keys()) == set(["scalar", "wind10m", "wind", "wind3d"])

    v = d["msl"]
    assert isinstance(v, mv.Fieldset)
    assert len(v) == 1
    assert mv.grib_get(v, ["shortName", "date:l", "time:l", "step:l"]) == [
        ["msl", 20160925, 0, 120]
    ]

    remove_dataset()
