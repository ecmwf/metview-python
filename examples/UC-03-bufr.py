# (C) Copyright 2017- ECMWF.
#
# This software is licensed under the terms of the Apache Licence Version 2.0
# which can be obtained at http://www.apache.org/licenses/LICENSE-2.0.
#
# In applying this licence, ECMWF does not waive the privileges and immunities
# granted to it by virtue of its status as an intergovernmental organisation
# nor does it submit to any jurisdiction.

"""
Metview Python use case

The Python analyst reads some BUFR data and plots it in various ways

--------------------------------------------------------------------------------
1. Python analyst reads BUFR data and plots it using the default style
--------------------------------------------------------------------------------

--------------------------------------------------------------------------------
2. Python analyst reads BUFR data and applies a visual definition
   to alter its plotting style
--------------------------------------------------------------------------------

--------------------------------------------------------------------------------
3. Python analyst reads BUFR data and filters a single parameter from it
   and plots it with a colour scale
--------------------------------------------------------------------------------

"""
import metview as mv


# define a view over the area of interest and set land shading on

land_shade = mv.mcoast(
    map_coastline_land_shade=True,
    map_coastline_land_shade_colour="RGB(0.98,0.95,0.82)",
    map_coastline_sea_shade=False,
    map_coastline_sea_shade_colour="RGB(0.85,0.93,1)",
)

area_view = mv.geoview(
    map_area_definition="corners",
    area=[45.83, -13.87, 62.03, 8.92],
    coastlines=land_shade,
)


# Simplest plot:
# NOTE that when plotting a 'raw' BUFR file, Magics will plot synop symbols as shown in
# https://software.ecmwf.int/wiki/display/METV/Data+Part+1 "Plotting BUFR Data"

obs = mv.read("../tests/obs_3day.bufr")

mv.setoutput(mv.png_output(output_width=1200, output_name="./obsplot1"))
mv.plot(area_view, obs)


# ALTERNATIVELY, add an Observations Plotting visual definition

obs_plotting = mv.mobs(
    obs_temperature=False,
    obs_cloud=False,
    obs_low_cloud=False,
    obs_dewpoint_colour="purple",
)


mv.setoutput(mv.png_output(output_width=1200, output_name="./obsplot2"))
mv.plot(area_view, obs, obs_plotting)


# ALTERNATIVELY, if we don't want to plot the whole observations, but instead want to
# extract a specific parameter from the BUFR messages, then we use the Observation Filter
# as shown here:

# dewpoint_t is a 'geopoints' variable
dewpoint_t = mv.obsfilter(output="geopoints", parameter="012006", data=obs)

# add an optional Symbol Plotting definition to get nice coloured circles
# at each point
symb_visdef = mv.msymb(
    legend=True,
    symbol_type="marker",
    symbol_table_mode="advanced",
    symbol_advanced_table_max_level_colour="red",
    symbol_advanced_table_min_level_colour="blue",
    symbol_advanced_table_colour_direction="clockwise",
)

mv.setoutput(mv.png_output(output_width=1200, output_name="./obsplot3"))
mv.plot(area_view, dewpoint_t, symb_visdef)
