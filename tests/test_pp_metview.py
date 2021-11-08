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
    assert type(f) is mv.Fieldset
    assert len(f) == 0


def test_fieldset_contructor_bad_file_path():
    with pytest.raises(FileNotFoundError):
        f = mv.Fieldset(path="does/not/exist")


def test_non_empty_fieldset_contructor_len():
    f = mv.Fieldset(path=os.path.join(PATH, "test.grib"))
    assert type(f) is mv.Fieldset
    assert len(f) == 1


def test_non_empty_fieldset_contructor_len_18():
    f = mv.Fieldset(path=os.path.join(PATH, "tuv_pl.grib"))
    assert type(f) is mv.Fieldset
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


def test_grib_set_string():
    f = mv.Fieldset(path=os.path.join(PATH, "tuv_pl.grib"))[0:2]
    g = f.grib_set_string("pressureUnits", "silly")
    assert g.grib_get_string("pressureUnits") == ["silly"] * 2
    assert f.grib_get_string("pressureUnits") == ["hPa"] * 2


def test_grib_set_long():
    f = mv.Fieldset(path=os.path.join(PATH, "tuv_pl.grib"))[0:2]
    g = f.grib_set_long("level", 95)
    assert g.grib_get_long("level") == [95] * 2
    assert f.grib_get_long("level") == [1000] * 2


def test_grib_set_double():
    f = mv.Fieldset(path=os.path.join(PATH, "tuv_pl.grib"))[0:2]
    g = f.grib_set_double("level", 95)
    assert g.grib_get_double("level") == [95] * 2
    assert f.grib_get_double("level") == [1000] * 2
    orig_point = f.grib_get_double("longitudeOfFirstGridPointInDegrees")
    g = f.grib_set_double("longitudeOfFirstGridPointInDegrees", 95.6)
    assert g.grib_get_double("longitudeOfFirstGridPointInDegrees") == [95.6] * 2
    assert f.grib_get_double("longitudeOfFirstGridPointInDegrees") == orig_point


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


def test_single_index_0():
    path = os.path.join(PATH, "tuv_pl.grib")
    f = mv.Fieldset(path=path)
    f0 = f[0]
    assert type(f0) is mv.Fieldset
    assert len(f0) == 1
    assert f0.grib_get_string("shortName") == "t"
    v = f0.values()
    eps = 0.001
    assert len(v) == 2664
    assert np.isclose(v[1088], 304.5642, eps)


def test_single_index_17():
    path = os.path.join(PATH, "tuv_pl.grib")
    f = mv.Fieldset(path=path)
    f17 = f[17]
    assert type(f17) is mv.Fieldset
    assert len(f17) == 1
    assert f17.grib_get_string("shortName") == "v"
    v = f17.values()
    eps = 0.001
    assert len(v) == 2664
    assert np.isclose(v[2663], -11.0797, eps)


def test_single_index_minus_1():
    path = os.path.join(PATH, "tuv_pl.grib")
    f = mv.Fieldset(path=path)
    fm1 = f[-1]
    assert type(fm1) is mv.Fieldset
    assert len(fm1) == 1
    assert fm1.grib_get_string("shortName") == "v"
    v = fm1.values()
    eps = 0.001
    assert len(v) == 2664
    assert np.isclose(v[2663], -11.0797, eps)


def test_single_index_bad():
    path = os.path.join(PATH, "tuv_pl.grib")
    f = mv.Fieldset(path=path)
    with pytest.raises(IndexError):
        fbad = f[27]


def test_slice_0_5():
    path = os.path.join(PATH, "tuv_pl.grib")
    f = mv.Fieldset(path=path)
    f05 = f[0:5]
    assert type(f05) is mv.Fieldset
    assert len(f05) == 5
    assert f05.grib_get_string("shortName") == ["t", "u", "v", "t", "u"]
    v = f05.values()
    assert v.shape == (5, 2664)
    # check the original fieldset
    assert len(f) == 18
    sn = f.grib_get_string("shortName")
    assert sn == ["t", "u", "v"] * 6


def test_array_indexing():
    path = os.path.join(PATH, "tuv_pl.grib")
    f = mv.Fieldset(path=path)
    indexes = np.array([1, 16, 5, 9])
    fv = f[indexes]
    assert type(fv) is mv.Fieldset
    assert len(fv) == 4
    assert fv.grib_get_string("shortName") == ["u", "u", "v", "t"]
    # check with bad indexes
    indexes = np.array([1, 36, 5, 9])
    with pytest.raises(IndexError):
        fvbad = f[indexes]


def test_fieldset_iterator():
    grib = mv.Fieldset(path=os.path.join(PATH, "tuv_pl.grib"))
    sn = grib.grib_get_string("shortName")
    assert len(sn) == 18
    iter_sn = []
    for f in grib:
        iter_sn.append(f.grib_get_string("shortName"))
    assert len(iter_sn) == len(sn)
    assert iter_sn == sn
    iter_sn = [f.grib_get_string("shortName") for f in grib]
    assert iter_sn == sn


def test_fieldset_iterator_multiple():
    grib = mv.Fieldset(path=os.path.join(PATH, "tuv_pl.grib"))
    sn = grib.grib_get_string("shortName")
    assert len(sn) == 18
    for i in [1, 2, 3]:
        iter_sn = []
        for f in grib:
            iter_sn.append(f.grib_get_string("shortName"))
        assert len(iter_sn) == len(sn)
        for i in range(0, 18):
            assert sn[i] == iter_sn[i]


def test_fieldset_iterator_with_zip():
    # this tests something different with the iterator - this does not try to
    # 'go off the edge' of the fieldset, because the length is determined by
    # the list of levels
    grib = mv.Fieldset(path=os.path.join(PATH, "tuv_pl.grib"))
    ref_levs = grib.grib_get_long("level")
    assert len(ref_levs) == 18
    levs1 = []
    levs2 = []
    for k, f in zip(grib.grib_get_long("level"), grib):
        levs1.append(k)
        levs2.append(f.grib_get_long("level"))
    assert levs1 == ref_levs
    assert levs2 == ref_levs


def test_fieldset_iterator_with_zip_multiple():
    # same as test_fieldset_iterator_with_zip() but multiple times
    grib = mv.Fieldset(path=os.path.join(PATH, "tuv_pl.grib"))
    ref_levs = grib.grib_get_long("level")
    assert len(ref_levs) == 18
    for i in [1, 2, 3]:
        levs1 = []
        levs2 = []
        for k, f in zip(grib.grib_get_long("level"), grib):
            levs1.append(k)
            levs2.append(f.grib_get_long("level"))
        print(grib.grib_get_long("level"))
        assert levs1 == ref_levs
        assert levs2 == ref_levs


def test_fieldset_reverse_iterator():
    grib = mv.Fieldset(path=os.path.join(PATH, "tuv_pl.grib"))
    sn = grib.grib_get_string("shortName")
    sn_reversed = list(reversed(sn))
    assert sn_reversed[0] == "v"
    assert sn_reversed[17] == "t"
    gribr = reversed(grib)
    iter_sn = [f.grib_get_string("shortName") for f in gribr]
    assert len(iter_sn) == len(sn_reversed)
    assert iter_sn == sn_reversed
    assert iter_sn == ["v", "u", "t"] * 6


def test_fieldset_append():
    g = mv.Fieldset(path=os.path.join(PATH, "tuv_pl.grib"))
    h = mv.Fieldset(path=os.path.join(PATH, "all_missing_vals.grib"))
    i = g[0:3]
    i.append(h)
    assert i.grib_get_string("shortName") == ["t", "u", "v", "z"]


def test_fieldset_merge():
    g = mv.Fieldset(path=os.path.join(PATH, "tuv_pl.grib"))
    h = mv.Fieldset(path=os.path.join(PATH, "all_missing_vals.grib"))
    i = g[0:3]
    j = i.merge(h)  # does not alter the original fieldset
    assert i.grib_get_string("shortName") == ["t", "u", "v"]
    assert j.grib_get_string("shortName") == ["t", "u", "v", "z"]


def test_field_scalar_func():
    f = mv.Fieldset(path=os.path.join(PATH, "tuv_pl.grib"))[0:3]
    # fieldset op scalar
    g = f + 10
    assert type(g) == mv.Fieldset
    assert len(g) == 3
    np.testing.assert_allclose(g.values(), f.values() + 10)
    q = f - 5
    np.testing.assert_allclose(q.values(), f.values() - 5)
    # scalar op fieldset
    h = 20 + f
    assert type(h) == mv.Fieldset
    assert len(h) == 3
    np.testing.assert_allclose(h.values(), f.values() + 20)
    r = 25 - f
    np.testing.assert_allclose(r.values(), 25 - f.values())


def test_fieldset_fieldset_func():
    f = mv.Fieldset(path=os.path.join(PATH, "tuv_pl.grib"))[0:3]
    g = mv.Fieldset(path=os.path.join(PATH, "tuv_pl.grib"))[5:8]
    h = f + g
    np.testing.assert_allclose(h.values(), f.values() + g.values())
    i = g + f
    np.testing.assert_allclose(i.values(), g.values() + f.values())
    q = f - g
    np.testing.assert_allclose(q.values(), f.values() - g.values())
    r = g - f
    np.testing.assert_allclose(r.values(), g.values() - f.values())


def test_fieldset_multiple_funcs():
    f = mv.Fieldset(path=os.path.join(PATH, "tuv_pl.grib"))
    g = 1 - ((f[0] + f[3]) - 5)
    np.testing.assert_allclose(g.values(), 1 - ((f[0].values() + f[3].values()) - 5))
