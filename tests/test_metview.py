
import os
import numpy as np

from mpy.metview import *


PATH = os.path.dirname(__file__)
MAX_VALUE = 316.09642028808594


def test_push_number():
    lib.p_push_number(5)
    lib.p_push_number(4)


def test_dict_to_request():
    dict = {
        'param1': True,
        'param2': False,
        'param3': 10,
        'param4': 10.5,
        'param5': 'metview',
        'param6': ['1', '2', '3']
    }
    dict_to_request(dict)


def test_print():
    pr('Start ', 7, 1, 3, ' Finished!')
    pr(6, 2, ' Middle ', 6)


def test_lowercase():
    a = low('MetViEw')
    assert a == 'metview'


def test_read():
    gg = read({'SOURCE': os.path.join(PATH, 'test.grib'), 'GRID': '80'})
    assert grib_get_string(gg, 'typeOfGrid') == 'regular_gg'


def test_write():
    gg = read({'SOURCE': os.path.join(PATH, 'test.grib'), 'GRID': '80'})
    regridded_grib = write(os.path.join(PATH, 'test_gg_grid.grib'), gg)
    assert regridded_grib == 0


def test_maxvalue():
    grib = Fieldset(os.path.join(PATH, 'test_gg_grid.grib'))
    maximum = maxvalue(grib)
    assert np.isclose(maximum, MAX_VALUE)


def test_add():
    grib = Fieldset(os.path.join(PATH, 'test_gg_grid.grib'))
    plus_two = grib + 2
    maximum = maxvalue(plus_two)
    assert np.isclose(maximum, MAX_VALUE + 2)


def test_product():
    grib = Fieldset(os.path.join(PATH, 'test_gg_grid.grib'))
    times_two = grib * 2
    maximum = maxvalue(times_two)
    assert np.isclose(maximum, MAX_VALUE * 2)


def test_division():
    grib = Fieldset(os.path.join(PATH, 'test_gg_grid.grib'))
    divided_two = grib / 2
    maximum = maxvalue(divided_two)
    assert np.isclose(maximum, MAX_VALUE / 2)


def test_power():
    grib = Fieldset(os.path.join(PATH, 'test_gg_grid.grib'))
    raised_two = grib ** 2
    maximum = maxvalue(raised_two)
    assert np.isclose(maximum, MAX_VALUE ** 2)


def test_met_plot():
    grib = Fieldset(os.path.join(PATH, 'test_gg_grid.grib'))
    contour = mcont(
        {
            'CONTOUR_LINE_COLOUR': 'PURPLE',
            'CONTOUR_LINE_THICKNESS': '3',
            'CONTOUR_HIGHLIGHT': False
        })
    coast = mcoast({'MAP_COASTLINE_LAND_SHADE': True})
    met_plot(grib, contour, coast)


def test_plot():
    grib = Fieldset(os.path.join(PATH, 'test_gg_grid.grib'))
    contour = mcont(
        {
            'CONTOUR_LINE_COLOUR': 'PURPLE',
            'CONTOUR_LINE_THICKNESS': '3',
            'CONTOUR_HIGHLIGHT': False
        })
    coast = mcoast({'MAP_COASTLINE_LAND_SHADE': True})
    png_output = {
        'output_type': 'png',
        'output_width': 1200,
        'output_name': os.path.join(PATH, 'test_plot')
    }
    plot(grib, contour, coast, **png_output)
    os.remove(grib.url)
    os.remove(os.path.join(PATH, 'test_plot.1.png'))
