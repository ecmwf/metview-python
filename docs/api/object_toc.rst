
Object functions
==================



Grib methods
--------------


.. list-table::
    :widths: 20 80
    :header-rows: 0


    * - :func:`abs`
      - Computes the absolute value

    * - :func:`accumulate`
      - Adds up the values per field in a :class:`Fieldset`

    * - :func:`acos`
      - Computes the arc cosine

    * - :func:`asin`
      - Computes the arc sine

    * - :func:`atan`
      - Computes the arc tangent

    * - :func:`atan2`
      - Computes the arc tangent of 2 :class:`Fieldset` objects

    * - :func:`average`
      - Computes the average per field in a :class:`Fieldset`

    * - :func:`average_ew`
      - Computes the zonal averages for each field in a :class:`Fieldset`

    * - :func:`average_ns`
      - Computes the meridional averages for each field in a :class:`Fieldset`

    * - :func:`base_date`
      - Returns the base date(s) of a given :class:`Fieldset`

    * - :func:`bearing`
      - Computes the bearings with respect to a reference in a :class:`Fieldset` point

    * - :func:`bitmap`
      - Converts numbers to missing values in a :class:`Fieldset`

    * - :func:`corr_a`
      - Computes the area-weighted correlation for each field in a :class:`Fieldset`

    * - :func:`cos`
      - Computes the cosine

    * - :func:`coslat`
      - Generates a field with the cosine of the latitudes in a :class:`Fieldset`

    * - :func:`covar`
      - Returns the covariance of two :class:`Fieldset` objects

    * - :func:`covar_a`
      - Computes the area-weighted covariance for each field in a :class:`Fieldset`

    * - :func:`datainfo`
      - Returns information on missing values in a :class:`Fieldset`

    * - :func:`dataset_to_fieldset`
      - Convert xndarray dataset to :class:`Fieldset`

    * - :func:`direction`
      - Computes the wind direction

    * - :func:`distance`
      - Computes the distances in a :class:`Fieldset` or :class:`Geopoints` to a reference point

    * - :func:`div`
      - Computes the integer part of a divison

    * - :func:`divergence`
      - Computes the horizontal divergence of a vector :class:`Fieldset`

    * - :func:`exp`
      - Computes the exponential

    * - :func:`fill_missing_values_ew`
      - Fills missing values along the horizontal line

    * - :func:`find`
      - Find locations of values in a :class:`Fieldset`

    * - :func:`first_derivative_x`
      - Computes first West-East derivative of a :class:`Fieldset`

    * - :func:`first_derivative_y`
      - Computes first South-North derivative of a :class:`Fieldset`

    * - :func:`float`
      - Converts int GRIB to float GRIB

    * - :func:`frequencies`
      - Computes the frequencies of a :class:`Fieldset`

    * - :func:`geostrophic_wind`
      - Computes geostrophic wind on pressure levels in a :class:`Fieldset`

    * - :func:`gfind`
      - Finds values in field and returns the result as :class:`Geopoints`

    * - :func:`gradient`
      - Computes horizontal gradient of a :class:`Fieldset`

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

    * - :func:`grid_cell_area`
      - Computes the grid cell area in a :class:`Fieldset`

    * - :func:`indexes`
      - Builds a :class:`Fieldset` containing each gridpoint's indexed position in the given vector

    * - :func:`int`
      - Integer part

    * - :func:`integer`
      - Converts float GRIB to int GRIB

    * - :func:`integral`
      - Computes the surface integral of a :class:`Fieldset`

    * - :func:`integrate`
      - Computes the average weighted by the gridcell area for each field in :class:`Fieldset`

    * - :func:`interpolate`
      - Interpolates :class:`Fieldset` values to the specified location

    * - :func:`laplacian`
      - Computes the horizontal Laplacian of :class:`Fieldset`

    * - :func:`latitudes`
      - Returns the latitudes of a :class:`Fieldset` or :class:`Geopoints`

    * - :func:`log`
      - Computes the natural logarithm

    * - :func:`log10`
      - Computes the base 10 logarithm

    * - :func:`longitudes`
      - Returns the longitudes from a :class:`Fieldset` or :class:`Geopoints`

    * - :func:`lookup`
      - Builds an output :class:`Fieldset` using the values in the first as indices into the second

    * - :func:`mask`
      - Generates masks for a :class:`Fieldset` or :class:`Geopoints`

    * - :func:`max`
      - Maximum

    * - :func:`maxvalue`
      - Maximum value of a :class:`Fieldset`

    * - :func:`mean`
      - Returns the mean of the values in a :class:`Fieldset` or :class:`Geopoints`

    * - :func:`mean_ew`
      - Generates a :class:`Fieldset` out of East-West means

    * - :func:`merge`
      - Merges 2 sets of :class:`Fieldset` or :class:`Geopoints`

    * - :func:`min`
      - Minimum

    * - :func:`minvalue`
      - Minimum value of a :class:`Fieldset` or :class:`Geopoints`

    * - :func:`ml_to_hl`
      - Interpolates a model level :class:`Fieldset` to height levels

    * - :func:`mod`
      - Computes the integer remainder of a divison

    * - :func:`mvl_geopotential_on_ml`
      - Computes the geopotential on model levels for a :class:`Fieldset`

    * - :func:`mvl_ml2hPa`
      - Interpolates a :class:`Fieldset` on model levels to pressure levels (in hPa)

    * - :func:`nearest_gridpoint`
      - Returns the nearest grid point value from a :class:`Fieldset`

    * - :func:`nearest_gridpoint_info`
      - Returns the nearest grid point value from a :class:`Fieldset`

    * - :func:`nobitmap`
      - Converts missing values to numbers in a :class:`Fieldset`

    * - :func:`pressure`
      - Computes the pressure on model levels in a :class:`Fieldset` (deprecated)

    * - :func:`rmask`
      - Generates masks based on a radius around a point for :class:`Fieldset`

    * - :func:`rms`
      - Returns the root mean square of all the fields in a :class:`Fieldset`

    * - :func:`second_derivative_x`
      - Computes the second West-East derivative of a :class:`Fieldset`

    * - :func:`second_derivative_y`
      - Computes the econd South-North derivative of a :class:`Fieldset`

    * - :func:`set_latitudes`
      - Sets the latitudes in a :class:`Fieldset` or :class:`Geopoints`

    * - :func:`set_longitudes`
      - Sets the longitudes in a :class:`Fieldset` or :class:`Geopoints`

    * - :func:`set_values`
      - Sets the values in a :class:`Fieldset` or :class:`Geopoints`

    * - :func:`sgn`
      - Computes the sign

    * - :func:`sin`
      - Computes the sine

    * - :func:`sinlat`
      - Generates a field with the cosine of the latitudes in a :class:`Fieldset`

    * - :func:`sort`
      - Sorts a vector according to an operator '<' (default) or '>'

    * - :func:`sqrt`
      - Computes the square root

    * - :func:`stdev`
      - Returns the standard deviation of all the fields in a :class:`Fieldset`

    * - :func:`stdev_a`
      - Computes the area-weighted standard deviation for each field in a :class:`Fieldset`

    * - :func:`sum`
      - Returns the sum of the values in a :class:`Fieldset` or :class:`Geopoints`

    * - :func:`surrounding_points_indexes`
      - Returns the indexes of the four surrounding grid points in a :class:`Fieldset`

    * - :func:`tan`
      - Computes the tangent

    * - :func:`tanlat`
      - Generates a field with the tangent of the latitudes in a :class:`Fieldset`

    * - :func:`thickness`
      - Computes the pressure thickness on model levels in a :class:`Fieldset` (deprecated)

    * - :func:`to_dataset`
      - Convert :class:`Fieldset` to xndarray dataset

    * - :func:`unipressure`
      - Computes the pressure on model levels in a :class:`Fieldset`

    * - :func:`unithickness`
      - Computes the pressure thickness of model levels in a :class:`Fieldset`

    * - :func:`univertint`
      - Performs a vertical integration for a :class:`Fieldset`

    * - :func:`valid_date`
      - Returns the valid date(s) of a given :class:`Fieldset`

    * - :func:`values`
      - Returns the values from a data object

    * - :func:`var`
      - Returns the variance of all the fields in a :class:`Fieldset`

    * - :func:`var_a`
      - Computes the area-weighted variance for each field in a :class:`Fieldset`

    * - :func:`vertint`
      - Performs a vertical integration for a :class:`Fieldset` (deprecated)

    * - :func:`vorticity`
      - Computes the relative vorticity of a vector :class:`Fieldset`


Geopoints methods
-------------------


.. list-table::
    :widths: 20 80
    :header-rows: 0


    * - :func:`abs`
      - Computes the absolute value

    * - :func:`accumulate`
      - Adds up the values per field in a :class:`Fieldset`

    * - :func:`acos`
      - Computes the arc cosine

    * - :func:`asin`
      - Computes the arc sine

    * - :func:`atan`
      - Computes the arc tangent

    * - :func:`columns`
      - Returns the list of column name from a :class:`Geopoints` or :class:`Odb`

    * - :func:`cos`
      - Computes the cosine

    * - :func:`db_info`
      - Returns a string of the database from the given :class:`Geopoints`.

    * - :func:`distance`
      - Computes the distances in a :class:`Fieldset` or :class:`Geopoints` to a reference point

    * - :func:`div`
      - Computes the integer part of a divison

    * - :func:`exp`
      - Computes the exponential

    * - :func:`geosort`
      - Sorts the :class:`Geopoints` North to South and West to East

    * - :func:`intbits`
      - Returns ranges of bits

    * - :func:`latitudes`
      - Returns the latitudes of a :class:`Fieldset` or :class:`Geopoints`

    * - :func:`levels`
      - Returns a list/vector of heights from the given :class:`Geopoints`.

    * - :func:`log`
      - Computes the natural logarithm

    * - :func:`log10`
      - Computes the base 10 logarithm

    * - :func:`longitudes`
      - Returns the longitudes from a :class:`Fieldset` or :class:`Geopoints`

    * - :func:`mask`
      - Generates masks for a :class:`Fieldset` or :class:`Geopoints`

    * - :func:`max`
      - Maximum

    * - :func:`mean`
      - Returns the mean of the values in a :class:`Fieldset` or :class:`Geopoints`

    * - :func:`merge`
      - Merges 2 sets of :class:`Fieldset` or :class:`Geopoints`

    * - :func:`metadata`
      - Returns a metadata definition from the given :class:`Geopoints`.

    * - :func:`min`
      - Minimum

    * - :func:`mod`
      - Computes the integer remainder of a divison

    * - :func:`offset`
      - Offsets the locations of :class:`Geopoints`

    * - :func:`polar_vector`
      - Combines two 1-parameter :class:`Geopoints` variables into polar vector style

    * - :func:`set_dates`
      - Sets the date column in the :class:`Geopoints` variable.

    * - :func:`set_latitudes`
      - Sets the latitudes in a :class:`Fieldset` or :class:`Geopoints`

    * - :func:`set_levels`
      - Sets the level column in a :class:`Geopoints`

    * - :func:`set_longitudes`
      - Sets the longitudes in a :class:`Fieldset` or :class:`Geopoints`

    * - :func:`set_metadata`
      - Sets a :class:`Geopoints` metadata from a definition

    * - :func:`set_stnids`
      - Sets the stnid column in a :class:`Geopoints`

    * - :func:`set_times`
      - Sets the time column in a :class:`Geopoints`

    * - :func:`set_value2s`
      - Sets the value2 column a :class:`Geopoints`

    * - :func:`set_values`
      - Sets the values in a :class:`Fieldset` or :class:`Geopoints`

    * - :func:`sgn`
      - Computes the sign

    * - :func:`sin`
      - Computes the sine

    * - :func:`sqrt`
      - Computes the square root

    * - :func:`stnids`
      - Returns thestation ids from a :class:`Geopoints`

    * - :func:`subsample`
      - Filters from the first :class:`Geopoints` variable points that exist in the second

    * - :func:`sum`
      - Returns the sum of the values in a :class:`Fieldset` or :class:`Geopoints`

    * - :func:`tan`
      - Computes the tangent

    * - :func:`times`
      - Returns the times from a :class:`Geopoints`

    * - :func:`to_dataframe`
      - Convert :class:`Geopoints` to Pandas dataframe

    * - :func:`value2s`
      - Returns the 2nd values column from a :class:`Geopoints`

    * - :func:`value_columns`
      - Returns a list of value column names for a :class:`Geopoints`

    * - :func:`values`
      - Returns the values from a data object

    * - :func:`xy_vector`
      - Combines two 1-parameter :class:`Geopoints` variables into u/v vector style


NetCDF methods
----------------


.. list-table::
    :widths: 20 80
    :header-rows: 0


    * - :func:`dimension_names`
      - Returns a list of the :class:`NetCdf`'s dimension names.

    * - :func:`dimensions`
      - Returns a list of the :class:`NetCdf`'s dimensions.

    * - :func:`global_attributes`
      - Returns a definition variable holding the :class:`NetCdf` global metadata.

    * - :func:`max`
      - Maximum

    * - :func:`min`
      - Minimum

    * - :func:`netcdf_auto_rescale_values_to_fit_packed_type`
      - Sets the behaviour of :class:`NetCdf` value handling: 1=on, 0=off

    * - :func:`netcdf_auto_scale_values`
      - Sets the behaviour of :class:`NetCdf` value handling: 1=on, 0=off

    * - :func:`netcdf_auto_translate_times`
      - Sets the behaviour of :class:`NetCdf` value handling: 1=on, 0=off

    * - :func:`netcdf_preserve_missing_values`
      - Sets the behaviour of :class:`NetCdf` value handling: 1=on, 0=off

    * - :func:`setcurrent`
      - Sets the variable number on which :class:`NetCdf` functions will operate.

    * - :func:`value`
      - Returns the n:th value from the current :class:`NetCdf` variable.

    * - :func:`values`
      - Returns the values from a data object

    * - :func:`variables`
      - Returns a list of the names of the given :class:`NetCdf` file's variables.
