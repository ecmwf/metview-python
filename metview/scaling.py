# (C) Copyright 2017- ECMWF.
#
# This software is licensed under the terms of the Apache Licence Version 2.0
# which can be obtained at http://www.apache.org/licenses/LICENSE-2.0.
#
# In applying this licence, ECMWF does not waive the privileges and immunities
# granted to it by virtue of its status as an intergovernmental organisation
# nor does it submit to any jurisdiction.
#

import json
import logging
import os
import sys

import yaml

LOG = logging.getLogger(__name__)

ETC_PATH = os.path.join(os.path.dirname(__file__), "etc")


class UnitsScalingMethod:
    """
    Performs units scaling of values
    """

    def __init__(self, scaling=1.0, offset=0.0, from_units="", to_units=""):
        self.scaling = scaling
        self.offset = offset
        self.from_units = from_units
        self.to_units = to_units

    def scale_value(self, value):
        return self.scaling * value + self.offset

    def inverse_scale_value(self, value):
        return (value - self.offset) / self.scaling

    def need_scaling(self, meta, scaling_retrieved, scaling_derived):
        gen_id = meta.get("generatingProcessIdentifier", 0)
        try:
            gen_id = int(gen_id)
        except:
            gen_id = 0

        return (scaling_retrieved and gen_id != 254) or (
            scaling_derived and gen_id == 254
        )

    def __str__(self):
        return "scaling: {} offset:{} from_units:{} to_units:{}".format(
            self.scaling, self.offset, self.from_units, self.to_units
        )


class ScalingRule:
    """
    Defines what countour scaling should be applied to a given field based
    on its metadata
    """

    def __init__(self, to_units, conf):
        self.to_units = to_units
        self.units_methods = [
            it for it in Scaling.methods if it.to_units == self.to_units
        ]
        self.conf = conf

    def find_method(self, meta):
        from_units = meta.get("units", "")
        if from_units == "":
            return None

        method = None
        for item in self.units_methods:
            if item.from_units == from_units:
                method = item
                break

        if method is None:
            return None

        for m in self.conf.get("match", []):
            match = False
            for k, v in m.items():
                if meta.get(k, None) == v:
                    match = True
                else:
                    break

            if match:
                return method

        param_id = meta.get("paramId", "")
        if param_id and param_id in self.conf.get("paramId", []):
            return method

        short_name = meta.get("shortName", "")
        if short_name and short_name in self.conf.get("shortName", []):
            return method

        return None

    def __str__(self):
        return "to_units:{}".format(self.to_units)


class Scaling:
    methods = []
    rules = []
    loaded = False

    @staticmethod
    def find_item(meta):
        if not Scaling.loaded:
            Scaling._load_def()
            Scaling.loaded = True

        for item in Scaling.rules:
            d = item.find_method(meta)
            if d:
                return d
        return None

    @staticmethod
    def _load_def():
        # load units conversion definition
        file_name = os.path.join(ETC_PATH, "units-rules.json")
        with open(file_name) as f:
            data = json.load(f)
            for k, v in data.items():
                for item in v:
                    item["to_units"] = item.pop("to")
                    item["from_units"] = item.pop("from")
                    Scaling.methods.append(UnitsScalingMethod(**item))

        # load rules defining when to apply scaling on a parameter
        file_name = os.path.join(ETC_PATH, "scaling_ecmwf.yaml")
        # print(f"file_name={file_name}")
        with open(file_name) as f:
            data = yaml.load(f, Loader=yaml.SafeLoader)
            for to_units, item in data.items():
                Scaling.rules.append(ScalingRule(to_units, item))
