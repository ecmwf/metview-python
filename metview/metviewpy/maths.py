# (C) Copyright 2017- ECMWF.
#
# This software is licensed under the terms of the Apache Licence Version 2.0
# which can be obtained at http://www.apache.org/licenses/LICENSE-2.0.
#
# In applying this licence, ECMWF does not waive the privileges and immunities
# granted to it by virtue of its status as an intergovernmental organisation
# nor does it submit to any jurisdiction.
import numpy as np


def neg(x):
    return -x


def pos(x):
    return x


# def abs(x):
#     return np.abs(x)


def not_func(x):
    return (~(x != 0)).astype(int)


def add(x, y):
    return x + y


def sub(x, y):
    return x - y


def mul(x, y):
    return x * y


def div(x, y):
    return x / y


def pow(x, y):
    return x**y


def ge(x, y):
    return (x >= y).astype(int)


def gt(x, y):
    return (x > y).astype(int)


def le(x, y):
    return (x <= y).astype(int)


def lt(x, y):
    return (x < y).astype(int)


def eq(x, y):
    return (x == y).astype(int)


def ne(x, y):
    return (x != y).astype(int)


def and_func(x, y):
    return ne(x, 0) * ne(y, 0)


def or_func(x, y):
    return np.clip(ne(x, 0) + ne(y, 0), 0, 1)


def set_from_other(x, y):
    return y


# single argument functions


def abs(x):
    return np.fabs(x)


def acos(x):
    return np.arccos(x)


def asin(x):
    return np.arcsin(x)


def atan(x):
    return np.arctan(x)


def cos(x):
    return np.cos(x)


def exp(x):
    return np.exp(x)


def log(x):
    return np.log(x)


def log10(x):
    return np.log10(x)


def sgn(x):
    return np.sign(x)


def square(x):
    return np.square(x)


def sqrt(x):
    return np.sqrt(x)


def sin(x):
    return np.sin(x)


def tan(x):
    return np.tan(x)


# double argument functions


def atan2(x, y):
    return np.arctan2(x, y)


def floor_div(x, y):
    return np.floor_divide(x, y)


def mod(x, y):
    return np.mod(x, y)


# bitmapping


def bitmap(x, y):
    if isinstance(y, (int, float)):
        x[x == y] = np.nan
        return x
    elif isinstance(y, np.ndarray):
        x[np.isnan(y)] = np.nan
        return x


def nobitmap(x, y):
    x[np.isnan(x)] = y
    return x
