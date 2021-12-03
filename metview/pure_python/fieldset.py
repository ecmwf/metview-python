# (C) Copyright 2017- ECMWF.
#
# This software is licensed under the terms of the Apache Licence Version 2.0
# which can be obtained at http://www.apache.org/licenses/LICENSE-2.0.
#
# In applying this licence, ECMWF does not waive the privileges and immunities
# granted to it by virtue of its status as an intergovernmental organisation
# nor does it submit to any jurisdiction.


from inspect import signature
from os import WEXITED
import sys

import numpy as np
import eccodes

import metview.pure_python.maths as maths
from .temporary import temp_file

import metview.indexdb as indexdb
import metview.utils as utils


BITS_PER_VALUE_FOR_WRITING = 24


class CodesHandle:
    """Wraps an ecCodes handle"""

    missing_value = 1e34

    def __init__(self, handle, path, offset):
        self.handle = handle
        self.path = path
        self.offset = offset
        eccodes.codes_set(handle, "missingValue", CodesHandle.missing_value)

    def __del__(self):
        # print("CodesHandle:release ", self)
        eccodes.codes_release(self.handle)

    def clone(self):
        new_handle = eccodes.codes_clone(self.handle)
        return CodesHandle(new_handle, None, None)

    # def __str__(self):
    #    s = "CodesHandle("
    #    return s + str(self.handle) + "," + self.path + "," + str(self.offset) + ")"

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

    def get_native(self, key):
        if eccodes.codes_get_size(self.handle, key) > 1:
            return eccodes.codes_get_array(self.handle, key)
        else:
            return eccodes.codes_get(self.handle, key)

    def get_values(self):
        vals = eccodes.codes_get_values(self.handle)
        if self.get_long("bitmapPresent"):
            vals[vals == CodesHandle.missing_value] = np.nan
        return vals

    def set_string(self, key, value):
        eccodes.codes_set_string(self.handle, key, value)

    def set_long(self, key, value):
        eccodes.codes_set_long(self.handle, key, value)

    def set_double(self, key, value):
        eccodes.codes_set_double(self.handle, key, value)

    def set_double_array(self, key, value):
        eccodes.codes_set_double_array(self.handle, key, value)

    def set_values(self, value):
        # replace nans with missing values
        values_nans_replaced = np.nan_to_num(
            value, copy=True, nan=CodesHandle.missing_value
        )
        self.set_long("bitsPerValue", BITS_PER_VALUE_FOR_WRITING)
        self.set_double_array("values", values_nans_replaced)

    def write(self, fout):
        eccodes.codes_write(self.handle, fout)


class GribFile:
    """Encapsulates a GRIB file, giving access to an iteration of CodesHandles"""

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

    KEY_TYPES = {
        "s": "grib_get_string",
        "d": "grib_get_double",
        "l": "grib_get_long",
        "la": "grib_get_long_array",
        "da": "grib_get_double_array",
        "n": "grib_get_native",
    }

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

    def grib_get_native(self, key):
        return self.handle.get_native(key)

    def values(self):
        if self.vals is None:
            vals = self.handle.get_values()
            if self.keep_values_in_memory:
                self.vals = vals
        else:
            vals = self.vals
        return vals

    def latitudes(self):
        return self.handle.get_double_array("latitudes")

    def longitudes(self):
        return self.handle.get_double_array("longitudes")

    def grib_get(self, keys, grouping):
        result = []
        for key in keys:
            ktype = "s"  # default is str
            parts = key.split(":")
            if len(parts) == 2:
                key = parts[0]
                ktype = parts[1]
            try:
                funcname = Field.KEY_TYPES[ktype]
            except Exception as e:
                print("Invalid key type: ", ktype)
                raise e
            func = getattr(self, funcname)
            result.append(func(key))
        return result

    def grib_set_string(self, key, value):
        result = self.clone()
        result.handle.set_string(key, value)
        return result

    def grib_set_long(self, key, value):
        result = self.clone()
        result.handle.set_long(key, value)
        return result

    def grib_set_double(self, key, value):
        result = self.clone()
        result.handle.set_double(key, value)
        return result

    # def grib_set_double_array(self, key, value):
    #    result = self.clone()
    #    result.handle.set_double_array(key, value)
    #    return result

    def encode_values(self, value):
        self.handle.set_long("bitmapPresent", 1)
        self.handle.set_values(value)
        if not self.keep_values_in_memory:
            self.vals = None

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
        result.encode_values(result.vals)
        return result

    def field_other_func(self, func, other, reverse_args=False):
        """Applies a function with something to all values, returning a new Field"""
        result = self.clone()
        if isinstance(other, Field):
            other = other.values()
        if reverse_args:
            result.vals = func(other, self.values())
        else:
            result.vals = func(self.values(), other)
        result.encode_values(result.vals)
        return result


# docorator to implement math functions in Fieldset
def wrap_maths(cls):
    def wrap_single_method(fn):
        def wrapper(self, *args, **kwargs):
            return self.field_func(fn)

        return wrapper

    def wrap_double_method(fn):
        def wrapper(self, *args, **kwargs):
            return self.fieldset_other_func(fn, *args, **kwargs)

        return wrapper

    for name, fn in cls.WRAP_MATHS_ATTRS.items():
        n = len(signature(fn).parameters)
        if n == 1:
            setattr(cls, name, wrap_single_method(fn))
        elif n == 2:
            setattr(cls, name, wrap_double_method(fn))
    return cls


@wrap_maths
class Fieldset:
    """A set of Fields, each of which can come from different GRIB files"""

    WRAP_MATHS_ATTRS = {
        "abs": maths.abs,
        "acos": maths.acos,
        "asin": maths.asin,
        "atan": maths.atan,
        "atan2": maths.atan2,
        "cos": maths.cos,
        "div": maths.floor_div,
        "exp": maths.exp,
        "log": maths.log,
        "log10": maths.log10,
        "mod": maths.mod,
        "sgn": maths.sgn,
        "sin": maths.sin,
        "square": maths.square,
        "sqrt": maths.sqrt,
        "tan": maths.tan,
    }

    # QUALIFIER_MAP = {"float": "d"}

    # INT_KEYS = ["Nx", "Ny", "number"]

    def __init__(
        self, path=None, fields=None, keep_values_in_memory=False, temporary=False
    ):
        self.fields = []
        self.count = 0
        self.temporary = None
        self._db = None

        if (path is not None) and (fields is not None):
            raise ValueError("Fieldset cannot take both path and fields")

        if path:
            if isinstance(path, list):
                v = []
                for p in path:
                    v.extend(utils.get_file_list(p))
                path = v
            else:
                path = utils.get_file_list(path)

            for p in path:
                g = GribFile(p)
                self.count = len(g)
                for handle in g:
                    self.fields.append(Field(handle, p, keep_values_in_memory))
        if temporary:
            self.temporary = temp_file()
        if fields:
            self.fields = fields

    def __len__(self):
        return len(self.fields)

    def __str__(self):
        n = len(self)
        s = "s" if n > 1 else ""
        return f"Fieldset ({n} field{s})"

    @staticmethod
    def _list_or_single(lst):
        return lst if len(lst) != 1 else lst[0]

    @staticmethod
    def _always_list(items):
        return items if isinstance(items, list) else [items]

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

    def grib_get(self, keys, grouping="field"):
        if grouping != "field" and grouping != "key":
            raise ValueError("grib_get: grouping must be field or key, not " + grouping)
        ret = [x.grib_get(keys, grouping) for x in self.fields]
        if grouping == "key":
            ret = list(map(list, zip(*ret)))  # transpose lists of lists
        return ret

    def _grib_set_any(self, key, value, funcname):
        result = Fieldset(temporary=True)
        with open(result.temporary.path, "wb") as fout:
            for f in self.fields:
                func = getattr(f, funcname)
                result._append_field(func(key, value))
                result.fields[-1].write(fout, temp=result.temporary)
        return result

    def grib_set_string(self, key, value):
        return self._grib_set_any(key, value, "grib_set_string")

    def grib_set_long(self, key, value):
        return self._grib_set_any(key, value, "grib_set_long")

    def grib_set_double(self, key, value):
        return self._grib_set_any(key, value, "grib_set_double")

    # def grib_set_double_array(self, key, value):
    #    return self._grib_set_any(key, value, "grib_set_double_array")

    def values(self):
        v = [x.values() for x in self.fields]
        return self._make_2d_array(v)

    def set_values(self, values):
        if isinstance(values, list):
            list_of_arrays = values
        else:
            if len(values.shape) > 1:
                list_of_arrays = [a for a in values]
            else:
                list_of_arrays = [values]
        if len(list_of_arrays) != len(self.fields):
            msg = str(len(list_of_arrays)) + " instead of " + str(len(self.fields))
            raise ValueError("set_values has the wrong number of arrays: " + msg)

        return self.fieldset_other_func(
            maths.set_from_other, list_of_arrays, index_other=True
        )

    def write(self, path):
        with open(path, "wb") as fout:
            for f in self.fields:
                f.write(fout)

    def _append_field(self, field):
        self.fields.append(field)

    def __getitem__(self, index):
        try:
            if isinstance(index, np.ndarray):
                return Fieldset(fields=[self.fields[i] for i in index])
            # # GRIB key
            # elif isinstance(index, str):
            #     keyname = index
            #     qualifier = "n"
            #     parts = keyname.split(":")
            #     if len(parts) > 1:
            #         keyname = parts[0]
            #         qualifier = Fieldset.QUALIFIER_MAP[parts[1]]

            #     native_key = keyname + ":" + qualifier
            #     # print("native_key", native_key)
            #     value = self.grib_get([native_key])[0][0]
            #     # print(value)
            #     if value is None:
            #         raise IndexError
            #     if index in Fieldset.INT_KEYS:
            #         # print("int value:", int(value))
            #         return int(value)
            #     # if isinstance(value, float):
            #     #    return int(value)
            #     return value

            else:
                return Fieldset(fields=self._always_list(self.fields[index]))
        except IndexError as ide:
            # print("This Fieldset contains", len(self), "fields; index is", index)
            raise ide

    def append(self, other):
        self.fields = self.fields + other.fields

    def merge(self, other):
        result = Fieldset(fields=self.fields, temporary=True)
        result.append(other)
        return result

    # def items(self):
    #     its = []
    #     for i in range(len(self)):
    #         its.append((i, Fieldset(fields=[self.fields[i]])))
    #     return its

    # def to_dataset(self, via_file=True, **kwarg):
    #     # soft dependency on cfgrib
    #     try:
    #         import xarray as xr
    #     except ImportError:  # pragma: no cover
    #         print("Package xarray not found. Try running 'pip install xarray'.")
    #         raise
    #     # dataset = xr.open_dataset(self.url(), engine="cfgrib", backend_kwargs=kwarg)
    #     if via_file:
    #         dataset = xr.open_dataset(self.url(), engine="cfgrib", backend_kwargs=kwarg)
    #     else:
    #         print("Using experimental cfgrib interface to go directly from Fieldset")
    #         dataset = xr.open_dataset(self, engine="cfgrib", backend_kwargs=kwarg)
    #     return dataset

    def field_func(self, func):
        """Applies a function to all values in all fields"""
        result = Fieldset(temporary=True)
        with open(result.temporary.path, "wb") as fout:
            for f in self.fields:
                result._append_field(f.field_func(func))
                result.fields[-1].write(fout, temp=result.temporary)
        return result

    def __neg__(self):
        return self.field_func(maths.neg)

    def __pos__(self):
        return self.field_func(maths.pos)

    def __invert__(self):
        return self.field_func(maths.not_func)

    def fieldset_other_func(self, func, other, reverse_args=False, index_other=False):
        """Applies a function to a fieldset and a scalar/fieldset, e.g. F+5"""
        result = Fieldset(temporary=True)
        with open(result.temporary.path, "wb") as fout:
            if isinstance(other, Fieldset):
                for f, g in zip(self.fields, other.fields):
                    new_field = f.field_other_func(func, g, reverse_args=reverse_args)
                    result._append_field(new_field)
                    result.fields[-1].write(fout, temp=result.temporary)
            elif index_other:
                for f, g in zip(self.fields, other):
                    new_field = f.field_other_func(func, g, reverse_args=reverse_args)
                    result._append_field(new_field)
                    result.fields[-1].write(fout, temp=result.temporary)
            else:
                for f in self.fields:
                    new_field = f.field_other_func(
                        func, other, reverse_args=reverse_args
                    )
                    result._append_field(new_field)
                    result.fields[-1].write(fout, temp=result.temporary)
        return result

    def __add__(self, other):
        return self.fieldset_other_func(maths.add, other)

    def __radd__(self, other):
        return self.fieldset_other_func(maths.add, other, reverse_args=True)

    def __sub__(self, other):
        return self.fieldset_other_func(maths.sub, other)

    def __rsub__(self, other):
        return self.fieldset_other_func(maths.sub, other, reverse_args=True)

    def __mul__(self, other):
        return self.fieldset_other_func(maths.mul, other)

    def __rmul__(self, other):
        return self.fieldset_other_func(maths.mul, other, reverse_args=True)

    def __truediv__(self, other):
        return self.fieldset_other_func(maths.div, other)

    def __rtruediv__(self, other):
        return self.fieldset_other_func(maths.div, other, reverse_args=True)

    def __pow__(self, other):
        return self.fieldset_other_func(maths.pow, other)

    def __rpow__(self, other):
        return self.fieldset_other_func(maths.pow, other, reverse_args=True)

    def __ge__(self, other):
        return self.fieldset_other_func(maths.ge, other)

    def __gt__(self, other):
        return self.fieldset_other_func(maths.gt, other)

    def __le__(self, other):
        return self.fieldset_other_func(maths.le, other)

    def __lt__(self, other):
        return self.fieldset_other_func(maths.lt, other)

    def __eq__(self, other):
        return self.fieldset_other_func(maths.eq, other)

    def __ne__(self, other):
        return self.fieldset_other_func(maths.ne, other)

    def __and__(self, other):
        return self.fieldset_other_func(maths.and_func, other)

    def __or__(self, other):
        return self.fieldset_other_func(maths.or_func, other)

    def base_date(self):
        result = []
        for f in self.fields:
            md = f.grib_get(["dataDate", "dataTime"], "field")
            result.append(utils.date_from_ecc_keys(md[0], md[1]))
        return Fieldset._list_or_single(result)

    def valid_date(self):
        result = []
        for f in self.fields:
            md = f.grib_get(["validityDate", "validityTime"], "field")
            result.append(utils.date_from_ecc_keys(md[0], md[1]))
        return Fieldset._list_or_single(result)

    def accumulate(self):
        result = np.array([np.nan] * len(self.fields))
        for i, f in enumerate(self.fields):
            result[i] = np.sum(f.values())
        return result

    def average(self):
        result = np.array([np.nan] * len(self.fields))
        for i, f in enumerate(self.fields):
            result[i] = f.values().mean()
        return result

    def maxvalue(self):
        result = np.array([np.nan] * len(self.fields))
        for i, f in enumerate(self.fields):
            result[i] = f.values().max()
        return result.max()

    def minvalue(self):
        result = np.array([np.nan] * len(self.fields))
        for i, f in enumerate(self.fields):
            result[i] = f.values().min()
        return result.min()

    def _make_single_result(self, v):
        assert len(self.fields) > 0
        result = Fieldset(temporary=True)
        with open(result.temporary.path, "wb") as fout:
            f = self.fields[0].clone()
            f.encode_values(v)
            result._append_field(f)
            result.fields[-1].write(fout, temp=result.temporary)
        return result

    def mean(self):
        if len(self.fields) > 0:
            v = self.fields[0].values()
            for i in range(1, len(self.fields)):
                v += self.fields[i].values()
            v = v / len(self.fields)
            return self._make_single_result(v)
        else:
            return None

    def rms(self):
        if len(self.fields) > 0:
            v = np.square(self.fields[0].values())
            for i in range(1, len(self.fields)):
                v += np.square(self.fields[i].values())
            v = np.sqrt(v / len(self.fields))
            return self._make_single_result(v)
        else:
            return None

    def stdev(self):
        v = self._compute_var()
        return self._make_single_result(np.sqrt(v)) if v is not None else None

    def sum(self):
        if len(self.fields) > 0:
            v = self.fields[0].values()
            for i in range(1, len(self.fields)):
                v += self.fields[i].values()
            return self._make_single_result(v)
        else:
            return None

    def var(self):
        v = self._compute_var()
        return self._make_single_result(v) if v is not None else None

    def _compute_var(self):
        if len(self.fields) > 0:
            v2 = self.fields[0].values()
            v1 = np.square(v2)
            for i in range(1, len(self.fields)):
                v = self.fields[i].values()
                v1 += np.square(v)
                v2 += v
            return v1 / len(self.fields) - np.square(v2 / len(self.fields))

    def latitudes(self):
        v = [x.latitudes() for x in self.fields]
        return self._make_2d_array(v)

    def longitudes(self):
        v = [x.longitudes() for x in self.fields]
        return self._make_2d_array(v)

    def coslat(self):
        v = [np.cos(np.deg2rad(x.latitudes())) for x in self.fields]
        return self._make_2d_array(v)

    def sinlat(self):
        v = [np.sin(np.deg2rad(x.latitudes())) for x in self.fields]
        return self._make_2d_array(v)

    def tanlat(self):
        v = [np.tan(np.deg2rad(x.latitudes())) for x in self.fields]
        return self._make_2d_array(v)

    def _make_2d_array(self, v):
        """Forms a 2D ndarray from a list of 1D ndarrays"""
        v = Fieldset._list_or_single(v)
        return np.stack(v, axis=0) if isinstance(v, list) else v

    # TODO: add all the field_func functions

    # TODO: add all field_field_func functions

    # TODO: add all field_scalar_func functions

    # TODO: add tests for all fieldset-fieldset methods:
    # **, ==, !=, &, |

    # TODO: allow these methods to be called as functions (?)

    # TODO: function to write to single file if fields from different files

    # TODO: optimise write() to copy file if exists

    # TODO: to_dataset()

    # TODO: pickling

    # TODO: gribsetbits, default=24

    def _get_db(self):
        if self._db is None:
            self._db = indexdb.FieldsetDb(fs=self)
        assert self._db is not None
        return self._db

    def select(self, *args, **kwargs):
        if len(args) == 1 and isinstance(args[0], dict):
            return self._get_db().select(**args[0])
        else:
            return self._get_db().select(**kwargs)

    def describe(self, *args, **kwargs):
        return self._get_db().describe(*args, **kwargs)

    def ls(self, **kwargs):
        return self._get_db().ls(**kwargs)


class FieldsetCF:
    def __init__(self, fs):
        self.fs = fs

    def items(self):
        its = []
        for i in range(len(self.fs)):
            its.append((i, FieldCF(self.fs[i])))
        # print("FieldsetCF items: ", d)
        return its

    def __getitem__(self, index):
        return FieldCF(self.fs[index])


class FieldCF:

    QUALIFIER_MAP = {"float": "d"}

    INT_KEYS = ["Nx", "Ny", "number"]

    def __init__(self, fs):
        self.fs = fs

    def __getitem__(self, key):
        keyname = key
        qualifier = "n"
        parts = key.split(":")
        if len(parts) > 1:
            keyname = parts[0]
            qualifier = FieldCF.QUALIFIER_MAP[parts[1]]

        native_key = keyname + ":" + qualifier
        # print("native_key", native_key)
        value = self.fs.grib_get([native_key])[0][0]
        # print(value)
        if value is None:
            raise IndexError
        if key in FieldCF.INT_KEYS:
            # print("int value:", int(value))
            return int(value)
        # if isinstance(value, float):
        #    return int(value)
        return value


# expose all Fieldset functions as a module level function
def _make_module_func(name):
    def wrapped(fs, *args):
        return getattr(fs, name)(*args)

    return wrapped


module_obj = sys.modules[__name__]
for fn in dir(Fieldset):
    if callable(getattr(Fieldset, fn)) and not fn.startswith("_"):
        setattr(module_obj, fn, _make_module_func(fn))
