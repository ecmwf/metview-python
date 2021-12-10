# (C) Copyright 2017- ECMWF.
#
# This software is licensed under the terms of the Apache Licence Version 2.0
# which can be obtained at http://www.apache.org/licenses/LICENSE-2.0.
#
# In applying this licence, ECMWF does not waive the privileges and immunities
# granted to it by virtue of its status as an intergovernmental organisation
# nor does it submit to any jurisdiction.
#

import datetime

from metviewpy import utils


def test_utils_date():

    d = utils.date_from_str("20210204")
    assert d == datetime.datetime(2021, 2, 4)

    d = utils.date_from_str("2021-02-04")
    assert d == datetime.datetime(2021, 2, 4)

    d = utils.date_from_str("2021-02-04 06")
    assert d == datetime.datetime(2021, 2, 4, 6, 0, 0)

    d = utils.date_from_str("2021-02-04 06:14")
    assert d == datetime.datetime(2021, 2, 4, 6, 14, 0)

    d = utils.date_from_str("2021-02-04 06:14:32")
    assert d == datetime.datetime(2021, 2, 4, 6, 14, 32)

    d = utils.date_from_str("20210204.25")
    assert d == datetime.datetime(2021, 2, 4, 6, 0, 0)


def test_utils_time():

    d = utils.time_from_str("6")
    assert d == datetime.time(6, 0, 0)

    d = utils.time_from_str("06")
    assert d == datetime.time(6, 0, 0)

    d = utils.time_from_str("14")
    assert d == datetime.time(14, 0, 0)

    d = utils.time_from_str("600")
    assert d == datetime.time(6, 0, 0)

    d = utils.time_from_str("612")
    assert d == datetime.time(6, 12, 0)

    d = utils.time_from_str("1100")
    assert d == datetime.time(11, 0, 0)

    d = utils.time_from_str("1457")
    assert d == datetime.time(14, 57, 0)

    d = utils.time_from_str("6:12")
    assert d == datetime.time(6, 12, 0)

    d = utils.time_from_str("06:12")
    assert d == datetime.time(6, 12, 0)

    d = utils.time_from_str("14:57")
    assert d == datetime.time(14, 57, 0)


def test_has_globbing():

    assert utils.has_globbing("a*") == True
    assert utils.has_globbing("a?") == True
    assert utils.has_globbing("my_path/a*.grib") == True
    assert utils.has_globbing("my_path/[Aa].grib") == True
    assert utils.has_globbing("my_path/[a-m].grib") == True
    assert utils.has_globbing("my_path/test.grib") == False
    assert utils.has_globbing("my_path/te[st.grib") == False
    assert utils.has_globbing("my_path/tes]t.grib") == False
    # assert utils.has_globbing("my_path/t]e[st.grib") == False
