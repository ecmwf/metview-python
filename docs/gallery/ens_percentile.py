"""
GRIB - ENS Windgust Percentile
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
    ret_core = {
        "stream": "enfo",
        "param": "10fg6",
        "date": 20140807,
        "time": 0,
        "step": [78, 84, 90],
        "levtype": "sfc",
        "grid": [0.25, 0.25],
        "area": [60, -20, 43, 10],
    }

    # perturbed ENS members
    pf = mv.retrieve(type="pf", number=["1", "TO", "50"], **ret_core)

    # control member
    cf = mv.retrieve(type="cf", **ret_core)

    g = mv.merge(pf, cf)
# read data from file
else:
    filename = "wgust_ens.grib"
    if mv.exist(filename):
        g = mv.read(filename)
    else:
        g = mv.gallery.load_dataset(filename)

# filter out a timestep
wg = mv.read(data=g, step=78)

# compute percentiles
percentiles = [25, 50, 75, 90]
pc = mv.percentile(data=wg, percentiles=percentiles)

# define contour shading
cont = mv.mcont(
    contour_automatic_setting="style_name",
    contour_style_name="sh_all_f03t70_beauf",
    legend="on",
)

# define coastline
coast = mv.mcoast(map_grid_colour="charcoal", map_grid_longitude_increment=10)

# define map view
view = mv.geoview(
    map_area_definition="corners", area=[43, -20, 60, 10], coastlines=coast
)

# create a 2x2 plot layout with the defined geoview
dw = mv.plot_superpage(pages=mv.mvl_regular_layout(view, 2, 2, 1, 1, [5, 100, 15, 100]))

# define the output plot file
mv.setoutput(mv.pdf_output(output_name="ens_percentile"))

# build plot definition
p_def = []
for i in range(4):
    title = mv.mtext(
        text_lines=[f"Wind gust - {percentiles[i]}% percentile"], text_font_size=0.5
    )
    p_def.extend([dw[i], pc[i], cont, title])

# generate plot
mv.plot(p_def)
