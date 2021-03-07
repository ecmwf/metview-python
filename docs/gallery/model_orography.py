"""
GRIB - Model Orography with Land Sea Mask
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

# get data from MARS
if use_mars:
    g = mv.retrieve(
        type="an",
        date=-1,
        time=0,
        levtype="sfc",
        param=["z", "lsm"],
        area=[90, -60, 20, 70],
        grid=[0.1, 0.1],
    )
# read data from GRIB file
else:
    filename = "model_orog.grib"
    if mv.exist(filename):
        g = mv.read(filename)
    else:
        g = mv.gallery.load_dataset(filename)


# convert geopotential to metres
h = g[0] / 9.81

# set all water surface points as missing in h
lsm = g[1]
h = mv.bitmap(h, mv.bitmap(lsm > 0.1, 0))

# define contour shading
cont = mv.mcont(
    legend="on",
    contour="off",
    contour_label="off",
    contour_level_list=[
        -400,
        0,
        20,
        100,
        200,
        300,
        500,
        800,
        1000,
        1500,
        2000,
        2500,
        3000,
        4000,
        5000,
        8000,
    ],
    contour_level_selection_type="level_list",
    contour_shade="on",
    contour_shade_colour_list=[
        "rgb(0.15,0.5,0.4)",
        "rgb(0.16,0.4,0)",
        "rgb(0.2,0.5,0)",
        "rgb(0.3,0.6,0)",
        "rgb(0.4,0.7,0)",
        "rgb(0.5,0.8,0)",
        "rgb(0.7,0.9,0)",
        "rgb(0.9,1,0)",
        "rgb(0.9,0.8,0)",
        "rgb(0.8,0.6,0)",
        "rgb(0.7,0.45,0)",
        "rgb(0.6,0.3,0)",
        "rgb(0.45,0.2,0)",
        "rgb(0.5,0.5,0.5)",
        "rgb(1,1,0.5)",
    ],
    contour_shade_colour_method="list",
    contour_shade_max_level=8000,
    contour_shade_method="area_fill",
    contour_shade_min_level=-400,
    contour_method="linear",
    contour_internal_reduction_factor=1,
)

# define coastlines
coast = mv.mcoast(
    map_coastline_resolution="medium",
    map_coastline_sea_shade="on",
    map_coastline_sea_shade_colour="RGB(0.4845,0.6572,0.9351)",
)

# define view
view = mv.geoview(area_mode="name", area_name="europe", coastlines=coast)

# define title
title = mv.mtext(text_lines=["Model Orography"], text_font_size=0.4)

# define the output plot file
mv.setoutput(mv.pdf_output(output_name="model_orography"))

# generate plot
mv.plot(view, h, cont, title)
