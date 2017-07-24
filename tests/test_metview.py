
import os
import numpy as np

from mpy.metview import *


PATH = os.path.dirname(__file__)
MAX_VALUE = 316.06060791015625
TEST_FIELDSET = read(os.path.join(PATH, 'test.grib'))


def file_in_testdir(filename):
    return os.path.join(PATH, filename)


def test_push_number():
    lib.p_push_number(5)
    lib.p_push_number(4)


def test_dict_to_pushed_request():
    dict = {
        'param1': True,
        'param2': False,
        'param3': 10,
        'param4': 10.5,
        'param5': 'metview',
        'param6': ['1', '2', '3']
    }
    dict_to_pushed_args(dict)


def test_print():
    pr('Start ', 7, 1, 3, ' Finished!')
    pr(6, 2, ' Middle ', 6)


def test_lowercase():
    a = low('MetViEw')
    assert a == 'metview'


def test_read():
    gg = read({'SOURCE': file_in_testdir('test.grib'), 'GRID': 80})
    assert grib_get_string(gg, 'typeOfGrid') == 'regular_gg'


def test_write():
    gg = read({'SOURCE': file_in_testdir('test.grib'), 'GRID': 80})
    regridded_grib = write(file_in_testdir('test_gg_grid.grib'), gg)
    assert regridded_grib == 0
    os.remove(file_in_testdir('test_gg_grid.grib'))


def test_maxvalue():
    maximum = maxvalue(TEST_FIELDSET)
    assert np.isclose(maximum, MAX_VALUE)


def test_add():
    plus_two = TEST_FIELDSET + 2
    maximum = maxvalue(plus_two)
    assert np.isclose(maximum, MAX_VALUE + 2)


def test_add_fieldsets():
    sum = TEST_FIELDSET + TEST_FIELDSET
    maximum = maxvalue(sum)
    assert np.isclose(maximum, MAX_VALUE + MAX_VALUE)


def test_sub():
    minus_two = TEST_FIELDSET - 2
    maximum = maxvalue(minus_two)
    assert np.isclose(maximum, MAX_VALUE - 2)


def test_sub_fieldsets():
    sub = TEST_FIELDSET - TEST_FIELDSET
    maximum = maxvalue(sub)
    assert np.isclose(maximum, 0)


def test_product():
    times_two = TEST_FIELDSET * 2
    maximum = maxvalue(times_two)
    assert np.isclose(maximum, MAX_VALUE * 2)


def test_product_fieldsets():
    prod = TEST_FIELDSET * TEST_FIELDSET
    maximum = maxvalue(prod)
    assert np.isclose(maximum, MAX_VALUE * MAX_VALUE)


def test_division():
    divided_two = TEST_FIELDSET / 2
    maximum = maxvalue(divided_two)
    assert np.isclose(maximum, MAX_VALUE / 2)


def test_division_fieldsets():
    div = TEST_FIELDSET / TEST_FIELDSET
    maximum = maxvalue(div)
    assert np.isclose(maximum, 1)


def test_power():
    raised_two = TEST_FIELDSET ** 2
    maximum = maxvalue(raised_two)
    assert np.isclose(maximum, MAX_VALUE ** 2)


def test_read_bufr():
    bufr = read(file_in_testdir('obs_3day.bufr'))
    assert(type(bufr) == 'observations')


def test_read_gpt():
    gpt = read(file_in_testdir('t2m_3day.gpt'))
    assert(type(gpt) == 'geopoints')
    assert(count(gpt) == 45)


def test_obsfilter():
    bufr = read(file_in_testdir('obs_3day.bufr'))

    # test two styles of passing parameters
    gpt1 = obsfilter({'data': bufr, 'parameter' : '012004', 'output' : "geopoints"})
    gpt2 = obsfilter(data = bufr, parameter = '012004', output = "geopoints")
    assert(type(gpt1) == 'geopoints')
    assert(count(gpt1) == 45)
    assert(type(gpt2) == 'geopoints')
    assert(count(gpt2) == 45)


def test_met_plot():
    contour = mcont(
        {
            'CONTOUR_LINE_COLOUR': 'PURPLE',
            'CONTOUR_LINE_THICKNESS': 3,
            'CONTOUR_HIGHLIGHT': False
        })
    coast = mcoast({'MAP_COASTLINE_LAND_SHADE': True})
    met_plot(TEST_FIELDSET, contour, coast)


def test_plot():
    png_output = {
        'output_type': 'PnG',
        'output_width': 1200,
        'output_name': file_in_testdir('test_plot')
    }
    grid_shade = {
        'legend': True,
        'contour': False,
        'contour_highlight': True,
        'contour_shade': True,
        'contour_shade_technique': 'grid_shading',
        'contour_shade_max_level_colour': 'red',
        'contour_shade_min_level_colour': 'blue',
        'contour_shade_colour_direction': 'clockwise',
    }
    plot(TEST_FIELDSET, grid_shade, **png_output)
    os.remove(file_in_testdir('test_plot.1.png'))
