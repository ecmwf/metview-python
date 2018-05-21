"""
Metview Python framework

UC-05. The Analyst retrieves, for a given time interval, the values
# of a derived parameter and plots its values for a specific time.

--------------------------------------------------------------------------------
1. Analyst retrieves, for a given time interval, the chosen parameter of a file
   (i.e. forecast, analyses, climatology) from a given source (i.e. MARS, files,
   observation databases)
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

uv = mv.read('./examples/uv.grib')

u = mv.read(data=uv, param='u')
v = mv.read(data=uv, param='v')

wind_speed = mv.sqrt(u * u + v * v)

mv.plot(wind_speed)
