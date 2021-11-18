# (C) Copyright 2017- ECMWF.
#
# This software is licensed under the terms of the Apache Licence Version 2.0
# which can be obtained at http://www.apache.org/licenses/LICENSE-2.0.
#
# In applying this licence, ECMWF does not waive the privileges and immunities
# granted to it by virtue of its status as an intergovernmental organisation
# nor does it submit to any jurisdiction.

import metview as mv

# this module is meant to expose some ui specific functions


def dialog(*args):
    res = mv._dialog(*args)
    return {k: v for k, v in res.items() if not k.startswith("_")}


def any(**kwargs):
    return mv._any(**kwargs)


def colour(**kwargs):
    return mv._colour(**kwargs)


def icon(**kwargs):
    return mv._icon(**kwargs)


def option_menu(**kwargs):
    return mv._option_menu(**kwargs)


def slider(**kwargs):
    return mv._slider(**kwargs)


def toggle(**kwargs):
    return mv._toggle(**kwargs)
