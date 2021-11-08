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

import metview.pure_python.maths as maths
from .temporary import temp_file


class CodesHandle:
    """Wraps an ecCodes handle"""

    missing_value = 1e34

    def __init__(self, handle, path, offset):
        self.handle = handle
        self.path = path
        self.offset = offset
        eccodes.codes_set(handle, "missingValue", self.missing_value)

    def __del__(self):
        # print("CodesHandle:release ", self)
        eccodes.codes_release(self.handle)

    def clone(self):
        new_handle = eccodes.codes_clone(self.handle)
        return CodesHandle(new_handle, None, None)

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
        vals = eccodes.codes_get_values(self.handle)
        if self.get_long("bitmapPresent"):
            vals[vals == self.missing_value] = np.nan
        return vals

    def write(self, fout):
        eccodes.codes_write(self.handle, fout)


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

    def __init__(self, handle, gribfile, keep_values_in_memory=False, temp=None):
        self.handle = handle
        self.gribfile = gribfile
        self.temp = temp
        self.vals = None
        self.keep_values_in_memory = keep_values_in_memory

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
        if self.vals is None:
            vals = self.handle.get_values()
            if self.keep_values_in_memory:
                self.vals = vals
        else:
            vals = self.vals
        return vals

    def write(self, fout, temp=None):
        self.temp = temp  # store a reference to the temp file object for persistence
        self.handle.write(fout)

    def clone(self):
        c = Field(self.handle.clone(), self.gribfile, self.keep_values_in_memory,)
        c.vals = None
        return c

    def field_func(self, func):
        """Applies a function to all values, returning a new Field"""
        result = self.clone()
        result.vals = func(self.values())
        return result


class Fieldset:
    """A set of Fields, each of which can come from different GRIB files"""

    def __init__(
        self, path=None, fields=None, keep_values_in_memory=False, temporary=False
    ):
        self.fields = []
        self.count = 0
        self.temporary = None

        if path:
            g = GribFile(path)
            self.count = len(g)
            for handle in g:
                self.fields.append(Field(handle, path, keep_values_in_memory))
        if temporary:
            self.temporary = temp_file()
        if fields:
            self.fields = fields

    def __len__(self):
        return len(self.fields)

    @staticmethod
    def _list_or_single(lst):
        if len(lst) == 1:
            lst = lst[0]
        return lst

    @staticmethod
    def _always_list(items):
        if not isinstance(items, list):
            return [items]
        return items

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

    # TODO: grib_get() general function

    # TODO: grib_set functions

    def values(self):
        ret = [x.values() for x in self.fields]
        ret = Fieldset._list_or_single(ret)
        if isinstance(ret, list):  # create a 2D array
            ret = np.stack(ret, axis=0)

        return ret

    def write(self, path):
        with open(path, "wb") as fout:
            for f in self.fields:
                f.write(fout)
            fout.close()

    def _append_field(self, field):
        self.fields.append(field)

    def __getitem__(self, index):
        try:
            if isinstance(index, np.ndarray):
                return Fieldset(fields=[self.fields[i] for i in index])
            else:
                return Fieldset(fields=self._always_list(self.fields[index]))
        except IndexError as ide:
            print("This Fieldset contains", len(self), "fields")
            raise ide

    def field_func(self, func):
        """Applies a function to all values in all fields"""
        result = Fieldset(temporary=True)
        with open(result.temporary.path, "wb") as fout:
            for f in self.fields:
                result._append_field(f.field_func(func))
                result.fields[-1].write(fout, temp=result.temporary)
        return result

    def abs(self):
        return self.field_func(maths.abs)

    def __neg__(self):
        return self.field_func(maths.neg)

    # TODO: add all the field_func functions

    # TODO: add all field_field_func functions

    # TODO: add all field_scalar_func functions

    # TODO: allow these methods to be called as functions (?)

    # TODO: function to write to single file if fields from different files
