"""
GRIB - ERA5 Ozone Latitude Hovmoeller
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

filename = "o3_era5_50hpa_mnth.grib"

# getting forecast data from CDS
if use_cds:
    c = cdsapi.Client()
    c.retrieve(
        "reanalysis-era5-pressure-levels-monthly-means",
        {
            "product_type": "monthly_averaged_reanalysis",
            "variable": "ozone_mass_mixing_ratio",
            "pressure_level": [50],
            "year": [2005, 2006, 2007],
            "month": list(range(13)),
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

# define time axis
time_axis = mv.maxis(
    axis_type="date",
    axis_date_type="months",
    axis_years_label_quality="high",
    axis_years_label_height=0.5,
    axis_months_label_quality="high",
    axis_months_label_height=0.3,
    axis_days_label="off",
)

# define vertical axis
geo_axis = mv.maxis(
    axis_tick_label_height=0.4, axis_title_text="Latitude", axis_title_height=0.5
)

# define view
view = mv.mhovmoellerview(
    type="area_hovm",
    area=[90, -180, -90, 180],  # N,W,S,E
    average_direcion="east_west",
    swap_axis="no",
    time_axis=time_axis,
    geo_axis=geo_axis,
)

# define contour shading
cont_shade = mv.mcont(
    legend="on",
    contour="off",
    contour_level_selection_type="interval",
    contour_shade_max_level=7e-6,
    contour_shade_min_level=0,
    contour_interval=5e-7,
    contour_label="off",
    contour_shade="on",
    contour_shade_colour_method="palette",
    contour_shade_method="area_fill",
    contour_shade_palette_name="colorbrewer_Spectral_14",
)

# define legend
legend = mv.mlegend(legend_text_font_size=0.3)

# define the output plot file
mv.setoutput(mv.pdf_output(output_name="ozone_era5_lat_hovmoeller"))

# generate plot
mv.plot(view, g, cont_shade, legend)
