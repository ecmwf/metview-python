"""
Metview Python framework

UC-04. The Analyst retrieves, for a given time interval, the values of
two parameters and combines their values on the same map

--------------------------------------------------------------------------------
1. Analyst retrieves, for a given time interval, the values of two chosen
   parameters (e.g. temperature, and geopotential) from a given source (i.e. MARS,
   files, observation databases)
--------------------------------------------------------------------------------

--------------------------------------------------------------------------------
2. Analyst customises many features of his map for each field he wants to plot
   (e.g. temperature field as shaded areas and geopotenti2. al field as isolines)
--------------------------------------------------------------------------------

--------------------------------------------------------------------------------
3. Analyst plots the data
--------------------------------------------------------------------------------
Analyst plots data variable t2 with contouring definition t_shade_c, and data
variable z with contouring definition mslp_isolines.
The fields will be plotted in the order they appear in the mpy.plot() command,
with the shaded temperature at the bottom, and the geopotential on top.
"""

import mpy.metview as mpy


# retrieve 2m temperature
t2 = mpy.read('./examples/t2_for_UC-04.grib')

# retrieve geopotential
z = mpy.read('./examples/z_for_UC-04.grib')

# t_shade_c = {
#     'legend': True,
#     'contour_highlight': False,
#     'contour_level_selection_type': 'level_list',
#     'contour_level_list': (-80, -30, -10, -5, 0, 5, 10, 15, 20, 30, 40, 80),
#     'contour_shade': True,
#     'contour_shade_method': 'area_fill',
#     'contour_shade_max_level_colour': 'red',
#     'contour_shade_min_level_colour': 'blue',
#     'contour_shade_colour_direction': 'clockwise',
# }
t_shade_c = mpy.mcont({
    'legend': True,
    'contour_highlight': False,
     'contour_level_selection_type': "interval",
     #'contour_level_list': [-80,-30,-10,-5,0,5,10,15,20,30,40,80],
    'contour_interval': 10,
    'contour_shade': True,
    'contour_shade_max_level': 60,
    'contour_shade_min_level': -60,
    'contour_shade_method': "area_fill",
    'contour_shade_max_level_colour': "red",
    'contour_shade_min_level_colour': "blue",
    'contour_shade_colour_direction': "clockwise"
 })

z_isolines = mpy.mcont({
    'legend': True,
    'contour_line_thickness': 2,
    'contour_line_colour': 'black',
    'contour_highlight_colour': 'black',
    'contour_highlight_thickness': 4,
    'contour_level_selection_type': 'interval',
    'contour_interval': 5,
    'contour_legend_text': 'Geopotential',
})

mpy.plot(t2, t_shade_c, z, z_isolines)