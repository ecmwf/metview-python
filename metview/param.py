# (C) Copyright 2017- ECMWF.
#
# This software is licensed under the terms of the Apache Licence Version 2.0
# which can be obtained at http://www.apache.org/licenses/LICENSE-2.0.
#
# In applying this licence, ECMWF does not waive the privileges and immunities
# granted to it by virtue of its status as an intergovernmental organisation
# nor does it submit to any jurisdiction.
#

import copy
import datetime
import logging
import os
import re
import sys

import metview as mv
from metview.indexer import GribIndexer

# logging.basicConfig(level=logging.INFO, format="%(levelname)s - %(message)s")
# logging.basicConfig(level=logging.DEBUG, format="%(levelname)s - %(message)s")
LOG = logging.getLogger(__name__)


class ParamInfo:
    SUFFIXES = {
        "hPa": "isobaricInhPa",
        "hpa": "isobaricInhPa",
        "K": "theta",
        "ml": "hybrid",
    }
    LEVEL_TYPES = {"sfc": "surface", "pl": "isobaricInhPa", "ml": "hybrid"}
    LEVEL_RE = re.compile(r"(\d+)")
    NUM_RE = re.compile(r"[0-9]+")
    SURF_RE = re.compile(r"^\d+\w+")
    # SURF_NAME_MAPPER = {"t2": "2t", "q2": "2q", "u10": "10u", "v10": "10v"}
    KNOWN_SURF_NAMES = ["2t", "2q", "10u", "10v", "msl", "wind10m"]
    VECTOR_NAMES = ["wind10m", "wind3d", "wind"]  # the longest ones first

    def __init__(self, name, meta=None, scalar=None):
        self.name = name
        self.scalar = scalar if scalar is not None else True
        self.meta = {} if meta is None else meta
        if len(self.meta) == 0:
            self.meta["shortName"] = name

    def make_filter(self):
        dims = {}
        if self.name:
            dims["shortName"] = [self.name]
        for n in ["level", "typeOfLevel"]:
            v = self.meta.get(n, None)
            if v is not None:
                dims[n] = [v]
        return dims

    @staticmethod
    def build_from_name(full_name, param_level_types=None):
        full_name = full_name
        name = full_name
        level = None
        level_type = ""

        # the name is a known param name
        if param_level_types:
            if name in param_level_types:
                lev_t = param_level_types.get(name, [])
                meta = {}
                if len(lev_t) == 1:
                    meta = {"typeOfLevel": lev_t[0], "level": None}
                scalar = not name in ParamInfo.VECTOR_NAMES
                return ParamInfo(name, meta=meta, scalar=scalar)

        t = full_name
        # surface fields
        if t in ParamInfo.KNOWN_SURF_NAMES or ParamInfo.SURF_RE.match(t) is not None:
            level_type = "surface"

        else:
            # guess the level type from the suffix
            for k, v in ParamInfo.SUFFIXES.items():
                if full_name.endswith(k):
                    level_type = v
                    t = full_name[: -(len(k))]
                    break

            # recognise vector params
            for v in ParamInfo.VECTOR_NAMES:
                if t.startswith(v):
                    name = v
                    t = t[len(v) :]
                    break

            # determine level value
            m = ParamInfo.LEVEL_RE.search(t)
            if m and m.groups() and len(m.groups()) == 1:
                level = int(m.group(1))
                if level_type == "" and level > 10:
                    level_type = "isobaricInhPa"
                if name == full_name:
                    name = ParamInfo.NUM_RE.sub("", t)

        # check param name in the conf
        if param_level_types:
            if not name in param_level_types:
                raise Exception(
                    f"Param={name} (guessed from name={full_name}) is not found in dataset!"
                )

            lev_t = param_level_types.get(name, [])
            if lev_t:
                if not level_type and len(lev_t) == 1:
                    level_type = lev_t[0]
                elif level_type and level_type not in lev_t:
                    raise Exception(
                        f"Level type cannot be guessed from param name={full_name}!"
                    )

        if level_type == "":
            level = None
        scalar = not name in ParamInfo.VECTOR_NAMES

        LOG.debug(f"scalar={scalar}")
        meta = {"level": level, "typeOfLevel": level_type}
        return ParamInfo(name, meta=meta, scalar=scalar)

    @staticmethod
    def build_from_fieldset(fs):
        assert isinstance(fs, mv.Fieldset)
        f = fs[0:3] if len(fs) >= 3 else fs
        m = ParamInfo._grib_get(f, GribIndexer.DEFAULT_ECC_KEYS)
        name = level = lev_type = ""
        scalar = True

        meta_same = True
        for x in m.keys():
            if x != "shortName" and m[x].count(m[x][0]) != len(m[x]):
                same = False
                break
        if meta_same:
            if len(m["shortName"]) == 3 and m["shortName"] == ["u", "v", "w"]:
                name = "wind3d"
                scalar = False
            elif len(m["shortName"]) >= 2:
                if m["shortName"][0:2] == ["u", "v"]:
                    name = "wind"
                    scalar = False
                elif m["shortName"][0:2] == ["10u", "10v"]:
                    name = "wind10m"
                    m["level"][0] = 0
                    m["typeOfLevel"][0] = "sfc"
                    scalar = False
        if not name:
            name = m["shortName"][0]

        if name:
            return ParamInfo(name, meta={k: v[0] for k, v in m.items()}, scalar=scalar)
        else:
            return None

    def _meta_match(self, meta, key):
        local_key = key if key != "levelist" else "level"
        if (
            key in meta
            and meta[key] is not None
            and meta[key]
            and local_key in self.meta
        ):
            # print(f"local={self.meta[local_key]} other={meta[key]}")
            if isinstance(meta[key], list):
                return str(self.meta[local_key]) in meta[key]
            else:
                return meta[key] == str(self.meta[local_key])
        else:
            return False

    def match(self, name, meta):
        # print(f"{self}, name={name}, meta={meta}")
        r = 0
        if self.name == name:
            r += 3
        for n in ["shortName", "paramId"]:
            if self._meta_match(meta, n):
                r += 1
        # we only check the rest if the param is ok
        if r > 0:
            if self._meta_match(meta, "typeOfLevel"):
                r += 1
                if self._meta_match(meta, "levelist"):
                    r += 1

        return r

    def update_meta(self, meta):
        self.meta = {**meta, **self.meta}

    @staticmethod
    def _grib_get(f, keys):
        md = mv.grib_get(f, keys, "key")
        m = {}
        for k, v in zip(keys, md):
            key_val = k.split(":")[0]
            val = v
            if k.endswith(":l"):
                val = []
                for x in v:
                    try:
                        val.append(int(x)) 
                    except:
                        val.append(None) 
            m[key_val] = val  
        return m

    def __str__(self):
        return "{}[name={}, scalar={}, meta={}]".format(
            self.__class__.__name__, self.name, self.scalar, self.meta
        )
