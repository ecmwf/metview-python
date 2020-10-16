
Data access
===========================



Data retrieval
-------------------------------

.. list-table::
    :widths: 20 80
    :header-rows: 0


    * - :func:`ecfs`
      - 

    * - :func:`flexpart_prepare`
      - 

    * - :func:`flextra_prepare`
      - 

    * - :func:`met3d_prepare`
      - 

    * - :func:`retrieve`
      - 

    * - :func:`vapor_prepare`
      - 

    * - :func:`wmsclient`
      - 


Data conversion
-------------------------------

.. list-table::
    :widths: 20 80
    :header-rows: 0


    * - :func:`geo_to_grib`
      - 

    * - :func:`geo_to_kml`
      - 

    * - :func:`grib_to_geo`
      - 


Grib data
-------------------------------

.. list-table::
    :widths: 20 80
    :header-rows: 0


    * - :func:`base_date`
      - Returns the base date(s) of a given fieldset

    * - :func:`datainfo`
      - Returns information on missing values in fieldsets

    * - :func:`duplicate`
      - Duplicates a field N times

    * - :func:`gfind`
      - Finds values in field and returns the result as geopoints

    * - :func:`grib_get`
      - Reads GRIB headers using ecCodes keys

    * - :func:`grib_get_double`
      - Reads GRIB headers using ecCodes keys

    * - :func:`grib_get_double_array`
      - Reads GRIB headers using ecCodes keys

    * - :func:`grib_get_long`
      - Reads GRIB headers using ecCodes keys

    * - :func:`grib_get_long_array`
      - Reads GRIB headers using ecCodes keys

    * - :func:`grib_get_string`
      - Reads GRIB headers using ecCodes keys

    * - :func:`grib_set`
      - Writes GRIB headers using ecCodes keys

    * - :func:`grib_set_double`
      - Writes GRIB headers using ecCodes keys

    * - :func:`grib_set_long`
      - Writes GRIB headers using ecCodes keys

    * - :func:`grib_set_string`
      - Writes GRIB headers using ecCodes keys

    * - :func:`gribsetbits`
      - Sets GRIB packing bit width


Geopoints data
-------------------------------

.. list-table::
    :widths: 20 80
    :header-rows: 0


    * - :func:`columns`
      - Returns the list of columns from the given ODB.

    * - :func:`db_info`
      - Returns a string of the database from the given geopoints.


NetCDF data
-------------------------------

.. list-table::
    :widths: 20 80
    :header-rows: 0


    * - :func:`attributes`
      - Returns the attributes of the current NetCDF variable

    * - :func:`dimension_names`
      - Returns a list of the netcdf's dimension names.

    * - :func:`dimensions`
      - Returns a list of the netcdf's dimensions.

    * - :func:`global_attributes`
      - Returns a definition variable holding the netcdf's global metadata.

    * - :func:`netcdf_auto_rescale_values_to_fit_packed_type`
      - Sets the behaviour of netcdf value handling: 1=on, 0=off

    * - :func:`netcdf_auto_scale_values`
      - Sets the behaviour of netcdf value handling: 1=on, 0=off

    * - :func:`netcdf_auto_translate_times`
      - Sets the behaviour of netcdf value handling: 1=on, 0=off

    * - :func:`netcdf_preserve_missing_values`
      - Sets the behaviour of netcdf value handling: 1=on, 0=off
