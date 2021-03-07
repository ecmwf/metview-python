"""
GRIB - Derive Divergent and Rotational Wind from Spectral Divergence and Vorticity
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
        date=20181114,
        time=12,
        step=24,
        levelist=850,
        levtype="pl",
        param=["d", "vo"],
    )
# read data from GRIB file
else:
    # read data from GRIB file
    filename = "spectral_d_vo_2018.grib"
    if mv.exist(filename):
        g = mv.read(filename)
    else:
        g = mv.gallery.load_dataset(filename)

# compute divergent wind from spectral divergence. The result is
# still spectral (T255)
d = mv.read(data=g, param="d")
dwind_sh = mv.divwind(data=d, truncation=255)

# transform spectral divergent wind into gridpoint space (reduced Gaussian grid N128)
dwind = mv.read(data=dwind_sh, grid=218)

# compute rotational wind from spectral voricity. The result is
# still spectral (T255)
vo = mv.read(data=g, param="vo")
rwind_sh = mv.divrot(data=vo, truncation=255)

# transform spectral rotational wind into gridpoint space (reduced Gaussian grid N128)
rwind = mv.read(data=rwind_sh, grid=218)

# define coastlines
coast = mv.mcoast(
    map_coastline_colour="cream",
    map_coastline_land_shade="on",
    map_coastline_land_shade_colour="RGB(0.2,0.2,0.2)",
    map_coastline_sea_shade="on",
    map_coastline_sea_shade_colour="RGB(0.3,0.3,0.3)",
    map_grid_colour="RGB(0.9333,0.9333,0.9333)",
)

# define view
view = mv.geoview(area_mode="name", area_name="north_atlantic", coastline=coast)

# define a 2x1 layout
page_0 = mv.plot_page(top=3, bottom=50, left=25, right=75, view=view)
page_1 = mv.plot_page(top=53, bottom=100, left=25, right=75, view=view)
dw = mv.plot_superpage(pages=[page_0, page_1])

# define wind plotting style
wind_style_div = mv.mwind(
    legend="on",
    wind_thinning_factor=2,
    wind_advanced_method="on",
    wind_advanced_colour_selection_type="interval",
    wind_advanced_colour_max_value=12,
    wind_advanced_colour_min_value=0,
    wind_advanced_colour_level_interval=2,
    wind_advanced_colour_max_level_colour="red",
    wind_advanced_colour_min_level_colour="sky",
    wind_advanced_colour_direction="clockwise",
    wind_arrow_unit_velocity=25.0,
)

# define wind plotting style
wind_style_rot = mv.mwind(
    legend="on",
    wind_thinning_factor=2,
    wind_advanced_method="on",
    wind_advanced_colour_selection_type="interval",
    wind_advanced_colour_max_value=50,
    wind_advanced_colour_min_value=0,
    wind_advanced_colour_level_interval=5,
    wind_advanced_colour_max_level_colour="red",
    wind_advanced_colour_min_level_colour="sky",
    wind_advanced_colour_direction="clockwise",
    wind_arrow_unit_velocity=60.0,
)

# define legend
legend = mv.mlegend(legend_text_font_size=0.3)

# define title
title_core = " <grib_info key='base-date'/> +<grib_info key='step'/>h Level: <grib_info key='level'/> hPa"
title_div = mv.mtext(text_lines=f"Divergent Wind - {title_core}", text_font_size=0.35)
title_rot = mv.mtext(text_lines=f"Rotational Wind - {title_core}", text_font_size=0.35)

# define the output plot file
mv.setoutput(mv.pdf_output(output_name="divergent_and_rotational_wind"))

# generate plot
mv.plot(
    dw[0],
    dwind,
    wind_style_div,
    legend,
    title_div,
    dw[1],
    rwind,
    wind_style_rot,
    title_rot,
    legend,
)
