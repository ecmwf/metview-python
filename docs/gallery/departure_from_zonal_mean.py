"""
GRIB - Departure from zonal mean
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

# getting data
use_mars = False

# getting forecast data from MARS
if use_mars:
    g = mv.retrieve(
        type="an",
        param="z",
        date=20200101,
        time=0,
        levtype="pl",
        levelist=500,
        grid=[1, 1],
    )
# read data from file
else:
    filename = "z500_an.grib"
    if mv.exist(filename):
        g = mv.read(filename)
    else:
        g = mv.gallery.load_dataset(filename)

# compute departure from zonal mean
dep = g - mv.mean_ew(g)

# define contour style for z500
cont = mv.mcont(
    contour_line_colour="black",
    contour_highlight_colour="black",
    contour_level_selection_type="interval",
    contour_interval=10,
)

# define contour shading for departures
cont_dep = mv.mcont(
    legend="on",
    contour="off",
    contour_level_selection_type="interval",
    contour_max_level=50,
    contour_min_level=-50,
    contour_interval=10,
    contour_label="off",
    contour_shade="on",
    contour_shade_colour_method="palette",
    contour_shade_method="area_fill",
    contour_shade_palette_name="colorbrewer_RdBu_10",
    grib_scaling_of_derived_fields="on",
)

# define coastline
coast_dep = mv.mcoast(
    map_coastline_colour="charcoal",
    map_coastline_thickness=2,
    map_label_height=0.2,
    map_label_blanking="off",
    map_grid_colour="RGB(0.5,0.5,0.5)",
)

coast = mv.mcoast(
    map_coastline_colour="grey",
    map_coastline_land_shade="on",
    map_coastline_land_shade_colour="RGB(0.8843,0.7567,0.5196)",
    map_coastline_sea_shade="on",
    map_coastline_sea_shade_colour="RGB(0.853,0.8859,0.9352)",
    map_label_height=0.2,
    map_label_blanking="off",
    map_grid_colour="RGB(0.5,0.5,0.5)",
)

# define map view
view = mv.geoview(
    map_projection="polar_stereographic",
    map_area_definition="corners",
    area=[0, -46, -0, 134],
    coastlines=coast,
)

# define layout
page_0 = mv.plot_page(top=20, bottom=80, right=50, view=view)

page_1 = mv.plot_page(top=20, bottom=80, left=50, right=100, view=view)

dw = mv.plot_superpage(page=[page_0, page_1])

# build title
title_dep = mv.mtext(
    text_lines=["Z500 hPa - Departure from zonal mean"], text_font_size=0.5
)

title = mv.mtext(text_lines=["Z500 hPa"], text_font_size=0.5)

# define the output plot file
mv.setoutput(mv.pdf_output(output_name="departure_from_zonal_mean"))

# generate plot
mv.plot(dw[0], coast_dep, dep, cont_dep, title_dep, dw[1], coast, g, cont, title)
