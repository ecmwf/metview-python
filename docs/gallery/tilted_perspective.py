"""
Tilted Perspective Projection
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
    map_coastline_resolution="low",
    map_coastline_thickness=2,
    map_grid_colour="RGB(0.4,0.4,0.4)",
    map_label_height=0.25,
)

# set up the geographical area
view = mv.geoview(
    map_projection="tpers",
    map_projection_view_latitude=40.0,
    map_projection_view_longitude=-40.0,
    coastlines=coast,
)

# define the output plot file
mv.setoutput(mv.pdf_output(output_name="tilted_perspective"))

# plot the data onto the map
mv.plot(view)
