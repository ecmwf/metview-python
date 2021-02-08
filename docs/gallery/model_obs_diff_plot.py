"""
GRIB, BUFR - Model minus Obs Difference
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
import numpy as np

use_mars = False
if use_mars:
    # retrieve model data for 2m temperature (GRIB)
    t2m_fc48 = mv.retrieve(
        type="fc", levtype="sfc", param="2t", date=-5, step=48, grid="o1280"
    )

    # retrieve obs data (BUFR)
    synop = mv.retrieve(type="ob", repres="bu", date=-3)
else:
    filename = "t2m_fc48.grib"
    if mv.exist(filename):
        t2m_fc48 = mv.read(filename)
    else:
        t2m_fc48 = mv.gallery.load_dataset(filename)

    filename = "t2m_obs.bufr"
    if mv.exist(filename):
        synop = mv.read(filename)
    else:
        synop = mv.gallery.load_dataset(filename)


# filter just the 2m temperature from the obs data (Geopoints)
synop_t2m = mv.obsfilter(output="geopoints", parameter="012004", data=synop)

# compute the difference
diff = t2m_fc48 - synop_t2m

# define the graphical symbol plotting style
max_diff = mv.maxvalue(mv.abs(diff))

diff_symb = mv.msymb(
    legend="on",
    symbol_type="marker",
    symbol_table_mode="advanced",
    symbol_outline="on",
    symbol_outline_colour="charcoal",
    symbol_advanced_table_selection_type="list",
    symbol_advanced_table_level_list=[-max_diff, -10, -5, -1, 0, 1, 5, 10, max_diff],
    symbol_advanced_table_colour_method="list",
    symbol_advanced_table_colour_list=[
        "blue",
        "sky",
        "rgb(0.82,0.85,1)",
        "white",
        "white",
        "rgb(0.9,0.8,0.8)",
        "rgb(0.9,0.45,0.45)",
        "red",
    ],
    symbol_advanced_table_height_list=[0.6, 0.5, 0.4, 0.3, 0.3, 0.4, 0.5, 0.6],
)

# shaded land and sea to make the points stand out more
grey_land_sea_shading = mv.mcoast(
    map_coastline_land_shade="on",
    map_coastline_land_shade_colour="RGB(0.89,0.89,0.89)",
    map_coastline_sea_shade="on",
    map_coastline_sea_shade_colour="grey",
    map_grid_latitude_increment=20,
    map_grid_longitude_increment=40,
    map_grid_colour="charcoal",
)

# use numpy to give us some statistics to put in the title
# - we could also have done this with Metview functions
vals = mv.values(diff)
title = mv.mtext(
    text_line_1="Min = "
    + format(np.amin(vals), ".2f")
    + " Mean = "
    + format(np.mean(vals), ".2f")
    + " Max = "
    + format(np.amax(vals), ".2f"),
    text_font_size=0.4,
)

# adjust the legend
legend = mv.mlegend(legend_text_font_size=0.35)

# set the view area
view = mv.geoview(
    map_area_definition="corners",
    area=[30, -28, 75, 48],
    coastlines=grey_land_sea_shading,
)

# define the output plot file
mv.setoutput(mv.pdf_output(output_name="model_obs_diff_plot"))

# plot the data with the style
mv.plot(view, diff, diff_symb, title, legend)
