# (C) Copyright 2017- ECMWF.
#
# This software is licensed under the terms of the Apache Licence Version 2.0
# which can be obtained at http://www.apache.org/licenses/LICENSE-2.0.
#
# In applying this licence, ECMWF does not waive the privileges and immunities
# granted to it by virtue of its status as an intergovernmental organisation
# nor does it submit to any jurisdiction.
#


import os
from resource import getrusage, RUSAGE_SELF

import yaml
import numpy as np
import metview as mv

import diag_util as diag

# memory stats files
MEMORY_REF_FILE = "mem_reference.yaml"
MEMORY_RES_FILE = "mem_result.yaml"

# maximum rss increase in % from ref rss
MAX_INCREASE_PERCENT = 10

# -----------------------------------
# Tests for memory usage
# To run it use:
# pytest diag_mem.py --forked
# ------------------------------------


# ------------------------------------------
# Stats
# ------------------------------------------


def _load_stats(fname):
    f_path = fname
    if os.path.exists(f_path):
        with open(f_path, "rt") as f:
            return yaml.safe_load(f)


def load_ref_stats():
    return _load_stats(MEMORY_REF_FILE)


def load_res_stats():
    return _load_stats(MEMORY_RES_FILE)


def get_ref_rss(name):
    try:
        r = load_ref_stats()
        if r is not None:
            v = r.get(name, None)
            if v is not None:
                return int(v)
    except:
        return None


def mem_usage(func):
    def wrapper():
        func()

        fn_name = func.__name__

        # load result data
        res = load_res_stats()
        if res is None:
            res = {}

        # get max rss
        rss = getrusage(RUSAGE_SELF).ru_maxrss
        rss = int(rss)
        # LOG.info(" RSS: {} MB".format(int(rss / (1024 * 1024))))

        # check departure from ref
        ref_rss = get_ref_rss(fn_name)
        if ref_rss is not None:
            delta = rss - ref_rss
            max_delta = MAX_INCREASE_PERCENT * ref_rss / 100.0
            assert delta < max_delta

        # add rss to data and save it to file
        res[fn_name] = rss
        s = yaml.dump(res, default_flow_style=False)
        with open(MEMORY_RES_FILE, "w") as f:
            f.write(s)

    return wrapper


# ------------------------------------------
# Individual tests
# ------------------------------------------


@mem_usage
def test_accumulate():
    t = diag.get_data(diag.TEST_FILE_2)
    g = mv.accumulate(t)
    assert len(g) == 20


@mem_usage
def test_add_op_1():
    t = diag.get_data(diag.TEST_FILE_2)
    g = t + 1
    assert len(g) == 20


@mem_usage
def test_add_op_2():
    t = diag.get_data(diag.TEST_FILE_2)
    g = t + t
    assert len(g) == 20


@mem_usage
def test_add_op_3():
    u = diag.get_data(diag.TEST_FILE_5)
    v = diag.get_data(diag.TEST_FILE_6)
    g = u + v
    assert len(g) == 20


@mem_usage
def test_average():
    t = diag.get_data(diag.TEST_FILE_2)
    g = mv.average(t)
    assert len(g) == 20


@mem_usage
def test_average_ew():
    t = diag.get_data(diag.TEST_FILE_2)
    g = mv.average_ew(t, [60, -180, -60, 180], 2)


@mem_usage
def test_bearing():
    t = diag.get_data(diag.TEST_FILE_2)
    g = mv.bearing(t, [45, 20])
    assert len(g) == 20


@mem_usage
def test_bitmap():
    t = diag.get_data(diag.TEST_FILE_2)
    g = mv.bitmap(t, 273)
    assert len(g) == 20


@mem_usage
def test_coslat():
    t = diag.get_data(diag.TEST_FILE_2)
    g = mv.coslat(t)
    assert len(g) == 20


@mem_usage
def test_corr_a():
    u = diag.get_data(diag.TEST_FILE_5)
    v = diag.get_data(diag.TEST_FILE_6)
    g = mv.corr_a(u, v, [50, -100, -80, 140])
    assert len(g) == 20


@mem_usage
def test_covar():
    u = diag.get_data(diag.TEST_FILE_5)
    v = diag.get_data(diag.TEST_FILE_6)
    g = mv.covar(u, v)
    assert len(g) == 1


@mem_usage
def test_covar_a():
    u = diag.get_data(diag.TEST_FILE_5)
    v = diag.get_data(diag.TEST_FILE_6)
    g = mv.covar_a(u, v, [50, -100, -80, 140])
    assert len(g) == 20


@mem_usage
def test_direction():
    u = diag.get_data(diag.TEST_FILE_5)
    v = diag.get_data(diag.TEST_FILE_6)
    g = mv.direction(u, v)
    assert len(g) == 20


@mem_usage
def test_divergence():
    u = diag.get_data(diag.TEST_FILE_5)
    v = diag.get_data(diag.TEST_FILE_6)
    g = mv.vorticity(u, v)
    assert len(g) == 20


@mem_usage
def test_filter_op():
    t = diag.get_data(diag.TEST_FILE_2)
    g = t > 273.16
    assert len(g) == 20


@mem_usage
def test_first_derivative_x():
    t = diag.get_data(diag.TEST_FILE_2)
    g = mv.first_derivative_x(t)
    assert len(g) == 20


@mem_usage
def test_first_derivative_y():
    t = diag.get_data(diag.TEST_FILE_2)
    g = mv.first_derivative_y(t)
    assert len(g) == 20


@mem_usage
def test_frequencies():
    t = diag.get_data(diag.TEST_FILE_2)
    g = mv.frequencies(t, list(range(220, 320, 10)))


@mem_usage
def test_gradient():
    t = diag.get_data(diag.TEST_FILE_2)
    g = mv.gradient(t)
    assert len(g) == 40


@mem_usage
def test_grid_cell_area():
    t = diag.get_data(diag.TEST_FILE_2)
    g = mv.grid_cell_area(t)
    assert len(g) == 20


@mem_usage
def test_integral():
    t = diag.get_data(diag.TEST_FILE_2)
    g = mv.integral(t)
    assert len(g) == 20


@mem_usage
def test_integrate():
    t = diag.get_data(diag.TEST_FILE_2)
    g = mv.integrate(t)
    assert len(g) == 20


@mem_usage
def test_laplacian():
    t = diag.get_data(diag.TEST_FILE_2)
    g = mv.laplacian(t)
    assert len(g) == 20


@mem_usage
def test_mask():
    t = diag.get_data(diag.TEST_FILE_2)
    g = mv.mask(t, [60, -30, 22, 45])
    assert len(g) == 20


@mem_usage
def test_max():
    t = diag.get_data(diag.TEST_FILE_2)
    g = mv.max(t)
    assert len(g) == 1


@mem_usage
def test_maxvalue():
    t = diag.get_data(diag.TEST_FILE_2)
    g = mv.maxvalue(t)


@mem_usage
def test_mean():
    t = diag.get_data(diag.TEST_FILE_2)
    g = mv.mean(t)
    assert len(g) == 1


@mem_usage
def test_mean_ew():
    t = diag.get_data(diag.TEST_FILE_2)
    g = mv.mean(t)


@mem_usage
def test_min():
    t = diag.get_data(diag.TEST_FILE_2)
    g = mv.min(t)
    assert len(g) == 1


@mem_usage
def test_minvalue():
    t = diag.get_data(diag.TEST_FILE_2)
    g = mv.minvalue(t)


@mem_usage
def test_poly_mask():
    t = diag.get_data(diag.TEST_FILE_2)
    lon = np.array([-42, -24, 20, 27, -7, -17])
    lat = np.array([28, 60, 51, 24, 5, 30])
    g = mv.poly_mask(t, lat, lon)
    assert len(g) == 20


@mem_usage
def test_rmask():
    t = diag.get_data(diag.TEST_FILE_2)
    g = mv.rmask(t, 60, -30, 1500 * 000)
    assert len(g) == 20


@mem_usage
def test_rms():
    t = diag.get_data(diag.TEST_FILE_2)
    g = mv.rms(t)
    assert len(g) == 1


@mem_usage
def test_second_derivative_x():
    t = diag.get_data(diag.TEST_FILE_2)
    g = mv.second_derivative_x(t)
    assert len(g) == 20


@mem_usage
def test_second_derivative_y():
    t = diag.get_data(diag.TEST_FILE_2)
    g = mv.second_derivative_y(t)
    assert len(g) == 20


@mem_usage
def test_shear_deformation():
    u = diag.get_data(diag.TEST_FILE_5)
    v = diag.get_data(diag.TEST_FILE_6)
    g = mv.shear_deformation(u, v)
    assert len(g) == 20


@mem_usage
def test_sin():
    t = diag.get_data(diag.TEST_FILE_2)
    g = mv.coslat(t)
    assert len(g) == 20


@mem_usage
def test_sinlat():
    t = diag.get_data(diag.TEST_FILE_2)
    g = mv.sinlat(t)
    assert len(g) == 20


@mem_usage
def test_speed():
    u = diag.get_data(diag.TEST_FILE_5)
    v = diag.get_data(diag.TEST_FILE_6)
    g = mv.speed(u, v)
    assert len(g) == 20


@mem_usage
def test_stdev():
    t = diag.get_data(diag.TEST_FILE_2)
    g = mv.stdev(t)
    assert len(g) == 1


@mem_usage
def test_stdev_a():
    t = diag.get_data(diag.TEST_FILE_2)
    g = mv.stdev_a(t, [50, -100, -80, 140])
    assert len(g) == 20


@mem_usage
def test_stretch_deformation():
    u = diag.get_data(diag.TEST_FILE_5)
    v = diag.get_data(diag.TEST_FILE_6)
    g = mv.stretch_deformation(u, v)
    assert len(g) == 20


@mem_usage
def test_sum():
    t = diag.get_data(diag.TEST_FILE_2)
    g = mv.sum(t)
    assert len(g) == 1


@mem_usage
def test_tanlat():
    t = diag.get_data(diag.TEST_FILE_2)
    g = mv.tanlat(t)
    assert len(g) == 20


@mem_usage
def test_unipressure():
    f = diag.get_data(diag.TEST_FILE_1)
    lnsp = mv.read(data=f, param="lnsp")
    g = mv.unipressure(lnsp)
    assert len(g) == 137


@mem_usage
def test_unithickness():
    f = diag.get_data(diag.TEST_FILE_1)
    lnsp = mv.read(data=f, param="lnsp")
    g = mv.unithickness(lnsp)
    assert len(g) == 137


@mem_usage
def test_univertint():
    f = diag.get_data(diag.TEST_FILE_1)
    lnsp = mv.read(data=f, param="lnsp")
    t = mv.read(data=f, param="t")
    g = mv.univertint(lnsp, t)
    assert len(g) == 1


@mem_usage
def test_var():
    t = diag.get_data(diag.TEST_FILE_2)
    g = mv.var(t)
    assert len(g) == 1


@mem_usage
def test_var_a():
    t = diag.get_data(diag.TEST_FILE_2)
    g = mv.var_a(t, [50, -100, -80, 140])
    assert len(g) == 20


@mem_usage
def test_vorticity():
    u = diag.get_data(diag.TEST_FILE_5)
    v = diag.get_data(diag.TEST_FILE_6)
    g = mv.vorticity(u, v)
    assert len(g) == 20
