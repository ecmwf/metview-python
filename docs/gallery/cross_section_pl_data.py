"""
Cross Section for Pressure Level Data
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

# ------------------------------------------------------------------
# Demonstrates how to use a Cross Section View to
# compute and plot a vertical cross section of GRIB data
# ------------------------------------------------------------------

import metview as mv

# read the GRIB data from file
filename = "t_fc24.grib"
if mv.exist(filename):
    t_fc = mv.read(filename)
else:
    t_fc = mv.gallery.load_dataset(filename)

# set up the view to plot the data into
cross_section_view = mv.mxsectview(
    bottom_level=1000.0,
    top_level=1,
    line=[-40.1, -105.6, 61.5, 85.1],  # lat,lon,lat,lon
)

# set up the contouring style
shading = mv.mcont(
    legend="on",
    contour="off",
    contour_level_count=12,
    contour_label="off",
    contour_shade="on",
    contour_shade_method="area_fill",
    contour_shade_max_level_colour="RGB(0.72,0.059,0.059)",
    contour_shade_min_level_colour="RGB(0.99,0.98,0.98)",
)

# set up the title, just to make the font bigger
title = mv.mtext(text_font_size=0.5)

# define the output plot file
mv.setoutput(mv.pdf_output(output_name="cross_section_pl_data"))

# plot the data into the Cross Section view with visdefs for styling
mv.plot(cross_section_view, t_fc, shading, title)
