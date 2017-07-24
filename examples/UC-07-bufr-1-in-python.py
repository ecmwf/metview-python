"""
Metview Python framework

UC-07. The Analyst compute simple differences between observations and analysis
and plot the values

BUFR version - BUFR is not tabular or gridded, but we can use Metview Python
framework to extract a particular parameter to a tabular format (geopoints)

--------------------------------------------------------------------------------
1. Analyst retrieves the analysis from a gridded data file
--------------------------------------------------------------------------------

--------------------------------------------------------------------------------
2. Analyst retrieves an observational parameter from a tabular or a gridded file
--------------------------------------------------------------------------------

--------------------------------------------------------------------------------
3. Analyst calculates the difference between the observational data and the
   analysis and classified the field values according to the magnitude of the
   difference
--------------------------------------------------------------------------------

--------------------------------------------------------------------------------
4. Analyst customises many features of his graph in order to create
   publication-quality plots
--------------------------------------------------------------------------------

--------------------------------------------------------------------------------
5. Analyst plots the data
--------------------------------------------------------------------------------
"""

import mpy.metview as mpy


t2m_grib = mpy.read('./examples/t2m_grib.grib')

obs_3day = mpy.read('./examples/obs_3day.bufr')

t2m_gpt = mpy.obsfilter({
    'parameter': '012004',   # 012004 -> dry bulb temperature at 2m
    'output': 'geopoints',
    'data': obs_3day
})

diff = t2m_grib - t2m_gpt

diff_symb = mpy.msymb({
    'legend': True,
    'symbol_type': 'marker',
    'symbol_table_mode': 'advanced',
    #'symbol_advanced_table_selection_type': 'list',
    #'symbol_advanced_table_level_list': [-1000,-1,1,1000],
    # 'symbol_advanced_table_colour_method': 'list',
    #'symbol_advanced_table_colour_list': ['blue','grey','red']
})

mpy.plot(diff, diff_symb)

# diff_symb_cold = mpy.msymb({
#     'legend': True,
#     'symbol_type': 'marker',
#     'symbol_table_mode': 'advanced',
#     'symbol_advanced_table_selection_type' : 'list',
#     'symbol_advanced_table_level_list': [-15, -10, -5, -1, 0],
#     'symbol_advanced_table_colour_method': 'list',
#     'symbol_advanced_table_colour_list': ['blue','sky', 'rgb(0.82, 0.85, 1)', 'white'],
#     'symbol_advanced_table_height_list': [0.6, 0.5, 0.4],
#     'symbol_outline': True,
#     'symbol_outline_colour': 'charcoal',
# })
#
# diff_symb_hot = mpy.symb({
#     'legend': True,
#     'symbol_type': 'marker',
#     'symbol_table_mode': 'advanced',
#     'symbol_advanced_table_selection_type': 'list',
#     'symbol_advanced_table_level_list': (0, 1, 5, 10, 15),
#     'symbol_advanced_table_max_level_colour': 'red',
#     'symbol_advanced_table_min_level_colour': 'white',
#     'symbol_advanced_table_colour_direction': 'clockwise',
#     'symbol_advanced_table_marker_list': 15,
#     'symbol_advanced_table_height_list': (0.4, 0.5, 0.6),
#     'symbol_outline': True,
#     'symbol_outline_colour': 'charcoal',
# })

#mpy.plot(diff, diff_symb_cold, diff, diff_symb_hot)
