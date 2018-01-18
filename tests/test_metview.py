
import os
import numpy as np

import pytest

import mpy.metview as mpy


PATH = os.path.dirname(__file__)
MAX_VALUE = 316.06060791015625
SEMI_EQUATOR = 20001600.0
MAX_SQRT_GPT = 16.867127793433
MAX_GPT = 284.5


def file_in_testdir(filename):
    return os.path.join(PATH, filename)


def test_push_number():
    mpy.lib.p_push_number(5)
    mpy.lib.p_push_number(4)


def test_version_info():
    out = mpy.version_info()
    assert 'metview_version' in out


def test_describe():
    mpy.describe('type')


def test_dict_to_pushed_request():
    dict = {
        'param1': True,
        'param2': False,
        'param3': 10,
        'param4': 10.5,
        'param5': 'metview',
        'param6': ['1', '2', '3']
    }
    mpy.dict_to_pushed_args(dict)


def test_definitions():
    mcont_def = mpy.mcont({'legend': True})
    msymb_def = mpy.msymb({'symbol_type': 'marker'})
    mcoast_def = mpy.mcoast({'map_coastline_land_shade': True})
    mobs_def = mpy.mobs({'obs_temperature': False})
    mtext_def = mpy.mtext({'text_font_size': '0.80'})
    geoview_def = mpy.geoview({'map_projection': 'polar_stereographic'})
    ps_output_def = mpy.ps_output({'output_name': 'test'})
    assert mcont_def['LEGEND'] == 'ON'
    assert msymb_def['SYMBOL_TYPE'] == 'MARKER'
    assert mcoast_def['MAP_COASTLINE_LAND_SHADE'] == 'ON'
    assert mobs_def['OBS_TEMPERATURE'] == 'OFF'
    assert mtext_def['TEXT_FONT_SIZE'] == 0.8
    assert geoview_def['MAP_PROJECTION'] == 'POLAR_STEREOGRAPHIC'
    assert ps_output_def['OUTPUT_NAME'] == 'test'


def test_print():
    mpy.pr('Start ', 7, 1, 3, ' Finished!')
    mpy.pr(6, 2, ' Middle ', 6)


def test_lowercase():
    a = mpy.low('MetViEw')
    assert a == 'metview'


# def test_lists():
#     m= mpy.mcont(contour_level_selection_type = 'level_list', contour_level_list = [1, 2, 6])
#     print('M: ', m)
# test_lists()


def test_create_list():
    inlist = [1, 5, 6, 5, 1, 9, 18]
    outlist = mpy.makelist(*inlist)
    assert outlist == inlist


def test_create_list_from_tuple():
    intuple = (10, 50, 60, 50, 1.1, 90)
    outlist = mpy.makelist(*intuple)
    assert outlist == list(intuple)


def test_list_unique():
    inlist = [1, 5, 6, 5, 1, 9]
    ulist = mpy.unique(inlist)
    assert ulist == [1, 5, 6, 9]


def test_tuple_unique():
    intuple = (3, 2, 2, 7, 3, 1.2, 2.1, 1.2)
    ulist = mpy.unique(intuple)
    assert ulist == [3, 2, 7, 1.2, 2.1]


def test_lists_as_input():
    my_list = [1, 5, 6]
    assert mpy.count(my_list) == 3


def test_tuples_as_input():
    my_tuple = [1, 0, 5, 6]
    assert mpy.count(my_tuple) == 4


def test_read():
    gg = mpy.read({'SOURCE': file_in_testdir('test.grib'), 'GRID': 80})
    assert mpy.grib_get_string(gg, 'typeOfGrid') == 'regular_gg'


def test_write():
    gg = mpy.read({'SOURCE': file_in_testdir('test.grib'), 'GRID': 80})
    regridded_grib = mpy.write(file_in_testdir('test_gg_grid.grib'), gg)
    assert regridded_grib == 0
    os.remove(file_in_testdir('test_gg_grid.grib'))


TEST_FIELDSET = mpy.read(os.path.join(PATH, 'test.grib'))


def test_type():
    out = mpy.type(TEST_FIELDSET)
    assert out == 'fieldset'


# def test_retrieve():
#     tccp = mpy.retrieve({
#         'levtype': 'sfc',
#         'param': 'tccp',
#         'grid': 'o640'  # octahedral grid (a specific form of a reduced Gaussian grid)
#     })
#     assert mpy.type(tccp)== 'fieldset'


def test_count():
    out = mpy.count(TEST_FIELDSET)
    assert out == 1


def test_maxvalue():
    maximum = mpy.maxvalue(TEST_FIELDSET)
    assert np.isclose(maximum, MAX_VALUE)


def test_accumulate():
    all_missing = mpy.read(file_in_testdir('all_missing_vals.grib'))
    out = mpy.accumulate(all_missing)
    assert out is None


def test_add():
    plus_two = TEST_FIELDSET + 2
    maximum = mpy.maxvalue(plus_two)
    assert np.isclose(maximum, MAX_VALUE + 2)


def test_add_fieldsets():
    sum = TEST_FIELDSET + TEST_FIELDSET
    maximum = mpy.maxvalue(sum)
    assert np.isclose(maximum, MAX_VALUE + MAX_VALUE)


def test_sub():
    minus_two = TEST_FIELDSET - 2
    maximum = mpy.maxvalue(minus_two)
    assert np.isclose(maximum, MAX_VALUE - 2)


def test_sub_fieldsets():
    sub = TEST_FIELDSET - TEST_FIELDSET
    maximum = mpy.maxvalue(sub)
    assert np.isclose(maximum, 0)


def test_sqrt():
    sqrt_fd = mpy.sqrt(TEST_FIELDSET)
    maximum = mpy.maxvalue(sqrt_fd)
    assert np.isclose(maximum, np.sqrt(MAX_VALUE))


def test_product():
    times_two = TEST_FIELDSET * 2
    maximum = mpy.maxvalue(times_two)
    assert np.isclose(maximum, MAX_VALUE * 2)


def test_product_fieldsets():
    prod = TEST_FIELDSET * TEST_FIELDSET
    maximum = mpy.maxvalue(prod)
    assert np.isclose(maximum, MAX_VALUE * MAX_VALUE)


def test_division():
    divided_two = TEST_FIELDSET / 2
    maximum = mpy.maxvalue(divided_two)
    assert np.isclose(maximum, MAX_VALUE / 2)


def test_division_fieldsets():
    div = TEST_FIELDSET / TEST_FIELDSET
    maximum = mpy.maxvalue(div)
    assert np.isclose(maximum, 1)


def test_power():
    raised_two = TEST_FIELDSET ** 2
    maximum = mpy.maxvalue(raised_two)
    assert np.isclose(maximum, MAX_VALUE ** 2)


def test_distance():
    dist = mpy.distance(TEST_FIELDSET, 0, 0)
    minimum = mpy.minvalue(dist)
    maximum = mpy.maxvalue(dist)
    assert np.isclose(minimum, 0.0)
    assert np.isclose(maximum, SEMI_EQUATOR)


def test_valid_date_len_1():
    vd = mpy.valid_date(TEST_FIELDSET)
    assert isinstance(vd,np.datetime64)
    assert vd == np.datetime64("2017-04-27T12:00:00")


def test_valid_date_len_6():
    grib = mpy.read(os.path.join(PATH, 't_for_xs.grib'))
    vd_grib = mpy.valid_date(grib)
    assert isinstance(vd_grib[1],np.datetime64)
    
    vd_ref = np.datetime64("2017-08-01T12:00:00")
    for vd in vd_grib:
        assert vd == vd_ref


def test_base_date():
    bd = mpy.base_date(TEST_FIELDSET)
    assert isinstance(bd,np.datetime64)
    assert bd == np.datetime64("2017-04-27T12:00:00")
    
    
def test_fieldset_len_1():
    flen = len(TEST_FIELDSET)
    assert(flen == 1)


def test_fieldset_len_6():
    grib = mpy.read(os.path.join(PATH, 't_for_xs.grib'))
    flen = len(grib)
    assert(flen == 6)


def test_fieldset_single_index():
    grib = mpy.read(os.path.join(PATH, 't_for_xs.grib'))
    grib4 = grib[3]  # 0-based indexing in Python
    assert(len(grib4) == 1)
    assert(mpy.grib_get_long(grib4, 'level') == 500)


def test_read_bufr():
    bufr = mpy.read(file_in_testdir('obs_3day.bufr'))
    assert(mpy.type(bufr) == 'observations')


def test_read_gpt():
    gpt = mpy.read(file_in_testdir('t2m_3day.gpt'))
    assert(mpy.type(gpt) == 'geopoints')
    assert(mpy.count(gpt) == 45)


TEST_GEOPOINTS = mpy.read(os.path.join(PATH, 't2m_3day.gpt'))


def test_filter_gpt():
    filter_out = TEST_GEOPOINTS.filter(TEST_GEOPOINTS >= 1)
    assert mpy.type(filter_out) == 'geopoints'


def test_sqrt_geopoints():
    sqrt_out = mpy.sqrt(TEST_GEOPOINTS)
    maximum = mpy.maxvalue(sqrt_out)
    assert mpy.type(sqrt_out) == 'geopoints'
    assert np.isclose(maximum, MAX_SQRT_GPT)


def test_add_geopoints():
    add = TEST_GEOPOINTS + TEST_GEOPOINTS
    maximum = mpy.maxvalue(add)
    assert np.isclose(maximum, MAX_GPT + MAX_GPT)


def test_prod_geopoints():
    prod = TEST_GEOPOINTS * TEST_GEOPOINTS
    maximum = mpy.maxvalue(prod)
    assert np.isclose(maximum, MAX_GPT * MAX_GPT)


def test_geopoints_relational_operator():
    lt = TEST_GEOPOINTS < 1
    le = TEST_GEOPOINTS <= 1
    gt = TEST_GEOPOINTS > 100
    ge = TEST_GEOPOINTS >= 100
    assert mpy.maxvalue(lt) == 0
    assert mpy.maxvalue(le) == 0
    assert mpy.maxvalue(gt) == 1
    assert mpy.maxvalue(ge) == 1


def test_geopoints_fieldset_operator():
    diff = TEST_FIELDSET - TEST_GEOPOINTS
    assert mpy.type(diff) == 'geopoints'


def test_obsfilter():
    bufr = mpy.read(file_in_testdir('obs_3day.bufr'))

    # test two styles of passing parameters
    gpt1 = mpy.obsfilter({'data': bufr, 'parameter': '012004', 'output': "geopoints"})
    gpt2 = mpy.obsfilter(data=bufr, parameter='012004', output="geopoints")
    assert(mpy.type(gpt1) == 'geopoints')
    assert(mpy.count(gpt1) == 45)
    assert(mpy.type(gpt2) == 'geopoints')
    assert(mpy.count(gpt2) == 45)


def test_date_year():
    d = np.datetime64("2017-04-27T06:18:02")
    assert mpy.year(d) == 2017
    
    
def test_date_month():
    d = np.datetime64("2017-04-27T06:18:02")
    assert mpy.month(d) == 4   
    
    
def test_date_day():
    d = np.datetime64("2017-04-27T06:18:02")
    assert mpy.day(d) == 27
    
    
def test_date_hour():
    d = np.datetime64("2017-04-27T06:18:02")
    assert mpy.hour(d) == 6 
 
 
# this tests the calling of the Cross Section module, but also the
# return of netCDF data and also that we can perform operations on it
# as input and output
def test_cross_section_data():
    grib = mpy.read(os.path.join(PATH, 't_for_xs.grib'))
    xs_data = mpy.mcross_sect(
        line=[59.9, -180, -13.5, 158.08],
        data=grib,
    )
    # the result of this should be a netCDF variable
    assert mpy.type(xs_data) == 'netcdf'
    mpy.setcurrent(xs_data, 't')
    assert mpy.dimension_names(xs_data) == ['time', 'nlev', 'lon']
    assert np.isclose(mpy.value(xs_data, 1), 230.39156)
    xs_data_x2 = xs_data * 2
    assert np.isclose(mpy.value(xs_data_x2, 1), 460.7831)


def test_met_plot():
    contour = mpy.mcont({
            'CONTOUR_LINE_COLOUR': 'PURPLE',
            'CONTOUR_LINE_THICKNESS': 3,
            'CONTOUR_HIGHLIGHT': False
    })
    coast = mpy.mcoast({'MAP_COASTLINE_LAND_SHADE': True})
    mpy.met_plot(TEST_FIELDSET, contour, coast)


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
    mpy.plot(TEST_FIELDSET, grid_shade, **png_output)
    os.remove(file_in_testdir('test_plot.1.png'))


def test_macro_error():
    with pytest.raises(Exception):
        TEST_FIELDSET[125]


def test_value_file_path():
    p = TEST_FIELDSET + 1  # this will force Metview to write a new temporary file
    assert(p.url != "")
    assert(os.path.isfile(p.url))


def test_mvl_ml2hPa():
    ml_data = mpy.read(file_in_testdir('ml_data.grib'))
    assert mpy.type(ml_data) == 'fieldset'
    ml_t = mpy.read(data=ml_data, param='t')
    ml_lnsp = mpy.read(data=ml_data, param='lnsp')
    desired_pls = [1000, 900, 850, 500, 300, 100, 10, 1, 0.8, 0.5, 0.3, 0.1]
    pl_data = mpy.mvl_ml2hPa(ml_lnsp, ml_t, desired_pls)
    assert mpy.type(pl_data) == 'fieldset'
    pls = mpy.grib_get_long(pl_data, 'level')
    lev_types = mpy.grib_get_string(pl_data, 'typeOfLevel')
    lev_divisors = [1 if x == 'isobaricInhPa' else 100 for x in lev_types]
    pl_in_hpa = [a / b for a, b in zip(pls, lev_divisors)]
    assert(pl_in_hpa == desired_pls)


def test_mf_function_caller():
    info = mpy.mf.nearest_gridpoint_info(TEST_FIELDSET[0], 10, 20)
    assert(isinstance(info, list))
    info0 = info[0]
    print(info0)
    assert(isinstance(info0, dict))
    assert(info0['latitude'] == 9.75)
    assert(info0['longitude'] == 20.25)
    assert(info0['index'] == 51388)


def test_push_nil():
    n = mpy.nil()
    assert(n == None)
    assert(mpy.type(n) == 'nil')
