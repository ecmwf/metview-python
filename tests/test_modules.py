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


def test_basetype_to_stream_number():
    key = 'dummy_key'
    content = {
        "type": "number",
        "list": False,
    }
    prefix = " " * 2
    type_stream = modules.basetype_to_stream(key, content, prefix)
    exp_stream = """
        DUMMY_KEY
        {
          *
        } = ''
    """

    assert type_stream == textwrap.dedent(exp_stream.strip("\n"))


def test_basetype_to_stream_numbers_list():
    key = 'dummy_key'
    content = {
        "type": "number",
        "list": True,
    }
    prefix = " " * 2
    type_stream = modules.basetype_to_stream(key, content, prefix)
    exp_stream = """
        DUMMY_KEY
        {
          *
          /
        } = ''
    """

    assert type_stream == textwrap.dedent(exp_stream.strip("\n"))


def test_basetype_to_stream_string():
    key = 'dummy_key'
    content = {
        "type": "string",
        "list": False,
    }
    prefix = " " * 2
    type_stream = modules.basetype_to_stream(key, content, prefix)
    exp_stream = """
        DUMMY_KEY
        {
          @
        } = ''
    """

    assert type_stream == textwrap.dedent(exp_stream.strip("\n"))


def test_basetype_to_stream_strings_list():
    key = 'dummy_key'
    content = {
        "type": "string",
        "list": True,
    }
    prefix = " " * 2
    type_stream = modules.basetype_to_stream(key, content, prefix)
    exp_stream = """
        DUMMY_KEY
        {
          @
          /
        } = ''
    """

    assert type_stream == textwrap.dedent(exp_stream.strip("\n"))


def test_basetype_to_stream_with_help():
    key = 'dummy_key'
    content = {
        "type": "string",
        "list": True,
        "help": "dummy_help",
        "interface": "dummy_interface",
    }
    prefix = " " * 2
    type_stream = modules.basetype_to_stream(key, content, prefix)
    exp_stream = """
        DUMMY_KEY [ help = dummy_help,interface = dummy_interface ]
        {
          @
          /
        } = ''
    """

    assert type_stream == textwrap.dedent(exp_stream.strip("\n"))


def test_datatype_to_stream():
    key = 'dummy_key'
    content = {
        "type": "grib",
        "interface": {
            "multi": False,
        }
    }
    prefix = " " * 2
    datatype_stream = modules.datatype_to_stream(key, content, prefix)
    exp_stream = """
        DUMMY_KEY
          [  interface = icon, class = GRIB, exclusive = true  ]
        { @ }
    """

    assert datatype_stream == textwrap.dedent(exp_stream.strip("\n"))


def test_datatype_to_stream_no_exclusive():
    key = 'dummy_key'
    content = {
        "type": "grib",
        "interface": {
            "multi": True,
        }
    }
    prefix = " " * 2
    datatype_stream = modules.datatype_to_stream(key, content, prefix)
    exp_stream = """
        DUMMY_KEY
          [  interface = icon, class = GRIB  ]
        { @ }
    """

    assert datatype_stream == textwrap.dedent(exp_stream.strip("\n"))


def test_datatype_to_stream_with_help():
    key = 'dummy_key'
    content = {
        "type": "grib",
        "interface": {
            "multi": False,
            "help": {"type": "data", "ke1": "value1", "key2": "value2"},
        }
    }
    prefix = " " * 2
    datatype_stream = modules.datatype_to_stream(key, content, prefix)
    exp_stream = """
        DUMMY_KEY
          [  interface = icon, class = GRIB, exclusive = true,
             help      = help_data,
             help_ke1  = value1,
             help_key2 = value2
          ]
        { @ }
    """

    assert datatype_stream == textwrap.dedent(exp_stream.strip("\n"))


def test_shared_param_to_stream_invalid_keys():
    key = "dummy"
    content = {"dummy_name": "dummy_value"}

    with pytest.raises(ValueError):
        modules.shared_param_to_stream(key, content, " ")


def test_shared_param_to_stream_no_mandatory_key():
    key = "dummy"
    content = {"type": "colour"}

    with pytest.raises(ValueError):
        modules.shared_param_to_stream(key, content, " ")


def test_shared_param_to_stream_invalid_type():
    key = "dummy"
    content = {"type": "dummy", "default": "dummy_default"}

    with pytest.raises(ValueError):
        modules.shared_param_to_stream(key, content, " ")


def test_shared_param_to_stream_colour_no_help():
    key = "dummy"
    content = {"type": "colour", "default": "dummy_colour"}
    prefix = " " * 4
    sh_param_stream = modules.shared_param_to_stream(key, content, prefix)
    exp_stream = """
        DUMMY
        {
            &PARAMSHARE&COLOUR
        } = DUMMY_COLOUR
    """

    assert sh_param_stream == textwrap.dedent(exp_stream.strip("\n"))


def test_shared_param_to_stream_colour_with_help():
    key = "dummy"
    content = {
        "type": "colour",
        "help": "help_colour",
        "interface": "colour",
        "default": "dummy_colour"
    }
    prefix = " " * 4
    sh_param_stream = modules.shared_param_to_stream(key, content, prefix)
    exp_stream = """
        DUMMY  [  help = help_colour,interface = colour  ]
        {
            &PARAMSHARE&COLOUR
        } = DUMMY_COLOUR
    """

    assert sh_param_stream == textwrap.dedent(exp_stream.strip("\n"))


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


def test_assemble_paramshare_section_no_param():
    params = []
    paramshare_stream = modules.assemble_paramshare_section(params, 4)

    assert paramshare_stream == ""


def test_assemble_paramshare_section_no_type():
    params = [{"param1": {"type": "dummy_type1"}}, {"param2": {"type": "dummy_type2"}}]
    paramshare_stream = modules.assemble_paramshare_section(params, 4)

    assert paramshare_stream == ""


def test_assemble_paramshare_section_colour():
    params = [{"param1": {"type": "colour"}}, {"param2": {"type": "dummy_type2"}}]
    paramshare_stream = modules.assemble_paramshare_section(params, 4)
    exp_stream = """
        PARAMSHARE; ParamShare; PARAMSHARE
        {
            COLOUR {
                %include MagicsColours.txt
            }
        }

    """

    assert paramshare_stream == textwrap.dedent(exp_stream.strip("\n"))


def test_assemble_paramshare_section_marker_line_style():
    params = [
        {"param1": {"type": "marker"}},
        {"param2": {"type": "line_style"}}
    ]
    paramshare_stream = modules.assemble_paramshare_section(params, 4)
    exp_stream = """
        PARAMSHARE; ParamShare; PARAMSHARE
        {
            MARKER {
                1; 1
                2; 2
                3; 3
                4; 4
                5; 5
            }
        
            LINE_STYLE {
                SOLID; SOLID
                DASH; DASH
                DOT; DOT
                CHAIN_DOT; CHAIN_DOT
                CHAIN_DASH; CHAIN_DASH
            }
        }

    """

    assert paramshare_stream == textwrap.dedent(exp_stream.strip("\n"))


def test_assemble_paramshare_section_onoff_quality():
    params = [
        {"param1": {"type": "onoff"}},
        {"param2": {"type": "quality"}}
    ]
    paramshare_stream = modules.assemble_paramshare_section(params, 4)
    exp_stream = """
        PARAMSHARE; ParamShare; PARAMSHARE
        {
            ONOFF {
                ON; ON
                OFF; OFF
            }

            QUALITY {
                LOW; LOW
                MEDIUM; MEDIUM
                HIGH; HIGH
            }
        }

    """

    assert paramshare_stream == textwrap.dedent(exp_stream.strip("\n"))


def test_assemble_paramshare_section_shading_thickness():
    params = [
        {"param1": {"type": "shading"}},
        {"param2": {"type": "thickness"}}
    ]
    paramshare_stream = modules.assemble_paramshare_section(params, 4)
    exp_stream = """
        PARAMSHARE; ParamShare; PARAMSHARE
        {
            SHADING {
                DOT; DOT
                HATCH; HATCH
                AREA_FILL; AREA_FILL
            }

            THICKNESS {
                1; 1
                2; 2
                3; 3
                4; 4
                5; 5
                6; 6
                7; 7
                8; 8
                9; 9
                10; 10
            }
        }

    """

    assert paramshare_stream == textwrap.dedent(exp_stream.strip("\n"))


def test_translate_definition(tmpdir):
    definition_content = """
        class: dummy_class
        params:
            - param1:
                type: option
                values:
                    - value1
                    - value2
                default: value2
            - param2:
                type: number
            - param3:
                type: grib
                interface:
                    help:
                        type: data
                        name: dummy name
            - param4:
                type: grib
                interface:
                    multi: false
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
            {
                *
            } = ''
            
            PARAM3
                [  interface = icon, class = GRIB,
                   help      = help_data,
                   help_name = dummy name
                ]
            { @ }
            
            PARAM4
                [  interface = icon, class = GRIB, exclusive = true  ]
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


def test_translate_rule_test_lowercase():
    width = 80
    indent_width = 4
    test = "param = value"
    test_stream = modules.translate_rule_test(test, width, indent_width)
    exp_stream = "%if param = value %then\n"

    assert test_stream == exp_stream


def test_translate_rule_test_uppercase():
    width = 80
    indent_width = 4
    test = "PARAM = VALUE"
    test_stream = modules.translate_rule_test(test, width, indent_width)
    exp_stream = "%if PARAM = VALUE %then\n"

    assert test_stream == exp_stream


def test_translate_rule_test_mixedcase():
    width = 80
    indent_width = 4
    test = "PARAM = value"
    test_stream = modules.translate_rule_test(test, width, indent_width)
    exp_stream = "%if PARAM = value %then\n"

    assert test_stream == exp_stream


def test_translate_rule_test_width():
    width = 80
    indent_width = 4
    test = "param = value and param2 > value2 or param3 <> value3 not (param4 in value4)"
    test_stream = modules.translate_rule_test(test, width, indent_width)
    exp_stream = "%if param = value %and param2 > value2 %or "
    exp_stream += "param3 <> value3 %not (param4 %in value4) %then\n"

    assert test_stream == exp_stream


def test_translate_rule_test_width2():
    width = 40
    indent_width = 4
    test = "param = value and param2 > value2 or param3 <> value3 not (param4 in value4)"
    test_stream = modules.translate_rule_test(test, width, indent_width)
    exp_stream = """
        %if param = value %and param2 > value2 %or
            param3 <> value3 %not (param4 %in value4) %then
    """

    assert test_stream == textwrap.dedent(exp_stream.strip("\n"))


def test_translate_rule_wrong_key():
    width = 89
    indent_width = 4
    rule = {
        "if": "dummy_test",
        "sunset": "dummy_parameter"
    }

    with pytest.raises(ValueError):
        modules.translate_rule(rule, width, indent_width)


def test_translate_rule_missing_if():
    width = 89
    indent_width = 4
    rule = {
        "error": "dummy_error",
        "set": "dummy_parameter"
    }

    with pytest.raises(ValueError):
        modules.translate_rule(rule, width, indent_width)


def test_translate_rule_set_as_string():
    width = 89
    indent_width = 4
    rule = {
        "if": "dummy_test",
        "set": "dummy_parameter"
    }
    rule_stream = modules.translate_rule(rule, width, indent_width)
    exp_stream = """
        %if dummy_test %then
            %set DUMMY_PARAMETER
    """

    assert rule_stream == textwrap.dedent(exp_stream.strip("\n"))


def test_translate_rule_unset_as_string():
    width = 89
    indent_width = 4
    rule = {
        "if": "dummy_test",
        "unset": "dummy_parameter"
    }
    rule_stream = modules.translate_rule(rule, width, indent_width)
    exp_stream = """
        %if dummy_test %then
            %unset DUMMY_PARAMETER
    """

    assert rule_stream == textwrap.dedent(exp_stream.strip("\n"))


def test_translate_rule_set_as_list():
    width = 89
    indent_width = 4
    rule = {
        "if": "dummy_test",
        "set": ["param1", "param2"]
    }
    rule_stream = modules.translate_rule(rule, width, indent_width)
    exp_stream = """
        %if dummy_test %then
            %set PARAM1
            %set PARAM2
    """

    assert rule_stream == textwrap.dedent(exp_stream.strip("\n"))


def test_translate_rule_unset_as_list():
    width = 89
    indent_width = 4
    rule = {
        "if": "dummy_test",
        "unset": ["param1", "param2"]
    }
    rule_stream = modules.translate_rule(rule, width, indent_width)
    exp_stream = """
        %if dummy_test %then
            %unset PARAM1
            %unset PARAM2
    """

    assert rule_stream == textwrap.dedent(exp_stream.strip("\n"))


def test_translate_rules_snippet1(tmpdir):
    rules_content = """
    - if: "LAYER <> mc_10fg and LAYER  <> mc_10ws and LAYER <> mc_2tmax and
        LAYER <> mc_2tmean and LAYER <> mc_2tmin and LAYER <> mc_cape and
        LAYER <> mc_capeshear and LAYER <> mc_sf and LAYER <> mc_swh and LAYER <> mc_tp"
      unset: quantile
    """
    rules_path = tmpdir.join("rules.yml")
    with open(rules_path, "w") as f:
        f.write(rules_content)
    rules_stream = modules.translate_rules(rules_path)
    exp_stream = """
        %if LAYER <> mc_10fg %and LAYER <> mc_10ws %and LAYER <> mc_2tmax %and LAYER <> mc_2tmean %and
            LAYER <> mc_2tmin %and LAYER <> mc_cape %and LAYER <> mc_capeshear %and LAYER <> mc_sf %and
            LAYER <> mc_swh %and LAYER <> mc_tp %then
                %unset QUANTILE

    """

    assert rules_stream == textwrap.dedent(exp_stream.strip("\n"))


def test_translate_rules_snippet2(tmpdir):
    rules_content = """
    - if: "AXIS_TICK_LABEL = OFF or AXIS_TICK_LABEL_TYPE = LABEL_LIST"
      unset:
        - axis_tick_label_format
        - axis_tick_label_frequency
    """
    rules_path = tmpdir.join("rules.yml")
    with open(rules_path, "w") as f:
        f.write(rules_content)
    rules_stream = modules.translate_rules(rules_path)
    exp_stream = """
        %if AXIS_TICK_LABEL = OFF %or AXIS_TICK_LABEL_TYPE = LABEL_LIST %then
            %unset AXIS_TICK_LABEL_FORMAT
            %unset AXIS_TICK_LABEL_FREQUENCY

    """

    assert rules_stream == textwrap.dedent(exp_stream.strip("\n"))


def test_translate_rules_snippet3(tmpdir):
    rules_content = """
    - if: "AXIS_TYPE <> DATE or AXIS_DATE_TYPE = MONTHS or AXIS_DATE_TYPE = YEARS or
           AXIS_DAYS_LABEL = OFF"
      unset:
        - axis_days_label_composition
        - axis_days_label_height
        - axis_days_label_quality
        - axis_days_label_colour
    """
    rules_path = tmpdir.join("rules.yml")
    with open(rules_path, "w") as f:
        f.write(rules_content)
    rules_stream = modules.translate_rules(rules_path)
    exp_stream = """
        %if AXIS_TYPE <> DATE %or AXIS_DATE_TYPE = MONTHS %or AXIS_DATE_TYPE = YEARS %or AXIS_DAYS_LABEL = OFF %then
            %unset AXIS_DAYS_LABEL_COMPOSITION
            %unset AXIS_DAYS_LABEL_HEIGHT
            %unset AXIS_DAYS_LABEL_QUALITY
            %unset AXIS_DAYS_LABEL_COLOUR

    """

    assert rules_stream == textwrap.dedent(exp_stream.strip("\n"))


def test_translate_rules_snippet4(tmpdir):
    rules_content = """
    - if: "SYMBOL_MARKER_MODE <> INDEX or SYMBOL_TABLE_MODE <> OFF or SYMBOL_TYPE <> BOTH and
            SYMBOL_TYPE <> MARKER"
      unset: symbol_marker_index
    """
    rules_path = tmpdir.join("rules.yml")
    with open(rules_path, "w") as f:
        f.write(rules_content)
    rules_stream = modules.translate_rules(rules_path)
    exp_stream = """
        %if SYMBOL_MARKER_MODE <> INDEX %or SYMBOL_TABLE_MODE <> OFF %or SYMBOL_TYPE <> BOTH %and SYMBOL_TYPE <> MARKER %then
            %unset SYMBOL_MARKER_INDEX

    """

    assert rules_stream == textwrap.dedent(exp_stream.strip("\n"))


def test_translate_rules_snippet5(tmpdir):
    rules_content = """
    - if: "TYPE = IM or TYPE = SIM or TYPE = OLDIM) and STREAM <> SSMI"
      set: repres = sv
      unset:
        - param
        - levtype
        - levelist
        - resol
        - duplicates
        - grid
        - rotation
    """
    rules_path = tmpdir.join("rules.yml")
    with open(rules_path, "w") as f:
        f.write(rules_content)
    rules_stream = modules.translate_rules(rules_path)
    exp_stream = """
        %if TYPE = IM %or TYPE = SIM %or TYPE = OLDIM) %and STREAM <> SSMI %then
            %set REPRES = SV
            %unset PARAM
            %unset LEVTYPE
            %unset LEVELIST
            %unset RESOL
            %unset DUPLICATES
            %unset GRID
            %unset ROTATION

    """

    assert rules_stream == textwrap.dedent(exp_stream.strip("\n"))


def test_translate_rules_snippet6(tmpdir):
    rules_content = """
    - if: "LEVTYPE = SFC and CLASS = ER and STREAM = OPER and (TYPE = AN or TYPE = FC) and (not REPRES)"
      set: repres = gg
    """
    rules_path = tmpdir.join("rules.yml")
    with open(rules_path, "w") as f:
        f.write(rules_content)
    rules_stream = modules.translate_rules(rules_path)
    exp_stream = """
        %if LEVTYPE = SFC %and CLASS = ER %and STREAM = OPER %and (TYPE = AN %or TYPE = FC) %and (%not REPRES) %then
            %set REPRES = GG

    """

    assert rules_stream == textwrap.dedent(exp_stream.strip("\n"))


def test_translate_rules_snippet7(tmpdir):
    rules_content = """
    - if: "not (TYPE = OLDIM or TYPE = OB or TYPE = FB or TYPE = AI or TYPE = AF or TYPE = AB or
      TYPE = TF or TYPE = OFB or TYPE = MFB or TYPE = OAI or TYPE = SFB or TYPE = FSOIFB or
      TYPE = FCDFB)"
      unset:
        - obstype
        - obsgroup
        - duplicates
    """
    rules_path = tmpdir.join("rules.yml")
    with open(rules_path, "w") as f:
        f.write(rules_content)
    rules_stream = modules.translate_rules(rules_path)
    exp_stream = """
        %if %not (TYPE = OLDIM %or TYPE = OB %or TYPE = FB %or TYPE = AI %or TYPE = AF %or TYPE = AB %or
            TYPE = TF %or TYPE = OFB %or TYPE = MFB %or TYPE = OAI %or TYPE = SFB %or TYPE = FSOIFB %or TYPE = FCDFB) %then
                %unset OBSTYPE
                %unset OBSGROUP
                %unset DUPLICATES

    """

    assert rules_stream == textwrap.dedent(exp_stream.strip("\n"))


def test_translate_rules_snippet8(tmpdir):
    rules_content = """
    - if: "(AREA = G or AREA = GLOBE) and (_APPL = diss)"
      warning: "Expand global AREA for dissemination to AREA = 90/0/-90/359.99"
      set: area = 90/0/-90/359.99
    """
    rules_path = tmpdir.join("rules.yml")
    with open(rules_path, "w") as f:
        f.write(rules_content)
    rules_stream = modules.translate_rules(rules_path)
    exp_stream = """
        %if (AREA = G %or AREA = GLOBE) %and (_APPL = diss) %then
            %warning "Expand global AREA for dissemination to AREA = 90/0/-90/359.99"
            %set AREA = 90/0/-90/359.99

    """

    assert rules_stream == textwrap.dedent(exp_stream.strip("\n"))


def test_translate_rules_snippet9(tmpdir):
    rules_content = """
    - if: "_VERB = READ and CLASS  <> ANY"
      warning: "CLASS ignored in READ"
    """
    rules_path = tmpdir.join("rules.yml")
    with open(rules_path, "w") as f:
        f.write(rules_content)
    rules_stream = modules.translate_rules(rules_path)
    exp_stream = """
        %if _VERB = READ %and CLASS <> ANY %then
            %warning "CLASS ignored in READ"

    """

    assert rules_stream == textwrap.dedent(exp_stream.strip("\n"))


def test_translate_rules_snippet10(tmpdir):
    rules_content = """
    - if: "LEVTYPE = DP and (SECTION = M or SECTION = Z) and
      (PRODUCT = INST or PRODUCT = TACC or PRODUCT = TAVG)"
      unset: levelist
    """
    rules_path = tmpdir.join("rules.yml")
    with open(rules_path, "w") as f:
        f.write(rules_content)
    rules_stream = modules.translate_rules(rules_path)
    exp_stream = """
        %if LEVTYPE = DP %and (SECTION = M %or SECTION = Z) %and (PRODUCT = INST %or PRODUCT = TACC %or PRODUCT = TAVG) %then
            %unset LEVELIST

    """

    assert rules_stream == textwrap.dedent(exp_stream.strip("\n"))


def test_translate_rules_snippet11(tmpdir):
    rules_content = """
    - if: "(TYPE=IM and OBSTYPE=10 and (IDENT=52 or IDENT=53 or IDENT=54))"
      warning: "Replacing OBSTYPE=10 by CHANNEL=3, INSTRUMENT=205"
      unset: obstype
      set:
        - channel = 3
        - instrument = 205
    """
    rules_path = tmpdir.join("rules.yml")
    with open(rules_path, "w") as f:
        f.write(rules_content)
    rules_stream = modules.translate_rules(rules_path)
    exp_stream = """
        %if (TYPE=IM %and OBSTYPE=10 %and (IDENT=52 %or IDENT=53 %or IDENT=54)) %then
            %warning "Replacing OBSTYPE=10 by CHANNEL=3, INSTRUMENT=205"
            %unset OBSTYPE
            %set CHANNEL = 3
            %set INSTRUMENT = 205

    """

    assert rules_stream == textwrap.dedent(exp_stream.strip("\n"))
