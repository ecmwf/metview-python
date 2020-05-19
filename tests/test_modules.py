# Copyright 2017- European Centre for Medium-Range Weather Forecasts (ECMWF).
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import textwrap

import pytest

from metview import modules


def test_check_keys_invalid_key():
    valid_keys = {"key1", "key2", "key3"}
    mandatory_keys = {"key1", "key2"}
    actual_keys = {"key1", "key2", "key4"}

    with pytest.raises(ValueError):
        modules.check_keys(valid_keys, mandatory_keys, actual_keys)


def test_check_keys_no_mandatory_key():
    valid_keys = {"key1", "key2", "key3"}
    mandatory_keys = {"key1", "key2"}
    actual_keys = {"key1", "key3"}

    with pytest.raises(ValueError):
        modules.check_keys(valid_keys, mandatory_keys, actual_keys)


def test_check_keys():
    valid_keys = {"key1", "key2", "key3"}
    mandatory_keys = {"key1", "key2"}
    actual_keys = {"key1", "key2"}

    assert modules.check_keys(valid_keys, mandatory_keys, actual_keys) is None


def test_option_to_stream():
    key = "dummy"
    content = {
        "type": "option",
        "values": ["value1", "value2"],
        "default": "value2"
    }
    prefix = " " * 100
    option_stream = modules.option_to_stream(key, content, prefix)
    exp_stream = f"{key.upper()}\n{{\n"
    exp_stream += prefix + f"{content['values'][0].upper()}\n"
    exp_stream += prefix + f"{content['values'][1].upper()}\n}} = {content['default'].upper()}\n"

    assert option_stream == exp_stream


def test_option_to_stream_2():
    key = "contour_highlight_thickness"
    content = {
        "type": "option",
        "values": ["*"],
        "default": 3
    }
    prefix = " " * 2
    option_stream = modules.option_to_stream(key, content, prefix)
    exp_stream = f"{key.upper()}\n{{\n"
    exp_stream += prefix + f"{content['values'][0].upper()}\n}} = 3\n"

    assert option_stream == exp_stream


def test_option_to_stream_3():
    key = "contour_level_selection_type"
    content = {
        "type": "option",
        "values": ["count", "interval", "level_list"],
        "default": "count"
    }
    prefix = " " * 2
    option_stream = modules.option_to_stream(key, content, prefix)
    exp_stream = f"{key.upper()}\n{{\n"
    exp_stream += prefix + f"{content['values'][0].upper()}\n"
    exp_stream += prefix + f"{content['values'][1].upper()}\n"
    exp_stream += prefix + f"{content['values'][2].upper()}\n}} = {content['default'].upper()}\n"

    assert option_stream == exp_stream


def test_param_to_stream():
    param = {"param1":  {"type": "type1"}}
    prefix = " " * 2
    param_stream = modules.param_to_stream(param, prefix)
    exp_stream = "PARAM1\n  [ interface = icon, class = TYPE1 ]\n{ @ }\n"

    assert param_stream == exp_stream


def test_param_to_stream_option():
    param = {
        "param1":  {
            "type": "option",
            "values": ["value1", "value2"],
            "default": "value2"
        }
    }
    prefix = " " * 2
    param_stream = modules.param_to_stream(param, prefix)
    exp_stream = "PARAM1\n{\n  VALUE1\n  VALUE2\n} = VALUE2\n"

    assert param_stream == exp_stream


def test_translate_definition(tmpdir):
    definition_content = """
        "class": "dummy_class"
        "params":
            - "param1":
                "type": "option"
                "values":
                    - "value1"
                    - "value2"
                "default": "value2"
            - "param2":
                "type": "type2"
    """
    definition_path = tmpdir.join("definition.yml")
    with open(definition_path, "w") as f:
        f.write(definition_content)

    definition_stream = modules.translate_definition(definition_path)
    exp_stream = "DUMMY_CLASS\n{\n"
    exp_stream += textwrap.indent("PARAM1\n{\n  VALUE1\n  VALUE2\n} = VALUE2\n\n", "  ")
    exp_stream += textwrap.indent("PARAM2\n  [ interface = icon, class = TYPE2 ]\n{ @ }\n", "  ")
    exp_stream += "}"

    assert definition_stream == exp_stream
