# (C) Copyright 2017- ECMWF.
#
# This software is licensed under the terms of the Apache Licence Version 2.0
# which can be obtained at http://www.apache.org/licenses/LICENSE-2.0.
#
# In applying this licence, ECMWF does not waive the privileges and immunities
# granted to it by virtue of its status as an intergovernmental organisation
# nor does it submit to any jurisdiction.

import argparse
import sys


def main(argv=None):
    parser = argparse.ArgumentParser()
    parser.add_argument("command")
    args = parser.parse_args(args=argv)
    if args.command == "selfcheck":
        sys.argv = []
        print("Trying to connect to a Metview installation...")
        try:
            from . import bindings as _bindings
        except Exception as exp:
            print("Could not find a valid Metview installation")
            raise (exp)
        mv = dict()
        _bindings.bind_functions(mv, module_name="mv")
        del _bindings

        try:
            mv["print"]("Hello world - printed from Metview!")
        except Exception as exp:
            print("Could not print a greeting from Metview")
            raise (exp)

        mv_version_f = mv["version_info"]
        mv_version = mv_version_f()
        mv_maj = str(int(mv_version["metview_major"]))
        mv_min = str(int(mv_version["metview_minor"]))
        mv_rev = str(int(mv_version["metview_revision"]))
        mv_version_string = mv_maj + "." + mv_min + "." + mv_rev
        print("Metview version", mv_version_string, "found")

        print("Your system is ready.")
    else:
        raise RuntimeError(
            "Command not recognised %r. See usage with --help." % args.command
        )


if __name__ == "__main__":
    main()
