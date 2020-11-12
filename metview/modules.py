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

import os
import textwrap
import yaml


PARAMSHARE_TYPES = {
    "colour": "%include MagicsColours.txt",
    "line_style": ["SOLID", "DASH", "DOT", "CHAIN_DOT", "CHAIN_DASH"],
    "marker": range(1, 6),
    "onoff": ["ON", "OFF"],
    "quality": ["LOW", "MEDIUM", "HIGH"],
    "shading": ["DOT", "HATCH", "AREA_FILL"],
    "thickness": range(1, 11),
}


def check_keys(valid_keys, mandatory_keys, actual_keys):
    """

    :param set valid_keys:
    :param set mandatory_keys:
    :param set actual_keys:
    :return:
    """
    if not actual_keys.issubset(valid_keys):
        invalid_keys = actual_keys.difference(valid_keys)
        raise ValueError(f"invalid key(s) in the definition file: {invalid_keys}")
    if not mandatory_keys.issubset(actual_keys):
        raise ValueError(f"the following keys are mandatory in a definition file: {mandatory_keys}")


def option_to_stream(key, content, prefix):
    """

    :param str key:
    :param dict content:
    :param str prefix:
    :return str:
    """
    valid_keys = {"type", "values", "default"}
    check_keys(valid_keys, valid_keys, set(content.keys()))
    if content["type"] != "option":
        raise ValueError(
            f"invalid 'type' value: {content['type']}. Valid type value is only 'option'"
        )
    if not all([isinstance(v, str) for v in content["values"]]):
        raise ValueError(f"for option type all values must be strings: {content['values']}")

    # incipit
    option_stream = f"{key.upper()}\n{{\n"
    # values
    values = "\n".join([f"{v.upper()}; {v.upper()}" for v in content["values"]])
    option_stream += f"{textwrap.indent(values, prefix)}\n}}"
    # default
    option_stream += f" = {str(content['default']).upper()}\n"

    return option_stream


def basetype_to_stream(key, content, prefix):
    """

    :param str key:
    :param dict content:
    :param str prefix:
    :return str:
    """
    type_to_symbol = {
        "number": "*",
        "string": "@",
    }
    # incipit
    help_ = f"help = {content.get('help')}" if content.get('help') else ""
    interface = f"interface = {content.get('interface')}" if content.get('interface') else ""
    declaration = ",".join(filter(None, [help_, interface]))
    declaration = f" [ {declaration} ]" if declaration else ""
    incipit = f"{key.upper()}{declaration}\n{{\n"
    # values
    list_symbol = "/\n" if content.get("list") is True else ""
    values = f"{type_to_symbol[content['type']]}\n{list_symbol}"
    default = content.get("default") if content.get("default") else "''"
    param_stream = f"{incipit}{textwrap.indent(values, prefix)}}} = {default}\n"

    return param_stream


def datatype_to_stream(key, content, prefix):
    """

    :param str key:
    :param dict content:
    :param str prefix:
    :return str:
    """
    bracket_prefix = "  "
    help_dict = content.get("interface", {}).get("help", {})
    if help_dict:
        width = max([len("help_" + k) for k in help_dict.keys()])
        helps = [f"{'help':{width}} = help_{help_dict.pop('type', '')}"]
        for hk, value in help_dict.items():
            helps.append(f"{'help_' + hk:{width}} = {value}")
        helps = ",\n" + textwrap.indent(",\n".join(helps), bracket_prefix + " ")
    else:
        helps = ""
    exclusive = ", exclusive = true" if content.get("interface", {}).get("multi") is False else ""
    declaration = f"interface = icon, class = {content['type'].upper()}{exclusive}"
    metadata = f"[{bracket_prefix}{declaration}{bracket_prefix if not helps else ''}{helps}"
    metadata += "\n]" if helps else "]"
    param_stream = f"{key.upper()}\n{textwrap.indent(metadata, prefix)}\n"
    param_stream += "{ @ }\n"
    return param_stream


def shared_param_to_stream(key, content, prefix):
    """

    :param str key:
    :param dict content:
    :param str prefix:
    :return str:
    """
    valid_keys = {"type", "default", "help", "interface"}
    mandatory_keys = {"type", "default"}
    check_keys(valid_keys, mandatory_keys, set(content.keys()))
    shared_type = content["type"]
    if shared_type not in PARAMSHARE_TYPES:
        raise ValueError(
            f"invalid 'type': {shared_type}. Valid types are only {PARAMSHARE_TYPES.keys()}"
        )

    bracket_prefix = "  "
    # incipit
    help_ = f"help = {content.get('help')}" if content.get("help") else ""
    interface = f"interface = {content.get('interface')}" if content.get("interface") else ""
    declaration = ",".join(filter(None, [help_, interface]))
    declaration = f"  [{bracket_prefix}{declaration}{bracket_prefix}]" if declaration else ""
    sh_param_stream = f"{key.upper()}{declaration}\n{{\n"
    # values
    sh_param_stream += f"{textwrap.indent(f'&PARAMSHARE&{shared_type.upper()}', prefix)}\n}}"
    # default
    sh_param_stream += f" = {str(content['default']).upper()}\n"

    return sh_param_stream


def param_to_stream(param, prefix):
    """

    :param dict param:
    :param str prefix:
    :return str:
    """
    base_types = ["string", "number"]
    data_types = ["grib", "netcdf", "geopoints"]
    key, content = list(param.items())[0]
    if content["type"] == "option":
        param_stream = option_to_stream(key, content, prefix)
    elif content["type"] in base_types:
        param_stream = basetype_to_stream(key, content, prefix)
    elif content["type"] in data_types:
        param_stream = datatype_to_stream(key, content, prefix)
    elif content["type"] in PARAMSHARE_TYPES:
        param_stream = shared_param_to_stream(key, content, prefix)
    else:
        valid_types = sorted(list(PARAMSHARE_TYPES.keys()) + base_types + data_types + ["option"])
        raise ValueError(f"invalid param type: '{content['type']}'. Valid types are: {valid_types}")

    return param_stream


def assemble_paramshare_section(params, indent_width):
    """

    :param list params:
    :param int indent_width:
    :return str:
    """
    # gather common subsets of parameters, if any
    shared_types = []
    for param_dict in params:
        param_descr = list(param_dict.values())[0]
        if param_descr.get("type") in PARAMSHARE_TYPES:
            shared_types.append(param_descr["type"])

    if not shared_types:
        return ""
    prefix = " " * indent_width
    types_stream = []
    for sh_type in shared_types:
        # incipit
        sh_type_stream = f"{sh_type.upper()} {{\n"
        # values
        if isinstance(PARAMSHARE_TYPES[sh_type], str):
            sh_type_stream += textwrap.indent(PARAMSHARE_TYPES[sh_type], prefix)
        else:
            values = "\n".join([f"{v}; {v}" for v in PARAMSHARE_TYPES[sh_type]])
            sh_type_stream += textwrap.indent(values, prefix)
        # closure
        sh_type_stream += "\n}\n"
        types_stream.append(sh_type_stream)
    types_stream = textwrap.indent("\n".join(types_stream), prefix)
    paramshare_stream = f"PARAMSHARE; ParamShare; PARAMSHARE\n{{\n{types_stream}}}\n\n"
    return paramshare_stream


def translate_definition(definition_path, indent_width=4):
    """

    :param str definition_path:
    :param int indent_width:
    :return str:
    """
    try:
        with open(definition_path, "r") as f:
            definition = yaml.safe_load(f.read())
    except Exception as err:
        raise ValueError(f"invalid definition YAML file: {err}")

    # validity-check
    valid_keys = {"class", "params"}
    mandatory_keys = {"class", "params"}
    actual_keys = set(definition.keys())
    check_keys(valid_keys, mandatory_keys, actual_keys)

    # incipit
    paramshare_stream = assemble_paramshare_section(definition["params"], indent_width)
    stream = f"{paramshare_stream}{definition['class'].upper()}; APPLICATION\n{{"
    # content
    prefix = " " * indent_width
    params = ""
    for param_dict in definition["params"]:
        params += f"\n{param_to_stream(param_dict, prefix)}"
    stream += textwrap.indent(params, prefix)
    # closure
    stream += "}"

    return stream


def objrows_to_stream(section_content):
    """

    :param dict section_content:
    :return str:
    """
    max_key_length = max((len(k) for k in section_content.keys()))
    rows = []
    for key, value in section_content.items():
        if key == "class":
            value = value.upper()
        row = f"{key:{max_key_length}} = {str(value)}"
        rows.append(row)
    rows_stream = ",\n".join(rows)

    return rows_stream


def objaction_to_stream(actions_list, indent_width):
    """

    :param list actions_list:
    :param int indent_width:
    :return str:
    """
    actions_stream = []
    for action_dict in actions_list:
        key = next(iter(action_dict))
        check_keys({"action", "service"}, {"action", "service"}, set(action_dict[key].keys()))
        incipit = "state,\n"
        if isinstance(action_dict[key]['action'], list):
            list_of_actions = '/'.join(action_dict[key]['action'])
        else:
            list_of_actions = action_dict[key]['action']
        rows = [
            f"class   = {key.upper()}",
            f"action  = {list_of_actions}",
            f"service = {action_dict[key]['service']}",
        ]
        rows_stream = textwrap.indent("\n".join(rows), " " * indent_width)
        actions_stream.append(incipit + rows_stream + "\n")
    actions_stream = "\n".join(actions_stream)

    return actions_stream


def objsection_to_stream(key, content, indent_width):
    """

    :param str key:
    :param dict_or_list content:
    :param int indent_width:
    :return str:
    """
    section_stream = f"{key},\n"
    if key == "actions":
        section_stream = objaction_to_stream(content, indent_width)
    else:
        prefix = ' ' * indent_width
        section_stream += f"{textwrap.indent(objrows_to_stream(content), prefix)}\n"

    return section_stream


def translate_objectspec(objectspec_path, defpath, rulespath, indent_width=4):
    """

    :param str objectspec_path:
    :param str defpath:
    :param str rulespath:
    :param int indent_width:
    :return str:
    """
    try:
        with open(objectspec_path, "r") as f:
            objectspec = yaml.safe_load(f.read())
    except Exception as err:
        raise ValueError(f"invalid objectspec YAML file: {err}")

    # validity-check
    valid_keys = {"actions", "object", "service"}
    mandatory_keys = {"actions", "object", "service"}
    actual_keys = set(objectspec.keys())
    check_keys(valid_keys, mandatory_keys, actual_keys)

    # set the paths with the translated files
    objectspec["object"]["definition_file"] = defpath
    objectspec["object"]["rules_file"] = rulespath

    sections = []
    for key, content in objectspec.items():
        sections.append(objsection_to_stream(key, content, indent_width))
    stream = "\n".join(sections)

    return stream


def translate_rule_test(test, width, indent_width):
    """

    :param str test:
    :param int width:
    :param int indent_width:
    :return str:
    """
    # The following replacements are done for two reasons:
    #   - add "%" character before logic operators (e.g. "and", "or", etc.)
    #   - split test after each logical operator
    rep = {
        " and ": " %and\n",
        " or ": " %or\n",
        " not ": " %not\n",  # tests starting with "not ..." fall in this case because we add "%if "
        "(not ": "(%not\n",
        " in ": " %in\n",
    }
    # add "%if" statement and remove multiple whitespace
    test = f"%if {' '.join(test.split())}"
    # apply replacements
    for k, v in rep.items():
        test = test.replace(k, v)
    # compose test-stream avoiding to end a line with an incomplete sub-test (e.g. " ...PARAM = \n")
    tests = test.splitlines()
    test_stream = tests[0]
    idx = 1
    for l in tests[1:]:
        if (len(test_stream) > idx * width) and tests[-1] != l:
            test_stream += f"\n{' ' * indent_width}{l}"
            idx += 1
        else:
            test_stream += f" {l}"
    return f"{test_stream} %then\n"


def translate_rule(rule, width, indent_width):
    """

    :param dict rule:
    :param int width:
    :param int indent_width:
    :return str:
    """
    # validity-check
    valid_keys = {"error", "if", "set", "unset", "warning"}
    mandatory_keys = {"if"}
    actual_keys = set(rule.keys())
    check_keys(valid_keys, mandatory_keys, actual_keys)

    test = rule.pop("if")
    rule_stream = translate_rule_test(test, width, indent_width)
    prefix = " " * indent_width if len(rule_stream.splitlines()) == 1 else " " * 2 * indent_width
    for action, value in rule.items():
        if "set" in action:  # "set" and "unset" can be list or string
            if isinstance(value, str):
                value = [value]
            action_stream = ""
            for param in value:
                action_stream += f"%{action} {param.upper()}\n"
            rule_stream += textwrap.indent(action_stream, prefix)
        else:
            rule_stream += textwrap.indent(f'%{action} "{value}"\n', prefix)
    return rule_stream


def translate_rules(rules_path, width=89, indent_width=4):
    """

    :param str rules_path:
    :param int width:
    :param int indent_width:
    :return str:
    """
    with open(rules_path, "r") as f:
        rules = yaml.safe_load(f.read())

    rules_stream = ""
    for rule in rules:
        rule_stream = translate_rule(rule, width, indent_width)
        rules_stream += f"{rule_stream}\n"
    return rules_stream


def translate_config(definition_yaml_path, objectspec_yaml_path, rules_yaml_path, output_path="."):
    output_path = os.path.abspath(output_path)

    defpath = os.path.join(output_path, "definition")
    with open(defpath, "w") as f:
        f.write(translate_definition(definition_yaml_path))

    rulespath = os.path.join(output_path, "rules")
    with open(rulespath, "w") as f:
        f.write(translate_rules(rules_yaml_path))

    objpath = os.path.join(output_path, "objectspec")
    with open(objpath, "w") as f:
        f.write(translate_objectspec(objectspec_yaml_path, defpath, rulespath))

    return defpath, objpath, rulespath
