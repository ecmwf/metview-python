"""
BUFR - SYNOP Map
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

# read bufr file
filename = "synop.bufr"
if mv.exist(filename):
    bd = mv.read(filename)
else:
    bd = mv.gallery.load_dataset(filename)

# define observation plotting
obsp = mv.mobs(obs_distance_apart=1.5, obs_size=0.25, obs_ring_size=0.2)

# define land-sea shading
coast = mv.mcoast(
    map_coastline_land_shade="on",
    map_coastline_land_shade_colour="grey",
    map_coastline_sea_shade="on",
    map_coastline_sea_shade_colour="RGB(0.7903,0.8438,0.943)",
    map_grid_colour="charcoal",
    map_grid_longitude_increment=10,
)


# define map
view = mv.geoview(
    map_area_definition="corners", area=[30, -16, 75, 45], coastlines=coast
)

mv.setoutput(mv.pdf_output(output_name="synop_map"))

# generate plot
mv.plot(view, bd, obsp)
