"""
BUFR - Hodograph
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
import math

# read BUFR data
filename = "temp.bufr"
if mv.exist(filename):
    b = mv.read(filename)
else:
    b = mv.gallery.load_dataset(filename)

# define station id
statid = "78583"

# extract thermo profile
nc = mv.thermo_bufr(data=b, station=mv.stations(search_key="ident", ident=statid))

# get individual profiles as vectors. Values are sorted by descending
# pressure, no missing values includes.
info = mv.thermo_data_values(nc, 0)
p = info["p_wind"]
u = info["u"]
v = info["v"]

# define the hodograph background
hodo_incr = 5
hodo_highlight = [10, 20, 30]
hodo_labels = [10, 20, 30]
hodo_max = 35
hodo_colour = "black"

# define the wind speed bins and their associated colours
pres_bins = [1050, 700, 500, 300, 200, 50]
pres_colours = ["red", "kelly_green", "sky", "blue", "magenta"]

# define horizontal and vertical  axes
h_axis = mv.maxis(axis_position="left", axis_tick_label_height=0.4)

v_axis = mv.maxis(axis_position="bottom", axis_tick_label_height=0.4)

# the view
view = mv.cartesianview(
    x_automatic="off",
    x_min=-hodo_max,
    x_max=hodo_max,
    y_automatic="off",
    y_min=-hodo_max,
    y_max=hodo_max,
    horizontal_axis=h_axis,
    vertical_axis=h_axis,
    subpage_x_position=10,
    subpage_y_position=5,
    subpage_x_length=80,
    subpage_y_length=80,
)

# define the plot page and superpage.
# NOTE: In order to correctly render the hodograph (we want
# concentric circles instead of ellipses) we have to make sure
# that the physical width and height of the plot are the same.
# Please note that while the page size is defined in % the
# superpage size is defined in cm! See also subpage size in the view.

# size is in % of the physical size of the superpage!
hodo_page = mv.plot_page(top=0, bottom=100, left=0, right=100, view=view)

# size is in cm!
dw = mv.plot_superpage(
    layout_size="custom", custom_width=15, custom_height=15, pages=hodo_page
)

gr_lst = []

# build the concentric circles
sp = hodo_incr
angle_incr = 2 * math.pi / 180
while sp <= hodo_max:
    xp = [math.cos(i * angle_incr) * sp for i in range(1, 182)]
    yp = [math.sin(i * angle_incr) * sp for i in range(1, 182)]

    if sp in hodo_highlight:
        gr = mv.xy_curve(xp, yp, hodo_colour, "solid", 3)
    else:
        gr = mv.xy_curve(xp, yp, hodo_colour, "solid", 1)

    gr_lst.append(gr)
    sp += hodo_incr

# build horizontal and vertical lines going
# throug the centre
gr_lst.append(mv.xy_curve([-hodo_max, hodo_max], [0, 0], hodo_colour, "solid", 1))
gr_lst.append(mv.xy_curve([0, 0], [-hodo_max, hodo_max], hodo_colour, "solid", 1))

# build labels on the horizontal line
vis = mv.input_visualiser(
    input_plot_type="xy_point",
    input_x_values=[-v for v in hodo_labels] + hodo_labels,
    input_y_values=[0 for i in range(len(hodo_labels) * 2)],
    input_values=hodo_labels + hodo_labels,
)

sym = mv.msymb(
    symbol_colour=hodo_colour,
    symbol_text_font_size=0.5,
    symbol_text_font_style="bold",
    symbol_text_position="bottom",
)

gr_lst.extend([vis, sym])

# build the graphical objects for the wind data (per bin)
gr_wind = []
for i in range(len(pres_bins) - 1):

    # collect wind data in bin
    u_val = []
    v_val = []
    for k in range(len(p)):
        if (
            not math.isnan(p[k])
            and not math.isnan(u[k])
            and not math.isnan(v[k])
            and p[k] <= pres_bins[i]
            and p[k] >= pres_bins[i + 1]
        ):
            u_val.append(u[k])
            v_val.append(v[k])

    # build graph object
    if u_val and v_val:
        vis = mv.input_visualiser(input_x_values=u_val, input_y_values=v_val)

        gr = mv.mgraph(
            legend="on",
            graph_line_colour=pres_colours[i],
            graph_line_style="solid",
            graph_line_thickness=5,
        )
        gr_wind.extend([vis, gr])

# define legend with custom labels
legend_text = []
for i in range(len(pres_bins) - 1):
    legend_text.append(str(pres_bins[i]) + "-" + str(pres_bins[i + 1]))

legend = mv.mlegend(
    legend_display_type="disjoint",
    legend_text_font_size=0.5,
    legend_text_composition="user_text_only",
    legend_user_lines=legend_text,
)

# define title
title_txt = "HODOGRAPH Date: {} {} Station: {} Lat/Lon: {}/{}".format(
    info["date"], info["time"], info["station"], info["lat"], info["lon"]
)

title = mv.mtext(text_lines=title_txt, text_font_size=0.5, text_colour="charcoal")

# define the output plot file
mv.setoutput(mv.pdf_output(output_name="hodograph"))

# generate the plot
mv.plot(dw, gr_lst, gr_wind, legend, title)
