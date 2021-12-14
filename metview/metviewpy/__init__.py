# (C) Copyright 2017- ECMWF.
#
# This software is licensed under the terms of the Apache Licence Version 2.0
# which can be obtained at http://www.apache.org/licenses/LICENSE-2.0.
#
# In applying this licence, ECMWF does not waive the privileges and immunities
# granted to it by virtue of its status as an intergovernmental organisation
# nor does it submit to any jurisdiction.
#

import os


# if we're running pytest, it will need the fieldset functionality, so detect if it
# is running and if so, import the user-facing functions


def running_from_pytest():
    from inspect import stack

    call_stack = [s.function for s in stack()]
    return "pytest_collection" in call_stack


if "METVIEW_PYTHON_ONLY" in os.environ or running_from_pytest():

    from . import fieldset

    fieldset.bind_functions(globals(), module_name=__name__)
