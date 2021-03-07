"""
GRIB - ERA5 SST El Nino Maps
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

# getting the data
use_cds = False

filename = "sst_era5_mnth.grib"

# getting forecast data from CDS
if use_cds:
    c = cdsapi.Client()
    c.retrieve(
        "reanalysis-era5-single-levels-monthly-means",
        {
            "product_type": "monthly_averaged_reanalysis",
            "variable": "sea_surface_temperature",
            "year": [1993, 1997, 1998],
            "month": [12],
            "day": "01",
            "time": "00:00",
            "area": [90, -180, -90, 180],
            "grid": [0.25, 0.25],
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


# define coastlines
coast = mv.mcoast(
    map_coastline_land_shade="on", map_coastline_land_shade_colour="charcoal"
)


# define the view
view = mv.geoview(
    map_area_definition="corners", area=[-20, 100, 20, -60], coastlines=coast
)

# define a 3x1 layout
page_0 = mv.plot_page(top=0, bottom=30, left=5, right=95, view=view)
page_1 = mv.plot_page(top=33, bottom=63, left=5, right=95, view=view)
page_2 = mv.plot_page(top=66, bottom=96, left=5, right=95, view=view)
dw = mv.plot_superpage(pages=[page_0, page_1, page_2])

# define isoline shading
cont = mv.mcont(
    legend="on",
    contour="off",
    contour_level_selection_type="interval",
    contour_max_level=32,
    contour_min_level=15,
    contour_interval=1,
    contour_label="off",
    contour_shade="on",
    contour_shade_colour_method="palette",
    contour_shade_method="area_fill",
    contour_shade_palette_name="colorbrewer_Spectral_17",
)

# define title
title_core = "ERA5 <grib_info key='shortName'/> Monthly mean: <grib_info key='valid-date' format='%Y %b'/>"

title_normal = mv.mtext(
    text_lines=f"Normal conditions - {title_core}", text_font_size=0.35
)
title_elnino = mv.mtext(text_lines=f"El Nino - {title_core}", text_font_size=0.35)
title_lanina = mv.mtext(text_lines=f"La Nina - {title_core}", text_font_size=0.35)

# define the output plot file
mv.setoutput(mv.pdf_output(output_name="sst_era5_elnino_map"))

# generate plot
mv.plot(
    dw[0],
    g[0],
    cont,
    title_normal,
    dw[1],
    g[1],
    cont,
    title_elnino,
    dw[2],
    g[2],
    cont,
    title_lanina,
)
