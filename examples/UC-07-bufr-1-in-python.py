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
})

mpy.plot(diff, diff_symb)


# Extract geopoints that are hotter by 1 deg or more
#hotter = mpy.filter(diff, diff >= 1)
hotter = diff.filter(diff >= 1)

# Extract geopoints that are colder by 1 deg or more
#colder = mpy.filter(diff, diff <= -1)
colder = diff.filter(diff <= -1)

# Get geopoints that are within +/-1
#exact = mpy.filter(diff, (diff > -1) * (diff < 1))
exact = diff.filter((diff > -1) * (diff < 1))

# Symbol visdefs for each classification
red = mpy.msymb({
    'symbol_type': 'marker',
    'symbol_colour': 'red'
})

blue  = mpy.msymb({
    'symbol_type': 'marker',
    'symbol_colour': 'blue'
})

grey  = mpy.msymb({
    'symbol_type': 'marker',
    'symbol_colour': 'grey'
})

# plot the 'exact' data set with visdef 'grey', 'hotter' with 'red', etc.
mpy.plot(exact, grey, hotter, red, colder, blue)
