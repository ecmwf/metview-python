"""
Cross Section 3D Parallel Wind
"""

# (C) Copyright 2017- ECMWF.
#
# This software is licensed under the terms of the Apache Licence Version 2.0
# which can be obtained at http://www.apache.org/licenses/LICENSE-2.0.
#
# In applying this licence, ECMWF does not waive the privileges and immunities
# granted to it by virtue of its status as an intergovernmental organisation
# nor does it submit to any jurisdiction.
#

import metview as mv

# read grib file - contains model level data with u, v, w, t and lnsp
filename = "joachim_ml.grib"
if mv.exist(filename):
    fs = mv.read(filename)
else:
    fs = mv.gallery.load_dataset(filename)

# define cross section line
line = [48.32, 1.18, 40.43, 2.44]

# define vertical axis
vertical_axis = mv.maxis(
    axis_orientation="vertical",
    axis_type="position_list",
    axis_tick_position_list=[1000, 925, 850, 700, 500, 400, 300, 250],
    axis_tick_label_height=0.4,
)

# define cross section for 3D wind projected onto the cross section
# plane
# - log pressure axis from 1015 to 250 hPa
# - the vertical velocity in m/s is computed from w (=omega),
#   then an additional scaling is applied to it (defined via w_wind_scaling_factor)
xs_view = mv.mxsectview(
    line=line,
    wind_parallel="on",
    w_wind_scaling_factor_mode="compute",
    w_wind_scaling_factor="50",
    bottom_level=1015,
    top_level=250,
    vertical_scaling="log",
    vertical_axis=vertical_axis,
)

# define wind plotting
wind_plotting = mv.mwind(wind_arrow_colour="purplish_blue")

# define orography area
orog_graph = mv.mgraph(graph_type="area", graph_shade_colour="charcoal")

# define title
title = mv.mtext(
    text_lines=["3D wind projected onto cross section plane"], text_font_size=0.4
)

# define the output plot file
mv.setoutput(mv.pdf_output(output_name="cross_section_wind_3d"))

# generate plot
mv.plot(xs_view, fs, wind_plotting, orog_graph, title)
