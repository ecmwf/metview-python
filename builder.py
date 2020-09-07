# (C) Copyright 2017- ECMWF.
#
# This software is licensed under the terms of the Apache Licence Version 2.0
# which can be obtained at http://www.apache.org/licenses/LICENSE-2.0.
#
# In applying this licence, ECMWF does not waive the privileges and immunities
# granted to it by virtue of its status as an intergovernmental organisation
# nor does it submit to any jurisdiction.

import logging

import cffi
import sys

ffibuilder = cffi.FFI()
ffibuilder.set_source(
    "metview._bindings",
    "#include <metview.h>",
    libraries=["MvMacro"],
)
ffibuilder.cdef(open("metview/metview.h").read())

if __name__ == "__main__":
    try:
        ffibuilder.compile(verbose=True)
    except Exception:
        logging.exception("can't compile Metview bindings")
        sys.exit(1)
