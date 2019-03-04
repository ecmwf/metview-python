#
# Copyright 2017-2019 B-Open Solutions srl.
# Copyright 2017-2019 European Centre for Medium-Range Weather Forecasts (ECMWF).
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

import argparse
import sys


def main(argv=None):
    parser = argparse.ArgumentParser()
    parser.add_argument('command')
    args = parser.parse_args(args=argv)
    if args.command == 'selfcheck':
        sys.argv = []
        print('Trying to connect to a Metview installation...')
        try:
            from . import bindings as _bindings
        except Exception as exp:
            print('Could not find a valid Metview installation')
            raise(exp)
        mv = dict()
        _bindings.bind_functions(mv, module_name='mv')
        del _bindings

        try:
            mv['print']('Hello world - printed from Metview!')
        except Exception as exp:
            print('Could not print a greeting from Metview')
            raise(exp)

        mv_version_f = mv['version_info']
        mv_version = mv_version_f()
        mv_maj = str(int(mv_version['metview_major']))
        mv_min = str(int(mv_version['metview_minor']))
        mv_rev = str(int(mv_version['metview_revision']))
        mv_version_string = mv_maj + '.' + mv_min + '.' + mv_rev
        print('Metview version', mv_version_string, 'found')

        print("Your system is ready.")
    else:
        raise RuntimeError("Command not recognised %r. See usage with --help." % args.command)


if __name__ == '__main__':
    main()
