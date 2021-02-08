"""
GRIB - SST on Extended Cylindrical Map
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

# read GRIB
filename = "sst.grib"
if mv.exist(filename):
    sst = mv.read(filename)
else:
    sst = mv.gallery.load_dataset(filename)

# define contouring
cont = mv.mcont(contour_automatic_setting="ecmwf", legend="on")

# define land-sea shading
coast = mv.mcoast(
    map_coastline_land_shade="on",
    map_coastline_land_shade_colour="RGB(0.16,0.16,0.16)",
    map_coastline_sea_shade="on",
    map_coastline_sea_shade_colour="RGB(0.4686,0.4686,0.4686)",
    map_coastline_colour="RGB(0.6686,0.6686,0.6686)",
    map_grid_colour="RGB(0.2686,0.2686,0.2686)",
    map_grid_longitude_increment=30,
    map_grid_latitude_increment=20,
)


# define the view - recentred and lon range is larger than 360!
view = mv.geoview(
    map_area_definition="corners", area=[-90, 20, 90, 420], coastlines=coast
)

# define the output plot file
mv.setoutput(mv.pdf_output(output_name="sst_extended_latlon"))

# generate plot
mv.plot(view, sst, cont)
