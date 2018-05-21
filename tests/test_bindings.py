
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
        'param1': True,
        'param2': False,
        'param3': 10,
        'param4': 10.5,
        'param5': 'metview',
        'param6': ['1', '2', '3']
    }
    bindings.dict_to_pushed_args(dict)


def test_bind_functions():
    namespace = {}

    bindings.bind_functions(namespace, module_name='metview')
    result = namespace['dictionary']

    assert 'dictionary' in namespace
    assert result.__name__ == result.__qualname__ == 'dictionary'
    assert result.__module__ == 'metview'


def test_lists_as_input():
    my_list = [1, 5, 6]
    assert bindings.count(my_list) == 3


def test_tuples_as_input():
    my_tuple = [1, 0, 5, 6]
    assert bindings.count(my_tuple) == 4


TEST_FIELDSET = bindings.read(os.path.join(PATH, 'test.grib'))


def test_mf_function_caller():
    info = bindings.mf.nearest_gridpoint_info(TEST_FIELDSET[0], 10, 20)
    assert(isinstance(info, list))
    info0 = info[0]
    print(info0)
    assert(isinstance(info0, dict))
    assert(info0['latitude'] == 9.75)
    assert(info0['longitude'] == 20.25)
    assert(info0['index'] == 51388)
