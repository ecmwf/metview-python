
import io
import os

from cffi import FFI


def read(fname):
    file_path = os.path.join(os.path.dirname(__file__), fname)
    return io.open(file_path, encoding='utf-8').read()


ffibuilder = FFI()
ffibuilder.set_source('mpy._metview', '',
    libraries=['MvMacro'],
    library_dirs=os.environ.get('LD_LIBRARY_PATH', '').split(':'),
    include_dirs=[],
)
ffibuilder.cdef(read('mpy/metview.h'))
