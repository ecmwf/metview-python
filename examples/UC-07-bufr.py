# (C) Copyright 2017- ECMWF.
#
# This software is licensed under the terms of the Apache Licence Version 2.0
# which can be obtained at http://www.apache.org/licenses/LICENSE-2.0.
#
# In applying this licence, ECMWF does not waive the privileges and immunities
# granted to it by virtue of its status as an intergovernmental organisation
# nor does it submit to any jurisdiction.

"""
Metview Python use case

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

import metview as mv

# define a view over the area of interest

area_view = mv.geoview(map_area_definition="corners", area=[45.83, -13.87, 62.03, 8.92])

t2m_grib = mv.read("./t2m_grib.grib")

obs_3day = mv.read("./obs_3day.bufr")

t2m_gpt = mv.obsfilter(parameter="012004", output="geopoints", data=obs_3day)

diff = t2m_grib - t2m_gpt

diff_symb = mv.msymb(
    legend=True,
    symbol_type="marker",
    symbol_table_mode="advanced",
)

mv.setoutput(mv.png_output(output_width=1000, output_name="./obsdiff1"))
mv.plot(area_view, diff, diff_symb)


# Extract geopoints that are hotter by 1 deg or more
# hotter = mv.filter(diff, diff >= 1)
hotter = diff.filter(diff >= 1)

# Extract geopoints that are colder by 1 deg or more
# colder = mv.filter(diff, diff <= -1)
colder = diff.filter(diff <= -1)

# Get geopoints that are within +/-1
# exact = mv.filter(diff, (diff > -1) * (diff < 1))
exact = diff.filter((diff > -1) * (diff < 1))

# Symbol visdefs for each classification
red = mv.msymb(symbol_type="marker", symbol_colour="red")

blue = mv.msymb(symbol_type="marker", symbol_colour="blue")

grey = mv.msymb(symbol_type="marker", symbol_colour="grey")

# plot the 'exact' data set with visdef 'grey', 'hotter' with 'red', etc.
mv.setoutput(mv.png_output(output_width=1000, output_name="./obsdiff2"))
mv.plot(area_view, exact, grey, hotter, red, colder, blue)
