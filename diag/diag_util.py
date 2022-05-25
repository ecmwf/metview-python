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

import metview as mv
from metview.metviewpy import utils

PATH = os.path.dirname(__file__)
DATA_PATH = os.path.join(PATH, "data")

# Generated test files
TEST_FILE_1 = "tq_ml137_01x01.grib"
TEST_FILE_2 = "t_20_01x01.grib"
TEST_FILE_3 = "z_ml137_01x01.grib"
TEST_FILE_4 = "uv_20_01x01.grib"
TEST_FILE_5 = "u_20_01x01.grib"
TEST_FILE_6 = "v_20_01x01.grib"


def get_test_data(filename):
    d_path = DATA_PATH
    os.makedirs(d_path, mode=0o755, exist_ok=True)
    f_path = os.path.join(d_path, filename)
    if not os.path.exists(f_path):
        URL = "https://get.ecmwf.int/repository/test-data/metview/tests"
        utils.simple_download(url=f"{URL}/{filename}", target=f_path)
    return f_path


def prepare_data():
    f_path = os.path.join(DATA_PATH, TEST_FILE_1)
    if not os.path.exists(f_path):
        print(f" Preparing data file: {TEST_FILE_1}")
        f = mv.read(get_test_data("tq_ml137.grib"))
        r = mv.read(data=f, grid=[0.1, 0.1])
        mv.write(f_path, r)

    f_path = os.path.join(DATA_PATH, TEST_FILE_2)
    if not os.path.exists(f_path):
        print(f" Preparing data file: {TEST_FILE_2}")
        f = mv.read(os.path.join(DATA_PATH, TEST_FILE_1))
        r = f.select(shortName="t")[-20:]
        mv.write(f_path, r)

    f_path = os.path.join(DATA_PATH, TEST_FILE_3)
    if not os.path.exists(f_path):
        print(f" Preparing data file: {TEST_FILE_3}")
        f = mv.read(get_test_data("z_ml137_5x5.grib"))
        r = mv.read(data=f, grid=[0.1, 0.1])
        mv.write(f_path, r)

    f_path = os.path.join(DATA_PATH, TEST_FILE_4)
    if not os.path.exists(f_path):
        print(f" Preparing data file: {TEST_FILE_4}")
        f = mv.read(get_test_data("uv_ml_5x5.grib"))
        r = mv.read(data=f, grid=[0.1, 0.1])
        mv.write(f_path, r)

    f_path = os.path.join(DATA_PATH, TEST_FILE_5)
    if not os.path.exists(f_path):
        print(f" Preparing data file: {TEST_FILE_5}")
        f = mv.read(os.path.join(DATA_PATH, TEST_FILE_4))
        r = f.select(shortName="u")
        mv.write(f_path, r)

    f_path = os.path.join(DATA_PATH, TEST_FILE_6)
    if not os.path.exists(f_path):
        print(f" Preparing data file: {TEST_FILE_5}")
        f = mv.read(os.path.join(DATA_PATH, TEST_FILE_4))
        r = f.select(shortName="v")
        mv.write(f_path, r)


def get_data(name):
    prepare_data()
    return mv.read(os.path.join(DATA_PATH, name))
