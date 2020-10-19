
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
      - Returns the base date(s) of a given :class:`Fieldset`

    * - :func:`datainfo`
      - Returns information on missing values in :class:`Fieldset`

    * - :func:`duplicate`
      - Duplicates a field N times

    * - :func:`fill_missing_values_ew`
      - Fills missing values along the horizontal line

    * - :func:`find`
      - Find where a number occurs in a vector

    * - :func:`float`
      - Converts int GRIB to float GRIB

    * - :func:`gfind`
      - Finds values in field and returns the result as :class:`Geopoints`

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

    * - :func:`indexes`
      - Builds an output :class:`Fieldset` containing each gridpoint's indexed position in the given vector

    * - :func:`int`
      - Integer part

    * - :func:`integer`
      - Converts float GRIB to int GRIB

    * - :func:`lookup`
      - Builds an output :class:`Fieldset` using the values in the first as indices into the second

    * - :func:`set_values`
      - Sets the value column in the :class:`Geopoints` variable.

    * - :func:`sort`
      - Sorts a vector according to an operator '<' (default) or '>'

    * - :func:`values`
      - Returns a list of values from the given ODB column.


Geopoints data
-------------------------------

.. list-table::
    :widths: 20 80
    :header-rows: 0


    * - :func:`columns`
      - Returns the list of columns from the given ODB.

    * - :func:`create_geo`
      - Creates a new set of :class:`Geopoints`

    * - :func:`create_geo_set`
      - Creates a new :class:`Geopoints` set

    * - :func:`dates`
      - Returns a list/vector of dates from the given :class:`Geopoints`.

    * - :func:`db_info`
      - Returns a string of the database from the given :class:`Geopoints`.

    * - :func:`levels`
      - Returns a list/vector of heights from the given :class:`Geopoints`.

    * - :func:`metadata`
      - Returns a metadata definition from the given :class:`Geopoints`.

    * - :func:`polar_vector`
      - Combines two 1-parameter :class:`Geopoints` variables into polar vector style

    * - :func:`remove_duplicates`
      - Removes geopoint duplicates

    * - :func:`set_dates`
      - Sets the date column in the :class:`Geopoints` variable.

    * - :func:`set_latitudes`
      - Sets the latitude column in the :class:`Geopoints` variable.

    * - :func:`set_levels`
      - Sets the level column in the :class:`Geopoints` variable.

    * - :func:`set_longitudes`
      - Sets the longitude column in the :class:`Geopoints` variable.

    * - :func:`set_metadata`
      - Sets a :class:`Geopoints` metadata from a definition

    * - :func:`set_stnids`
      - Sets the stnid column in the :class:`Geopoints` variable.

    * - :func:`set_times`
      - Sets the time column in the :class:`Geopoints` variable.

    * - :func:`set_value2s`
      - Sets the value2 column in the :class:`Geopoints` variable.

    * - :func:`set_values`
      - Sets the value column in the :class:`Geopoints` variable.

    * - :func:`stnids`
      - Returns a list/vector of station ids from the given :class:`Geopoints`.

    * - :func:`subsample`
      - Filters from the first :class:`Geopoints` variable points that exist in the second

    * - :func:`times`
      - Returns a list/vector of times from the given :class:`Geopoints`.

    * - :func:`value2s`
      - Returns a list/vector of 2nd values from the given :class:`Geopoints`.

    * - :func:`values`
      - Returns a list of values from the given ODB column.

    * - :func:`xy_vector`
      - Combines two 1-parameter :class:`Geopoints` variables into u/v vector style


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

    * - :func:`setcurrent`
      - Sets the variable number on which netcdf functions will operate.

    * - :func:`value`
      - Returns the n:th value from the current netcdf variable.

    * - :func:`value_columns`
      - Returns a list of column names for a :class:`Geopoints` variable

    * - :func:`values`
      - Returns a list of values from the given ODB column.

    * - :func:`variables`
      - Returns a list of the names of the given netcdf file's variables.


Flextra and Flexpart
-------------------------------

.. list-table::
    :widths: 20 80
    :header-rows: 0


    * - :func:`flexpart_build_title`
      - Generates title for plotting FLEXPART gridded output fields

    * - :func:`flexpart_convert_trajectory`
      - Converts raw FLEXPART trajectory output to CSV

    * - :func:`flexpart_filter`
      - Extract fields from FLEXPART output GRIB files

    * - :func:`flexpart_prepare`
      - 

    * - :func:`flexpart_release`
      - 

    * - :func:`flexpart_run`
      - 

    * - :func:`flexpart_total_column`
      - Computes the sum/vertical integral of fields in a FLEXPART output GRIB file.

    * - :func:`flextra_group_get`
      - Returns a list of available meta data keys for the given table

    * - :func:`flextra_run`
      - 

    * - :func:`flextra_tr_get`
      - Returns a list of available meta data keys for the given table

    * - :func:`flextra_visualiser`
      - 


Table data
-------------------------------

.. list-table::
    :widths: 20 80
    :header-rows: 0


    * - :func:`metadata_keys`
      - Returns a list of available meta data keys for the given table

    * - :func:`metadata_value`
      - Returns the value of then given meta data key for a table

    * - :func:`name`
      - Returns the name of the given table column.

    * - :func:`read_table`
      - Reads a table file with parameters for parsing it.

    * - :func:`values`
      - Returns a list of values from the given ODB column.


Single Column Model
-------------------------------

.. list-table::
    :widths: 20 80
    :header-rows: 0


    * - :func:`scm_run`
      - 

    * - :func:`scm_visualiser`
      - 


RTTOV
-------------------------------

.. list-table::
    :widths: 20 80
    :header-rows: 0


    * - :func:`rttov_run`
      - 

    * - :func:`rttov_visualiser`
      - 
