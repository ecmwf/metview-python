"""
GRIB - Contour Shading Only Over Land
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

# read grib data
filename = "2m_temperature.grib"
if mv.exist(filename):
    f = mv.read(filename)
else:
    f = mv.gallery.load_dataset(filename)

# define coastlines with sea shading but no land shading.
# We set map_layer_mode="foreground" to make the
# sea shading appear on top of the contour plot!
coast = mv.mcoast(
    map_coastline_sea_shade="on",
    map_coastline_sea_shade_colour="charcoal",
    map_grid_colour="RGB(0.4,0.4,0.4)",
    map_grid_frame="on",
    map_label="off",
    map_layer_mode="foreground",
)

# define map view
view = mv.geoview(
    map_projection="mollweide",
    subpage_y_position=15,
    subpage_frame="off",
    coastlines=coast,
)

# define contour_shading
cont = mv.mcont(
    contour_automatic_setting="style_name",
    contour_style_name="sh_all_fM64t52i4",
    legend="on",
)

# define the output plot file
mv.setoutput(mv.pdf_output(output_name="shading_only_over_land"))

# generate plot
mv.plot(view, f, cont)
