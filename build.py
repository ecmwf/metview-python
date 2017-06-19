
import io
import os
import sys

from cffi import FFI


def read(fname):
    file_path = os.path.join(os.path.dirname(__file__), fname)
    return io.open(file_path, encoding='utf-8').read()


ffibuilder = FFI()
ffibuilder.set_source('mpy._metview', '',
    libraries=['MvMacro'],
    library_dirs=os.environ['LD_LIBRARY_PATH'].split(':'),
    include_dirs=[
        os.path.join(os.environ['METVIEW_DIR'], 'metview/src/Macro/include'),
        os.path.join(os.environ['METVIEW_DIR'], 'metview/src/libUtil'),
        os.path.join(os.environ['METVIEW_DIR'], 'mars-client/src'),
        os.path.join(os.environ['METVIEW_DIR'], 'metview/src/libMars'),
    ],
)
ffibuilder.cdef(read('mpy/metview.h'))
