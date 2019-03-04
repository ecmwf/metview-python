
import os
import numpy as np
import datetime
import pytest
import pandas as pd
import xarray as xr

import metview as mv
from metview import bindings


PATH = os.path.dirname(__file__)
MAX_VALUE = 316.06060791015625
SEMI_EQUATOR = 20001600.0
MAX_SQRT_GPT = 16.867127793433
MAX_GPT = 284.5


def metview_version():
    version = mv.version_info()
    return version['metview_version']


def supports_float32_vectors():
    return metview_version() >= 50200


def test_names():
    assert mv.dictionary.__name__ == mv.dictionary.__qualname__ == 'dictionary'
    assert mv.dictionary.__module__ == 'metview'


def file_in_testdir(filename):
    return os.path.join(PATH, filename)


def test_version_info():
    out = mv.version_info()
    assert 'metview_version' in out


def test_describe():
    mv.describe('type')


def test_definitions():
    mcont_def = mv.mcont({'legend': True})
    msymb_def = mv.msymb({'symbol_type': 'marker'})
    mcoast_def = mv.mcoast({'map_coastline_land_shade': True})
    mobs_def = mv.mobs({'obs_temperature': False})
    mtext_def = mv.mtext({'text_font_size': '0.80'})
    geoview_def = mv.geoview({'map_projection': 'polar_stereographic'})
    ps_output_def = mv.ps_output({'output_name': 'test'})
    assert mcont_def['LEGEND'] == 'ON'
    assert msymb_def['SYMBOL_TYPE'] == 'MARKER'
    assert mcoast_def['MAP_COASTLINE_LAND_SHADE'] == 'ON'
    assert mobs_def['OBS_TEMPERATURE'] == 'OFF'
    assert mtext_def['TEXT_FONT_SIZE'] == 0.8
    assert geoview_def['MAP_PROJECTION'] == 'POLAR_STEREOGRAPHIC'
    assert ps_output_def['OUTPUT_NAME'] == 'test'


def test_print():
    mv.print('Start ', 7, 1, 3, ' Finished!')
    mv.print(6, 2, ' Middle ', 6)


def test_lowercase():
    a = mv.lowercase('MetViEw')
    assert a == 'metview'


# def test_lists():
#     m= mv.mcont(contour_level_selection_type = 'level_list', contour_level_list = [1, 2, 6])
#     print('M: ', m)
# test_lists()


def test_create_list():
    inlist = [1, 5, 6, 5, 1, 9, 18]
    outlist = mv.list(*inlist)
    assert outlist == inlist


def test_create_empty_list():
    outlist = mv.list()
    assert outlist == []


def test_create_list_from_tuple():
    intuple = (10, 50, 60, 50, 1.1, 90)
    outlist = mv.list(*intuple)
    assert outlist == list(intuple)


def test_list_unique():
    inlist = [1, 5, 6, 5, 1, 9]
    ulist = mv.unique(inlist)
    assert ulist == [1, 5, 6, 9]


def test_list_sort():
    s = [4, 7, 2, 3, 4, 9, 0]
    so = mv.sort(s)
    assert(so == [0, 2, 3, 4, 4, 7, 9])


def test_list_sort_indices():
    s = [4, 7, 2, 3, 4, 9, 0]
    soi = mv.sort_indices(s)
    assert(soi == [6, 2, 3, 0, 4, 1, 5])


def test_list_find():
    s = [4, 7, 2, 3, 4, 9, 0]
    f = mv.find(s, 2)
    assert(f == 2)
    f = mv.find(s, 4)
    assert(f == 0)
    f = mv.find(s, 4, 'all')
    assert(f == [0, 4])


def test_tuple_unique():
    intuple = (3, 2, 2, 7, 3, 1.2, 2.1, 1.2)
    ulist = mv.unique(intuple)
    assert ulist == [3, 2, 7, 1.2, 2.1]


def test_read():
    gg = mv.read({'SOURCE': file_in_testdir('test.grib'), 'GRID': 80})
    assert mv.grib_get_string(gg, 'typeOfGrid') == 'regular_gg'


def test_read_filter_1():
    mls = mv.read(source=file_in_testdir('ml_data.grib'), param='t', levelist=[5, 49, 101])
    assert(mv.grib_get_long(mls, 'level') == [5, 49, 101])


def test_read_filter_2():
    tuv_all_levs = mv.read(file_in_testdir('tuv_pl.grib'))
    u_all_levs = mv.read(data=tuv_all_levs, param='u')
    assert(mv.grib_get_long(u_all_levs, 'level') == [1000, 850, 700, 500, 400, 300])
    assert(mv.grib_get_string(u_all_levs, 'shortName') == ['u', 'u', 'u', 'u', 'u', 'u'])
    u_2levs = mv.read(data=u_all_levs, levelist=[700, 400])
    assert(mv.grib_get_long(u_2levs, 'level') == [700, 400])


def test_write():
    gg = mv.read({'SOURCE': file_in_testdir('test.grib'), 'GRID': 80})
    regridded_grib = mv.write(file_in_testdir('test_gg_grid.grib'), gg)
    assert regridded_grib == 0
    os.remove(file_in_testdir('test_gg_grid.grib'))


def test_class_():
    # these generate warnings, but if they pass then they show that the conversion
    # from class_ to class is working
    gg = mv.read(file_in_testdir('test.grib'))
    c = mv.read(data=gg, class_='od')
    assert(mv.type(c) == 'fieldset')
    c = mv.read({'data': gg, 'class_' : 'od'})
    assert(mv.type(c) == 'fieldset')
    c = mv.read({'data': gg, 'class' : 'od'})
    assert(mv.type(c) == 'fieldset')


TEST_FIELDSET = mv.read(os.path.join(PATH, 'test.grib'))


def test_type():
    out = mv.type(TEST_FIELDSET)
    assert out == 'fieldset'


# def test_retrieve():
#     tccp = mv.retrieve({
#         'levtype': 'sfc',
#         'param': 'tccp',
#         'grid': 'o640'  # octahedral grid (a specific form of a reduced Gaussian grid)
#     })
#     assert mv.type(tccp)== 'fieldset'


def test_count():
    out = mv.count(TEST_FIELDSET)
    assert out == 1


def test_maxvalue():
    maximum = mv.maxvalue(TEST_FIELDSET)
    assert np.isclose(maximum, MAX_VALUE)


def test_accumulate():
    all_missing = mv.read(file_in_testdir('all_missing_vals.grib'))
    out = mv.accumulate(all_missing)
    assert out is None


def test_add():
    plus_two = TEST_FIELDSET + 2
    maximum = mv.maxvalue(plus_two)
    assert np.isclose(maximum, MAX_VALUE + 2)


def test_add_fieldsets():
    sum = TEST_FIELDSET + TEST_FIELDSET
    maximum = mv.maxvalue(sum)
    assert np.isclose(maximum, MAX_VALUE + MAX_VALUE)


def test_sub():
    minus_two = TEST_FIELDSET - 2
    maximum = mv.maxvalue(minus_two)
    assert np.isclose(maximum, MAX_VALUE - 2)


def test_sub_fieldsets():
    sub = TEST_FIELDSET - TEST_FIELDSET
    maximum = mv.maxvalue(sub)
    assert np.isclose(maximum, 0)


def test_sqrt():
    sqrt_fd = mv.sqrt(TEST_FIELDSET)
    maximum = mv.maxvalue(sqrt_fd)
    assert np.isclose(maximum, np.sqrt(MAX_VALUE))


def test_product():
    times_two = TEST_FIELDSET * 2
    maximum = mv.maxvalue(times_two)
    assert np.isclose(maximum, MAX_VALUE * 2)


def test_product_fieldsets():
    prod = TEST_FIELDSET * TEST_FIELDSET
    maximum = mv.maxvalue(prod)
    assert np.isclose(maximum, MAX_VALUE * MAX_VALUE)


def test_division():
    divided_two = TEST_FIELDSET / 2
    maximum = mv.maxvalue(divided_two)
    assert np.isclose(maximum, MAX_VALUE / 2)


def test_division_fieldsets():
    div = TEST_FIELDSET / TEST_FIELDSET
    maximum = mv.maxvalue(div)
    assert np.isclose(maximum, 1)


def test_power():
    raised_two = TEST_FIELDSET ** 2
    maximum = mv.maxvalue(raised_two)
    assert np.isclose(maximum, MAX_VALUE ** 2)


def test_distance():
    dist = mv.distance(TEST_FIELDSET, 0, 0)
    minimum = mv.minvalue(dist)
    maximum = mv.maxvalue(dist)
    assert np.isclose(minimum, 0.0)
    assert np.isclose(maximum, SEMI_EQUATOR)


def test_valid_date_len_1():
    vd = mv.valid_date(TEST_FIELDSET)
    assert isinstance(vd, datetime.datetime)
    assert vd == datetime.datetime(2017, 4, 27, 12, 0, 0)


def test_valid_date_len_6():
    grib = mv.read(os.path.join(PATH, 't_for_xs.grib'))
    vd_grib = mv.valid_date(grib)
    assert isinstance(vd_grib[1], datetime.datetime)

    vd_ref = datetime.datetime(2017, 8, 1, 12, 0, 0)
    for vd in vd_grib:
        assert vd == vd_ref


def test_base_date():
    bd = mv.base_date(TEST_FIELDSET)
    assert isinstance(bd, datetime.datetime)
    assert bd == datetime.datetime(2017, 4, 27, 12, 0, 0)


def test_fieldset_len_1():
    flen = len(TEST_FIELDSET)
    assert(flen == 1)


def test_fieldset_len_6():
    grib = mv.read(os.path.join(PATH, 't_for_xs.grib'))
    flen = len(grib)
    assert(flen == 6)


def test_fieldset_single_index():
    grib = mv.read(os.path.join(PATH, 't_for_xs.grib'))
    grib4 = grib[3]  # 0-based indexing in Python
    assert(len(grib4) == 1)
    assert(mv.grib_get_long(grib4, 'level') == 500)


def test_fieldset_slice():
    grib = mv.read(os.path.join(PATH, 't_for_xs.grib'))
    # slice [start,stop+1,step]
    assert(mv.grib_get_long(grib[0:6:1], 'level') == [1000, 850, 700, 500, 400, 300])
    assert(mv.grib_get_long(grib[0:6:2], 'level') == [1000, 700, 400])
    assert(mv.grib_get_long(grib[4:6:1], 'level') == [400, 300])
    assert(mv.grib_get_long(grib[5:6:1], 'level') == 300)
    assert(mv.grib_get_long(grib[4:12:1], 'level') == [400, 300])
    assert(mv.grib_get_long(grib[1:6:3], 'level') == [850, 400])
    assert(mv.grib_get_long(grib[-1::], 'level') == 300)
    assert(mv.grib_get_long(grib[-1:-4:-1], 'level') == [300, 400, 500])

    grib = mv.read(os.path.join(PATH, 'tuv_pl.grib'))
    assert(mv.grib_get_long(grib[0:18:1], 'level') == [1000, 1000, 1000, 850, 850, 850,
                                                       700, 700, 700, 500, 500, 500,
                                                       400, 400, 400, 300, 300, 300])


def test_fieldset_iterator():
    grib = mv.read(os.path.join(PATH, 't_for_xs.grib'))
    avg = mv.average(grib)
    assert(len(avg) == 6)
    iteravg = []
    for f in grib:
        iteravg.append(mv.average(f))
    assert(len(iteravg) == len(avg))
    for i in range(0, 6):
        assert np.isclose(avg[i], iteravg[i])


def test_fieldset_assignment_to_field_index():
    grib = mv.read(os.path.join(PATH, 't_for_xs.grib'))
    # check numbers before assignment
    assert(np.isclose(mv.integrate(grib[0]), 290.802))
    assert(np.isclose(mv.integrate(grib[3]), 260.601))
    assert(np.isclose(mv.integrate(grib[4]), 249.617))
    # change one field and check some fields
    grib[0] = grib[0] * 10
    assert(np.isclose(mv.integrate(grib[0]), 2908.02))
    assert(np.isclose(mv.integrate(grib[3]), 260.601))
    assert(np.isclose(mv.integrate(grib[4]), 249.617))
    # another assignment
    grib[4] = grib[3] * 10
    assert(np.isclose(mv.integrate(grib[0]), 2908.02))
    assert(np.isclose(mv.integrate(grib[3]), 260.601))
    assert(np.isclose(mv.integrate(grib[4]), 2606.01))


def test_fieldset_relational_operators():
    a = mv.read(os.path.join(PATH, 'test.grib'))
    a = mv.int(a)
    assert(mv.accumulate(a > 273) == 76001)
    assert(mv.accumulate(a >= 273) == 78156)
    assert(mv.accumulate(a < 273) == 37524)
    assert(mv.accumulate(a <= 273) == 39679)


def test_fieldset_equality_operator():
    a = mv.read(os.path.join(PATH, 'test.grib'))
    v = mv.values(a)
    v[10] = -29
    v[13] = -31
    v[15] = -33
    b = a.set_values(v)
    same = (a == b)
    assert(type(same) == mv.Fieldset)
    vsame = same.values()
    assert(mv.sum(vsame) == len(vsame) - 3)  # all but 3 should be the same
    assert(vsame[5]  == 1)
    assert(vsame[10] == 0)
    assert(vsame[11] == 1)
    assert(vsame[12] == 1)
    assert(vsame[13] == 0)
    assert(vsame[14] == 1)
    assert(vsame[15] == 0)


def test_fieldset_nonequality_operator():
    a = mv.read(os.path.join(PATH, 'test.grib'))
    v = mv.values(a)
    v[10] = -29
    v[13] = -31
    v[15] = -33
    b = a.set_values(v)
    diff = (a != b)
    assert(type(diff) == mv.Fieldset)
    vdiff = diff.values()
    assert(mv.sum(vdiff) == 3)  # there should be exactly 3 differences
    assert(vdiff[5]  == 0)
    assert(vdiff[10] == 1)
    assert(vdiff[11] == 0)
    assert(vdiff[12] == 0)
    assert(vdiff[13] == 1)
    assert(vdiff[14] == 0)
    assert(vdiff[15] == 1)


def test_nearest_gridpoint_info():
    a = mv.read(os.path.join(PATH, 'test.grib'))
    ni = mv.nearest_gridpoint_info(a, 57.193, -2.360)
    ni0 = ni[0]
    assert(np.isclose(ni0['latitude'],  57.0))
    assert(np.isclose(ni0['longitude'], 357.75))
    assert(np.isclose(ni0['distance'],  22.4505))
    assert(np.isclose(ni0['value'],     282.436))
    assert(ni0['index'] == 21597)


def test_surrounding_gridpoints():
    a = mv.read(os.path.join(PATH, 'test.grib'))
    sgi = mv.surrounding_points_indexes(a, 11.552, 50.653)
    assert(np.array_equal(sgi, np.array([50468, 50467, 49988, 49987])))


def test_datainfo():
    a = mv.read(os.path.join(PATH, 'tuv_pl.grib'))
    di = mv.datainfo(a)
    di3 = di[3]
    assert(di3['index'] == 3)
    assert(di3['number_present'] == 2664)
    assert(di3['number_missing'] == 0)
    assert(di3['proportion_present'] == 1)
    assert(di3['proportion_missing'] == 0)


def test_empty_fieldset_contructor():
    f = mv.Fieldset()
    assert(type(f) == mv.Fieldset)
    assert(len(f) == 0)


def test_fieldset_contructor_with_path():
    f = mv.Fieldset(path=os.path.join(PATH, 'test.grib'))
    assert(type(f) == mv.Fieldset)
    assert(len(f) == 1)
    ni = mv.nearest_gridpoint_info(f, 57.193, -2.360)
    ni0 = ni[0]
    assert(np.isclose(ni0['latitude'],  57.0))
    assert(np.isclose(ni0['longitude'], 357.75))
    assert(np.isclose(ni0['distance'],  22.4505))
    assert(np.isclose(ni0['value'],     282.436))
    assert(ni0['index'] == 21597)


def test_fieldset_append_from_empty():
    f = mv.Fieldset()
    g = mv.read(os.path.join(PATH, 'tuv_pl.grib'))
    f.append(g[0])
    assert(type(f) == mv.Fieldset)
    assert(len(f) == 1)
    shortnames = f.grib_get_string('shortName')
    assert(shortnames == 't')
    f.append(g[1])
    assert(type(f) == mv.Fieldset)
    assert(len(f) == 2)
    shortnames = f.grib_get_string('shortName')
    assert(shortnames == ['t', 'u'])
    f.append(g[15:18])
    assert(type(f) == mv.Fieldset)
    assert(len(f) == 5)
    shortnames = f.grib_get_string('shortName')
    assert(shortnames == ['t', 'u', 't', 'u', 'v'])


def test_read_bufr():
    bufr = mv.read(file_in_testdir('obs_3day.bufr'))
    assert(mv.type(bufr) == 'observations')


def test_read_gpt():
    gpt = mv.read(file_in_testdir('t2m_3day.gpt'))
    assert(mv.type(gpt) == 'geopoints')
    assert(mv.count(gpt) == 45)


TEST_GEOPOINTS = mv.read(os.path.join(PATH, 't2m_3day.gpt'))


def test_filter_gpt():
    filter_out = TEST_GEOPOINTS.filter(TEST_GEOPOINTS >= 280)
    assert mv.type(filter_out) == 'geopoints'
    assert mv.count(filter_out) == 38


def test_sqrt_geopoints():
    sqrt_out = mv.sqrt(TEST_GEOPOINTS)
    maximum = mv.maxvalue(sqrt_out)
    assert mv.type(sqrt_out) == 'geopoints'
    assert np.isclose(maximum, MAX_SQRT_GPT)


def test_add_geopoints():
    add = TEST_GEOPOINTS + TEST_GEOPOINTS
    maximum = mv.maxvalue(add)
    assert np.isclose(maximum, MAX_GPT + MAX_GPT)


def test_prod_geopoints():
    prod = TEST_GEOPOINTS * TEST_GEOPOINTS
    maximum = mv.maxvalue(prod)
    assert np.isclose(maximum, MAX_GPT * MAX_GPT)


def test_geopoints_element():
    g1 = TEST_GEOPOINTS[0]
    assert(isinstance(g1, dict))
    assert(g1['latitude']       == 49.43)
    assert(g1['longitude']      == -2.6)
    assert(g1['height']         == 0)
    assert(g1['date']           == 20170425)
    assert(g1['time']           == 1200)
    assert(g1['value']          == 282.4)
    assert(g1['value2']         == 0)
    assert(g1['value_missing']  == 0)
    assert(g1['value2_missing'] == 0)
    g44 = TEST_GEOPOINTS[44]
    assert(isinstance(g44, dict))
    assert(g44['latitude']      == 59.53)


def test_geopoints_relational_operator():
    lt = TEST_GEOPOINTS < 1
    le = TEST_GEOPOINTS <= 1
    gt = TEST_GEOPOINTS > 100
    ge = TEST_GEOPOINTS >= 100
    assert mv.maxvalue(lt) == 0
    assert mv.maxvalue(le) == 0
    assert mv.maxvalue(gt) == 1
    assert mv.maxvalue(ge) == 1


def test_geopoints_equality_operator():
    a = mv.read(file_in_testdir('t2m_3day.gpt'))
    assert(mv.type(a) == 'geopoints')
    v = mv.values(a)
    v[10] = -29
    v[13] = -31
    v[15] = -33
    b = a.set_values(v)
    same = (a == b)
    assert(mv.type(same) == 'geopoints')
    vsame = same.values()
    assert(mv.sum(vsame) == len(vsame) - 3)  # all but 3 should be the same
    assert(vsame[5]  == 1)
    assert(vsame[10] == 0)
    assert(vsame[11] == 1)
    assert(vsame[12] == 1)
    assert(vsame[13] == 0)
    assert(vsame[14] == 1)
    assert(vsame[15] == 0)


def test_geopoints_nonequality_operator():
    a = mv.read(file_in_testdir('t2m_3day.gpt'))
    assert(mv.type(a) == 'geopoints')
    v = mv.values(a)
    v[10] = -29
    v[13] = -31
    v[15] = -33
    b = a.set_values(v)
    diff = (a != b)
    assert(mv.type(diff) == 'geopoints')
    vdiff = diff.values()
    assert(mv.sum(vdiff) == 3)  # there should be exactly 3 differences
    assert(vdiff[5]  == 0)
    assert(vdiff[10] == 1)
    assert(vdiff[11] == 0)
    assert(vdiff[12] == 0)
    assert(vdiff[13] == 1)
    assert(vdiff[14] == 0)
    assert(vdiff[15] == 1)


def test_geopoints_fieldset_operator():
    diff = TEST_FIELDSET - TEST_GEOPOINTS
    assert mv.type(diff) == 'geopoints'


def test_obsfilter():
    bufr = mv.read(file_in_testdir('obs_3day.bufr'))

    # test two styles of passing parameters
    gpt1 = mv.obsfilter({'data': bufr, 'parameter': '012004', 'output': "geopoints"})
    gpt2 = mv.obsfilter(data=bufr, parameter='012004', output="geopoints")
    assert(mv.type(gpt1) == 'geopoints')
    assert(mv.count(gpt1) == 45)
    assert(mv.type(gpt2) == 'geopoints')
    assert(mv.count(gpt2) == 45)


def test_read_gptset():
    gpts = mv.read(file_in_testdir('geopointset_1.gpts'))
    assert(mv.type(gpts) == 'geopointset')
    assert(mv.count(gpts) == 6)
    gpt1 = gpts[0]
    assert(mv.type(gpt1) == 'geopoints')
    assert(mv.count(gpt1) == 11)
    assert(mv.metadata(gpt1) is None)
    gpt2 = gpts[1]
    assert(mv.type(gpt2) == 'geopoints')
    assert(mv.count(gpt2) == 1)
    # check the metadata
    md = mv.metadata(gpt2)
    assert(isinstance(md, dict))
    assert(md['mykey1'] == 'val1')
    assert(md['mykey2'] == 5)
    # check that it is iterable
    counts = [mv.count(c) for c in gpts]
    assert(counts == [11.0, 1.0, 44.0, 11.0, 1.0, 44.0])
    # test the filtering
    bad_filter = mv.filter(gpts, {'badkey' : 7})
    assert(bad_filter is None)
    good_filter = mv.filter(gpts, {'mykey2' : 5})
    assert(mv.type(good_filter) == 'geopointset')
    assert(mv.count(good_filter) == 1)
    assert(mv.count(good_filter[0]) == 1)
    lats = good_filter[0].latitudes()
    assert(len(lats) == 1)
    assert(lats[0] == 60.82)


def test_date_year():
    npd1 = np.datetime64("2017-04-27T06:18:02")
    assert mv.year(npd1) == 2017
    npd2 = np.datetime64("2017-04-27T06:18:02.16")
    assert mv.year(npd2) == 2017

    dt1 = datetime.datetime(2017, 4, 27, 6, 18, 2)
    assert mv.year(dt1) == 2017
    dt2 = datetime.datetime(2017, 4, 27, 6, 18, 2, 16)
    assert mv.year(dt2) == 2017

    d1 = datetime.date(2017, 4, 27)
    assert mv.year(d1) == 2017


def test_date_month():
    npd1 = np.datetime64("2017-04-27T06:18:02")
    assert mv.month(npd1) == 4
    npd2 = np.datetime64("2017-04-27T06:18:02.16")
    assert mv.month(npd2) == 4

    dt1 = datetime.datetime(2017, 4, 27, 6, 18, 2)
    assert mv.month(dt1) == 4
    dt2 = datetime.datetime(2017, 4, 27, 6, 18, 2, 16)
    assert mv.month(dt2) == 4

    d1 = datetime.date(2017, 4, 27)
    assert mv.month(d1) == 4


def test_date_day():
    npd1 = np.datetime64("2017-04-27T06:18:02")
    assert mv.day(npd1) == 27
    npd2 = np.datetime64("2017-04-27T06:18:02.16")
    assert mv.day(npd2) == 27

    dt1 = datetime.datetime(2017, 4, 27, 6, 18, 2)
    assert mv.day(dt1) == 27
    dt2 = datetime.datetime(2017, 4, 27, 6, 18, 2, 16)
    assert mv.day(dt2) == 27

    d1 = datetime.date(2017, 4, 27)
    assert mv.day(d1) == 27


def test_date_hour():
    npd1 = np.datetime64("2017-04-27T06:18:02")
    assert mv.hour(npd1) == 6
    npd2 = np.datetime64("2017-04-27T06:18:02.16")
    assert mv.hour(npd2) == 6

    dt1 = datetime.datetime(2017, 4, 27, 6, 18, 2)
    assert mv.hour(dt1) == 6
    dt2 = datetime.datetime(2017, 4, 27, 6, 18, 2, 16)
    assert mv.hour(dt2) == 6

    d1 = datetime.date(2017, 4, 27)
    assert mv.hour(d1) == 0


def test_date_minute():
    npd1 = np.datetime64("2017-04-27T06:18:02")
    assert mv.minute(npd1) == 18
    npd2 = np.datetime64("2017-04-27T06:18:02.16")
    assert mv.minute(npd2) == 18

    dt1 = datetime.datetime(2017, 4, 27, 6, 18, 2)
    assert mv.minute(dt1) == 18
    dt2 = datetime.datetime(2017, 4, 27, 6, 18, 2, 16)
    assert mv.minute(dt2) == 18

    d1 = datetime.date(2017, 4, 27)
    assert mv.minute(d1) == 0


def test_date_second():
    npd1 = np.datetime64("2017-04-27T06:18:02")
    assert mv.second(npd1) == 2
    npd2 = np.datetime64("2017-04-27T06:18:02.16")
    assert mv.second(npd2) == 2

    dt1 = datetime.datetime(2017, 4, 27, 6, 18, 2)
    assert mv.second(dt1) == 2
    dt2 = datetime.datetime(2017, 4, 27, 6, 18, 2, 16)
    assert mv.second(dt2) == 2

    d1 = datetime.date(2017, 4, 27)
    assert mv.second(d1) == 0


def test_numpy_numeric_args():
    # we don't test them all here, but hopefully a representative sample
    assert(mv.call('+', np.int32(5), 1) == 6)
    assert(mv.call('+', np.int64(5), 1) == 6)
    assert(mv.call('+', np.byte(8), 1) == 9)
    assert(mv.call('+', np.uint16(8), 1) == 9)
    assert(np.isclose(mv.call('+', np.float32(5.5), 1), 6.5))
    assert(np.isclose(mv.call('+', np.float64(5.5), 1), 6.5))


def test_odb():
    if mv.is_feature_available('odb') == 0:
        print('Skipping test_odb because ODB is not enabled in this Metview version')
        return

    db = mv.read(file_in_testdir('temp_u.odb'))
    assert(mv.type(db) == 'odb')

    # assert isinstance(db,mv.Odb)
    assert(mv.count(db) == 88)

    p_val = mv.values(db, 'p')
    assert(mv.count(p_val) == 88)
    assert(np.isclose(p_val[0], 98065.578125))
    assert(np.isclose(p_val[87], 97651.2109375))

    t_val = mv.values(db, 't')
    assert(mv.count(t_val) == 88)
    assert(np.isclose(t_val[0], 144700))
    assert(np.isclose(t_val[87], 94700))

    v_val = mv.values(db, 'val')
    assert(mv.count(v_val) == 88)
    assert(np.isclose(v_val[0], -4.62306786))
    assert(np.isclose(v_val[87], -4.27525187))


def test_odb_filter():
    if mv.is_feature_available('odb') == 0:
        print('Skipping test_odb_filter because ODB is not enabled in this Metview version')
        return

    db = mv.read(file_in_testdir('temp_u.odb'))
    # assert isinstance(db,mv.Odb)
    assert(mv.count(db) == 88)

    db_res = mv.odb_filter({
        'odb_data': db,
        'odb_query': "select p, t, val where val < -8",
    })

    # assert isinstance(db_res,mv.Odb)
    assert(mv.count(db_res) == 6)
    val = mv.values(db_res, 'val')
    a = np.array([-9.11442089, -8.16880512, -8.07200909, -8.06602955, -8.49743557, -8.21722794])
    np.testing.assert_allclose(val, a)


def test_odb_to_dataframe_1():
    if mv.is_feature_available('odb') == 0:
        print('Skipping test_odb because ODB is not enabled in this Metview version')
        return

    db = mv.read(file_in_testdir('temp_u.odb'))
    assert(mv.type(db) == 'odb')

    df = db.to_dataframe()
    assert(isinstance(df, pd.DataFrame))

    assert(df.shape == (88, 3))
    dt1_loc = df.iloc[0]['p']
    assert(np.isclose(dt1_loc, 98065.6))
    dt1_loc = df.iloc[5]['t']
    assert(np.isclose(dt1_loc, 144700))
    dt1_loc = df.iloc[50]['t']
    assert(np.isclose(dt1_loc, 103200))
    dt1_loc = df.iloc[29]['val']
    assert(np.isclose(dt1_loc, -6.06863))
    dt1_loc = df.iloc[87]['val']
    assert(np.isclose(dt1_loc, -4.27525))


# test an ODB that has strings
def test_odb_to_dataframe_2():
    if mv.is_feature_available('odb') == 0:
        print('Skipping test_odb because ODB is not enabled in this Metview version')
        return

    db = mv.read(file_in_testdir('small_odb.odb'))
    assert(mv.type(db) == 'odb')

    df = db.to_dataframe()
    assert(isinstance(df, pd.DataFrame))

    assert(df.shape == (273, 54))
    dt1_loc = df.iloc[0]['an_depar@body']
    assert(np.isclose(dt1_loc, -0.123831))
    dt1_loc = df.iloc[0]['class@desc']
    assert(dt1_loc.strip() == 'rd')      # strings from ODB are padded with spaces
    dt1_loc = df.iloc[20]['expver@desc']
    assert(dt1_loc.strip() == 'fgww')    # strings from ODB are padded with spaces
    dt1_loc = df.iloc[20]['sensor@hdr']  # test a constant integer field
    assert(dt1_loc == 3)


# this tests the calling of the Cross Section module, but also the
# return of netCDF data and also that we can perform operations on it
# as input and output
def test_cross_section_data():
    grib = mv.read(os.path.join(PATH, 't_for_xs.grib'))
    xs_data = mv.mcross_sect(
        line=[59.9, -180, -13.5, 158.08],
        data=grib,
    )
    # the result of this should be a netCDF variable
    assert mv.type(xs_data) == 'netcdf'
    mv.setcurrent(xs_data, 't')
    assert mv.dimension_names(xs_data) == ['time', 'nlev', 'lon']
    assert np.isclose(mv.value(xs_data, 0), 230.39156)
    xs_data_x2 = xs_data * 2
    assert np.isclose(mv.value(xs_data_x2, 0), 460.7831)


def test_netcdf_var_indexing():
    nc = mv.read(file_in_testdir('xs_date_mv5.nc'))
    mv.setcurrent(nc, 0)
    assert(mv.attributes(nc)['long_name'] == "time")
    mv.setcurrent(nc, 1)
    assert(mv.attributes(nc)['long_name'] == "latitude")
    mv.setcurrent(nc, 4)
    assert(mv.attributes(nc)['long_name'] == "Temperature")


def test_netcdf_single_value():
    nc = mv.read(file_in_testdir('xs_date_mv5.nc'))
    mv.setcurrent(nc, 't')
    assert(mv.attributes(nc)['long_name'] == "Temperature")
    assert(np.isclose(mv.value(nc, 0), 234.7144))
    assert(np.isclose(mv.value(nc, 4), 237.4377))


def test_netcdf_multi_indexed_values():
    nc = mv.read(file_in_testdir('xs_date_mv5.nc'))
    mv.setcurrent(nc, 't')
    assert(mv.attributes(nc)['long_name'] == "Temperature")
    assert(np.isclose(mv.values(nc, [0, 0, 0]), 234.7144))
    assert(np.isclose(mv.values(nc, [0, 0, 4]), 237.4377))
    assert(np.isclose(mv.values(nc, [0, 1, 0]), 248.7220))
    assert(np.isclose(mv.values(nc, [0, 1, 1]), 249.3030))


def test_netcdf_multi_indexed_values_with_all():
    nc = mv.read(file_in_testdir('xs_date_mv5.nc'))
    mv.setcurrent(nc, 't')
    assert(mv.attributes(nc)['long_name'] == "Temperature")
    v = mv.values(nc, [0, 0, 'all'])
    assert(len(v) == 64)
    assert(np.isclose(v[0],  234.714))
    assert(np.isclose(v[63], 258.979))
    v = mv.values(nc, [0, 'all', 0])
    assert(len(v) == 5)
    assert(np.isclose(v[0], 234.714))
    assert(np.isclose(v[4], 260.484))


def test_netcdf_to_dataset():
    nc = mv.read(file_in_testdir('xs_date_mv5.nc'))
    x = nc.to_dataset()
    assert(isinstance(x, xr.core.dataset.Dataset))
    assert(isinstance(x['t'], xr.DataArray))


@pytest.mark.filterwarnings("ignore:GRIB write")
def test_dataset_to_fieldset():
    grib = mv.read(file_in_testdir('t_for_xs.grib'))
    x = grib.to_dataset()
    f = mv.dataset_to_fieldset(x)
    assert(mv.type(f) == 'fieldset')
    assert(len(f) == 6)


@pytest.mark.filterwarnings("ignore:GRIB write")
def test_pass_dataset_as_arg():
    grib = mv.read(file_in_testdir('t_for_xs.grib'))
    x = grib.to_dataset()
    fs = mv.mean(x * 2)  # *2 is done by xarray, mean is done by Metview
    assert(mv.type(fs) == 'fieldset')
    assert(len(fs) == 1)


def test_strings():
    sentence = "Hello this is a sentence with many many words"
    sthis = mv.search(sentence, "this")
    assert(sthis == 6)


@pytest.mark.skip()
def test_met_plot():
    contour = mv.mcont({
        'CONTOUR_LINE_COLOUR': 'PURPLE',
        'CONTOUR_LINE_THICKNESS': 3,
        'CONTOUR_HIGHLIGHT': False
    })
    coast = mv.mcoast({'MAP_COASTLINE_LAND_SHADE': True})
    bindings.met_plot(TEST_FIELDSET, contour, coast)


def test_plot_1():
    output_name = file_in_testdir('test_plot_1')
    mv.setoutput(mv.png_output(output_name=output_name))
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
    degraded_field = mv.read(data=TEST_FIELDSET, grid=[4, 4])
    mv.plot(degraded_field, mv.mcont(grid_shade))
    output_name_from_magics = output_name + '.1.png'
    assert(os.path.isfile(output_name_from_magics))
    os.remove(output_name_from_magics)


def test_plot_2():
    output_name = file_in_testdir('test_plot_2')
    png = mv.png_output(output_name=output_name)
    grid_shade = {
        'legend': True,
        'contour': False,
        'contour_highlight': True,
        'contour_shade': True,
        'contour_shade_technique': 'grid_shading',
        'contour_shade_max_level_colour': 'olive',
        'contour_shade_min_level_colour': 'blue',
        'contour_shade_colour_direction': 'clockwise',
    }
    degraded_field = mv.read(data=TEST_FIELDSET, grid=[4, 4])
    mv.plot(png, degraded_field, mv.mcont(grid_shade))
    output_name_from_magics = output_name + '.1.png'
    assert(os.path.isfile(output_name_from_magics))
    os.remove(output_name_from_magics)


@pytest.mark.skip()
def test_plot_3():
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
    bindings.plot(TEST_FIELDSET, grid_shade, **png_output)
    os.remove(file_in_testdir('test_plot.1.png'))


def test_plot_2_pages():
    output_name = file_in_testdir('test_plot_2_pages')
    png = mv.png_output(output_name=output_name)
    degraded_field = mv.read(data=TEST_FIELDSET, grid=[4, 4])
    page1 = mv.plot_page(top=2.2, bottom=52.2, right=100)
    page2 = mv.plot_page(top=50)
    dw = mv.plot_superpage(pages=[page1, page2])
    mv.setoutput(png)
    mv.plot(dw[0], degraded_field, dw[1], degraded_field + 50)
    output_name_from_magics = output_name + '.1.png'
    assert(os.path.isfile(output_name_from_magics))
    os.remove(output_name_from_magics)


def test_macro_error():
    with pytest.raises(Exception):
        TEST_FIELDSET[125]


def test_value_file_path():
    p = TEST_FIELDSET + 1  # this will force Metview to write a new temporary file
    assert(p.url() != "")
    assert(os.path.isfile(p.url()))


@pytest.mark.parametrize('file_name', [
    'ml_data.grib',
    't2m_3day.gpt',
])
def test_temporary_file_deletion(file_name):
    g = mv.read(file_in_testdir(file_name))
    h = g + 1  # this will force Metview to write a new temporary file
    temp_filepath = h.url()
    assert(temp_filepath != "")  # file should exist right now
    assert(os.path.isfile(temp_filepath))  # file should exist right now
    h = 0  # this should force deletion of the variable
    # here we make the assumption that the system has not created
    # another temporary file with the same name between object
    # deletion and the following test for the file
    assert(not(os.path.isfile(temp_filepath)))


def test_mvl_ml2hPa():
    ml_data = mv.read(file_in_testdir('ml_data.grib'))
    assert mv.type(ml_data) == 'fieldset'
    ml_t = mv.read(data=ml_data, param='t')
    ml_lnsp = mv.read(data=ml_data, param='lnsp')
    desired_pls = [1000, 900, 850, 500, 300, 100, 10, 1, 0.8, 0.5, 0.3, 0.1]
    pl_data = mv.mvl_ml2hPa(ml_lnsp, ml_t, desired_pls)
    assert mv.type(pl_data) == 'fieldset'
    pls = mv.grib_get_long(pl_data, 'level')
    lev_types = mv.grib_get_string(pl_data, 'typeOfLevel')
    lev_divisors = [1 if x == 'isobaricInhPa' else 100 for x in lev_types]
    pl_in_hpa = [a / b for a, b in zip(pls, lev_divisors)]
    assert(pl_in_hpa == desired_pls)


def test_push_nil():
    n = mv.nil()
    assert(n is None)
    assert(mv.type(n) == 'nil')


def test_simple_get_vector():
    a = [5, 6, 7, 8, 9]
    v = mv.vector(a)
    assert(isinstance(v, np.ndarray))
    assert(len(v) == 5)
    assert(v[1] == 6)
    assert(v.dtype == np.dtype('float64'))


def test_simple_get_vector_float32():
    if supports_float32_vectors():
        mv.vector_set_default_type('float32')
        a = [5, 6, 7, 8, 9]
        v = mv.vector(a)
        assert(isinstance(v, np.ndarray))
        assert(len(v) == 5)
        assert(v[1] == 6)
        assert(v.dtype == np.dtype('float32'))
        mv.vector_set_default_type('float64')  # reset to default type for the other tests


def test_get_vector_from_grib():
    v = mv.values(TEST_FIELDSET[0])
    assert(isinstance(v, np.ndarray))
    assert(v.dtype == np.dtype('float64'))
    assert(len(v) == 115680)
    assert(np.isclose(min(v), 206.93560791))
    assert(np.isclose(max(v), 316.06060791))


def test_get_vector_float32_from_grib():
    if supports_float32_vectors():
        mv.vector_set_default_type('float32')
        v = mv.values(TEST_FIELDSET[0])
        assert(isinstance(v, np.ndarray))
        assert(v.dtype == np.dtype('float32'))
        assert(len(v) == 115680)
        assert(np.isclose(min(v), 206.93560791))
        assert(np.isclose(max(v), 316.06060791))
        mv.vector_set_default_type('float64')  # reset to default type for the other tests


def test_get_vector_from_multi_field_grib():
    g = mv.read(os.path.join(PATH, 't_for_xs.grib'))
    v = mv.values(g)
    assert(isinstance(v, np.ndarray))
    assert(v.shape == (6, 2664))


def test_vector_sort():
    v1 = np.array([5, 3, 4, 9, 1, 4.2])
    vsortasc = mv.sort(v1)
    assert(np.array_equal(vsortasc, np.array([1, 3, 4, 4.2, 5, 9])))


def test_vector_sort_indices():
    v1 = np.array([5, 3, 4, 9, 1, 4.2])
    vsortindasc = mv.sort_indices(v1)
    assert(np.array_equal(vsortindasc, np.array([4, 1, 2, 5, 0, 3])))


def test_vector_find():
    s = np.array([4, 7, 2, 3, 4, 9, 0], dtype=np.float64)
    f = mv.find(s, 2)
    assert(f == 2)
    f = mv.find(s, 4)
    assert(f == 0)
    f = mv.find(s, 4, 'all')
    assert(np.array_equal(f, np.array([0, 4], dtype=np.float64)))


def test_set_vector_from_numpy_array():
    r = np.arange(1, 21, dtype=np.float64)
    assert(mv.type(r) == 'vector')
    assert(mv.dtype(r) == 'float64')
    assert(mv.count(r) == 20)
    assert(mv.maxvalue(r) == 20)


def test_set_vector_float32_from_numpy_array():
    if supports_float32_vectors():
        r = np.arange(1, 21, dtype=np.float32)
        assert(mv.type(r) == 'vector')
        assert(mv.dtype(r) == 'float32')
        assert(mv.count(r) == 20)
        assert(mv.maxvalue(r) == 20)


def test_simple_vector_with_nans():
    a = np.array([1, np.nan, 2, 3])
    n = -a
    assert(mv.count(a) == 4)
    assert(mv.sum(a) == 6)  # missing vals Python->Macro
    # seems that comparing numPy arrays that have NaNs in them is not
    # so straightforward, but this works:
    np.testing.assert_array_equal(mv.neg(a), n)  # missing vals Macro->Python


def test_zero_length_vector_from_numpy():
    a = np.array([])
    assert(mv.type(a) == 'vector')
    assert(mv.count(a) == 0)


def test_numpy_array_from_zero_length_vector():
    v = mv.vector(0)
    assert(isinstance(v, np.ndarray))
    assert(len(v) == 0)


def test_oo_interface_on_fieldsets():
    fs = mv.read(os.path.join(PATH, 't_for_xs.grib'))
    assert(np.isclose(fs.maxvalue(), 320.434))
    assert(np.isclose(fs[2].nearest_gridpoint(10, 20), 282.697))


def test_oo_interface_on_geopoints():
    gpt = mv.read(file_in_testdir('t2m_3day.gpt'))
    assert(gpt.count() == 45)
    assert(np.isclose(gpt.mean(), 281.247))


def test_std_gpts_to_dataframe():
    gpt = mv.read(file_in_testdir('t2m_3day.gpt'))
    df = gpt.to_dataframe()
    print(df)
    assert(isinstance(df, pd.DataFrame))
    assert(df.shape == (45, 5))
    # dt1_iloc = df.iloc[0][0]
    dt1_iloc = df.iloc[0]['latitude']
    assert(isinstance(dt1_iloc, float))
    assert(np.isclose(dt1_iloc, 49.43))
    # dt2_iloc = df.iloc[0][4]
    dt2_iloc = df.iloc[0]['date']
    assert(isinstance(dt2_iloc, datetime.datetime))
    dt3_loc = df.iloc[0]['date']
    assert(isinstance(dt3_loc, datetime.datetime))
    assert(dt3_loc == datetime.datetime(2017, 4, 25, 12, 0, 0))
    assert(df.loc[5]['latitude'] == 51.15)
    assert(df.loc[25]['longitude'] == 2.65)
    assert(df.loc[8]['level'] == 0)
    assert(np.isclose(df.loc[4]['value'], 281.2))


def test_xy_vector_gpts_to_dataframe():
    gpt = mv.read(file_in_testdir('uv.gpt'))
    df = gpt.to_dataframe()
    assert(isinstance(df, pd.DataFrame))
    assert(df.shape == (39, 6))
    # dt1_iloc = df.iloc[0][0]
    dt1_iloc = df.iloc[0]['latitude']
    assert(isinstance(dt1_iloc, float))
    assert(np.isclose(dt1_iloc, 70.0))
    # dt2_iloc = df.iloc[0][4]
    # assert(isinstance(dt2_iloc, datetime.datetime))
    dt3_loc = df.iloc[0]['date']
    assert(isinstance(dt3_loc, datetime.datetime))
    assert(dt3_loc == datetime.datetime(2018, 5, 14, 12, 0, 0))
    assert(df.loc[5]['latitude'] == 70)
    assert(df.loc[25]['longitude'] == 30)
    assert(df.loc[8]['level'] == 500)
    assert(np.isclose(df.loc[4]['x-comp'], -10.865656))
    assert(np.isclose(df.loc[4]['y-comp'], 17.589124))


def test_xyv_gpts_to_dataframe():
    gpt = mv.read(file_in_testdir('xyv.gpt'))
    df = gpt.to_dataframe()
    assert(isinstance(df, pd.DataFrame))
    assert(df.shape == (60, 3))
    assert(df.loc[5]['latitude'] == 70)
    assert(df.loc[25]['longitude'] == 20)
    assert(np.isclose(df.loc[4]['value'], -10.8656))


def test_grib_to_dataset():
    grib = mv.read(file_in_testdir('t_for_xs.grib'))
    x = grib.to_dataset()
    assert(isinstance(x, xr.core.dataset.Dataset))
    assert(isinstance(x['t'], xr.DataArray))


def test_read_filter_to_dataset():
    tuv_all_levs = mv.read(file_in_testdir('tuv_pl.grib'))
    u_all_levs = mv.read(data=tuv_all_levs, param='u')
    assert(mv.grib_get_long(u_all_levs, 'level') == [1000, 850, 700, 500, 400, 300])
    assert(mv.grib_get_string(u_all_levs, 'shortName') == ['u', 'u', 'u', 'u', 'u', 'u'])
    x = u_all_levs.to_dataset()
    x_keys = x.keys()
    assert('u' in x_keys)      # only 'u' should be there
    assert('v' not in x_keys)  # only 'u' should be there
    assert('t' not in x_keys)  # only 'u' should be there


@pytest.mark.xfail()
def test_table():
    # test csv with metadata
    db = mv.read_table(
        table_filename=file_in_testdir('sample_metadata.csv'),
        table_delimiter=' ',
        table_combine_delimiters='on',
        table_header_row=2,
        table_meta_data_rows=1
    )
    assert(db.type() == 'table')
    assert(db.count() == 9)
    assert(db.name(3) == "LATIT")
    assert(len(db.metadata_keys()) == 16)
    assert(db.metadata_value('integration') == 'PETTERSSEN')
    v = db.values(0)
    assert(isinstance(v, np.ndarray))
    assert(len(v) == 7)
    assert(np.array_equal(v, np.array([0, 3600, 7200, 10800, 14400, 18000, 21600])))
    v = db.values(4)
    assert(isinstance(v, np.ndarray))
    assert(len(v) == 7)
    assert(np.array_equal(v, np.array([963.5, 964.1, 964.0, 963.3, 961.8, 960.3, 959.0])))

    # test csv with no metadata
    db = mv.read(file_in_testdir('sample.csv'))
    assert(db.type() == 'table')
    assert(db.count() == 4)
    assert(db.name(2) == "h2")
    v = db.values(2)
    assert(isinstance(v, np.ndarray))
    assert(len(v) == 6)
    assert(np.array_equal(v, np.array([4, 5, 6, 7, 8, 9])))


def test_flextra():
    flx = mv.read(file_in_testdir('flextra_output.txt'))
    assert(flx.type() == 'definition')
    trNum = int(mv.flextra_group_get(flx, "trNum"))
    assert(trNum == 5)

    startLst = ['03:00:00', '06:00:00', '09:00:00', '12:00:00', '15:00:00']
    stopIndexLst = [1, 1, 1, 1, 1]
    for i in range(trNum):
        vals = mv.flextra_tr_get(flx, i, ["startTime", "stopIndex"])
        assert(len(vals) == 2)
        assert(vals[0] == startLst[i])
        assert(int(vals[1]) == stopIndexLst[i])

    # Read data for the first trajectory
    vals = mv.flextra_tr_get(flx, 0, ["lat", "lon", "date"])
    assert(len(vals) == 3)
    assert(vals[0].size == 25)
    assert(vals[1].size == 25)
    assert(len(vals[2]) == 25)
    assert(isinstance(vals[0], np.ndarray))
    assert(isinstance(vals[1], np.ndarray))
    assert(isinstance(vals[2], list))
    assert(np.isclose(vals[0].mean(), 63.369828))
    assert(np.isclose(vals[0].std(), 2.2269590))
    assert(np.isclose(vals[1].mean(), 18.014544))
    assert(np.isclose(vals[1].std(), 14.98830786689625))
    assert(vals[2][0] == datetime.datetime(2012, 1, 11, 3, 0, 0))
