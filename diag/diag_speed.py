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
# pytest --benchmark-autosave  --benchmark-max-time=5 --benchmark-min-rounds=1 diag_speed.py
# ------------------------------------


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


# def test_average_ew():
#     t = get_data(TEST_FILE_2)
#     g = mv.average_ew(t, [60, -180, -60, 180], 2)


# def test_bearing(benchmark):
#     def _target(t):
#         g = mv.bearing(t, [45, 20])
#         return len(g)

#     t = diag.get_data(diag.TEST_FILE_2)
#     r = benchmark(_target, t)
#     assert r == 20


# def test_bitmap():
#     t = get_data(TEST_FILE_2)
#     g = mv.bitmap(t, 273)


# def test_coslat():
#     t = get_data(TEST_FILE_2)
#     g = mv.coslat(t)


# def test_corr_a():
#     u = get_data(TEST_FILE_5)
#     v = get_data(TEST_FILE_6)
#     g = mv.corr_a(u, v, [50, -100, -80, 140])


# def test_covar():
#     u = get_data(TEST_FILE_5)
#     v = get_data(TEST_FILE_6)
#     g = mv.covar(u, v)


# def test_covar_a():
#     u = get_data(TEST_FILE_5)
#     v = get_data(TEST_FILE_6)
#     g = mv.covar_a(u, v, [50, -100, -80, 140])


# def test_direction():
#     u = get_data(TEST_FILE_5)
#     v = get_data(TEST_FILE_6)
#     g = mv.direction(u, v)


# def test_divergence():
#     u = get_data(TEST_FILE_5)
#     v = get_data(TEST_FILE_6)
#     g = mv.vorticity(u, v)


# def test_filter_op():
#     t = get_data(TEST_FILE_2)
#     g = t > 273.16


# def test_first_derivative_x():
#     t = get_data(TEST_FILE_1)
#     g = mv.first_derivative_x(t)


# def test_first_derivative_y():
#     t = get_data(TEST_FILE_1)
#     g = mv.first_derivative_y(t)


# def test_frequencies():
#     t = get_data(TEST_FILE_1)
#     g = mv.frequencies(t, list(range(220, 320, 10)))


# def test_gradient():
#     t = get_data(TEST_FILE_2)
#     g = mv.gradient(t)


# def test_grid_cell_area():
#     t = get_data(TEST_FILE_2)
#     g = mv.grid_cell_area(t)


# def test_integral():
#     t = get_data(TEST_FILE_1)
#     g = mv.integral(t)


# def test_integrate():
#     t = get_data(TEST_FILE_1)
#     g = mv.integral(t)


# # def test_laplacian():
# #     t = get_data(TEST_FILE_1)
# #     g = mv.laplacian(t)


# def test_mask():
#     t = get_data(TEST_FILE_2)
#     g = mv.mask(t, [60, -30, 22, 45])


# def test_max():
#     t = get_data(TEST_FILE_2)
#     g = mv.max(t)


# def test_maxvalue():
#     t = get_data(TEST_FILE_2)
#     g = mv.maxvalue(t)


# def test_mean():
#     t = get_data(TEST_FILE_2)
#     g = mv.mean(t)


# def test_mean_ew():
#     t = get_data(TEST_FILE_2)
#     g = mv.mean(t)


# def test_min():
#     t = get_data(TEST_FILE_2)
#     g = mv.min(t)


# def test_minvalue():
#     t = get_data(TEST_FILE_2)
#     g = mv.minvalue(t)


# def test_poly_mask():
#     t = get_data(TEST_FILE_2)
#     lon = np.array([-42, -24, 20, 27, -7, -17])
#     lat = np.array([28, 60, 51, 24, 5, 30])
#     g = mv.poly_mask(t, lat, lon)


# def test_rmask():
#     t = get_data(TEST_FILE_2)
#     g = mv.rmask(t, 60, -30, 1500 * 000)


# def test_rms():
#     t = get_data(TEST_FILE_2)
#     g = mv.rms(t)


# # def test_second_derivative_x():
# #     t = get_data(TEST_FILE_1)
# #     g = mv.second_derivative_x(t)


# # def test_second_derivative_y():
# #     t = get_data(TEST_FILE_1)
# #     g = mv.second_derivative_y(t)


# def test_shear_deformation():
#     u = get_data(TEST_FILE_5)
#     v = get_data(TEST_FILE_6)
#     g = mv.shear_deformation(u, v)


# def test_sin():
#     t = get_data(TEST_FILE_2)
#     g = mv.coslat(t)


# def test_sinlat():
#     t = get_data(TEST_FILE_2)
#     g = mv.sinlat(t)


# def test_speed():
#     u = get_data(TEST_FILE_5)
#     v = get_data(TEST_FILE_6)
#     g = mv.speed(u, v)


# def test_stdev():
#     t = get_data(TEST_FILE_2)
#     g = mv.stdev(t)


# def test_stdev_a():
#     t = get_data(TEST_FILE_2)
#     g = mv.stdev_a(t, [50, -100, -80, 140])


# def test_stretch_deformation():
#     u = get_data(TEST_FILE_5)
#     v = get_data(TEST_FILE_6)
#     g = mv.stretch_deformation(u, v)


# def test_sum():
#     t = get_data(TEST_FILE_2)
#     g = mv.sum(t)


# def test_tanlat():
#     t = get_data(TEST_FILE_2)
#     g = mv.tanlat(t)


# def test_unipressure():
#     f = get_data(TEST_FILE_1)
#     lnsp = mv.read(data=f, param="lnsp")
#     g = mv.unipressure(lnsp)


# def test_unithickness():
#     f = get_data(TEST_FILE_1)
#     lnsp = mv.read(data=f, param="lnsp")
#     g = mv.unithickness(lnsp)


# def test_univertint():
#     f = get_data(TEST_FILE_1)
#     lnsp = mv.read(data=f, param="lnsp")
#     t = mv.read(data=f, param="t")
#     g = mv.univertint(lnsp, t)


# def test_var():
#     t = get_data(TEST_FILE_2)
#     g = mv.var(t)


# def test_var_a():
#     t = get_data(TEST_FILE_2)
#     g = mv.var_a(t, [50, -100, -80, 140])


# def test_vorticity():
#     u = get_data(TEST_FILE_5)
#     v = get_data(TEST_FILE_6)
#     g = mv.vorticity(u, v)
