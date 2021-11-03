# (C) Copyright 2017- ECMWF.
#
# This software is licensed under the terms of the Apache Licence Version 2.0
# which can be obtained at http://www.apache.org/licenses/LICENSE-2.0.
#
# In applying this licence, ECMWF does not waive the privileges and immunities
# granted to it by virtue of its status as an intergovernmental organisation
# nor does it submit to any jurisdiction.

import numpy as np
import eccodes


class CodesHandle:
    """Wraps an ecCodes handle"""

    def __init__(self, handle, path, offset):
        self.handle = handle
        self.path = path
        self.offset = offset

    def __del__(self):
        # print("CodesHandle:release ", self)
        eccodes.codes_release(self.handle)

    def __str__(self):
        s = "CodesHandle("
        return s + str(self.handle) + "," + self.path + "," + str(self.offset) + ")"

    def get_string(self, key):
        return eccodes.codes_get_string(self.handle, key)

    def get_long(self, key):
        return eccodes.codes_get_long(self.handle, key)

    def get_double(self, key):
        return eccodes.codes_get_double(self.handle, key)

    def get_long_array(self, key):
        return eccodes.codes_get_long_array(self.handle, key)

    def get_double_array(self, key):
        return eccodes.codes_get_double_array(self.handle, key)

    def get_values(self):
        return eccodes.codes_get_values(self.handle)


class GribFile:
    """ Encapsulates a GRIB file, giving access to an iteration of CodesHandles """

    def __init__(self, path):
        self.path = path
        self.file = open(path, "rb")
        self.num_messages = eccodes.codes_count_in_file(self.file)

    def __del__(self):
        try:
            # print("GribFile:close")
            self.file.close()
        except Exception:
            pass

    def __len__(self):
        return self.num_messages

    def __iter__(self):
        return self

    def __next__(self):
        handle = self._next_handle()
        if handle is None:
            raise StopIteration()
        return handle

    def _next_handle(self):
        offset = self.file.tell()
        handle = eccodes.codes_new_from_file(self.file, eccodes.CODES_PRODUCT_GRIB)
        if not handle:
            return None
        return CodesHandle(handle, self.path, offset)


class Field:
    """Encapsulates single GRIB message"""

    def __init__(self, handle, gribfile):
        self.handle = handle
        self.gribfile = gribfile
        # print("Field=", handle, gribfile)

    def grib_get_string(self, key):
        return self.handle.get_string(key)

    def grib_get_long(self, key):
        return self.handle.get_long(key)

    def grib_get_double(self, key):
        return self.handle.get_double(key)

    def grib_get_long_array(self, key):
        return self.handle.get_long_array(key)

    def grib_get_double_array(self, key):
        return self.handle.get_double_array(key)

    def values(self):
        return self.handle.get_values()


class Fieldset:
    """A set of Fields, each of which can come from different GRIB files"""

    def __init__(self, path=None, fields=None):
        self.fields = []
        self.count = 0
        if path:
            g = GribFile(path)
            self.count = len(g)
            for handle in g:
                self.fields.append(Field(handle, path))

    def __len__(self):
        return len(self.fields)

    @staticmethod
    def _list_or_single(lst):
        if len(lst) == 1:
            lst = lst[0]
        return lst

    def grib_get_string(self, key):
        ret = [x.grib_get_string(key) for x in self.fields]
        return Fieldset._list_or_single(ret)

    def grib_get_long(self, key):
        ret = [x.grib_get_long(key) for x in self.fields]
        return Fieldset._list_or_single(ret)

    def grib_get_double(self, key):
        ret = [x.grib_get_double(key) for x in self.fields]
        return Fieldset._list_or_single(ret)

    def grib_get_long_array(self, key):
        ret = [x.grib_get_long_array(key) for x in self.fields]
        return Fieldset._list_or_single(ret)

    def grib_get_double_array(self, key):
        ret = [x.grib_get_double_array(key) for x in self.fields]
        return Fieldset._list_or_single(ret)

    def values(self):
        ret = [x.values() for x in self.fields]
        ret = Fieldset._list_or_single(ret)
        if isinstance(ret, list):  # create a 2D array
            ret = np.stack(ret, axis=0)
        return ret
