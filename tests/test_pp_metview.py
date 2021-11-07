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


def test_grib_get_long_array_1():
    f = mv.Fieldset(path=os.path.join(PATH, "rgg_small_subarea_cellarea_ref.grib"))
    pl = f.grib_get_long_array("pl")
    assert isinstance(pl, np.ndarray)
    assert len(pl) == 73
    assert pl[0] == 24
    assert pl[1] == 28
    assert pl[20] == 104
    assert pl[72] == 312


def test_grib_get_double_array_1():
    f = mv.Fieldset(path=os.path.join(PATH, "test.grib"))
    v = f.grib_get_double_array("values")
    assert isinstance(v, np.ndarray)
    assert len(v) == 115680
    assert np.isclose(v[0], 260.4356)
    assert np.isclose(v[24226], 276.1856)
    assert np.isclose(v[36169], 287.9356)
    assert np.isclose(v[115679], 227.1856)


def test_grib_get_double_array_18():
    f = mv.Fieldset(path=os.path.join(PATH, "tuv_pl.grib"))
    v = f.grib_get_double_array("values")
    assert isinstance(v, list)
    assert len(v) == 18
    assert isinstance(v[0], np.ndarray)
    assert isinstance(v[17], np.ndarray)
    assert len(v[0]) == 2664
    assert len(v[17]) == 2664
    eps = 0.001
    assert np.isclose(v[0][0], 272.5642, eps)
    assert np.isclose(v[0][1088], 304.5642, eps)
    assert np.isclose(v[17][0], -3.0797, eps)
    assert np.isclose(v[17][2663], -11.0797, eps)


def test_values_1():
    f = mv.Fieldset(path=os.path.join(PATH, "test.grib"))
    v = f.values()
    assert isinstance(v, np.ndarray)
    assert len(v) == 115680
    assert np.isclose(v[0], 260.4356)
    assert np.isclose(v[24226], 276.1856)
    assert np.isclose(v[36169], 287.9356)
    assert np.isclose(v[115679], 227.1856)


def test_values_18():
    f = mv.Fieldset(path=os.path.join(PATH, "tuv_pl.grib"))
    v = f.values()
    assert isinstance(v, np.ndarray)
    assert v.shape == (18, 2664)
    assert isinstance(v[0], np.ndarray)
    assert isinstance(v[17], np.ndarray)
    assert len(v[0]) == 2664
    assert len(v[17]) == 2664
    eps = 0.001
    assert np.isclose(v[0][0], 272.5642, eps)
    assert np.isclose(v[0][1088], 304.5642, eps)
    assert np.isclose(v[17][0], -3.0797, eps)
    assert np.isclose(v[17][2663], -11.0797, eps)


def test_values_with_missing():
    f = mv.Fieldset(path=os.path.join(PATH, "t_with_missing.grib"))
    v = f.values()
    assert isinstance(v, np.ndarray)
    assert v.shape == (2664,)
    eps = 0.001
    assert np.isclose(v[0], 272.5642, eps)
    assert np.isnan(v[798])
    assert np.isnan(v[806])
    assert np.isnan(v[1447])
    assert np.isclose(v[2663], 240.5642, eps)


def test_write_fieldset():
    f = mv.Fieldset(path=os.path.join(PATH, "tuv_pl.grib"))
    temp_path = "written_tuv_pl.grib"
    f.write(temp_path)
    assert os.path.isfile(temp_path)
    g = mv.Fieldset(path=temp_path)
    assert type(g) == mv.Fieldset
    assert len(g) == 18
    sn = g.grib_get_string("shortName")
    assert sn == ["t", "u", "v"] * 6
    f = 0
    os.remove(temp_path)


def test_field_func():
    def sqr_func(x):
        return x * x

    f = mv.Fieldset(path=os.path.join(PATH, "tuv_pl.grib"))
    g = f.field_func(sqr_func)
    assert type(g) == mv.Fieldset
    assert len(g) == 18
    vf = f.values()
    vg = g.values()
    np.testing.assert_allclose(vg, vf * vf)


def test_field_func_neg():
    f = mv.Fieldset(path=os.path.join(PATH, "tuv_pl.grib"))
    g = -f
    assert type(g) == mv.Fieldset
    assert len(g) == 18
    vf = f.values()
    vg = g.values()
    np.testing.assert_allclose(vg, -vf)


def test_field_func_abs():
    f = mv.Fieldset(path=os.path.join(PATH, "tuv_pl.grib"))
    g = f.abs()
    assert type(g) == mv.Fieldset
    assert len(g) == 18
    vf = f.values()
    vg = g.values()
    np.testing.assert_allclose(vg, np.abs(vf))


def test_temporary_file():
    # create a temp file, then delete the fieldset - temp should be removed
    f = mv.Fieldset(path=os.path.join(PATH, "tuv_pl.grib"))
    g = -f
    temp_path = g.temporary.path
    assert os.path.isfile(temp_path)
    g = None
    assert not os.path.isfile(temp_path)


def test_permanent_file_not_accidentally_deleted():
    path = os.path.join(PATH, "tuv_pl.grib")
    f = mv.Fieldset(path=path)
    assert os.path.isfile(path)
    f = None
    assert os.path.isfile(path)
