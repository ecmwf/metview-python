"""
Cross Section in Height for Model Level Data with Orography
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

# get data
use_mars = False
if use_mars:
    # retrieve data from MARS
    ret_core = {
        "date": 20200822,
        "time": 0,
        "area": [40, -93, 51, -84],
        "grid": [0.5, 0.5],
    }

    # forecast fields on all the model levels (bottom=ML-137, top=ML-1)
    # Note= log surface pressure (lnsp) is defined on ML-1!
    fs_ml = mv.retrieve(
        **ret_core,
        type="fc",
        levtype="ml",
        levelist=[1, "TO", 137],
        step=12,
        param=["t", "q", "lnsp"]
    )

    # surface geopotential is available in
    # the analysis only! It is available on ML-1!
    zs = mv.retrieve(**ret_core, type="an", levtype="ml", levelist=1, param="z")
else:
    # read data from GRIB file
    filename = "xs_ml_orog.grib"
    if mv.exist(filename):
        fs_ml = mv.read(filename)
    else:
        fs_ml = mv.gallery.load_dataset(filename)
    zs = mv.read(data=fs_ml, param="z")

# extract ml data
t = mv.read(data=fs_ml, param="t")
q = mv.read(data=fs_ml, param="q")
lnsp = mv.read(data=fs_ml, param="lnsp")

# compute geopotential on model levels
z = mv.mvl_geopotential_on_ml(t, q, lnsp, zs)

# define cross section line
line = [50.21, -91.82, 40.82, -84.71]

# define bottom level (m)
bottom_level = 0

# extract a set of levels needed for the cross section
# and converts temperature from K to C and z to m
t = mv.read(data=t, levelist=[137, "TO", 100]) - 273.16
z = mv.read(data=z, levelist=[137, "TO", 100]) / 9.81

# compute cross section in height (above sea level) for t
# (using z, paramId=129)
xs_t = mv.mcross_sect(
    data=mv.merge(t, z),
    line=line,
    vertical_coordinates="user",
    vertical_coordinate_param=129,
    vertical_coordinate_extrapolate="on",
)

# generate orography area curve
orog_curve = mv.xs_build_orog(xs_t, zs / 9.81, bottom_level, "charcoal")

# define contour shading for temperature
cont = mv.mcont(
    legend="on",
    contour_line_colour="charcoal",
    contour_highlight="off",
    contour_level_selection_type="interval",
    contour_max_level=23.5,
    contour_min_level=16.5,
    contour_interval=0.5,
    contour_shade="on",
    contour_shade_method="area_fill",
    contour_shade_max_level_colour="red",
    contour_shade_min_level_colour="green",
    contour_shade_colour_direction="clockwise",
)

# define vertical axis
vertical_axis = mv.maxis(
    axis_orientation="vertical",
    axis_title_text="Height ASL (m)",
    axis_tick_label_height=0.4,
)

# define cross section in height above sea level  (m)
xs_view = mv.mxsectview(
    line=line, top_level=1000, bottom_level=bottom_level, vertical_axis=vertical_axis
)

# define legend
legend = mv.mlegend(legend_text_font_size=0.35)

# define title
title = mv.mtext(text_font_size=0.4)

# define the output plot file
mv.setoutput(mv.pdf_output(output_name="cross_section_height_ml_orog"))

# generate plot
mv.plot(xs_view, xs_t, cont, orog_curve, legend, title)
