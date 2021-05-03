"""
GRIB - Derive Wind from Spectral Divergence and Vorticity
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

# get data
use_mars = False

# get data from MARS (T1279 spectral resolution)
if use_mars:
    g = mv.retrieve(
        type="fc",
        date=20171016,
        time=0,
        step=24,
        levelist=850,
        levtype="pl",
        param=["d", "vo"],
    )
# read data from GRIB file
else:
    # read data from GRIB file
    filename = "ophelia_spectral_d_vo.grib"
    if mv.exist(filename):
        g = mv.read(filename)
    else:
        g = mv.gallery.load_dataset(filename)

# compute u/v from spectral divergence and voricity. The result is
# still spectral (T255)
uv_sh = mv.uvwind(data=g, truncation=255)

# transform spectral u/v into gridpoint space (reduced Gaussian grid N128)
uv = mv.read(data=uv_sh, grid=218)

# define wind plotting style
wind_style = mv.mwind(
    wind_thinning_factor=3, wind_arrow_colour="navy", wind_arrow_unit_velocity=25
)

# define coastlines
coast = mv.mcoast(
    map_coastline_land_shade="on",
    map_coastline_land_shade_colour="RGB(0.9603,0.7863,0.5064)",
    map_coastline_sea_shade="on",
    map_coastline_sea_shade_colour="RGB(0.9,0.9,0.9)",
)

# define view
view = mv.geoview(area_mode="name", area_name="north_atlantic", coastline=coast)

# define the output plot file
mv.setoutput(mv.pdf_output(output_name="wind_from_spectral_div_and_vor"))

# generate plot
mv.plot(view, uv, wind_style)
