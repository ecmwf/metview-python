
Data access
===========================



Data retrieval
-------------------------------

.. list-table::
    :widths: 20 10 70
    :header-rows: 0


    * - :func:`ecfs`
      - .. image:: _static/MCONT.png 
           :width: 16px
      - 

    * - :func:`flexpart_prepare`
      - .. image:: _static/MCONT.png 
           :width: 16px
      - 

    * - :func:`flextra_prepare`
      - .. image:: _static/MCONT.png 
           :width: 16px
      - 

    * - :func:`met3d_prepare`
      - .. image:: _static/MCONT.png 
           :width: 16px
      - 

    * - :func:`retrieve`
      - .. image:: _static/MCONT.png 
           :width: 16px
      - 

    * - :func:`vapor_prepare`
      - .. image:: _static/MCONT.png 
           :width: 16px
      - 

    * - :func:`wmsclient`
      - .. image:: _static/MCONT.png 
           :width: 16px
      - 


Data conversion
-------------------------------

.. list-table::
    :widths: 20 10 70
    :header-rows: 0


    * - :func:`geo_to_grib`
      - .. image:: _static/MCONT.png 
           :width: 16px
      - 

    * - :func:`geo_to_kml`
      - .. image:: _static/MCONT.png 
           :width: 16px
      - 

    * - :func:`grib_to_geo`
      - .. image:: _static/MCONT.png 
           :width: 16px
      - 


Grib data
-------------------------------

.. list-table::
    :widths: 20 10 70
    :header-rows: 0


    * - :func:`base_date`
      - .. image:: _static/MCONT.png 
           :width: 16px
      - Returns the base date(s) of a given fieldset

    * - :func:`datainfo`
      - .. image:: _static/MCONT.png 
           :width: 16px
      - Returns information on missing values in fieldsets

    * - :func:`duplicate`
      - .. image:: _static/MCONT.png 
           :width: 16px
      - Duplicates a field N times

    * - :func:`gfind`
      - .. image:: _static/MCONT.png 
           :width: 16px
      - Finds values in field and returns the result as geopoints

    * - :func:`grib_get`
      - .. image:: _static/MCONT.png 
           :width: 16px
      - Reads GRIB headers using ecCodes keys

    * - :func:`grib_get_double`
      - .. image:: _static/MCONT.png 
           :width: 16px
      - Reads GRIB headers using ecCodes keys

    * - :func:`grib_get_double_array`
      - .. image:: _static/MCONT.png 
           :width: 16px
      - Reads GRIB headers using ecCodes keys

    * - :func:`grib_get_long`
      - .. image:: _static/MCONT.png 
           :width: 16px
      - Reads GRIB headers using ecCodes keys

    * - :func:`grib_get_long_array`
      - .. image:: _static/MCONT.png 
           :width: 16px
      - Reads GRIB headers using ecCodes keys

    * - :func:`grib_get_string`
      - .. image:: _static/MCONT.png 
           :width: 16px
      - Reads GRIB headers using ecCodes keys

    * - :func:`grib_set`
      - .. image:: _static/MCONT.png 
           :width: 16px
      - Writes GRIB headers using ecCodes keys

    * - :func:`grib_set_double`
      - .. image:: _static/MCONT.png 
           :width: 16px
      - Writes GRIB headers using ecCodes keys

    * - :func:`grib_set_long`
      - .. image:: _static/MCONT.png 
           :width: 16px
      - Writes GRIB headers using ecCodes keys

    * - :func:`grib_set_string`
      - .. image:: _static/MCONT.png 
           :width: 16px
      - Writes GRIB headers using ecCodes keys

    * - :func:`gribsetbits`
      - .. image:: _static/MCONT.png 
           :width: 16px
      - Sets GRIB packing bit width


Geopoints data
-------------------------------

.. list-table::
    :widths: 20 10 70
    :header-rows: 0


    * - :func:`columns`
      - .. image:: _static/MCONT.png 
           :width: 16px
      - Returns the list of columns from the given ODB.

    * - :func:`db_info`
      - .. image:: _static/MCONT.png 
           :width: 16px
      - Returns a string of the database from the given geopoints.


NetCDF data
-------------------------------

.. list-table::
    :widths: 20 10 70
    :header-rows: 0


    * - :func:`attributes`
      - .. image:: _static/MCONT.png 
           :width: 16px
      - Returns the attributes of the current NetCDF variable

    * - :func:`dimension_names`
      - .. image:: _static/MCONT.png 
           :width: 16px
      - Returns a list of the netcdf's dimension names.

    * - :func:`dimensions`
      - .. image:: _static/MCONT.png 
           :width: 16px
      - Returns a list of the netcdf's dimensions.

    * - :func:`global_attributes`
      - .. image:: _static/MCONT.png 
           :width: 16px
      - Returns a definition variable holding the netcdf's global metadata.

    * - :func:`netcdf_auto_rescale_values_to_fit_packed_type`
      - .. image:: _static/MCONT.png 
           :width: 16px
      - Sets the behaviour of netcdf value handling: 1=on, 0=off

    * - :func:`netcdf_auto_scale_values`
      - .. image:: _static/MCONT.png 
           :width: 16px
      - Sets the behaviour of netcdf value handling: 1=on, 0=off

    * - :func:`netcdf_auto_translate_times`
      - .. image:: _static/MCONT.png 
           :width: 16px
      - Sets the behaviour of netcdf value handling: 1=on, 0=off

    * - :func:`netcdf_preserve_missing_values`
      - .. image:: _static/MCONT.png 
           :width: 16px
      - Sets the behaviour of netcdf value handling: 1=on, 0=off
