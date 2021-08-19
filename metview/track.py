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

from metview.style import Style


class Track:
    def __init__(
        self,
        path,
        skiprows=None,
        sep=None,
        date_index=None,
        time_index=None,
        lat_index=None,
        lon_index=None,
    ):
        self.path = path
        self.skiprows = 0 if skiprows is None else skiprows
        self.sep = sep
        if self.sep == " ":
            self.sep = r"\s+"
        self.date_index = 0 if date_index is None else date_index
        self.time_index = 1 if time_index is None else time_index
        self.lat_index = 3 if lat_index is None else lat_index
        self.lon_index = 2 if lon_index is None else lon_index

    def style(self):
        return mv.style.get_db().get_style("track").clone()

    def build(self, style=[]):
        df = pd.read_csv(
            filepath_or_buffer=self.path,
            sep=self.sep,
            skiprows=self.skiprows,
            header=None,
            engine="python",
        )

        # print(df)

        v_date = df.iloc[:, self.date_index]
        v_time = df.iloc[:, self.time_index]
        val = [" {}/{:02d}".format(str(d)[-2:], t) for d, t in zip(v_date, v_time)]
        lon = df.iloc[:, self.lon_index].values
        lat = df.iloc[:, self.lat_index].values
        idx_val = list(range(len(val)))

        # print(f"lon={lon}")
        # print(f"lat={lat}")
        # print(f"val={val}")
        # for x in style:
        #     print(f"style={x}")

        if len(style) == 0:
            s = mv.style.get_db().get_style("track").clone()
        if len(style) == 1 and isinstance(style[0], Style):
            s = style[0].clone()
        else:
            assert all(not isinstance(x, Style) for x in style)
            s = mv.style.get_db().get_style("track").clone()

        for vd in s.visdefs:
            if vd.verb == "msymb":
                vd.change_symbol_text_list(val, idx_val)

        r = s.to_request()

        vis = mv.input_visualiser(
            input_plot_type="geo_points",
            input_longitude_values=lon,
            input_latitude_values=lat,
            input_values=idx_val,
        )

        return [vis, *r]
