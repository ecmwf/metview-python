import os
import shutil
import mpy.metview
from mpy._metview import ffi, lib
from mpy.metview import make, dict_to_request

def test_push_number():
    lib.p_push_number(5)
    lib.p_push_number(4)

def test_print():
    # call Metview's 'print' function with any number of arguments
    pr = make('print')
    pr('Start ', 7, 1, 3, ' Finished!')
    pr(6, 2, ' Middle ', 6)

def test_lowercase():
    # call Metview's 'lowercase' string function
    low = make('lowercase')
    a = low('MetViEw')
    assert a == 'metview'

def test_read():
    read = make('read')
    path = os.path.dirname(__file__)
    gg = read({'SOURCE' : os.path.join(path, 'test.grib'), 'GRID' : '80'})
    regidded_grib = shutil.copyfile(gg, os.path.join(path, 'test_gg_grid.grib'))
    grib_path = read(regidded_grib)
    
def test_plot():
    grib_path = os.path.join(os.path.dirname(__file__), 'test_gg_grid.grib')
    mcont  = make('mcont')
    mcoast = make('mcoast')
    contour = mcont({
        'CONTOUR_LINE_COLOUR'    : 'PURPLE',
        'CONTOUR_LINE_THICKNESS' : '3',
        'CONTOUR_HIGHLIGHT'      : 'OFF'})
    coast = mcoast({
        'MAP_COASTLINE_LAND_SHADE' : 'ON'})
    lib.p_push_grib(grib_path.encode('utf-8'))
    lib.p_push_request(dict_to_request(contour))
    lib.p_push_request(dict_to_request(coast))
    lib.p_call_function('plot'.encode('utf-8'), 3)
    #os.remove(grib_path)


#test_push_number()
#test_print()
#test_lowercase()
#test_read()
#test_plot()

