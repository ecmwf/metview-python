# (C) Copyright 2017- ECMWF.
#
# This software is licensed under the terms of the Apache Licence Version 2.0
# which can be obtained at http://www.apache.org/licenses/LICENSE-2.0.
#
# In applying this licence, ECMWF does not waive the privileges and immunities
# granted to it by virtue of its status as an intergovernmental organisation
# nor does it submit to any jurisdiction.

# requires a Python 3 interpreter
import sys

if sys.version_info[0] < 3:  # pragma: no cover
    raise EnvironmentError(
        "Metview's Python interface requires Python 3. You are using Python "
        + repr(sys.version_info)
    )


# if the user has started via "python -m metview selfcheck"
# then we do not want to import anything yet because we want to
# catch errors differently

if len(sys.argv) != 2 or sys.argv[0] != "-m" or sys.argv[1] != "selfcheck":

    from . import bindings as _bindings

    _bindings.bind_functions(globals(), module_name=__name__)

    # Remove "_bindings" from the public API.
    del _bindings


from . import gallery
from . import style
from . import indexer
from . import title
from . import layout
