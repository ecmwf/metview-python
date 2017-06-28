import os
import shutil
from mpy._metview import ffi, lib
from mpy.metview import *


def test_push_number():
    lib.p_push_number(5)
    lib.p_push_number(4)

def test_print():
    pr('Start ', 7, 1, 3, ' Finished!')
    pr(6, 2, ' Middle ', 6)

def test_lowercase():
    a = low('MetViEw')
    assert a == 'metview'

def test_read():
    path = os.path.dirname(__file__)
    gg = read({'SOURCE' : os.path.join(path, 'test.grib'), 'GRID' : '80'})
    regidded_grib = shutil.copyfile(gg.url, os.path.join(path, 'test_gg_grid.grib'))
    grib_path = read(regidded_grib)
    
def test_plot():
    grib_path = Fieldset(os.path.join(os.path.dirname(__file__), 'test_gg_grid.grib'))
    contour = mcont({
        'CONTOUR_LINE_COLOUR': 'PURPLE',
        'CONTOUR_LINE_THICKNESS': '3',
        'CONTOUR_HIGHLIGHT': 'OFF'
    })
    coast = mcoast({'MAP_COASTLINE_LAND_SHADE': 'ON'})
    lib.p_push_grib(grib_path.push())
    lib.p_push_request(dict_to_request(contour))
    lib.p_push_request(dict_to_request(coast))
    lib.p_call_function('plot'.encode('utf-8'), 3)
    os.remove(grib_path.url)
