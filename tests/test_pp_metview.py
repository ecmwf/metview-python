# (C) Copyright 2017- ECMWF.
#
# This software is licensed under the terms of the Apache Licence Version 2.0
# which can be obtained at http://www.apache.org/licenses/LICENSE-2.0.
#
# In applying this licence, ECMWF does not waive the privileges and immunities
# granted to it by virtue of its status as an intergovernmental organisation
# nor does it submit to any jurisdiction.

import numpy as np
import os
import pytest

from metview.pure_python import fieldset as mv

PATH = os.path.dirname(__file__)


def test_empty_fieldset_contructor():
    f = mv.Fieldset()
    assert type(f) == mv.Fieldset
    assert len(f) == 0


def test_fieldset_contructor_bad_file_path():
    with pytest.raises(FileNotFoundError):
        f = mv.Fieldset(path="does/not/exist")


def test_non_empty_fieldset_contructor_len():
    f = mv.Fieldset(path=os.path.join(PATH, "test.grib"))
    assert type(f) == mv.Fieldset
    assert len(f) == 1


def test_non_empty_fieldset_contructor_len_18():
    f = mv.Fieldset(path=os.path.join(PATH, "tuv_pl.grib"))
    assert type(f) == mv.Fieldset
    assert len(f) == 18


def test_grib_get_string_1():
    f = mv.Fieldset(path=os.path.join(PATH, "test.grib"))
    sn = f.grib_get_string("shortName")
    assert sn == "2t"


def test_grib_get_string_18():
    f = mv.Fieldset(path=os.path.join(PATH, "tuv_pl.grib"))
    sn = f.grib_get_string("shortName")
    assert sn == ["t", "u", "v"] * 6


def test_grib_get_long_1():
    f = mv.Fieldset(path=os.path.join(PATH, "test.grib"))
    lev = f.grib_get_long("level")
    assert lev == 0


def test_grib_get_long_18():
    f = mv.Fieldset(path=os.path.join(PATH, "tuv_pl.grib"))
    lev = f.grib_get_long("level")
    assert lev == ([1000] * 3) + ([850] * 3) + ([700] * 3) + ([500] * 3) + (
        [400] * 3
    ) + ([300] * 3)


def test_grib_get_double_1():
    f = mv.Fieldset(path=os.path.join(PATH, "test.grib"))
    m = f.grib_get_double("max")
    assert np.isclose(m, 316.061)


def test_grib_get_double_18():
    f = mv.Fieldset(path=os.path.join(PATH, "tuv_pl.grib"))
    m = f.grib_get_double("max")
    ref_m = [
        320.564,
        21.7131,
        19.8335,
        304.539,
        43.1016,
        28.661,
        295.265,
        44.1455,
        31.6385,
        275.843,
        52.74,
        47.0099,
        264.003,
        62.2138,
        55.9496,
        250.653,
        66.4555,
        68.9203,
    ]
    np.testing.assert_allclose(m, ref_m, 0.001)
