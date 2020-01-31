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

UC-05. The Analyst retrieves certain parameters, computes a derived
parameter and plots its values for a specific time.

--------------------------------------------------------------------------------
1. Analyst filters, the chosen parameters of a file from a given
   source (i.e. MARS, files, observation databases)
--------------------------------------------------------------------------------

--------------------------------------------------------------------------------
2. Analyst computes the desired derived parameter (i.e. wind velocity from zonal
   and meridional components)
--------------------------------------------------------------------------------

--------------------------------------------------------------------------------
3. Analyst plots the derived parameter values
--------------------------------------------------------------------------------
"""

import metview as mv

uv = mv.read("./uv.grib")

u = mv.read(data=uv, param="u")
v = mv.read(data=uv, param="v")

wind_speed = mv.sqrt(u * u + v * v)

mv.setoutput(mv.png_output(output_width=1000, output_name="./uvplot"))
mv.plot(wind_speed)
