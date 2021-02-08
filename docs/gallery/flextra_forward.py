"""
FLEXTRA - Forward Trajectories
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

# read file containing the results of a FLEXTRA
# forward simulation with 5 trajectories started at the
# same location and height at different times
# (i.e. a FLEXTRA simulation with mode="normal")
filename = "flextra_res_normal.txt"
if mv.exist(filename):
    f = mv.read(filename)
else:
    f = mv.gallery.load_dataset(filename)

# define visualiser
vis = mv.flextra_visualiser(flextra_data=f)

# define coastlines
coast = mv.mcoast(
    map_coastline_resolution="medium",
    map_coastline_land_shade="on",
    map_coastline_land_shade_colour="RGB(0.5569,0.5569,0.5569)",
    map_coastline_sea_shade="on",
    map_coastline_sea_shade_colour="RGB(0.8,0.8,0.8)",
    map_boundaries="on",
    map_boundaries_colour="burgundy",
)

# define view
view = mv.geoview(
    map_projection="polar_stereographic",
    map_area_definition="corners",
    area=[31.81, -20.24, 52.57, 63.93],
    coastlines=coast,
)

# define symbol plotting
sym = mv.msymb(
    legend="on",
    symbol_type="marker",
    symbol_table_mode="advanced",
    symbol_connect_line="on",
    symbol_advanced_table_selection_type="interval",
    symbol_advanced_table_min_value=1,
    symbol_advanced_table_max_value=6,
    symbol_advanced_table_interval=1,
    symbol_advanced_table_max_level_colour="blue",
    symbol_advanced_table_min_level_colour="magenta",
    symbol_advanced_table_colour_direction="clockwise",
    symbol_advanced_table_marker_list=[15, 16, 17, 18, 19],
    symbol_advanced_table_height_list=0.5,
)

# define title
title = mv.mtext(text_font_size=0.6)

# define legend
legend = mv.mlegend(legend_display_type="disjoint", legend_text_font_size=0.35)

# define output
mv.setoutput(mv.pdf_output(output_name="flextra_forward"))

# generate plot
mv.plot(view, legend, vis, sym, title)
