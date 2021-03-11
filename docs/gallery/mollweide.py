"""
Mollweide projection
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
    map_coastline_land_shade_colour="beige",
    map_coastline_sea_shade="on",
    map_coastline_sea_shade_colour="RGB(0.8178,0.9234,0.9234)",
    map_grid_colour="RGB(0.4,0.4,0.4)",
    map_label_height=0.35,
)

# set up the geographical area
view = mv.geoview(map_projection="mollweide", coastlines=coast)

# define the output plot file
mv.setoutput(mv.pdf_output(output_name="mollweide"))

# plot the data onto the map
mv.plot(view)
