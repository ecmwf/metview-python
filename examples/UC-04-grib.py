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

UC-04. The Analyst retrieves, for a given time interval, the values of
two parameters and combines their values on the same map

--------------------------------------------------------------------------------
1. Analyst retrieves, for a given time interval, the values of two chosen
   parameters (e.g. temperature, and geopotential) from a given source (i.e. MARS,
   files, observation databases)
--------------------------------------------------------------------------------

--------------------------------------------------------------------------------
2. Analyst customises many features of his map for each field he wants to plot
   (e.g. temperature field as shaded areas and geopotenti2. al field as isolines)
--------------------------------------------------------------------------------

--------------------------------------------------------------------------------
3. Analyst plots the data
--------------------------------------------------------------------------------
Analyst plots data variable t2 with contouring definition t_shade_c, and data
variable z with contouring definition mslp_isolines.
The fields will be plotted in the order they appear in the mv.plot() command,
with the shaded temperature at the bottom, and the geopotential on top.
"""

import metview as mv


# read 2m temperature
t2 = mv.read("./t2_for_UC-04.grib")

# read geopotential
z = mv.read("./z_for_UC-04.grib")

t_shade_c = mv.mcont(
    legend=True,
    contour_highlight=False,
    contour_level_selection_type="interval",
    contour_interval=10,
    contour_shade=True,
    contour_shade_max_level=60,
    contour_shade_min_level=-60,
    contour_shade_method="area_fill",
    contour_shade_max_level_colour="red",
    contour_shade_min_level_colour="blue",
    contour_shade_colour_direction="clockwise",
)

z_isolines = mv.mcont(
    legend=True,
    contour_line_thickness=2,
    contour_line_colour="black",
    contour_highlight_colour="black",
    contour_highlight_thickness=4,
    contour_level_selection_type="interval",
    contour_interval=5,
    contour_legend_text="Geopotential",
)

mv.setoutput(mv.png_output(output_width=1000, output_name="./gribplot"))
mv.plot(t2, t_shade_c, z, z_isolines)
