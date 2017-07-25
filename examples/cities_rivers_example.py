
import mpy.metview as mpy


'''
================================================================================
Python version of the MACRO example at
https://software.ecmwf.int/wiki/display/METV/Boundaries%2C+Cities+and+Rivers+Example
================================================================================
'''

# set up the geographical view
my_view = mpy.geoview({
    'map_area_definition': 'FULL',
    'map_projection': 'CYLINDRICAL',
})

# set up the coastlines so that cities, rivers, borders and admnistrative boundaries
# are shown
my_coast = mpy.mcoast({
    'map_administrative_boundaries_colour'         : 'ORANGE',
    'map_boundaries'                               : True,
    'map_coastline_resolution'                     : 'HIGH',
    'map_coastline_land_shade_colour'              : 'CREAM',
    'map_cities'                                   : True,
    'map_grid'                                     : False,
    'map_boundaries_colour'                        : 'RED',
    'map_grid_colour'                              : 'TAN',
    'map_rivers'                                   : True,
    'map_administrative_boundaries_countries_list' : 'GBR',
    'map_coastline_land_shade'                     : True,
    'map_coastline_colour'                         : 'TAN',
    'map_administrative_boundaries'                : True
})

my_text = mpy.mtext({
    'text_font_size'     : '0.80',
    'text_lines'         : 'Administrative boundaries, cities and rivers',
    'text_justification' : 'LEFT',
    'text_colour'        : 'CHARCOAL'
})

# define the output media
to_psfile = mpy.ps_output({
    'output_name' : './examples/plot' # extension is added automatically
})
mpy.setoutput(to_psfile)

# plot the coastlines data onto the map
mpy.plot(my_view, my_coast, my_text)
