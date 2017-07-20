"""
Metview Python Framework

The Python analyst retrieves, for a given time interval, the values of a
desired parameter and plots its values for a specific time

--------------------------------------------------------------------------------
1. Python analyst retrieves, for a given time interval, the chosen
   parameter of a file (i.e. forecast, analyses, climatology) from a given
   source (i.e. MARS, files, observation databases)
--------------------------------------------------------------------------------

--------------------------------------------------------------------------------
2. Python analyst plots the 2D field (map) of values for a specific time
--------------------------------------------------------------------------------

"""
import mpy.metview as mpy


# Simplest plot:
# NOTE that when plotting a 'raw' BUFR file, Magics will plot synop symbols as shown in
# https://software.ecmwf.int/wiki/display/METV/Data+Part+1 "Plotting BUFR Data"

obs = mpy.read('./tests/obs_3day.bufr')

mpy.plot(obs)


# ALTERNATIVELY, add an Observations Plotting visual definition and add land/sea shading

obs_plotting = mpy.mobs({
    'obs_temperature': False,
    'obs_cloud': False,
    'obs_low_cloud': False,
    'obs_dewpoint_colour': 'purple'
})

land_sea_shade = mpy.mcoast({
    'map_coastline_land_shade': True,
    'map_coastline_land_shade_colour': "RGB(0.98,0.95,0.82)",
    'map_coastline_sea_shade': False,
    'map_coastline_sea_shade_colour': "RGB(0.85,0.93,1)"
})

mpy.plot(obs, land_sea_shade, obs_plotting)

# ALTERNATIVELY, if we don't want to plot the whole observations, but instead want to
# extract a specific parameter from the BUFR messages, then we use the Observation Filter
# as shown here:

# dewpoint_t is a 'geopoints' variable
dewpoint_t = mpy.obsfilter({
    'output': "geopoints",
    'parameter': '012006',
    'data': obs
})

# add an optional Symbol Plotting definition to get nice coloured circles
# at each point
symb_visdef = mpy.msymb({
    'legend': True,
    'symbol_type': 'marker',
    'symbol_table_mode': 'advanced',
    'symbol_advanced_table_max_level_colour': 'red',
    'symbol_advanced_table_min_level_colour': 'blue',
    'symbol_advanced_table_colour_direction': 'clockwise'
})

mpy.plot(dewpoint_t, symb_visdef)
