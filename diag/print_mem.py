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


def load_stats(fname):
    f_path = fname
    try:
        if os.path.exists(f_path):
            with open(f_path, "rt") as f:
                return yaml.safe_load(f)
    except:
        return dict()

    return dict()


def scale_to_mb(v):
    try:
        return int(int(v) / (1024 * 1024))
    except:
        return "???"


def print_stats(files):
    x = PrettyTable()
    labels = []
    for name in files:
        labels.append(name.replace(".yaml", "").replace("mem_", "") + " RSS")

    x.field_names = ["Name", *labels]
    x.align["Name"] = "l"
    d = []
    keys = []
    for i, lbl in enumerate(labels):
        x.align[lbl] = "r"
        d.append(load_stats(files[i]))
        keys.extend(list(d[i].keys()))

    keys = list(set(keys))
    keys.sort()

    for k in keys:
        row = [k.replace("test_", "")]
        for dv in d:
            row.append(f"{scale_to_mb(dv.get(k, None))} MB")

        x.add_row(row)

    print(x)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--res", action="store_true", help="print result")
    parser.add_argument("--ref", action="store_true", help="print reference")
    parser.add_argument("files", nargs="*", default=None)

    # on error this will write to stderr
    args = parser.parse_args()

    files = args.files

    if len(files) > 0:
        print_stats(files)
    else:
        if args.res:
            files = [MEMORY_RES_FILE]
            print_stats(files)

        elif args.ref:
            files = [MEMORY_REF_FILE]
            print_stats(files)

        else:
            files = [MEMORY_RES_FILE, MEMORY_REF_FILE]
            print_stats(files)


main()
