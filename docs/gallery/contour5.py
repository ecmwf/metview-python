"""
GRIB - Contour Shading and Positional Legend
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
# Demonstrates how to show a field using contour shading and
# define a positional vertical legend.
# ------------------------------------------------------------------

import metview as mv

# read the input grib file
filename = "t850.grb"
if mv.exist(filename):
    my_data = mv.read(filename)
else:
    my_data = mv.gallery.load_dataset(filename)

# set up the geographical view
my_view = mv.geoview(
    map_area_definition="CORNERS",
    map_projection="CYLINDRICAL",
    area=[20.00, -20.00, 70.00, 50.00],
)

# set up the coastlines
my_coast = mv.mcoast(
    map_coastline_thickness=3,
    map_grid_thickness=2,
    map_grid_colour="GREY",
    map_coastline_colour="RGB(0.4,0.4,0.4)",
    map_grid="ON",
)

# set up the contour so that colour shading is used
my_contour = mv.mcont(
    contour_level_selection_type="LEVEL_LIST",
    contour_level_list=[-20, -10, -5, -2.5, -1, -0.5, 0, 0.5, 1, 2.5, 5, 10, 20, 30],
    contour_shade="ON",
    contour_shade_method="AREA_FILL",
    contour_shade_colour_method="CALCULATE",
    contour_shade_colour_direction="CLOCKWISE",
    contour_shade_max_level_colour="RED",
    contour_shade_min_level_colour="BLUE",
    contour_line_colour="GREY",
    contour_line_thickness=2,
    contour_highlight="OFF",
    contour_label="OFF",
    legend="ON",
)

# set up the position and properties of the legend
my_legend = mv.mlegend(
    legend_title="ON",
    legend_box_mode="POSITIONAL",
    legend_box_x_position=26.00,
    legend_box_x_length=2.00,
    legend_box_y_position=2.00,
    legend_box_y_length=10.00,
    legend_display_type="CONTINUOUS",
    legend_border="OFF",
    legend_text_font_size=0.50,
    legend_text_colour="NAVY",
    legend_title_text="850hpa Temperature",
    legend_title_orientation="VERTICAL",
)

# set up the title
my_title = mv.mtext(
    text_font_size=0.70,
    text_lines=[
        "Contour shading and positional legend.",
        "User-defined list of contour levels.",
        "",
    ],
    text_justification="LEFT",
    text_colour="CHARCOAL",
)

# define the output plot file
mv.setoutput(mv.pdf_output(output_name="contour5"))

# plot the data onto the map
mv.plot(my_view, my_data, my_contour, my_legend, my_coast, my_title)
