# Metview Example

#  **************************** LICENSE START ***********************************
#
#  Copyright 2018 ECMWF. This software is distributed under the terms
#  of the Apache License version 2.0. In applying this license, ECMWF does not
#  waive the privileges and immunities granted to it by virtue of its status as
#  an Intergovernmental Organization or submit itself to any jurisdiction.
#
#  ***************************** LICENSE END ************************************

"""
Boundaries, Cities and Rivers
==============================
"""

# ---------------------------------------------------------------
# Description: Demonstrates how to show main cities, rivers, borders
#              and admnistrative boundaries.
# ---------------------------------------------------------------

import metview as mv

# set up the geographical view
my_view = mv.geoview(
    map_area_definition="CORNERS",
    map_projection="CYLINDRICAL",
    area=[48.00, -3.00, 55.00, 10.00],
)

# set up the coastlines so that cities, rivers, borders and admnistrative boundaries are shown
my_coast = mv.mcoast(
    map_administrative_boundaries_colour="ORANGE",
    map_boundaries="ON",
    map_coastline_resolution="HIGH",
    map_coastline_land_shade_colour="CREAM",
    map_cities="ON",
    map_grid="OFF",
    map_boundaries_colour="RED",
    map_grid_colour="TAN",
    map_rivers="ON",
    map_administrative_boundaries_countries_list=["FRA", "DEU", "GBR"],
    map_coastline_land_shade="ON",
    map_coastline_colour="TAN",
    map_administrative_boundaries="ON",
)

my_text = mv.mtext(
    text_font_size=0.80,
    text_lines=["Administrative boundaries, cities and rivers"],
    text_justification="LEFT",
    text_colour="CHARCOAL",
)


# define the output plot file
mv.setoutput(mv.pdf_output(output_name="coastlines2"))

# plot the map with the given style
mv.plot(my_view, my_coast, my_text)
