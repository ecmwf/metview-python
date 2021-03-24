"""
GRIB - Potential Temperature
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
        type="fc",
        date=20160925,
        time=0,
        step=42,
        levtype="pl",
        levelist=850,
        param=["t", "z"],
        area=[90, -100, 15, 50],
        grid=[0.25, 0.25],
    )
# read data from GRIB file
else:
    filename = "karl_tz_850.grib"
    if mv.exist(filename):
        g = mv.read(filename)
    else:
        g = mv.gallery.load_dataset(filename)

# extract temperature and geopotential
t = mv.read(data=g, param="t")
z = mv.read(data=g, param="z")

# compute potential temperature
pt = mv.pott_p(temperature=t)

# define contour shading
cont_pt = mv.mcont(
    legend="on",
    contour="off",
    contour_level_selection_type="interval",
    contour_max_level=320,
    contour_min_level=275,
    contour_interval=5,
    contour_label="off",
    contour_shade="on",
    contour_shade_method="area_fill",
    contour_shade_colour_method="palette",
    contour_shade_palette_name="colorbrewer_Spectral_9",
    grib_scaling_of_retrieved_fields="off",
)

# define contouring for z
cont_z = mv.mcont(contour_automatic_setting="ecmwf")

# define coastlines
coast = mv.mcoast(
    map_coastline_resolution="medium",
    map_coastline_thickness=2,
    map_coastline_colour="RGB(0.1882,0.1882,0.1882)",
)

# define view
view = mv.geoview(
    map_area_definition="corners", area=[72, -85, 20, 15], coastlines=coast
)

# define legend
legend = mv.mlegend(legend_text_font_size=0.35)

# define title
title = mv.mtext(text_font_size=0.4)

# define the output plot file
mv.setoutput(mv.pdf_output(output_name="potential_temperature"))

# generate plot
mv.plot(view, pt, cont_pt, z, cont_z, title, legend)
