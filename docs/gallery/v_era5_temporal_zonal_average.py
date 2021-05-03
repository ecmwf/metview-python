"""
GRIB - Temporal Zonal Average of ERA5 V Wind Component
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
import cdsapi

# getting data
use_cds = False

filename = "v_era5_mnth.grib"

pressures = [1000, 925, 850, 700, 500, 400, 300, 250, 200, 150, 100]

# getting forecast data from CDS
if use_cds:
    c = cdsapi.Client()
    c.retrieve(
        "reanalysis-era5-pressure-levels-monthly-means",
        {
            "product_type": "monthly_averaged_reanalysis",
            "variable": "v_component_of_wind",
            "pressure_level": pressures,
            "year": [2006],
            "month": [3, 4, 5],
            "day": "01",
            "time": "00:00",
            "area": [90, -180, -90, 180],
            "grid": [1, 1],
            "format": "grib",
        },
        filename,
    )
    g = mv.read(filename)
# read data from file
else:
    if mv.exist(filename):
        g = mv.read(filename)
    else:
        g = mv.gallery.load_dataset(filename)

# compute temporal mean on each pressure level
g_m = mv.Fieldset()
for lev in pressures:
    g_lev = mv.read(data=g, levelist=lev)
    g_m.append(mv.mean(g_lev))

# define horizontal axis
horiz_axis = mv.maxis(axis_tick_label_height=0.4)

# define vertical axis
vertical_axis = mv.maxis(
    axis_orientation="vertical",
    axis_type="position_list",
    axis_tick_position_list=[
        1000,
        925,
        850,
        700,
        500,
        400,
        300,
        250,
        200,
        150,
        100,
    ],
    axis_tick_label_height=0.4,
)

# define averaging area - one half of the Northern Hemisphere
area = [90, -180, -90, 180]  # N,W,S,E

# define average view for zonal mean
view = mv.maverageview(
    top_level=100,
    bottom_level=1000,
    vertical_scaling="log",
    area=area,
    direction="ew",
    horizontal_axis=horiz_axis,
    vertical_axis=vertical_axis,
)

# define isoline shading for v
cont = mv.mcont(
    legend="on",
    contour_line_colour="charcoal",
    contour_highlight="off",
    contour_level_selection_type="interval",
    contour_max_level=4,
    contour_min_level=-4,
    contour_interval=0.5,
    contour_label="off",
    contour_shade="on",
    contour_shade_colour_method="palette",
    contour_shade_method="area_fill",
    contour_shade_palette_name="colorbrewer_PuOr_16",
)

# define dashed contours for t
cont_t = mv.mcont(
    contour_line_style="dash",
    contour_line_thickness=2,
    contour_line_colour="charcoal",
    contour_highlight_style="dash",
    contour_highlight_colour="charcoal",
    contour_highlight_thickness=4,
    contour_level_selection_type="interval",
    contour_interval=10,
)

title = mv.mtext(
    text_lines="ERA5 - Zonal Average of V wind component - 2006 March-April-May",
    text_font_size=0.4,
)

# define the output plot file
mv.setoutput(mv.pdf_output(output_name="v_era5_temporal_zonal_average"))

# generate plot
mv.plot(view, g_m, cont, title)
