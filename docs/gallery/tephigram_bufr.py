"""
BUFR - Tephigram
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

# read BUFR data
filename = "temp.bufr"
if mv.exist(filename):
    b = mv.read(filename)
else:
    b = mv.gallery.load_dataset(filename)

# extract thermo profile for a given station
prof = mv.thermo_bufr(data=b, station=mv.stations(search_key="ident", ident=96481))

# define the thermodynamic view
view = mv.thermoview(
    type="tephigram", minimum_temperature=-120, maximum_temperature=35, top_pressure=100
)

# visual definition for t and td profile
vis = mv.mthermo(
    thermo_temperature_line_colour="purplish_red",
    thermo_temperature_line_thickness=6,
    thermo_temperature_missing_data_colour="purplish_red",
    thermo_temperature_missing_data_thickness=6,
    thermo_dewpoint_line_colour="purplish_red",
    thermo_dewpoint_line_thickness=6,
    thermo_dewpoint_missing_data_colour="purplish_red",
    thermo_dewpoint_missing_data_thickness=6,
)

# define the output plot file
mv.setoutput(mv.pdf_output(output_name="tephigram_bufr"))

# plot the profile
mv.plot(view, prof, vis)
