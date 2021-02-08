"""
BUFR - TEMP Map
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

# read TEMP bufr file
filename = "temp.bufr"
if mv.exist(filename):
    bd = mv.read(filename)
else:
    bd = mv.gallery.load_dataset(filename)

# define observation plotting - selecting level 250 hPa
obsp = mv.mobs(
    obs_distance_apart=1,
    obs_level=250,
    obs_size=0.35,
    obs_ring_size=0.4,
    obs_station_ring="off",
)

# define land-sea shading
coast = mv.mcoast(
    map_coastline_land_shade="on",
    map_coastline_land_shade_colour="grey",
    map_coastline_sea_shade="on",
    map_coastline_sea_shade_colour="RGB(0.8944,0.9086,0.9330)",
    map_grid_colour="charcoal",
    map_grid_longitude_increment=10,
)

# define map projection
view = mv.geoview(
    map_projection="polar_stereographic",
    map_area_definition="corners",
    area=[17.44, -73.61, 43.74, 33.84],
    map_vertical_longitude=-40,
    coastlines=coast,
)

# add title
title = mv.mtext(text_lines="TEMP 250 hpa", text_font_size=0.4)

# define the output plot file
mv.setoutput(mv.pdf_output(output_name="temp_map"))

# generate plot
mv.plot(view, bd, obsp, title)
