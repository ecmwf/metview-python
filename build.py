
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
        '/home/dibari/Progetti/metview_api_python/MetviewBundle-2017.05.0-Source_with_tarball/metview/src/Macro/include',
        '/home/dibari/Progetti/metview_api_python/MetviewBundle-2017.05.0-Source_with_tarball/metview/src/libUtil',
        '/home/dibari/Progetti/metview_api_python/MetviewBundle-2017.05.0-Source_with_tarball/mars-client/src',
        '/home/dibari/Progetti/metview_api_python/MetviewBundle-2017.05.0_Build_with_tarball/metview/src/libMars',
    ],
)
ffibuilder.cdef(read('mpy/metview.h'))
