# (C) Copyright 2017- ECMWF.
#
# This software is licensed under the terms of the Apache Licence Version 2.0
# which can be obtained at http://www.apache.org/licenses/LICENSE-2.0.
#
# In applying this licence, ECMWF does not waive the privileges and immunities
# granted to it by virtue of its status as an intergovernmental organisation
# nor does it submit to any jurisdiction.

import os

from metview import bindings


PATH = os.path.dirname(__file__)
MAX_VALUE = 316.06060791015625
SEMI_EQUATOR = 20001600.0
MAX_SQRT_GPT = 16.867127793433
MAX_GPT = 284.5


def file_in_testdir(filename):
    return os.path.join(PATH, filename)


def test_push_number():
    bindings.lib.p_push_number(5)
    bindings.lib.p_push_number(4)


def test_dict_to_pushed_request():
    dict = {
        "param1": True,
        "param2": False,
        "param3": 10,
        "param4": 10.5,
        "param5": "metview",
        "param6": ["1", "2", "3"],
    }
    bindings.dict_to_pushed_args(dict)


def test_bind_functions():
    namespace = {}

    bindings.bind_functions(namespace, module_name="metview")
    result = namespace["dictionary"]

    assert "dictionary" in namespace
    assert result.__name__ == result.__qualname__ == "dictionary"
    assert result.__module__ == "metview"


def test_lists_as_input():
    my_list = [1, 5, 6]
    assert bindings.count(my_list) == 3


def test_tuples_as_input():
    my_tuple = [1, 0, 5, 6]
    assert bindings.count(my_tuple) == 4
