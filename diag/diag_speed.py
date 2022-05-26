# (C) Copyright 2017- ECMWF.
#
# This software is licensed under the terms of the Apache Licence Version 2.0
# which can be obtained at http://www.apache.org/licenses/LICENSE-2.0.
#
# In applying this licence, ECMWF does not waive the privileges and immunities
# granted to it by virtue of its status as an intergovernmental organisation
# nor does it submit to any jurisdiction.
#

import numpy as np
import metview as mv

import diag_util as diag

# -----------------------------------
# Tests for execution speed
# To run it use:
# pytest diag_speed.py --benchmark-autosave  --benchmark-max-time=5 --benchmark-min-rounds=1 --benchmark-sort=name
# ------------------------------------


def test_absolute_vorticity(benchmark):
    def _target(t):
        g = mv.absolute_vorticity(t)
        return len(g)

    t = diag.get_data(diag.TEST_FILE_2)
    r = benchmark(_target, t)
    assert r == 20


def test_accumulate(benchmark):
    def _target(t):
        g = mv.accumulate(t)
        return len(g)

    t = diag.get_data(diag.TEST_FILE_2)
    r = benchmark(_target, t)
    assert r == 20


def test_add_op_1(benchmark):
    def _target(t):
        g = t + 1
        return len(g)

    t = diag.get_data(diag.TEST_FILE_2)
    r = benchmark(_target, t)
    assert r == 20


def test_add_op_2(benchmark):
    def _target(t):
        g = t + t
        return len(g)

    t = diag.get_data(diag.TEST_FILE_2)
    r = benchmark(_target, t)
    assert r == 20


def test_add_op_3(benchmark):
    def _target(u, v):
        g = u + v
        return len(g)

    u = diag.get_data(diag.TEST_FILE_5)
    v = diag.get_data(diag.TEST_FILE_6)
    r = benchmark(_target, u, v)
    assert r == 20


def test_average(benchmark):
    def _target(t):
        g = mv.average(t)
        return len(g)

    t = diag.get_data(diag.TEST_FILE_2)
    r = benchmark(_target, t)
    assert r == 20


def test_average_ew(benchmark):
    def _target(t):
        g = mv.average_ew(t, [60, -180, -60, 180], 2)
        return len(g)

    t = diag.get_data(diag.TEST_FILE_2)
    r = benchmark(_target, t)
    assert r > 1


def test_bearing(benchmark):
    def _target(t):
        g = mv.bearing(t, [45, 20])
        return len(g)

    t = diag.get_data(diag.TEST_FILE_2)
    r = benchmark(_target, t)
    assert r == 20


def test_bitmap(benchmark):
    def _target(t):
        g = mv.bitmap(t, 273)
        return len(g)

    t = diag.get_data(diag.TEST_FILE_2)
    r = benchmark(_target, t)
    assert r == 20


def test_cos(benchmark):
    def _target(t):
        g = mv.cos(t)
        return len(g)

    t = diag.get_data(diag.TEST_FILE_2)
    r = benchmark(_target, t)
    assert r == 20


def test_coslat(benchmark):
    def _target(t):
        g = mv.coslat(t)
        return len(g)

    t = diag.get_data(diag.TEST_FILE_2)
    r = benchmark(_target, t)
    assert r == 20


def test_corr_a(benchmark):
    def _target(u, v):
        g = mv.corr_a(u, v, [50, -100, -80, 140])
        return len(g)

    u = diag.get_data(diag.TEST_FILE_5)
    v = diag.get_data(diag.TEST_FILE_6)
    r = benchmark(_target, u, v)
    assert r == 20


def test_covar(benchmark):
    def _target(u, v):
        g = mv.covar(u, v)
        return len(g)

    u = diag.get_data(diag.TEST_FILE_5)
    v = diag.get_data(diag.TEST_FILE_6)
    r = benchmark(_target, u, v)
    assert r == 1


def test_covar_a(benchmark):
    def _target(u, v):
        g = mv.covar_a(u, v, [50, -100, -80, 140])
        return len(g)

    u = diag.get_data(diag.TEST_FILE_5)
    v = diag.get_data(diag.TEST_FILE_6)
    r = benchmark(_target, u, v)
    assert r == 20


def test_direction(benchmark):
    def _target(u, v):
        g = mv.direction(u, v)
        return len(g)

    u = diag.get_data(diag.TEST_FILE_5)
    v = diag.get_data(diag.TEST_FILE_6)
    r = benchmark(_target, u, v)
    assert r == 20


def test_divergence(benchmark):
    def _target(u, v):
        g = mv.divergence(u, v)
        return len(g)

    u = diag.get_data(diag.TEST_FILE_5)[:10]
    v = diag.get_data(diag.TEST_FILE_6)[:10]
    r = benchmark(_target, u, v)
    assert r == 10


def test_filter_op(benchmark):
    def _target(t):
        g = t > 273.16
        return len(g)

    t = diag.get_data(diag.TEST_FILE_2)
    r = benchmark(_target, t)
    assert r == 20


def test_first_derivative_x(benchmark):
    def _target(t):
        g = mv.first_derivative_x(t)
        return len(g)

    t = diag.get_data(diag.TEST_FILE_2)
    r = benchmark(_target, t)
    assert r == 20


def test_first_derivative_y(benchmark):
    def _target(t):
        g = mv.first_derivative_y(t)
        return len(g)

    t = diag.get_data(diag.TEST_FILE_2)
    r = benchmark(_target, t)
    assert r == 20


def test_frequencies(benchmark):
    def _target(t):
        g = mv.frequencies(t, list(range(220, 320, 10)))
        return len(g)

    t = diag.get_data(diag.TEST_FILE_2)
    r = benchmark(_target, t)
    assert r > 0


def test_gradient(benchmark):
    def _target(t):
        g = mv.gradient(t)
        return len(g)

    t = diag.get_data(diag.TEST_FILE_2)
    r = benchmark(_target, t)
    assert r == 40


def test_grib_get(benchmark):
    def _target(t):
        g = mv.grib_get(t, ["paramId", "shortName"])
        return len(g)

    t = diag.get_data(diag.TEST_FILE_2)
    r = benchmark(_target, t)
    assert r == 20


def test_grib_get_long(benchmark):
    def _target(t):
        g = mv.grib_get_long(t, "paramId")
        return len(g)

    t = diag.get_data(diag.TEST_FILE_2)
    r = benchmark(_target, t)
    assert r == 20


def test_grib_get_string(benchmark):
    def _target(t):
        g = mv.grib_get_string(t, "shortName")
        return len(g)

    t = diag.get_data(diag.TEST_FILE_2)
    r = benchmark(_target, t)
    assert r == 20


def test_grib_set(benchmark):
    def _target(t):
        g = mv.grib_set(t, ["shortName", "z", "paramId", 129])
        return len(g)

    t = diag.get_data(diag.TEST_FILE_2)
    r = benchmark(_target, t)
    assert r == 20


def test_grib_set_long(benchmark):
    def _target(t):
        g = mv.grib_set_long(t, ["paramId", 129])
        return len(g)

    t = diag.get_data(diag.TEST_FILE_2)
    r = benchmark(_target, t)
    assert r == 20


def test_grib_set_string(benchmark):
    def _target(t):
        g = mv.grib_set_string(t, ["shortName", "z"])
        return len(g)

    t = diag.get_data(diag.TEST_FILE_2)
    r = benchmark(_target, t)
    assert r == 20


def test_grid_cell_area(benchmark):
    def _target(t):
        g = mv.grid_cell_area(t)
        return len(g)

    t = diag.get_data(diag.TEST_FILE_2)
    r = benchmark(_target, t)
    assert r == 20


def test_integral(benchmark):
    def _target(t):
        g = mv.integral(t)
        return len(g)

    t = diag.get_data(diag.TEST_FILE_2)
    r = benchmark(_target, t)
    assert r == 20


def test_integrate(benchmark):
    def _target(t):
        g = mv.integrate(t)
        return len(g)

    t = diag.get_data(diag.TEST_FILE_2)
    r = benchmark(_target, t)
    assert r == 20


def test_laplacian(benchmark):
    def _target(t):
        g = mv.laplacian(t)
        return len(g)

    t = diag.get_data(diag.TEST_FILE_2)[:10]
    r = benchmark(_target, t)
    assert r == 10


def test_mask(benchmark):
    def _target(t):
        g = mv.mask(t, [60, -30, 22, 45])
        return len(g)

    t = diag.get_data(diag.TEST_FILE_2)
    r = benchmark(_target, t)
    assert r == 20


def test_max(benchmark):
    def _target(t):
        g = mv.max(t)
        return len(g)

    t = diag.get_data(diag.TEST_FILE_2)
    r = benchmark(_target, t)
    assert r == 1


def test_maxvalue(benchmark):
    def _target(t):
        g = mv.maxvalue(t)
        return g

    t = diag.get_data(diag.TEST_FILE_2)
    r = benchmark(_target, t)
    assert r is not None


def test_mean(benchmark):
    def _target(t):
        g = mv.mean(t)
        return len(g)

    t = diag.get_data(diag.TEST_FILE_2)
    r = benchmark(_target, t)
    assert r == 1


def test_mean_ew(benchmark):
    def _target(t):
        g = mv.mean_ew(t)
        return len(g)

    t = diag.get_data(diag.TEST_FILE_2)
    r = benchmark(_target, t)
    assert r == 20


def test_min(benchmark):
    def _target(t):
        g = mv.min(t)
        return len(g)

    t = diag.get_data(diag.TEST_FILE_2)
    r = benchmark(_target, t)
    assert r == 1


def test_minvalue(benchmark):
    def _target(t):
        g = mv.minvalue(t)
        return g

    t = diag.get_data(diag.TEST_FILE_2)
    r = benchmark(_target, t)
    assert r is not None


def test_poly_mask(benchmark):
    def _target(t, lat, lon):
        g = mv.poly_mask(t, lat, lon)
        return len(g)

    t = diag.get_data(diag.TEST_FILE_2)
    lon = np.array([-42, -24, 20, 27, -7, -17])
    lat = np.array([28, 60, 51, 24, 5, 30])
    r = benchmark(_target, t, lat, lon)
    assert r == 20


def test_rmask(benchmark):
    def _target(t):
        g = mv.rmask(t, 60, -30, 1500 * 1000)
        return len(g)

    t = diag.get_data(diag.TEST_FILE_2)
    r = benchmark(_target, t)
    assert r == 20


def test_rms(benchmark):
    def _target(t):
        g = mv.rms(t)
        return len(g)

    t = diag.get_data(diag.TEST_FILE_2)
    r = benchmark(_target, t)
    assert r == 1


def test_second_derivative_x(benchmark):
    def _target(t):
        g = mv.second_derivative_x(t)
        return len(g)

    t = diag.get_data(diag.TEST_FILE_2)
    r = benchmark(_target, t)
    assert r == 20


def test_second_derivative_y(benchmark):
    def _target(t):
        g = mv.second_derivative_y(t)
        return len(g)

    t = diag.get_data(diag.TEST_FILE_2)
    r = benchmark(_target, t)
    assert r == 20


def test_shear_deformation(benchmark):
    def _target(u, v):
        g = mv.shear_deformation(u, v)
        return len(g)

    u = diag.get_data(diag.TEST_FILE_5)[:10]
    v = diag.get_data(diag.TEST_FILE_6)[:10]
    r = benchmark(_target, u, v)
    assert r == 10


def test_sin(benchmark):
    def _target(t):
        g = mv.sin(t)
        return len(g)

    t = diag.get_data(diag.TEST_FILE_2)
    r = benchmark(_target, t)
    assert r == 20


def test_sinlat(benchmark):
    def _target(t):
        g = mv.sinlat(t)
        return len(g)

    t = diag.get_data(diag.TEST_FILE_2)
    r = benchmark(_target, t)
    assert r == 20


def test_speed(benchmark):
    def _target(u, v):
        g = mv.speed(u, v)
        return len(g)

    u = diag.get_data(diag.TEST_FILE_5)
    v = diag.get_data(diag.TEST_FILE_6)
    r = benchmark(_target, u, v)
    assert r == 20


def test_stdev(benchmark):
    def _target(t):
        g = mv.stdev(t)
        return len(g)

    t = diag.get_data(diag.TEST_FILE_2)
    r = benchmark(_target, t)
    assert r == 1


def test_stdev_a(benchmark):
    def _target(t):
        g = mv.stdev_a(t, [50, -100, -80, 140])
        return len(g)

    t = diag.get_data(diag.TEST_FILE_2)
    r = benchmark(_target, t)
    assert r == 20


def test_stretch_deformation(benchmark):
    def _target(u, v):
        g = mv.stretch_deformation(u, v)
        return len(g)

    u = diag.get_data(diag.TEST_FILE_5)[:10]
    v = diag.get_data(diag.TEST_FILE_6)[:10]
    r = benchmark(_target, u, v)
    assert r == 10


def test_sum(benchmark):
    def _target(t):
        g = mv.sum(t)
        return len(g)

    t = diag.get_data(diag.TEST_FILE_2)
    r = benchmark(_target, t)
    assert r == 1


def test_tanlat(benchmark):
    def _target(t):
        g = mv.tanlat(t)
        return len(g)

    t = diag.get_data(diag.TEST_FILE_2)
    r = benchmark(_target, t)
    assert r == 20


def test_unipressure(benchmark):
    def _target(lnsp):
        g = mv.unipressure(lnsp)
        return len(g)

    f = diag.get_data(diag.TEST_FILE_1)
    lnsp = mv.read(data=f, param="lnsp")
    r = benchmark(_target, lnsp)
    assert r == 137


def test_unithickness(benchmark):
    def _target(lnsp):
        g = mv.unithickness(lnsp)
        return len(g)

    f = diag.get_data(diag.TEST_FILE_1)
    lnsp = mv.read(data=f, param="lnsp")
    r = benchmark(_target, lnsp)
    assert r == 137


def test_univertint(benchmark):
    def _target(lnsp, t):
        g = mv.univertint(lnsp, t)
        return len(g)

    f = diag.get_data(diag.TEST_FILE_1)
    lnsp = mv.read(data=f, param="lnsp")
    t = mv.read(data=f, param="t")
    r = benchmark(_target, lnsp, t)
    assert r == 1


def test_var(benchmark):
    def _target(t):
        g = mv.var(t)
        return len(g)

    t = diag.get_data(diag.TEST_FILE_2)
    r = benchmark(_target, t)
    assert r == 1


def test_var_a(benchmark):
    def _target(t):
        g = mv.var_a(t, [50, -100, -80, 140])
        return len(g)

    t = diag.get_data(diag.TEST_FILE_2)
    r = benchmark(_target, t)
    assert r == 20


def test_vorticity(benchmark):
    def _target(u, v):
        g = mv.vorticity(u, v)
        return len(g)

    u = diag.get_data(diag.TEST_FILE_5)[:10]
    v = diag.get_data(diag.TEST_FILE_6)[:10]
    r = benchmark(_target, u, v)
    assert r == 10
