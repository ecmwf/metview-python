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

# requires a Python 3 interpreter
import sys
if sys.version_info[0] < 3:
    raise EnvironmentError("Metview's Python interface requires Python 3. You are using Python "
                           + repr(sys.version_info))


# if the user has started via "python -m metview selfcheck"
# then we do not want to import anything yet because we want to
# catch errors differently

if len(sys.argv) != 2 or sys.argv[0] != "-m" or sys.argv[1] != "selfcheck":

    from . import bindings as _bindings

    _bindings.bind_functions(globals(), module_name=__name__)

    # Remove "_bindings" from the public API.
    del _bindings
