"""
NetCDF - Wind
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

# read ERA5 monthly mean
filename = "era5_2000_aug.nc"
if mv.exist(filename):
    nc = mv.read(filename)
else:
    nc = mv.gallery.load_dataset(filename)


# this NetCDF data has the following structure:
#
# dimensions:
# 	longitude = 1440 ;
# 	latitude = 721 ;
# 	time = 1 ;
# variables:
# 	float longitude(longitude) ;
# 	float latitude(latitude) ;
# 	int time(time) ;
# 	short u10(time, latitude, longitude) ;
# 	short v10(time, latitude, longitude) ;

# define netcdf plotting based on the data structure above
vis = mv.netcdf_visualiser(
    netcdf_plot_type="geo_matrix_vectors",
    netcdf_latitude_variable="latitude",
    netcdf_longitude_variable="longitude",
    netcdf_x_component_variable="u10",
    netcdf_y_component_variable="v10",
    netcdf_data=nc,
)

# define wind plotting
wind_plotting = mv.mwind(
    wind_thinning_factor=6,
    legend="on",
    wind_advanced_method="on",
    wind_advanced_colour_selection_type="interval",
    wind_advanced_colour_min_value=1,
    wind_advanced_colour_level_interval=1,
    wind_advanced_colour_max_level_colour="RGB(0.9765,0.003845,0.1498)",
    wind_advanced_colour_min_level_colour="RGB(0.1628,0.1959,0.8255)",
    wind_arrow_unit_velocity=8,
)

# define coastlines
coastlines = mv.mcoast(
    map_coastline_land_shade="on",
    map_coastline_land_shade_colour="RGB(0.8,0.8,0.8)",
    map_coastline_sea_shade="on",
    map_coastline_sea_shade_colour="RGB(0.949,0.949,0.949)",
    map_grid_colour="RGB(0.337,0.314,0.314)",
)

# define geographical view
view = mv.geoview(
    map_projection="polar_stereographic",
    map_area_definition="corners",
    area=[1.77, -70.71, 28.28, 44.99],
    map_vertical_longitude=-40,
    coastlines=coastlines,
)

# define title
title = mv.mtext(
    text_lines=["ERA5 - 10m wind - August 2000 monthly mean"], text_font_size=0.4
)

# define output
mv.setoutput(mv.pdf_output(output_name="nc_era5_wind"))

# generate plot
mv.plot(view, vis, wind_plotting, title)
