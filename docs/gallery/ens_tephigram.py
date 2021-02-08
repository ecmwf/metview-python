"""
GRIB - ENS Tephigram
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

import numpy as np
import metview as mv

# read ENS data
filename = "ens_prof.grib"
if mv.exist(filename):
    data = mv.read(filename)
else:
    data = mv.gallery.load_dataset(filename)

# define profile location
location = [17.51, -7.04]

# the starting x coordinate of the sidebar on the right.
# Wind and dewpoint depression is plotted there.
# Do not change it!
sidebar_x_offset = 1000

# the ensemble size (perturbed members)
ens_num = 50

# filter control (cf) and perturbed (pf) forcasts
g_cf = mv.read(data=data, type="cf")
g_pf = mv.read(data=data, type="pf")

# extract thermo profile for cf
nc = mv.thermo_grib(
    data=g_cf, point_extraction="nearest_gridpoint", coordinates=location
)

prof_cf = mv.thermo_data_values(nc, 0)

# extract thermo profile for pf
nc = mv.thermo_grib(
    data=g_pf, point_extraction="nearest_gridpoint", coordinates=location
)

prof_pf = mv.thermo_data_values(nc, 0)

# define colours for shaded areas
t_col_outer = "RGB(1.0000,0.7922,0.7961)"
t_col_inner = "RGB(0.8863,0.0000,0.0000)"
td_col_outer = "RGB(0.8,0.9137,0.8)"
td_col_inner = "RGB(0.3882,0.7765,0.3843)"
ddep_col_outer = "RGB(0.8118,0.8902,1)"
ddep_col_inner = "RGB(0.4353,0.6314,1)"

# define colours for curves
t_col_line = "RGB(0.8706,0,0)"
td_col_line = "RGB(0,0.2784,0.007843)"
ddep_col_line = "RGB(0,0.3725,1)"

# define cf curve data
t_cf = prof_cf["t"]
td_cf = prof_cf["td"]
ddep_cf = (t_cf - td_cf) + sidebar_x_offset

# get pressure levels for t and td (from pf)
# and compute ENS mean profiles
lev_num = int(len(prof_pf["p"]) / ens_num)
p = np.empty(lev_num)
t_mean = np.empty(lev_num)
td_mean = np.empty(lev_num)
ddep_mean = np.empty(lev_num)

for i in range(len(p)):
    # get pressure
    p[i] = prof_pf["p"][i * ens_num]

    # get t and td for all the perturbed members
    idx_start = i * ens_num
    idx_end = (i + 1) * ens_num - 1
    t_v = prof_pf["t"][idx_start:idx_end]
    td_v = prof_pf["td"][idx_start:idx_end]

    # add t and td from cf
    t_v = np.append(t_v, t_cf[i])
    td_v = np.append(td_v, td_cf[i])

    # compute means
    t_mean[i] = mv.mean(t_v)
    td_mean[i] = mv.mean(td_v)
    ddep_mean[i] = mv.mean(t_v - td_v) + sidebar_x_offset

# compute areas (polygons) for t, td and dew point depression (ddep)
# outer area = full ENS range
# inner area = 25-75 percentile range
p_poly = np.empty(lev_num * 2)
t_poly_inner = np.empty(lev_num * 2)
t_poly_outer = np.empty(lev_num * 2)
td_poly_inner = np.empty(lev_num * 2)
td_poly_outer = np.empty(lev_num * 2)
ddep_poly_inner = np.empty(lev_num * 2)
ddep_poly_outer = np.empty(lev_num * 2)

for i in range(lev_num):
    # collect t and td (pf+cf) for the given level
    idx_start = i * ens_num
    idx_end = (i + 1) * ens_num - 1
    t_v = prof_pf["t"][idx_start:idx_end]
    td_v = prof_pf["td"][idx_start:idx_end]
    t_v = np.append(t_v, t_cf[i])
    td_v = np.append(td_v, td_cf[i])

    i_left = i
    i_right = 2 * lev_num - i - 1

    p_poly[i_left] = p[i]
    p_poly[i_right] = p[i]

    t_poly_outer[i_left] = mv.minvalue(t_v)
    t_poly_outer[i_right] = mv.maxvalue(t_v)
    perc = mv.percentile(t_v, [25, 75])
    t_poly_inner[i_left] = perc[0]
    t_poly_inner[i_right] = perc[1]

    td_poly_outer[i_left] = mv.minvalue(td_v)
    td_poly_outer[i_right] = mv.maxvalue(td_v)
    perc = mv.percentile(td_v, [25, 75])
    td_poly_inner[i_left] = perc[0]
    td_poly_inner[i_right] = perc[1]

    ddep_v = t_v - td_v + sidebar_x_offset
    ddep_poly_outer[i_left] = mv.minvalue(ddep_v)
    ddep_poly_outer[i_right] = mv.maxvalue(ddep_v)
    perc = mv.percentile(ddep_v, [25, 75])
    ddep_poly_inner[i_left] = perc[0]
    ddep_poly_inner[i_right] = perc[1]

# generate graphic objects (areas) for the shaded areas
gr_lst = [
    mv.xy_area(t_poly_outer, p_poly, t_col_outer),
    mv.xy_area(t_poly_inner, p_poly, t_col_inner),
    mv.xy_area(td_poly_outer, p_poly, td_col_outer),
    mv.xy_area(td_poly_inner, p_poly, td_col_inner),
    mv.xy_area(ddep_poly_outer, p_poly, ddep_col_outer),
    mv.xy_area(ddep_poly_inner, p_poly, ddep_col_inner),
]

# generate graphic objects (curves) for the mean ENS and cf profiles
gr_lst.extend(
    [
        mv.xy_curve(t_mean, p, t_col_line, "solid", 4),
        mv.xy_curve(td_mean, p, td_col_line, "solid", 4),
        mv.xy_curve(ddep_mean, p, ddep_col_line, "solid", 4),
        mv.xy_curve(t_cf, prof_cf["p"], t_col_line, "dash", 3),
        mv.xy_curve(td_cf, prof_cf["p"], td_col_line, "dash", 3),
        mv.xy_curve(ddep_cf, prof_cf["p"], ddep_col_line, "dash", 3),
    ]
)

# generate graphic object for wind profile from cf
vis = mv.input_visualiser(
    input_plot_type="xy_vectors",
    input_x_values=[sidebar_x_offset + 10 for i in prof_cf["p_wind"]],
    input_y_values=prof_cf["p_wind"],
    input_x_component_values=prof_cf["u"],
    input_y_component_values=prof_cf["v"],
)

wind_plotting = mv.mwind(wind_field_type="flags", wind_flag_colour="charcoal")

gr_lst.extend([vis, wind_plotting])

# define title
title_txt = "ENS Tephigram Date: {} {} UTC Lat/Lon: {}/{} ".format(
    prof_cf["date"], prof_cf["time"], prof_cf["lat"], prof_cf["lon"]
)

title = mv.mtext(text_lines=title_txt, text_font_size=0.5, text_colour="charcoal")

# define thermodynamic grid
grid = mv.mthermogrid(
    thermo_isotherm_colour="RGB(0.2577,0.6364,0.5039)",
    thermo_isotherm_reference_colour="blue",
    thermo_dry_adiabatic_colour="grey",
    thermo_dry_adiabatic_label_frequency=2,
    thermo_mixing_ratio_colour="RGB(0.2577,0.6364,0.5039)",
    thermo_mixing_ratio_label_colour="RGB(0.2577,0.6364,0.5039)",
    thermo_mixing_ratio_label_font_size=0.4,
    thermo_grid_layer_mode="foreground",
)

# define thermodynamic view
view = mv.thermoview(
    type="tephigram",
    minimum_temperature=-110,
    maximum_temperature=30,
    subpage_clipping="on",
)


# define the output plot file
mv.setoutput(mv.pdf_output(output_name="ens_tephigram"))

# generate the plot
mv.plot(view, gr_lst, grid, title)
