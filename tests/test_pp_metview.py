# (C) Copyright 2017- ECMWF.
#
# This software is licensed under the terms of the Apache Licence Version 2.0
# which can be obtained at http://www.apache.org/licenses/LICENSE-2.0.
#
# In applying this licence, ECMWF does not waive the privileges and immunities
# granted to it by virtue of its status as an intergovernmental organisation
# nor does it submit to any jurisdiction.

from inspect import ArgInfo
import numpy as np
import os
import pytest

import metview.metviewpy as mv
from metview.metviewpy import utils
from metview.metviewpy.temporary import is_temp_file

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


def test_fieldset_create_from_list_of_paths():
    paths = [os.path.join(PATH, "t_for_xs.grib"), os.path.join(PATH, "ml_data.grib")]
    f = mv.Fieldset(path=paths)
    assert len(f) == 42
    assert f[0:2].grib_get_long("level") == [1000, 850]
    assert f[5:9].grib_get_long("level") == [300, 1, 1, 5]
    assert f[40:42].grib_get_long("level") == [133, 137]


def test_fieldset_create_from_glob_path_single():
    f = mv.Fieldset(path=os.path.join(PATH, "test.g*ib"))
    assert type(f) == mv.Fieldset
    assert len(f) == 1


def test_fieldset_create_from_glob_path_multi():
    f = mv.Fieldset(path=os.path.join(PATH, "t_*.grib"))
    assert type(f) == mv.Fieldset
    assert len(f) == 17
    par_ref = [
        ["t", "1000"],
        ["t", "850"],
        ["t", "700"],
        ["t", "500"],
        ["t", "400"],
        ["t", "300"],
        ["t", "1000"],
        ["z", "1000"],
        ["t", "1000"],
        ["z", "1000"],
        ["t", "1000"],
        ["z", "1000"],
        ["t", "1000"],
        ["z", "1000"],
        ["t", "1000"],
        ["z", "1000"],
        ["t", "1000"],
    ]
    assert par_ref == f.grib_get(["shortName", "level"])


def test_fieldset_create_from_glob_paths():
    f = mv.Fieldset(
        path=[os.path.join(PATH, "test.g*ib"), os.path.join(PATH, "t_*.grib")]
    )
    assert type(f) == mv.Fieldset
    assert len(f) == 18
    par_ref = [
        ["2t", "0"],
        ["t", "1000"],
        ["t", "850"],
        ["t", "700"],
        ["t", "500"],
        ["t", "400"],
        ["t", "300"],
        ["t", "1000"],
        ["z", "1000"],
        ["t", "1000"],
        ["z", "1000"],
        ["t", "1000"],
        ["z", "1000"],
        ["t", "1000"],
        ["z", "1000"],
        ["t", "1000"],
        ["z", "1000"],
        ["t", "1000"],
    ]
    assert par_ref == f.grib_get(["shortName", "level"])


def test_read_1():
    f = mv.read(os.path.join(PATH, "test.grib"))
    assert type(f) is mv.Fieldset
    assert len(f) == 1


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


def test_grib_get_generic():
    f = mv.Fieldset(path=os.path.join(PATH, "tuv_pl.grib"))[0:4]
    sn = f.grib_get(["shortName"])
    assert sn == [["t"], ["u"], ["v"], ["t"]]
    cs = f.grib_get(["centre:s"])
    assert cs == [["ecmf"], ["ecmf"], ["ecmf"], ["ecmf"]]
    cl = f.grib_get(["centre:l"])
    assert cl == [[98], [98], [98], [98]]
    lg = f.grib_get(["level:d", "cfVarName"])
    assert lg == [[1000, "t"], [1000, "u"], [1000, "v"], [850, "t"]]
    lgk = f.grib_get(["level:d", "cfVarName"], "key")
    assert lgk == [[1000, 1000, 1000, 850], ["t", "u", "v", "t"]]
    with pytest.raises(ValueError):
        lgk = f.grib_get(["level:d", "cfVarName"], "silly")
    ln = f.grib_get(["level:n"])
    assert ln == [[1000], [1000], [1000], [850]]
    cn = f.grib_get(["centre:n"])
    assert cn == [["ecmf"], ["ecmf"], ["ecmf"], ["ecmf"]]
    vn = f[0].grib_get(["longitudes:n"])
    assert vn[0][0][0] == 0
    assert vn[0][0][1] == 5
    assert vn[0][0][5] == 25


def test_grib_get_generic_key_not_exist():
    a = mv.Fieldset(path=os.path.join(PATH, "tuv_pl.grib"))[0:2]
    kv = a.grib_get(["silly"])
    assert kv == [[None], [None]]
    with pytest.raises(Exception):
        kv = a.grib_get_long(["silly"])


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
    g = f.grib_set_string(["pressureUnits", "silly"])
    assert g.grib_get_string("pressureUnits") == ["silly"] * 2
    assert f.grib_get_string("pressureUnits") == ["hPa"] * 2
    g = f.grib_set_string(["pressureUnits", "silly", "shortName", "q"])
    assert g.grib_get_string("pressureUnits") == ["silly"] * 2
    assert g.grib_get_string("shortName") == ["q", "q"]
    assert f.grib_get_string("pressureUnits") == ["hPa"] * 2
    assert f.grib_get_string("shortName") == ["t", "u"]


def test_grib_set_long():
    f = mv.Fieldset(path=os.path.join(PATH, "tuv_pl.grib"))[0:2]
    g = f.grib_set_long(["level", 95])
    assert g.grib_get_long("level") == [95] * 2
    assert f.grib_get_long("level") == [1000] * 2
    g = f.grib_set_long(["level", 95, "time", 1800])
    assert g.grib_get_long("level") == [95] * 2
    assert g.grib_get_long("time") == [1800] * 2
    assert f.grib_get_long("level") == [1000] * 2
    assert f.grib_get_long("time") == [1200] * 2


def test_grib_set_double():
    f = mv.Fieldset(path=os.path.join(PATH, "tuv_pl.grib"))[0:2]
    g = f.grib_set_double(["level", 95])
    assert g.grib_get_double("level") == [95] * 2
    assert f.grib_get_double("level") == [1000] * 2
    orig_point = f.grib_get_double("longitudeOfFirstGridPointInDegrees")
    g = f.grib_set_double(["longitudeOfFirstGridPointInDegrees", 95.6])
    assert g.grib_get_double("longitudeOfFirstGridPointInDegrees") == [95.6] * 2
    assert f.grib_get_double("longitudeOfFirstGridPointInDegrees") == orig_point


def test_grib_set_generic():
    f = mv.Fieldset(path=os.path.join(PATH, "tuv_pl.grib"))[0:2]
    g = f.grib_set(["shortName", "r"])
    assert g.grib_get_string("shortName") == ["r"] * 2
    assert f.grib_get_string("shortName") == ["t", "u"]
    g = f.grib_set(["shortName:s", "q"])
    assert g.grib_get_string("shortName") == ["q"] * 2
    assert f.grib_get_string("shortName") == ["t", "u"]

    g = f.grib_set(["level:l", 500, "shortName", "z"])
    assert g.grib_get_long("level") == [500] * 2
    assert g.grib_get_string("shortName") == ["z"] * 2
    assert f.grib_get_long("level") == [1000] * 2
    assert f.grib_get_string("shortName") == ["t", "u"]

    g = f.grib_set(["level:d", 500])
    np.testing.assert_allclose(
        np.array(g.grib_get_double("level")), np.array([500] * 2)
    )
    np.testing.assert_allclose(
        np.array(f.grib_get_double("level")), np.array([1000] * 2)
    )

    g = f.grib_set_double(["longitudeOfFirstGridPointInDegrees", 95.6])
    np.testing.assert_allclose(
        np.array(g.grib_get_double("longitudeOfFirstGridPointInDegrees")),
        np.array([95.6] * 2),
    )
    np.testing.assert_allclose(
        np.array(f.grib_get_double("longitudeOfFirstGridPointInDegrees")), [0, 0]
    )


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


def test_write_modified_fieldset_binop():
    f = mv.Fieldset(path=os.path.join(PATH, "tuv_pl.grib"))
    fp20 = f + 20
    temp_path = "written_tuv_pl.grib"
    fp20.write(temp_path)
    assert os.path.isfile(temp_path)
    g = mv.Fieldset(path=temp_path)
    assert type(g) == mv.Fieldset
    assert len(g) == 18
    sn = g.grib_get_string("shortName")
    assert sn == ["t", "u", "v"] * 6
    np.testing.assert_allclose(g.values(), f.values() + 20)
    f = 0
    os.remove(temp_path)


def test_write_modified_fieldset_unop():
    f = mv.Fieldset(path=os.path.join(PATH, "tuv_pl.grib"))
    negf = -f
    temp_path = "written_tuv_pl_unop.grib"
    negf.write(temp_path)
    assert os.path.isfile(temp_path)
    g = mv.Fieldset(path=temp_path)
    assert type(g) == mv.Fieldset
    assert len(g) == 18
    sn = g.grib_get_string("shortName")
    assert sn == ["t", "u", "v"] * 6
    np.testing.assert_allclose(g.values(), -f.values(), 0.0001)
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
    np.testing.assert_allclose(vg, vf * vf, 0.0001)


def test_field_func_neg():
    f = mv.Fieldset(path=os.path.join(PATH, "tuv_pl.grib"))
    g = -f
    assert type(g) == mv.Fieldset
    assert len(g) == 18
    vf = f.values()
    vg = g.values()
    np.testing.assert_allclose(vg, -vf)


def test_field_func_pos():
    f = mv.Fieldset(path=os.path.join(PATH, "tuv_pl.grib"))
    g = +f  # should return values unaltered
    assert type(g) == mv.Fieldset
    assert len(g) == 18
    vf = f.values()
    vg = g.values()
    np.testing.assert_allclose(vg, vf)


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
    m = f * 1.5
    np.testing.assert_allclose(m.values(), f.values() * 1.5)
    d = f / 3.0
    np.testing.assert_allclose(d.values(), f.values() / 3.0, 0.0001)
    p = f**2
    np.testing.assert_allclose(p.values(), f.values() ** 2)
    first_val = f.values()[0][0]  # 272
    ge = f >= first_val
    v = ge.values()
    assert v[0][0] == 1  # 272
    assert v[0][2645] == 0  # 240
    assert v[0][148] == 1  # 280
    assert v[1][0] == 0  # -6
    gt = f > first_val
    v = gt.values()
    assert v[0][0] == 0  # 272
    assert v[0][2645] == 0  # 240
    assert v[0][148] == 1  # 280
    assert v[1][0] == 0  # - 6
    lt = f < first_val
    v = lt.values()
    assert v[0][0] == 0  # 272
    assert v[0][2645] == 1  # 240
    assert v[0][148] == 0  # 280
    assert v[1][0] == 1  # - 6
    lt = f <= first_val
    v = lt.values()
    assert v[0][0] == 1  # 272
    assert v[0][2645] == 1  # 240
    assert v[0][148] == 0  # 280
    assert v[1][0] == 1  # - 6
    e = f == first_val
    v = e.values()
    assert v[0][0] == 1  # 272
    assert v[0][2645] == 0  # 240
    assert v[0][148] == 0  # 280
    assert v[1][0] == 0  # - 6
    ne = f != first_val
    v = ne.values()
    assert v[0][0] == 0  # 272
    assert v[0][2645] == 1  # 240
    assert v[0][148] == 1  # 280
    assert v[1][0] == 1  # - 6
    andd = (f > 270) & (f < 290)  # and
    v = andd.values()
    assert v[0][0] == 1  # 272
    assert v[0][2645] == 0  # 240
    assert v[0][148] == 1  # 280
    assert v[1][0] == 0  # - 6
    orr = (f < 270) | (f > 279)  # or
    v = orr.values()
    assert v[0][0] == 0  # 272
    assert v[0][2645] == 1  # 240
    assert v[0][148] == 1  # 280
    assert v[1][0] == 1  # - 6
    nott = ~((f > 270) & (f < 290))  # not
    v = nott.values()
    assert v[0][0] == 0  # 272
    assert v[0][2645] == 1  # 240
    assert v[0][148] == 0  # 280
    assert v[1][0] == 1  # - 6
    # scalar op fieldset
    h = 20 + f
    assert type(h) == mv.Fieldset
    assert len(h) == 3
    np.testing.assert_allclose(h.values(), f.values() + 20)
    r = 25 - f
    np.testing.assert_allclose(r.values(), 25 - f.values())
    mr = 3 * f
    np.testing.assert_allclose(mr.values(), f.values() * 3)
    dr = 200 / f
    np.testing.assert_allclose(dr.values(), 200 / f.values(), 0.0001)
    pr = 2**f
    np.testing.assert_allclose(pr.values(), 2 ** f.values(), 1)


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
    t = g * f
    np.testing.assert_allclose(t.values(), g.values() * f.values(), 0.0001)
    d = g / f
    np.testing.assert_allclose(d.values(), g.values() / f.values(), 0.0001)
    gt = f > g
    assert gt[0].values()[0] == 1
    assert gt[1].values()[0] == 0
    assert gt[2].values()[0] == 1
    assert gt[2].values()[22] == 0
    gt = f >= g
    assert gt[0].values()[0] == 1
    assert gt[1].values()[0] == 0
    assert gt[2].values()[0] == 1
    assert gt[2].values()[22] == 0
    lt = f < g
    assert lt[0].values()[0] == 0
    assert lt[1].values()[0] == 1
    assert lt[2].values()[0] == 0
    assert lt[2].values()[22] == 1
    lt = f <= g
    assert lt[0].values()[0] == 0
    assert lt[1].values()[0] == 1
    assert lt[2].values()[0] == 0
    assert lt[2].values()[22] == 1


def test_fieldset_multiple_funcs():
    f = mv.Fieldset(path=os.path.join(PATH, "tuv_pl.grib"))
    g = 1 - ((f[0] + f[3]) - 5)
    np.testing.assert_allclose(g.values(), 1 - ((f[0].values() + f[3].values()) - 5))


def test_fieldset_funs_with_read():
    f = mv.read(os.path.join(PATH, "tuv_pl.grib"))
    assert isinstance(f, mv.Fieldset)
    g = f + 18
    assert isinstance(g, mv.Fieldset)
    diff = g - f
    assert isinstance(diff, mv.Fieldset)
    assert np.isclose(diff.minvalue(), 18)
    assert np.isclose(diff.maxvalue(), 18)


def test_field_maths_funcs():
    f = mv.Fieldset(path=os.path.join(PATH, "tuv_pl.grib"))
    f = f[0]
    v = f.values()

    # no arg
    r = f.abs()
    np.testing.assert_allclose(r.values(), np.fabs(v), rtol=1e-05)

    r = f.cos()
    np.testing.assert_allclose(r.values(), np.cos(v), rtol=1e-05)

    f1 = f / 100
    r = f1.exp()
    np.testing.assert_allclose(r.values(), np.exp(f1.values()), rtol=1e-05)

    r = f.log()
    np.testing.assert_allclose(r.values(), np.log(v), rtol=1e-05)

    r = f.log10()
    np.testing.assert_allclose(r.values(), np.log10(v), rtol=1e-05)

    r = f.sgn()
    np.testing.assert_allclose(r.values(), np.sign(v), rtol=1e-05)

    r = f.sin()
    np.testing.assert_allclose(r.values(), np.sin(v), rtol=1e-05)

    r = f.sqrt()
    np.testing.assert_allclose(r.values(), np.sqrt(v), rtol=1e-05)

    r = f.tan()
    np.testing.assert_allclose(r.values(), np.tan(v), rtol=1e-04)

    # inverse functions
    # scale input between [-1, 1]
    f1 = (f - 282) / 80
    v1 = f1.values()
    r = f1.acos()
    np.testing.assert_allclose(r.values(), np.arccos(v1), rtol=1e-05)

    r = f1.asin()
    np.testing.assert_allclose(r.values(), np.arcsin(v1), rtol=1e-05)

    r = f1.atan()
    np.testing.assert_allclose(r.values(), np.arctan(v1), rtol=1e-05)

    # 1 arg
    f1 = f - 274
    v1 = f1.values()

    r = f.atan2(f1)
    np.testing.assert_allclose(r.values(), np.arctan2(v, v1), rtol=1e-05)

    r = f.div(f1)
    np.testing.assert_allclose(r.values(), np.floor_divide(v, v1), rtol=1e-05)

    r = f.mod(f1)
    np.testing.assert_allclose(r.values(), np.mod(v, v1), rtol=1e-04)


def test_str():
    f = mv.Fieldset(path=os.path.join(PATH, "tuv_pl.grib"))
    assert str(f) == "Fieldset (18 fields)"


def test_set_values_single_field():
    f = mv.Fieldset(path=os.path.join(PATH, "tuv_pl.grib"))
    f0 = f[0]
    f0_vals = f0.values()
    vals_plus_10 = f0_vals + 10
    f0_modified = f0.set_values(vals_plus_10)
    f0_mod_vals = f0_modified.values()
    np.testing.assert_allclose(f0_mod_vals, vals_plus_10)
    # write to disk, read and check again
    testpath = "f0_modified.grib"
    f0_modified.write(testpath)
    f0_read = mv.Fieldset(path=testpath)
    np.testing.assert_allclose(f0_read.values(), vals_plus_10)
    os.remove(testpath)


def test_set_values_multiple_fields():
    f = mv.Fieldset(path=os.path.join(PATH, "tuv_pl.grib"))
    f03 = f[0:3]
    f47 = f[4:7]
    f03_modified = f03.set_values(f47.values())
    np.testing.assert_allclose(f03_modified.values(), f47.values())
    # same, but with a list of arrays instead of a 2D array
    list_of_arrays = [f.values() for f in f47]
    f03_modified_2 = f03.set_values(list_of_arrays)
    np.testing.assert_allclose(f03_modified_2.values(), f47.values())
    # wrong number of arrays
    f48 = f[4:8]
    with pytest.raises(ValueError):
        f03_modified_3 = f03.set_values(f48.values())


def test_set_values_with_missing_values():
    f = mv.Fieldset(path=os.path.join(PATH, "t_with_missing.grib"))
    new_vals = f.values() + 40
    g = f.set_values(new_vals)
    v = g.values()
    assert v.shape == (2664,)
    eps = 0.001
    assert np.isclose(v[0], 272.5642 + 40, eps)
    assert np.isnan(v[798])
    assert np.isnan(v[806])
    assert np.isnan(v[1447])
    assert np.isclose(v[2663], 240.5642 + 40, eps)


def test_set_values_with_missing_values_2():
    f = mv.Fieldset(path=os.path.join(PATH, "t_with_missing.grib"))
    g = f[0]
    v = g.values()
    v[1] = np.nan
    h = g.set_values(v)
    hv = h.values()[:10]
    assert np.isclose(hv[0], 272.56417847)
    assert np.isnan(hv[1])
    assert np.isclose(hv[2], 272.56417847)


def test_set_values_resize():
    # NOTE: the current change in behavour - in 'standard Metview' the user
    # has to supply "resize" as an optional argument in order to allow an array
    # of different size to be used; if not supplied, and the given array is not the
    # same size as the original field, an error is thrown; here, we allow resizing
    # without the need for an extra argument - do we want to do this check?
    f = mv.Fieldset(path=os.path.join(PATH, "tuv_pl.grib"))
    f0 = f[0]
    f0_20vals = f0.values()[0:20]
    f0_modified = f0.set_values(f0_20vals)
    f0_mod_vals = f0_modified.values()
    eps = 0.001
    np.testing.assert_allclose(f0_mod_vals, f0_20vals, eps)


def test_vals_destroyed():
    f = mv.Fieldset(path=os.path.join(PATH, "test.grib"))
    assert f.fields[0].vals is None
    g = f.values()
    assert isinstance(g, np.ndarray)
    assert f.fields[0].vals is None
    f = -f
    assert f.fields[0].vals is None
    g = f.values()
    assert isinstance(g, np.ndarray)
    assert f.fields[0].vals is None
    f = f + 1
    assert f.fields[0].vals is None
    g = f.values()
    assert isinstance(g, np.ndarray)
    assert f.fields[0].vals is None


def test_accumulate():
    f = mv.Fieldset(path=os.path.join(PATH, "t1000_LL_7x7.grb"))
    v = mv.accumulate(f)
    assert isinstance(v, float)
    assert np.isclose(v, 393334.244141)

    f = mv.Fieldset(path=os.path.join(PATH, "monthly_avg.grib"))
    v = mv.accumulate(f)
    assert isinstance(v, list)
    v_ref = [
        408058.256226,
        413695.059631,
        430591.282776,
        428943.981812,
        422329.622498,
        418016.024231,
        409755.097961,
        402741.786194,
    ]
    assert len(v) == len(f)
    np.testing.assert_allclose(v, v_ref)


def test_average():
    fs = mv.Fieldset(path=os.path.join(PATH, "test.grib"))

    # const fields
    v = mv.average(fs * 0 + 1)
    assert isinstance(v, float)
    assert np.isclose(v, 1)

    # # single field
    v = mv.average(fs)
    assert isinstance(v, float)
    assert np.isclose(v, 279.06647863)

    # multiple fields
    f = mv.Fieldset(path=os.path.join(PATH, "monthly_avg.grib"))
    v = mv.average(f)
    assert isinstance(v, list)
    v_ref = [
        290.639783636,
        294.654600877,
        306.688947846,
        305.515656561,
        300.804574428,
        297.732210991,
        291.848360371,
        286.85312407,
    ]

    assert len(v) == len(f)
    np.testing.assert_allclose(v, v_ref)


def test_latitudes():
    fs = mv.Fieldset(path=os.path.join(PATH, "t1000_LL_2x2.grb"))

    v = mv.latitudes(fs)
    assert isinstance(v, np.ndarray)
    assert len(v) == 16380
    assert np.isclose(v[0], 90)
    assert np.isclose(v[1], 90)
    assert np.isclose(v[8103], 0)
    assert np.isclose(v[11335], -34)
    assert np.isclose(v[16379], -90)

    f = fs.merge(fs)
    lst = mv.latitudes(f)
    assert len(lst) == 2
    for v in lst:
        assert np.isclose(v[0], 90)
        assert np.isclose(v[1], 90)
        assert np.isclose(v[8103], 0)
        assert np.isclose(v[11335], -34)
        assert np.isclose(v[16379], -90)


def test_longitudes():
    fs = mv.Fieldset(path=os.path.join(PATH, "t1000_LL_2x2.grb"))

    v = mv.longitudes(fs)
    assert isinstance(v, np.ndarray)
    assert len(v) == 16380
    assert np.isclose(v[0], 0)
    assert np.isclose(v[1], 2)
    assert np.isclose(v[8103], 6)
    assert np.isclose(v[11335], 350)
    assert np.isclose(v[16379], 358)

    f = fs.merge(fs)
    lst = mv.longitudes(f)
    assert len(lst) == 2
    for v in lst:
        assert np.isclose(v[0], 0)
        assert np.isclose(v[1], 2)
        assert np.isclose(v[8103], 6)
        assert np.isclose(v[11335], 350)
        assert np.isclose(v[16379], 358)


def test_coslat():
    fs = mv.Fieldset(path=os.path.join(PATH, "t_time_series.grib"))

    # WARN: it is important that the data should be at least 16 bit
    #  to keep accuracy in resulting fields

    f = fs[0]
    r = mv.coslat(f)
    np.testing.assert_allclose(
        r.values(), np.cos(np.deg2rad(f.latitudes())), rtol=1e-06
    )

    f = fs[:2]
    r = mv.coslat(f)
    assert len(r) == 2
    for i in range(len(r)):
        np.testing.assert_allclose(
            r[i].values(), np.cos(np.deg2rad(f[i].latitudes())), rtol=1e-06
        )


def test_mean():
    fs = mv.Fieldset(path=os.path.join(PATH, "test.grib"))

    # single fields
    f = fs
    r = mv.mean(f)
    v_ref = mv.values(fs)
    assert len(r) == 1
    np.testing.assert_allclose(r.values(), v_ref, rtol=1e-05)

    # known mean
    f = fs.merge(2 * fs)
    f = f.merge(3 * fs)
    r = f.mean()
    v_ref = mv.values(fs) * 2
    assert len(r) == 1
    np.testing.assert_allclose(r.values(), v_ref, rtol=1e-05)


def test_maxvalue():
    fs = mv.Fieldset(path=os.path.join(PATH, "test.grib"))

    f = fs
    f = f.merge(3 * fs)
    f = f.merge(2 * fs)
    v = mv.maxvalue(f)
    assert isinstance(v, float)
    assert np.isclose(v, 948.1818237304688)


def test_minvalue():
    fs = mv.Fieldset(path=os.path.join(PATH, "test.grib"))

    f = 3 * fs
    f = f.merge(fs)
    f = f.merge(2 * fs)
    v = mv.minvalue(f)
    assert isinstance(v, float)
    assert np.isclose(v, 206.93560791015625)


def test_sinlat():
    fs = mv.Fieldset(path=os.path.join(PATH, "t_time_series.grib"))

    # WARN: it is important that the data should be at least 16 bit
    #  to keep accuracy in resulting fields

    f = fs[0]
    r = mv.sinlat(f)
    np.testing.assert_allclose(
        r.values(), np.sin(np.deg2rad(f.latitudes())), rtol=1e-06
    )

    f = fs[:2]
    r = mv.sinlat(f)
    assert len(r) == 2
    for i in range(len(r)):
        np.testing.assert_allclose(
            r[i].values(), np.sin(np.deg2rad(f[i].latitudes())), rtol=1e-06
        )


def test_tanlat():
    fs = mv.Fieldset(path=os.path.join(PATH, "t_time_series.grib"))

    # WARN: it is important that the data should be at least 16 bit
    #  to keep accuracy in resulting fields

    # TODO: use pole_limit value from fieldset

    pole_limit = 90.0 - 1e-06

    f = fs[0]
    r = mv.tanlat(f)
    lat = f.latitudes()
    lat[np.fabs(lat) > pole_limit] = np.nan
    np.testing.assert_allclose(
        r.values(), np.tan(np.deg2rad(lat)), rtol=1e-06, atol=1e-06
    )

    f = fs[:2]
    r = mv.tanlat(f)
    assert len(r) == 2
    for i in range(len(r)):
        lat = f[i].latitudes()
        lat[np.fabs(lat) > pole_limit] = np.nan
        np.testing.assert_allclose(
            r[i].values(), np.tan(np.deg2rad(lat)), rtol=1e-06, atol=1e-06
        )


def test_stdev():
    fs = mv.Fieldset(path=os.path.join(PATH, "t1000_LL_7x7.grb"))

    # single field
    r = mv.stdev(fs)
    assert len(r) == 1
    np.testing.assert_allclose(r.values(), fs.values() * 0)

    # known variance
    f = fs.merge(4 * fs)
    f = f.merge(10 * fs)
    r = mv.stdev(f)
    assert len(r) == 1
    np.testing.assert_allclose(r.values(), np.sqrt(np.square(fs.values()) * 42 / 3))

    # real life example
    fs = mv.Fieldset(path=os.path.join(PATH, "monthly_avg.grib"))
    r = mv.stdev(fs)
    assert len(r) == 1

    v_ref = np.ma.std(np.array([x.values() for x in fs]), axis=0)
    np.testing.assert_allclose(r.values(), v_ref, rtol=1e-03)


def test_sum():
    fs = mv.Fieldset(path=os.path.join(PATH, "t1000_LL_7x7.grb"))

    # single fields
    f = fs
    r = mv.sum(f)
    assert len(r) == 1
    np.testing.assert_allclose(r.values(), fs.values())

    # known sum
    f = fs.merge(fs)
    f = f.merge(fs)
    r = f.sum()
    assert len(r) == 1
    np.testing.assert_allclose(r.values(), fs.values() * 3)

    # real life example
    f = mv.Fieldset(path=os.path.join(PATH, "monthly_avg.grib"))
    r = f.sum()
    assert len(r) == 1
    v_ref = r.values() * 0
    for g in f:
        v_ref += g.values()
    np.testing.assert_allclose(r.values(), v_ref)


def test_var():
    fs = mv.Fieldset(path=os.path.join(PATH, "t1000_LL_7x7.grb"))

    # single field
    r = mv.var(fs)
    assert len(r) == 1
    np.testing.assert_allclose(r.values(), fs.values() * 0)

    # known variance
    f = fs.merge(4 * fs)
    f = f.merge(10 * fs)
    r = mv.var(f)
    assert len(r) == 1
    np.testing.assert_allclose(r.values(), np.square(fs.values()) * 42 / 3)

    # real life example
    fs = mv.Fieldset(path=os.path.join(PATH, "monthly_avg.grib"))
    r = mv.var(fs)
    assert len(r) == 1

    v_ref = np.ma.var(np.array([x.values() for x in fs]), axis=0)
    np.testing.assert_allclose(r.values(), v_ref, rtol=1e-03)


def test_date():

    fs = mv.Fieldset(path=os.path.join(PATH, "monthly_avg.grib"))

    # analysis, so valid=base
    bdate_ref = [
        "2016-01-01 00:00:00",
        "2016-02-01 00:00:00",
        "2016-03-01 00:00:00",
        "2016-04-01 00:00:00",
        "2016-05-01 00:00:00",
        "2016-06-01 00:00:00",
        "2016-07-01 00:00:00",
        "2016-08-01 00:00:00",
    ]
    vdate_ref = bdate_ref

    v = mv.base_date(fs)
    assert len(v) == len(fs)
    for i, d in enumerate(v):
        assert d == utils.date_from_str(bdate_ref[i])

    v = mv.valid_date(fs)
    assert len(v) == len(fs)
    for i, d in enumerate(v):
        assert d == utils.date_from_str(vdate_ref[i])


def test_bitmap():
    fs = mv.Fieldset(path=os.path.join(PATH, "t1000_LL_2x2.grb"))

    # -- const field
    f = fs * 0 + 1

    # non missing
    r = mv.bitmap(f, 0)
    np.testing.assert_allclose(r.values(), f.values())

    # all missing
    r = mv.bitmap(f, 1)
    np.testing.assert_allclose(r.values(), f.values() * np.nan)

    # -- non const field
    f = fs

    # bitmap with value
    f_mask = f > 300
    r = mv.bitmap(f_mask, 1)
    v_ref = f_mask.values()
    v_ref[v_ref == 1] = np.nan
    np.testing.assert_allclose(r.values(), v_ref)

    f_mask = f > 300
    r = mv.bitmap(f_mask * 2, 2)
    v_ref = f_mask.values() * 2
    v_ref[v_ref == 2] = np.nan
    np.testing.assert_allclose(r.values(), v_ref)

    # bitmap with field
    f = mv.bitmap(fs > 300, 0)
    r = mv.bitmap(fs, f)
    v_ref = fs.values() * f.values()
    np.testing.assert_allclose(r.values(), v_ref)

    # multiple fields
    f = mv.Fieldset(path=os.path.join(PATH, "monthly_avg.grib"))
    f = f[0:2]

    # with value
    f_mask = f > 300
    r = mv.bitmap(f_mask, 1)
    assert len(r) == len(f)
    for i in range(len(r)):
        v_ref = f_mask[i].values()
        v_ref[v_ref == 1] = np.nan
        np.testing.assert_allclose(r[i].values(), v_ref)

    # with field
    f1 = mv.bitmap(f > 300, 0)
    r = mv.bitmap(f, f1)
    assert len(r) == len(f1)
    for i in range(len(r)):
        v_ref = f[i].values() * f1[i].values()
        np.testing.assert_allclose(r[i].values(), v_ref)

    # with single field
    f1 = mv.bitmap(f[0] > 300, 0)
    r = mv.bitmap(f, f1)
    assert len(r) == len(f)
    for i in range(len(r)):
        v_ref = f[i].values() * f1.values()
        np.testing.assert_allclose(r[i].values(), v_ref)


def test_nobitmap():

    fs = mv.Fieldset(path=os.path.join(PATH, "t_with_missing.grib"))

    # single field
    f = fs
    r = mv.nobitmap(f, 1)
    assert len(r) == 1
    v_ref = f.values()
    v_ref[np.isnan(v_ref)] = 1
    np.testing.assert_allclose(r.values(), v_ref)

    # multiple fields
    f = fs.merge(2 * fs)
    r = mv.nobitmap(f, 1)
    assert len(r) == 2

    for i in range(len(r)):
        v_ref = f[i].values()
        v_ref[np.isnan(v_ref)] = 1
        np.testing.assert_allclose(r[i].values(), v_ref)


def test_grib_index_0():
    # empty fieldset
    fs = mv.Fieldset()
    gi = fs.grib_index()
    assert gi == []


def test_grib_index_1():
    # single field
    grib_path = os.path.join(PATH, "test.grib")
    fs = mv.Fieldset(path=grib_path)
    gi = fs.grib_index()
    assert gi == [(grib_path, 0)]


def test_grib_index_2():
    # multiple fields
    grib_path = os.path.join(PATH, "tuv_pl.grib")
    fs = mv.Fieldset(path=grib_path)
    gi = fs.grib_index()
    assert isinstance(gi, list)
    assert len(gi) == 18
    for f, g in zip(fs, gi):
        assert g == (grib_path, f.grib_get_long("offset"))
    assert gi[5] == (grib_path, 7200)


def test_grib_index_3():
    # merged fields from different files
    gp1 = os.path.join(PATH, "tuv_pl.grib")
    gp2 = os.path.join(PATH, "t_time_series.grib")
    fs1 = mv.Fieldset(path=gp1)
    fs2 = mv.Fieldset(path=gp2)
    fs3 = fs1[4:7]
    fs3.append(fs2[1])
    fs3.append(fs1[2])
    gi = fs3.grib_index()
    assert isinstance(gi, list)
    assert len(gi) == 5
    # assert gi == [(gp1, 5760), (gp1, 7200), (gp1, 8640), (gp2, 5520), (gp1, 2880)]
    assert gi == [(gp1, 5760), (gp1, 7200), (gp1, 8640), (gp2, 5436), (gp1, 2880)]


def test_grib_index_4():
    # test with a derived fieldset
    fs = mv.Fieldset(os.path.join(PATH, "t_time_series.grib"))[0:4]
    fs1 = fs + 1
    gi = fs1.grib_index()
    for i in gi:
        assert is_temp_file(i[0])
    offsets = [i[1] for i in gi]
    assert offsets == [0, 8440, 16880, 25320]


def test_grib_index_5():
    # test with grib written with write() function
    f_orig = mv.Fieldset(path=os.path.join(PATH, "tuv_pl.grib"))
    f = (f_orig[0:4]).merge(f_orig[7])
    p = "written_tuv_pl.grib"
    f.write(p)
    gi = f.grib_index()
    assert gi == [(p, 0), (p, 1440), (p, 2880), (p, 4320), (p, 5760)]
    f = 0
    os.remove(p)
