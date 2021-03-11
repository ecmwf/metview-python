"""
Capital Cities
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

# define coastlines
coast = mv.mcoast(
    map_coastline_colour="charcoal",
    map_coastline_resolution="medium",
    map_coastline_land_shade="on",
    map_coastline_land_shade_colour="grey",
    map_coastline_sea_shade="on",
    map_coastline_sea_shade_colour="RGB(0.8178,0.9234,0.9234)",
    map_boundaries="on",
    map_boundaries_colour="brown",
    map_boundaries_thickness=1,
    map_cities="on",
    map_cities_font_size=3,
    map_cities_font_colour="brick",
    map_cities_marker="box",
    map_cities_marker_colour="red",
    map_cities_marker_height=1,
    map_grid_line_style="dot",
    map_label_height=0.35,
)

# define view
view = mv.geoview(
    area_mode="name",
    area_name="south_east_asia_and_indonesia",
    coastlines=coast,
)

# define the output plot file
mv.setoutput(mv.pdf_output(output_name="capitals"))

# plot the data onto the map
mv.plot(view)
