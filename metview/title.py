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

import logging

import metview as mv

LOG = logging.getLogger(__name__)

FC_TIME_PART = "Step: +<grib_info key='step' />h Valid: <grib_info key='valid-date' format='%Y-%m-%d %H' />"
LEVEL_PART = "Lev: <grib_info key='level' /> (<grib_info key='levelType' />)"


class Title:
    def __init__(self, font_size=0.4):
        self.font_size = font_size

    def _make_font_size(self, font_size):
        if font_size is None:
            return self.font_size
        else:
            return font_size

    def build(self, data, font_size=None):
        font_size = self._make_font_size(font_size)
        label = ""
        if data:
            if not isinstance(data, list):
                data = [data]

            lines = []
            lines = {"text_line_count": len(data)}
            for i, d_item in enumerate(data):
                # print(f"d_item={d_item}")
                if isinstance(d_item, tuple):
                    d = d_item[0]
                    data_id = d_item[1]
                else:
                    d = d_item
                    data_id = None

                param = d.param_info
                if param is not None:
                    if param.meta.get("typeOfLevel", "") == "surface":
                        # lines.append(self.build_surface_fc(d.experiment.label, d.param.name, condition=cond))
                        lines[f"text_line_{i+1}"] = self.build_surface_fc(
                            d.label, param.name, data_id=data_id
                        )
                    else:
                        # lines.append(self.build_upper_fc(d.experiment.label, d.param.name, condition=cond))
                        lines[f"text_line_{i+1}"] = self.build_upper_fc(
                            d.label, param.name, data_id=data_id
                        )

            # print(f"line={lines}")
            # return mv.mtext(text_lines=lines, text_font_size=font_size)
            return mv.mtext(**lines, text_font_size=font_size)

        return mv.mtext(
            {
                "text_line_1": f"""{label} Par: <grib_info key='shortName'/> Lev: <grib_info key='level'/> (<grib_info key='levelType'/>) Step: +<grib_info key='step'/>h Valid: <grib_info key='valid-date' format='%Y-%m-%d %H'/>""",
                "text_font_size": font_size,
            }
        )

    def _build_condition_str(self, condition):
        if condition:
            t = "where="
            for k, v in condition.items():
                t += f"'{k}={v}'"
            return t
        return str()

    def _add_grib_info(self, t, data_id):
        if data_id is not None and data_id != "":
            t = t.replace("<grib_info", f"<grib_info id='{data_id}'")
        return t

    def build_surface_fc(self, label, par, condition=None, data_id=None):
        t = FC_TIME_PART
        t = self._add_grib_info(t, data_id)
        return f"""{label} Par: {par} {t}"""

    def build_upper_fc(self, label, par, condition=None, data_id=None):
        lev = LEVEL_PART
        t = FC_TIME_PART
        lev = self._add_grib_info(lev, data_id)
        t = self._add_grib_info(t, data_id)
        return f"""{label} Par: {par} {lev} {t}"""

    def build_xs(self, data):
        if data:
            if not isinstance(data, list):
                data = [data]

            lines = []
            for d in data:
                line = d.label
                # print(f"label={d.label}")
                param = d.param_info
                if param is not None:
                    # print(f"meta={param.meta}")
                    line += f" Par: {param.name}"
                    meta = param.meta
                    if meta.get("mars.type", "") == "an":
                        pass
                    else:
                        r = meta.get("date", 0)
                        h = meta.get("time", 0)
                        s = meta.get("step", "")
                        line += f" Run: {r} {h} UTC Step: +{s}h"
                lines.append(line)

            return mv.mtext(text_lines=lines, text_font_size=self.font_size)

        return mv.mtext(text_font_size=self.font_size)

    def build_stamp(self, data, member=""):
        if data:
            if not isinstance(data, list):
                data = [data]

            # exp_conf = data[0].experiment
            label = data[0].label

            member_txt = ""
            if member:
                if member == "0":
                    member_txt = "CF"
                else:
                    member_txt = f"PF {member}"

            return mv.mtext(
                {
                    "text_line_1": f"""{label} {member_txt} Step: +<grib_info key='step'/>h Valid: <grib_info key='valid-date' format='%Y-%m-%d %H'/>""",
                    "text_font_size": self.font_size,
                }
            )

        return mv.mtext(
            {
                "text_font_size": self.font_size,
            }
        )
