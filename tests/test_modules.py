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


def test_option_to_stream_invalid_type():
    key = "dummy"
    content = {
        "type": "option",
        "values": ["value1", 3],
        "default": "value2"
    }
    with pytest.raises(ValueError):
        modules.option_to_stream(key, content, " " * 2)


def test_option_to_stream():
    key = "dummy"
    content = {
        "type": "option",
        "values": ["value1", "value2"],
        "default": "value2"
    }
    prefix = " " * 2
    option_stream = modules.option_to_stream(key, content, prefix)
    exp_stream = f"{key.upper()}\n{{\n"
    exp_stream += prefix + f"{content['values'][0].upper()}; {content['values'][0].upper()}\n"
    exp_stream += prefix + f"{content['values'][1].upper()}; {content['values'][1].upper()}\n"
    exp_stream += f"}} = {content['default'].upper()}\n"

    assert option_stream == exp_stream


def test_type_to_stream_number():
    key = 'dummy_key'
    content = {
        "type": "number",
        "list": False,
    }
    prefix = " " * 2
    type_stream = modules.type_to_stream(key, content, prefix)
    exp_stream = """
        DUMMY_KEY
        {
          *
        } = ''
    """

    assert type_stream == textwrap.dedent(exp_stream.strip("\n"))


def test_type_to_stream_numbers_list():
    key = 'dummy_key'
    content = {
        "type": "number",
        "list": True,
    }
    prefix = " " * 2
    type_stream = modules.type_to_stream(key, content, prefix)
    exp_stream = """
        DUMMY_KEY
        {
          *
          /
        } = ''
    """

    assert type_stream == textwrap.dedent(exp_stream.strip("\n"))


def test_type_to_stream_string():
    key = 'dummy_key'
    content = {
        "type": "string",
        "list": False,
    }
    prefix = " " * 2
    type_stream = modules.type_to_stream(key, content, prefix)
    exp_stream = """
        DUMMY_KEY
        {
          @
        } = ''
    """

    assert type_stream == textwrap.dedent(exp_stream.strip("\n"))


def test_type_to_stream_strings_list():
    key = 'dummy_key'
    content = {
        "type": "string",
        "list": True,
    }
    prefix = " " * 2
    type_stream = modules.type_to_stream(key, content, prefix)
    exp_stream = """
        DUMMY_KEY
        {
          @
          /
        } = ''
    """

    assert type_stream == textwrap.dedent(exp_stream.strip("\n"))


def test_type_to_stream_with_help():
    key = 'dummy_key'
    content = {
        "type": "string",
        "list": True,
        "help": "dummy_help",
        "interface": "dummy_interface",
    }
    prefix = " " * 2
    type_stream = modules.type_to_stream(key, content, prefix)
    exp_stream = """
        DUMMY_KEY [ help = dummy_help,interface = dummy_interface ]
        {
          @
          /
        } = ''
    """

    assert type_stream == textwrap.dedent(exp_stream.strip("\n"))


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
    exp_stream = """
        PARAM1
        {
          VALUE1; VALUE1
          VALUE2; VALUE2
        } = VALUE2
    """

    assert param_stream == textwrap.dedent(exp_stream.strip("\n"))


def test_param_to_stream_number():
    param = {
        "contour_highlight_thickness": {
            "type": "number",
            "default": 3
        }
    }
    prefix = " " * 2
    option_stream = modules.param_to_stream(param, prefix)
    exp_stream = """
        CONTOUR_HIGHLIGHT_THICKNESS
        {
          *
        } = 3
    """

    assert option_stream == textwrap.dedent(exp_stream.strip("\n"))


def test_param_to_stream_numbers_list():
    param = {
        "contour_level_list": {
            "type": "number",
            "default": [],
            "list": True,
        }
    }
    prefix = " " * 2
    option_stream = modules.param_to_stream(param, prefix)
    exp_stream = """
        CONTOUR_LEVEL_LIST
        {
          *
          /
        } = ''
    """

    assert option_stream == textwrap.dedent(exp_stream.strip("\n"))


def test_param_to_stream_strings_list():
    param = {
        "contour_legend_text": {
            "type": "string",
            "list": True,
            "default": [],
        }
    }
    prefix = " " * 2
    option_stream = modules.param_to_stream(param, prefix)
    exp_stream = """
        CONTOUR_LEGEND_TEXT
        {
          @
          /
        } = ''
    """

    assert option_stream == textwrap.dedent(exp_stream.strip("\n"))


def test_param_to_stream_strings_list_help():
    param = {
        "contour_shade_colour_table": {
            "type": "string",
            "list": True,
            "default": [],
            "help": "help_colour",
            "interface": "colour",
        }
    }
    prefix = " " * 2
    option_stream = modules.param_to_stream(param, prefix)
    exp_stream = """
        CONTOUR_SHADE_COLOUR_TABLE [ help = help_colour,interface = colour ]
        {
          @
          /
        } = ''
    """

    assert option_stream == textwrap.dedent(exp_stream.strip("\n"))


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
    exp_stream = """
        DUMMY_CLASS; APPLICATION
        {
          PARAM1
          {
            VALUE1; VALUE1
            VALUE2; VALUE2
          } = VALUE2
        
          PARAM2
            [ interface = icon, class = TYPE2 ]
          { @ }
        }
    """

    assert definition_stream == textwrap.dedent(exp_stream).strip("\n")


def test_objaction_to_stream():
    actions = [
        {"dummy1": {"action": ["action1_1", "action1_2"], "service": "service1"}},
        {"dummy2": {"action": ["action2_1", "action2_2"], "service": "service2"}},
    ]
    actions_stream = modules.objaction_to_stream(actions, 2)
    exp_stream = "state,\n"
    exp_stream += textwrap.indent(
        "class   = DUMMY1\naction  = action1_1/action1_2\nservice = service1\n\n", "  ")
    exp_stream += "state,\n"
    exp_stream += textwrap.indent(
        "class   = DUMMY2\naction  = action2_1/action2_2\nservice = service2\n", "  ")

    assert actions_stream == exp_stream


def test_translate_objectspec(tmpdir):
    objectspec_content = """
        object:
            var1: value1
            var2: true
            definition_file: path1
            rules_file: path2
        actions:
          - action1:
               action:
                   - action1_1
                   - action1_2
               service: service1
          - action2:
              action: action2_1
              service: service2
        service:
          var3: value3
          var4: value4
    """
    objectspec_path = tmpdir.join("objectspec.yml")
    with open(objectspec_path, "w") as f:
        f.write(objectspec_content)

    defpath = "<definition_path>"
    rulespath = "<rules_path>"
    objectspec_stream = modules.translate_objectspec(objectspec_path, defpath, rulespath)
    exp_stream = """
        object,
            var1            = value1,
            var2            = True,
            definition_file = <definition_path>,
            rules_file      = <rules_path>
    
        state,
            class   = ACTION1
            action  = action1_1/action1_2
            service = service1
        
        state,
            class   = ACTION2
            action  = action2_1
            service = service2
        
        service,
            var3 = value3,
            var4 = value4
    """
    # "strip" to remove the first with line
    exp_stream = textwrap.dedent(exp_stream.strip("\n"))

    assert objectspec_stream == exp_stream
