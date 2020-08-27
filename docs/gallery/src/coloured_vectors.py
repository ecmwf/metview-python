"""
Wind Coloured by temperature
=============================
"""

#  **************************** LICENSE START ***********************************
#
#  Copyright 2018 ECMWF. This software is distributed under the terms
#  of the Apache License version 2.0. In applying this license, ECMWF does not
#  waive the privileges and immunities granted to it by virtue of its status as
#  an Intergovernmental Organization or submit itself to any jurisdiction.
#
#  ***************************** LICENSE END ************************************

import metview as mv


# retrieve the wind and temperature data from MARS
# we could also read from a GRIB file with mv.read('/path/to/file')
uvt = mv.retrieve(param=["u", "v", "t"], levelist=1000, grid=[2, 2], date=-10)

# use the Grib Vectors module to combine wind and temperature for plotting
grib_vectors_coloured = mv.grib_vectors(
    u_component=mv.read(data=uvt, param="u"),  # filter U
    v_component=mv.read(data=uvt, param="v"),  # filter V
    colouring_field=mv.read(data=uvt, param="t"),  # filter T
)

# set up dark coastlines so that the vector field shows up better
coastlines = mv.mcoast(
    map_coastline_colour="white",
    map_coastline_resolution="low",
    map_coastline_thickness=3,
    map_coastline_land_shade="on",
    map_coastline_land_shade_colour="RGB(0.25,0.25,0.25)",
    map_coastline_sea_shade="on",
    map_coastline_sea_shade_colour="black",
)

# set up the geographical view
view = mv.geoview(coastlines=coastlines)

# wind visdef - wind_advanced_colour_parameter can be set to@
#   'speed'     : arrows will be coloured according to the wind speed
#   'parameter' : arrows will be coloured according to the 'colouring_field'
wind_visdef = mv.mwind(
    legend="on",
    wind_arrow_legend_text="m/s",
    wind_advanced_method="on",
    wind_advanced_colour_parameter="parameter",
    wind_advanced_colour_min_level_colour="blue",
    wind_advanced_colour_max_level_colour="red",
    wind_advanced_colour_direction="clockwise",
    wind_thinning_factor=1,
)

# define the output plot file
mv.setoutput(mv.pdf_output(output_name="coloured_vectors"))

# plot the data onto the default map
mv.plot(view, grib_vectors_coloured, wind_visdef)
