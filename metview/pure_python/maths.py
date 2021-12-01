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


def abs(x):
    return np.abs(x)


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
    return x ** y


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
