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

    # incipit
    option_stream = f"{key.upper()}\n{{\n"
    # values
    values = "\n".join([str(v).upper() for v in content["values"]])
    option_stream += f"{textwrap.indent(values, prefix)}\n}}"
    # default
    option_stream += f" = {str(content['default']).upper()}\n"

    return option_stream


def param_to_stream(param, prefix):
    """

    :param dict param:
    :param str prefix:
    :return str:
    """
    key, content = list(param.items())[0]
    if content.get("type") == "option":
        param_stream = option_to_stream(key, content, prefix)
    else:
        value_stream = f"[ interface = icon, class = {param[key]['type'].upper()} ]"
        param_stream = f"{key.upper()}\n{textwrap.indent(value_stream, prefix )}\n"
        param_stream += "{ @ }\n"

    return param_stream


def translate_definition(definition_path, indent_width=2):
    """

    :param str definition_path:
    :param int indent_width:
    :return str:
    """
    with open(definition_path, "r") as f:
        definition = yaml.safe_load(f.read())

    # validity-check
    valid_keys = {"class", "params"}
    mandatory_keys = {"class", "params"}
    actual_keys = set(definition.keys())
    check_keys(valid_keys, mandatory_keys, actual_keys)

    # incipit
    stream = f"{definition['class'].upper()}\n{{"
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
        if str(value).lower() == "true":
            value = "True"
        row = f"{key:{max_key_length}} = {value}"
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
    with open(objectspec_path, "r") as f:
        objectspec = yaml.safe_load(f.read())

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


def translate_rules(rules_path):
    return ""


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
