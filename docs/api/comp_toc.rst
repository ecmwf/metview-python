
Computation functions
===========================



Basic mathematics
-------------------------------

.. list-table::
    :widths: 20 80
    :header-rows: 0


    * - :func:`abs`
      - Compute the absolute value

    * - :func:`acos`
      - Arc cosine

    * - :func:`asin`
      - Arc sine

    * - :func:`atan`
      - Arc tangent

    * - :func:`atan2`
      - Arc tangent of 2 variables

    * - :func:`cos`
      - Cosine

    * - :func:`exp`
      - Exponential

    * - :func:`intbits`
      - Returns ranges of bits in a geopoints variable

    * - :func:`log`
      - Natural logarithm

    * - :func:`log10`
      - Base 10 logarithm

    * - :func:`sgn`
      - Signum

    * - :func:`sin`
      - Sine

    * - :func:`sqrt`
      - Square root

    * - :func:`tan`
      - Tangent


Calculus
-------------------------------

.. list-table::
    :widths: 20 80
    :header-rows: 0


    * - :func:`divergence`
      - Compute horizontal divergence of vector fields

    * - :func:`divrot`
      - 

    * - :func:`divwind`
      - 

    * - :func:`first_derivative_x`
      - Computes first West-East derivative of fields

    * - :func:`first_derivative_y`
      - Computes first South-North derivative of fields

    * - :func:`gradient`
      - Computes horizontal gradient of fields

    * - :func:`integral`
      - Computes surface integral for fields

    * - :func:`laplacian`
      - Computes horizontal Laplacian of fields

    * - :func:`second_derivative_x`
      - Computes second West-East derivative of fields

    * - :func:`second_derivative_y`
      - Computes second South-North derivative of fields

    * - :func:`vorticity`
      - Compute relative vorticity of vector fields


Statistics
-------------------------------

.. list-table::
    :widths: 20 80
    :header-rows: 0


    * - :func:`accumulate`
      - Adds up the values in a given field

    * - :func:`average`
      - Averages the values in a given field

    * - :func:`average_ew`
      - Returns the zonal averages as a list (or list of lists) of numbers.

    * - :func:`average_ns`
      - Returns the meridional averages as a list (or list of lists) of numbers.

    * - :func:`corr_a`
      - Computes the area-weighted correlation for each field in a fieldset

    * - :func:`covar`
      - Returns the covariance of all two fieldsets

    * - :func:`covar_a`
      - Computes the area-weighted covariance for each field in a fieldset

    * - :func:`frequencies`
      - Computes frequencies of a field

    * - :func:`integrate`
      - Computes the average weighted by the gridcell area for each field in fieldset

    * - :func:`mean`
      - Returns the sum or mean of the values in a geopoints variable

    * - :func:`mean_ew`
      - Generates a fieldset out of East-West means

    * - :func:`percentile`
      - Returns a set of percentiles of a vector

    * - :func:`rms`
      - Returns the root mean square of all the fields of a variable

    * - :func:`stdev`
      - Returns the standard deviation of all the fields of a variable

    * - :func:`stdev_a`
      - Computes the area-weighted standard deviation for each field in a fieldset

    * - :func:`sum`
      - Returns the sum or mean of the values in a geopoints variable

    * - :func:`var`
      - Returns the variance of all the fields of a variable

    * - :func:`var_a`
      - Computes the area-weighted variance for each field in a fieldset


Thermodynamics
-------------------------------

.. list-table::
    :widths: 20 80
    :header-rows: 0


    * - :func:`dewpoint_from_relative_humidity`
      - Computes the dewpoint for a given temperature and relative humidity

    * - :func:`dewpoint_from_specific_humidity`
      - Computes the dewpoint for a given specific humidity and pressure

    * - :func:`eqpott_m`
      - 

    * - :func:`eqpott_p`
      - 

    * - :func:`lifted_condensation_level`
      - Computes the Lifted Condensation Level (LCL) using the parcel method

    * - :func:`mixing_ratio`
      - Computes the mixing ratio from specific humidity

    * - :func:`potential_temperature`
      - computes the potential temperature for a given temperature and pressure

    * - :func:`pott_m`
      - 

    * - :func:`pott_p`
      - 

    * - :func:`relative_humidity_from_dewpoint`
      - Computes the relative humidity for a given temperature and dewpoint

    * - :func:`saturation_mixing_ratio`
      - Computes the saturation mixing ratio for a given temperature and pressure

    * - :func:`saturation_vapour_pressure`
      - Computes the saturation vapour pressure for a given temperature

    * - :func:`seqpott_m`
      - 

    * - :func:`seqpott_p`
      - 

    * - :func:`temperature_from_potential_temperature`
      - Computes the temperature from potential tempearture and pressure

    * - :func:`thermo_bufr`
      - 

    * - :func:`thermo_data_values`
      - extracts data and metadata from a thermo data object

    * - :func:`thermo_grib`
      - 

    * - :func:`thermo_parcel_area`
      - returns a set of coloured areas from a thermo parcel path

    * - :func:`thermo_parcel_path`
      - computes the path of an ascending thermodynamic parcel

    * - :func:`vapour_pressure`
      - Computes the vapour pressure for a given specific humidity and pressure


Geographic
-------------------------------

.. list-table::
    :widths: 20 80
    :header-rows: 0


    * - :func:`bearing`
      - Computes the bearings for all the gridpoints with respect to a reference point

    * - :func:`coslat`
      - Generates a field with the cosine of the gridpoint latitudes

    * - :func:`direction`
      - Computes meteorological wind direction using U and V wind components

    * - :func:`distance`
      - Computes the distances of all the gridpoints from a point

    * - :func:`geosort`
      - Sorts the geopoints North to South and West to East

    * - :func:`grid_cell_area`
      - Computes grid cell area for each gridpoints in a field

    * - :func:`latitudes`
      - Returns a list/vector of latitudes from the given geopoints.

    * - :func:`longitudes`
      - Returns a list/vector of longitudes from the given geopoints.

    * - :func:`nearest_gridpoint`
      - Returns the nearest grid point value from a field

    * - :func:`nearest_gridpoint_info`
      - Returns the nearest grid point value from a field

    * - :func:`offset`
      - Offsets the locations of geopoints

    * - :func:`sinlat`
      - Generates a field with the sine of the gridpoint latitudes

    * - :func:`tanlat`
      - Generates a field with the tangent of the gridpoint latitudes


Filtering
-------------------------------

.. list-table::
    :widths: 20 80
    :header-rows: 0


    * - :func:`bitmap`
      - Converts numbers to missing values in a vector

    * - :func:`bufr_picker`
      - 

    * - :func:`cleanfile`
      - 

    * - :func:`filter`
      - Filters a vector according to the values of a second vector

    * - :func:`nobitmap`
      - Converts missing values to numbers in a vector

    * - :func:`obsfilter`
      - 

    * - :func:`odb_filter`
      - 

    * - :func:`read`
      - 

    * - :func:`rmask`
      - Generates masks based on a radius around a point for fieldsets


Grid
-------------------------------

.. list-table::
    :widths: 20 80
    :header-rows: 0


    * - :func:`interpolate`
      - Interpolates field values to the specified location

    * - :func:`surrounding_points_indexes`
      - Returns the indexes of the four surrounding grid points


Vertical
-------------------------------

.. list-table::
    :widths: 20 80
    :header-rows: 0


    * - :func:`cross_sect`
      - 

    * - :func:`geostrophic_wind`
      - Computes geostrophic wind on pressure levels

    * - :func:`ml_to_hl`
      - Interpolates model level fields to height levels

    * - :func:`mvl_geopotential_on_ml`
      - Computes geopotential on model levels

    * - :func:`mvl_ml2hPa`
      - Interpolates a fieldset on model levels to pressure levels (in hPa)

    * - :func:`pressure`
      - Creates fields of pressure or thickness (input in lat/lon only).

    * - :func:`thickness`
      - Creates fields of pressure or thickness (input in lat/lon only).

    * - :func:`unipressure`
      - Creates fields of pressure or thickness (accepts several grid types)

    * - :func:`unithickness`
      - Creates fields of pressure or thickness (accepts several grid types)

    * - :func:`univertint`
      - Universal vertical integration, also for sparse vertical data

    * - :func:`vert_prof`
      - 

    * - :func:`vertint`
      - Performs vertical integration

    * - :func:`w_from_omega`
      - Computes the vertical velocity in m/s from pressure velocity
