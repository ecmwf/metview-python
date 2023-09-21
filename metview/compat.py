# (C) Copyright 2017- ECMWF.
#
# This software is licensed under the terms of the Apache Licence Version 2.0
# which can be obtained at http://www.apache.org/licenses/LICENSE-2.0.
#
# In applying this licence, ECMWF does not waive the privileges and immunities
# granted to it by virtue of its status as an intergovernmental organisation
# nor does it submit to any jurisdiction.

import numpy as np

import metview as mv


def concat(*args):
    if len(args) <= 1:
        raise ValueError(f"concat requires at least 2 arguments, got only {len(args)}")

    vals = list(args)
    if vals[0] is None:
        vals.pop(0)
        if len(vals) == 1:
            return vals[0]

    # concatenate strings
    if isinstance(vals[0], str):
        return "".join([str(v) for v in vals])
    elif isinstance(vals[0], np.ndarray):
        return np.concatenate(vals)
    elif isinstance(
        vals[0],
        (mv.Fieldset, mv.bindings.Geopoints, mv.bindings.GeopointSet, mv.bindings.Bufr),
    ):
        return mv.merge(*vals)
    elif isinstance(vals[0], list):
        first = []
        for v in vals:
            if isinstance(v, list):
                first.extend(v)
            else:
                first.append(v)
        return first

    raise ValueError(f"concat failed to handle the specified arguments={args}")


def index4(vals, start, stop, step, num):
    """
    Return a boolean index ndarray to select a subset of elements from ``vals``.

    Parameters
    ----------
    vals: ndarray
        Input array.
    start: int
        Start index.
    stop: int
        Stop index.
    step: int
        Step.
    num: int
        Number of elements to be selected for each step.

    Returns
    -------
    ndarray
        Boolean index array

    Examples
    --------

    >>> import numpy as np
    >>> import metview
    >>> vals = np.array(list(range(12)))
    >>> r = index4(vals, 0, 11, 4, 2)
    [ True  True  True  True  True  True False False False False False False]
    a[]
    >>> vals[r]
    array([0, 1, 4, 5, 8, 9])

    """
    num = min(num, step)
    m = np.zeros(len(vals), dtype=bool)
    for i in range(start, stop, step):
        m[i : i + num] = 1
    return m
