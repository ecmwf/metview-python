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

uv = mv.read('./uv.grib')

u = mv.read(data=uv, param='u')
v = mv.read(data=uv, param='v')

wind_speed = mv.sqrt(u * u + v * v)

mv.setoutput(mv.png_output(output_width = 1000, output_name = './uvplot'))
mv.plot(wind_speed)
