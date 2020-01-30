import logging

import cffi
import sys

ffibuilder = cffi.FFI()
ffibuilder.set_source(
    "metview._bindings", "#include <metview.h>", libraries=["MvMacro"],
)
ffibuilder.cdef(open("metview/metview.h").read())

if __name__ == "__main__":
    try:
        ffibuilder.compile(verbose=True)
    except Exception:
        logging.exception("can't compile Metview bindings")
        sys.exit(1)
