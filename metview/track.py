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

from datetime import datetime

import metview as mv
import pandas as pd

from metview.style import Style, StyleDb


class Track:
    def __init__(self, path):
        self.path = path

    def style(self):
        return StyleDb.get_db().get_style("track").clone()

    def build(self, style=[]):
        df = pd.read_csv(filepath_or_buffer=self.path, skiprows=10)

        v_date = df.iloc[:, 0]
        v_time = df.iloc[:, 1]
        val = ["{}/{:02d}".format(str(d)[-2:], t) for d, t in zip(v_date, v_time)]
        lon = df.iloc[:, 4].values
        lat = df.iloc[:, 3].values

        if len(style) == 0:
            s = StyleDb.get_db().get_style("track").clone()
        if len(style) == 1 and isinstance(style[0], Style):
            s = style[0].clone()
        else:
            assert all(not isinstance(x, Style) for x in style)
            s = StyleDb.get_db().get_style("track").clone()

        for vd in s.visdefs:
            if vd.verb == "msymb":
                vd.change_symbol_text_list(val)
        r = s.to_request()

        vis = mv.input_visualiser(
            input_plot_type="geo_points",
            input_longitude_values=lon,
            input_latitude_values=lat,
        )

        return [vis, *r]
