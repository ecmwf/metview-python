# (C) Copyright 2017- ECMWF.
#
# This software is licensed under the terms of the Apache Licence Version 2.0
# which can be obtained at http://www.apache.org/licenses/LICENSE-2.0.
#
# In applying this licence, ECMWF does not waive the privileges and immunities
# granted to it by virtue of its status as an intergovernmental organisation
# nor does it submit to any jurisdiction.
#

import argparse
import os

import yaml
from prettytable import PrettyTable

# memory stats files
MEMORY_REF_FILE = "mem_reference.yaml"
MEMORY_RES_FILE = "mem_result.yaml"


def _load_stats(fname):
    f_path = fname
    if os.path.exists(f_path):
        with open(f_path, "rt") as f:
            return yaml.safe_load(f)


def load_ref_stats():
    return _load_stats(MEMORY_REF_FILE)


def load_res_stats():
    return _load_stats(MEMORY_RES_FILE)


def print_one(d, label):
    x = PrettyTable()
    x.field_names = ["Name", f"{label} RSS"]
    x.align["Name"] = "l"
    x.align[f"{label} RSS"] = "r"

    for k, v in d.items():
        x.add_row([k.replace("test_", ""), f"{int(int(v)/(1024*1024))} MB"])

    print(x)


def print_both():
    x = PrettyTable()
    x.field_names = ["Name", "Res RSS", "Ref RSS"]
    x.align["Name"] = "l"
    x.align["Res RSS"] = "r"
    x.align["Ref RSS"] = "r"

    ref = load_ref_stats()
    if ref is None:
        ref = {}
    res = load_res_stats()
    if res is None:
        res = {}

    keys = list(ref.keys())
    keys.extend(list(res.keys()))
    keys = list(set(keys))
    keys.sort()

    for k in keys:
        v1 = res.get(k, None)
        v2 = ref.get(k, None)
        try:
            v1 = int(int(v1) / (1024 * 1024))
        except:
            v1 = "???"
        try:
            v2 = int(int(v2) / (1024 * 1024))
        except:
            v2 = "???"
        x.add_row([k.replace("test_", ""), f"{v1} MB", f"{v2} MB"])

    print(x)


def print_ref():
    d = load_ref_stats()
    if d is None:
        d = {}
    print_one(d, "Ref")


def print_res():
    d = load_res_stats()
    if d is None:
        d = {}
    print_one(d, "Res")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--res", action="store_true", help=argparse.SUPPRESS)
    parser.add_argument("--ref", action="store_true", help=argparse.SUPPRESS)

    # on error this will write to stderr
    args = parser.parse_args()

    if args.res:
        print_res()
    elif args.ref:
        print_ref()
    else:
        print_both()


main()
