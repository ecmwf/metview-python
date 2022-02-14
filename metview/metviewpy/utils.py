#
# (C) Copyright 2017- ECMWF.
#
# This software is licensed under the terms of the Apache Licence Version 2.0
# which can be obtained at http://www.apache.org/licenses/LICENSE-2.0.
#
# In applying this licence, ECMWF does not waive the privileges and immunities
# granted to it by virtue of its status as an intergovernmental organisation
# nor does it submit to any jurisdiction.
#

import datetime
import getpass
import glob
import logging
import math
from pathlib import Path
import shutil
import os
import re
import tempfile

LOG = logging.getLogger(__name__)


CACHE_DIR = os.path.join(tempfile.gettempdir(), f"mpy-{getpass.getuser()}")


def deacc(fs, key=None, skip_first=False, mark_derived=False):
    r = None
    if key is None or key == "":
        if len(fs) > 1:
            v = fs[1:] - fs[:-1]
        if not skip_first:
            r = fs[0] * 0
            r = r.merge(v)
        else:
            r = v
    else:
        if not isinstance(key, str):
            raise TypeError(f"deacc(): key must be a str (got {type(key)})!")
        fs._get_db().load([key])
        key_vals = fs._unique_metadata(key)
        if key_vals:
            v = fs.select({key: key_vals[0]})
            gr_num = len(v)
            r = None
            if not skip_first:
                r = v * 0
            for i in range(1, len(key_vals)):
                v_next = fs.select({key: key_vals[i]})
                if len(v_next) != gr_num:
                    raise ValueError(
                        f"deacc(): unexpected number of fields (={len(v_next)}) found for {key}={key_vals[i]}! For each {key} value the number of fields must be the same as for {key}={key_vals[0]} (={gr_num})!"
                    )
                if r is None:
                    r = v_next - v
                else:
                    # print(f"i={i}")
                    # v.ls()
                    # v_next.ls()
                    r.append(v_next - v)
                v = v_next
    if not mark_derived:
        r = r.grib_set_long(["generatingProcessIdentifier", 148])
    return r


def date_from_str(d_str):
    # yyyymmdd
    if len(d_str) == 8:
        return datetime.datetime.strptime(d_str, "%Y%m%d")
    # yyyy-mm-dd ....
    elif len(d_str) >= 10 and d_str[4] == "-" and d_str[7] == "-":
        # yyyy-mm-dd
        if len(d_str) == 10:
            return datetime.datetime.strptime(d_str, "%Y-%m-%d")
        # yyyy-mm-dd hh
        elif len(d_str) == 13:
            return datetime.datetime.strptime(d_str, "%Y-%m-%d %H")
        # yyyy-mm-dd hh:mm
        elif len(d_str) == 16:
            return datetime.datetime.strptime(d_str, "%Y-%m-%d %H:%M")
        # yyyy-mm-dd hh:mm:ss
        elif len(d_str) == 19:
            return datetime.datetime.strptime(d_str, "%Y-%m-%d %H:%M:%S")
    # yyyymmdd.decimal_day
    elif len(d_str) > 8 and d_str[8] == ".":
        f = float("0" + d_str[8:])
        if f >= 1:
            raise ValueError
        else:
            return datetime.datetime.strptime(d_str[:8], "%Y%m%d") + datetime.timedelta(
                seconds=int(f * 86400)
            )
    # mmdd or mdd (as in daily climatologies)
    elif len(d_str) in [3, 4]:
        # try to convert to datatime to see if it is valid date
        d = datetime.datetime.strptime("0004" + d_str.rjust(4, "0"), "%Y%m%d")
        # we just return a tuple since datetime cannot have an invalid date
        return (d.month, d.day)
    # b-dd e.g. apr-02 (as in daily climatologies)
    elif len(d_str) == 6 and d_str[3] == "-":
        months = [
            "jan",
            "feb",
            "mar",
            "apr",
            "may",
            "jun",
            "jul",
            "aug",
            "sep",
            "nov",
            "dec",
        ]
        m = d_str[0:3].lower()
        try:
            m_num = months.index(m) + 1
        except:
            raise ValueError(f"Invalid month={m} specified in date={d_str}!")
        # try to convert to datatime to see if it is valid date
        d = datetime.datetime.strptime("0004" + f"{m_num:02}" + d_str[4:6], "%Y%m%d")
        # we just return a tuple since datetime cannot have an invalid date
        return (d.month, d.day)


def time_from_str(t_str):
    h = m = 0
    if not ":" in t_str:
        # formats: h[mm], hh[mm]
        if len(t_str) in [1, 2]:
            h = int(t_str)
        elif len(t_str) in [3, 4]:
            r = int(t_str)
            h = int(r / 100)
            m = int(r - h * 100)
        else:
            raise Exception(f"Invalid time={t_str}")
    else:
        # formats: h:mm, hh:mm
        lst = t_str.split(":")
        if len(lst) >= 2:
            h = int(lst[0])
            m = int(lst[1])
        else:
            raise Exception(f"Invalid time={t_str}")

    return datetime.time(hour=h, minute=m)


def date_from_ecc_keys(d, t):
    try:
        return datetime.datetime.combine(
            date_from_str(str(d)).date(), time_from_str(str(t))
        )
    except:
        return None


def is_fieldset_type(thing):
    # will return True for binary or python fieldset objects
    return "Fieldset" in thing.__class__.__name__


def get_file_list(path, file_name_pattern=None):
    m = None
    # if isinstance(file_name_pattern, re.Pattern):
    #    m = file_name_pattern.match
    # elif isinstance(file_name_pattern, str):
    if isinstance(file_name_pattern, str):
        if file_name_pattern.startswith('re"'):
            m = re.compile(file_name_pattern[3:-1]).match

    # print(f"path={path} file_name_pattern={file_name_pattern}")

    if m is not None:
        return [os.path.join(path, f) for f in filter(m, os.listdir(path=path))]
    else:
        if isinstance(file_name_pattern, str) and file_name_pattern != "":
            path = os.path.join(path, file_name_pattern)
        if not has_globbing(path):
            return [path]
        else:
            return sorted(glob.glob(path))


def has_globbing(text):
    for x in ["*", "?"]:
        if x in text:
            return True
    if "[" in text and "]" in text:
        return True
    else:
        return False


def unpack(file_path, remove=False):
    if any(file_path.endswith(x) for x in [".tar", ".tar.gz", ".tar.bz2"]):
        target_dir = os.path.dirname(file_path)
        LOG.debug(f"file_path={file_path} target_dir={target_dir}")
        shutil.unpack_archive(file_path, target_dir)
        if remove:
            os.remove(file_path)


def download(url, target):
    from tqdm import tqdm
    import requests

    resp = requests.get(url, stream=True)
    total = int(resp.headers.get("content-length", 0))
    with open(target, "wb") as file, tqdm(
        desc=target,
        total=total,
        unit="iB",
        unit_scale=True,
        unit_divisor=1024,
    ) as bar:
        for data in resp.iter_content(chunk_size=1024):
            size = file.write(data)
            bar.update(size)


class Cache:
    ROOT_DIR = os.path.join(tempfile.gettempdir(), f"mpy_ds_{getpass.getuser()}")

    def all_exists(self, items, path):
        for name in items:
            p = os.path.join(path, name)
            # print(f"p={p}")
            if not os.path.exists(p):
                return False
            elif os.path.isdir(p):
                cont_file = os.path.join(path, f".content_{name}")
                if os.path.exists(cont_file):
                    with open(cont_file, "r") as f:
                        try:
                            for item in f.read().split("\n"):
                                if item and not os.path.exists(
                                    os.path.join(path, item)
                                ):
                                    return False
                        except:
                            return False
                else:
                    return False
        return True

    def make_reference(self, items, path):
        for name in items:
            p = os.path.join(path, name)
            if os.path.isdir(p):
                cont_file = os.path.join(path, f".content_{name}")
                with open(cont_file, "w") as f:
                    for item in Path(p).rglob("*"):
                        if item.is_file():
                            f.write(item.relative_to(path).as_posix() + "\n")


CACHE = Cache()
