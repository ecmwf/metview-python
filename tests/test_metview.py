import os
import shutil

from mpy._metview import ffi, lib
from mpy.metview import make


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
    lib.p_push_grib(grib_path.encode('utf-8'))
    lib.p_call_function('plot'.encode('utf-8'), 1)
    os.remove(grib_path)