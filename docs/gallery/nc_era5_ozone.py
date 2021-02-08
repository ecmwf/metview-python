"""
NetCDF - Ozone Layout 2x2
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

# read ERA5 monthly mean O3 on 70 hPa
filename = "era5_ozone_1999.nc"
if mv.exist(filename):
    nc = mv.read(filename)
else:
    nc = mv.gallery.load_dataset(filename)

# this NetCDF data has the following structure:
#
# dimensions:
# 	longitude = 1440 ;
# 	latitude = 721 ;
# 	time = 4 ;
# variables:
# 	float longitude(longitude) ;
# 	float latitude(latitude) ;
# 	int time(time) ;
# 		time:units = "hours since 1900-01-01 00:00:00.0" ;
# 	short o3(time, latitude, longitude) ;
# 		o3:units = "kg kg**-1" ;
# 		o3:long_name = "Ozone mass mixing ratio" ;

# define contour shading
cont = mv.mcont(
    legend="on",
    contour="off",
    contour_max_level=4e-6,
    contour_min_level=5e-7,
    contour_label="off",
    contour_shade="on",
    contour_shade_colour_method="palette",
    contour_shade_method="area_fill",
    contour_shade_palette_name="m_purple_9",
)

# define coastlines
coastlines = mv.mcoast(
    map_coastline_thickness=2, map_grid_colour="RGB(0.349,0.349,0.349)", map_label="off"
)

# define goegraphical view
view = mv.geoview(
    map_projection="polar_stereographic",
    map_area_definition="corners",
    map_hemisphere="south",
    area=[-5.23, 46.28, -5.72, -132.72],
    coastlines=coastlines,
)

# create a 2x2 plot layout with the defined geoview
dw = mv.plot_superpage(pages=mv.mvl_regular_layout(view, 2, 2, 1, 1, [5, 100, 10, 100]))

# define month names for plot titles
months = ["JAN", "APR", "JUL", "OCT"]

# we build the plot object for each map in a loop
p_obj = []
for i in range(4):

    # define netcdf plotting
    vis = mv.netcdf_visualiser(
        netcdf_plot_type="geo_matrix",
        netcdf_latitude_variable="latitude",
        netcdf_longitude_variable="longitude",
        netcdf_value_variable="o3",
        netcdf_dimension_setting_method="index",
        netcdf_dimension_setting=["time:" + str(i)],
        netcdf_data=nc,
    )

    # define title
    title = mv.mtext(
        text_lines=[
            "<netcdf_info variable='o3' attribute='long_name'/> "
            + "[<netcdf_info variable='o3' attribute='units'/>] 70 hPa - 1999 "
            + months[i]
        ],
        text_font_size=0.3,
    )

    # add current plot definition to the plot object
    p_obj.append([dw[i], vis, cont, title])


# define output
mv.setoutput(mv.pdf_output(output_name="nc_era5_ozone"))

# generate plot
mv.plot(p_obj)
