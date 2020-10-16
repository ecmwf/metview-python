
Computation functions
===========================



Basic mathematics
-------------------------------

.. list-table::
    :widths: 20 10 70
    :header-rows: 0


    * - :func:`abs`
      - .. image:: _static/MCONT.png 
           :width: 16px
      - Compute the absolute value

    * - :func:`acos`
      - .. image:: _static/MCONT.png 
           :width: 16px
      - Arc cosine

    * - :func:`asin`
      - .. image:: _static/MCONT.png 
           :width: 16px
      - Arc sine

    * - :func:`atan`
      - .. image:: _static/MCONT.png 
           :width: 16px
      - Arc tangent

    * - :func:`atan2`
      - .. image:: _static/MCONT.png 
           :width: 16px
      - Arc tangent of 2 variables

    * - :func:`cos`
      - .. image:: _static/MCONT.png 
           :width: 16px
      - Cosine

    * - :func:`exp`
      - .. image:: _static/MCONT.png 
           :width: 16px
      - Exponential

    * - :func:`intbits`
      - .. image:: _static/MCONT.png 
           :width: 16px
      - Returns ranges of bits in a geopoints variable

    * - :func:`log`
      - .. image:: _static/MCONT.png 
           :width: 16px
      - Natural logarithm

    * - :func:`log10`
      - .. image:: _static/MCONT.png 
           :width: 16px
      - Base 10 logarithm

    * - :func:`sgn`
      - .. image:: _static/MCONT.png 
           :width: 16px
      - Signum

    * - :func:`sin`
      - .. image:: _static/MCONT.png 
           :width: 16px
      - Sine

    * - :func:`sqrt`
      - .. image:: _static/MCONT.png 
           :width: 16px
      - Square root

    * - :func:`tan`
      - .. image:: _static/MCONT.png 
           :width: 16px
      - Tangent


Calculus
-------------------------------

.. list-table::
    :widths: 20 10 70
    :header-rows: 0


    * - :func:`divergence`
      - .. image:: _static/MCONT.png 
           :width: 16px
      - Compute horizontal divergence of vector fields

    * - :func:`divrot`
      - .. image:: _static/MCONT.png 
           :width: 16px
      - 

    * - :func:`divwind`
      - .. image:: _static/MCONT.png 
           :width: 16px
      - 

    * - :func:`first_derivative_x`
      - .. image:: _static/MCONT.png 
           :width: 16px
      - Computes first West-East derivative of fields

    * - :func:`first_derivative_y`
      - .. image:: _static/MCONT.png 
           :width: 16px
      - Computes first South-North derivative of fields

    * - :func:`gradient`
      - .. image:: _static/MCONT.png 
           :width: 16px
      - Computes horizontal gradient of fields

    * - :func:`integral`
      - .. image:: _static/MCONT.png 
           :width: 16px
      - Computes surface integral for fields

    * - :func:`laplacian`
      - .. image:: _static/MCONT.png 
           :width: 16px
      - Computes horizontal Laplacian of fields

    * - :func:`second_derivative_x`
      - .. image:: _static/MCONT.png 
           :width: 16px
      - Computes second West-East derivative of fields

    * - :func:`second_derivative_y`
      - .. image:: _static/MCONT.png 
           :width: 16px
      - Computes second South-North derivative of fields

    * - :func:`vorticity`
      - .. image:: _static/MCONT.png 
           :width: 16px
      - Compute relative vorticity of vector fields


Statistics
-------------------------------

.. list-table::
    :widths: 20 10 70
    :header-rows: 0


    * - :func:`accumulate`
      - .. image:: _static/MCONT.png 
           :width: 16px
      - Adds up the values in a given field

    * - :func:`average`
      - .. image:: _static/MCONT.png 
           :width: 16px
      - Averages the values in a given field

    * - :func:`average_ew`
      - .. image:: _static/MCONT.png 
           :width: 16px
      - Returns the zonal averages as a list (or list of lists) of numbers.

    * - :func:`average_ns`
      - .. image:: _static/MCONT.png 
           :width: 16px
      - Returns the meridional averages as a list (or list of lists) of numbers.

    * - :func:`corr_a`
      - .. image:: _static/MCONT.png 
           :width: 16px
      - Computes the area-weighted correlation for each field in a fieldset

    * - :func:`covar`
      - .. image:: _static/MCONT.png 
           :width: 16px
      - Returns the covariance of all two fieldsets

    * - :func:`covar_a`
      - .. image:: _static/MCONT.png 
           :width: 16px
      - Computes the area-weighted covariance for each field in a fieldset

    * - :func:`frequencies`
      - .. image:: _static/MCONT.png 
           :width: 16px
      - Computes frequencies of a field

    * - :func:`integrate`
      - .. image:: _static/MCONT.png 
           :width: 16px
      - Computes the average weighted by the gridcell area for each field in fieldset

    * - :func:`mean`
      - .. image:: _static/MCONT.png 
           :width: 16px
      - Returns the sum or mean of the values in a geopoints variable

    * - :func:`mean_ew`
      - .. image:: _static/MCONT.png 
           :width: 16px
      - Generates a fieldset out of East-West means

    * - :func:`percentile`
      - .. image:: _static/MCONT.png 
           :width: 16px
      - Returns a set of percentiles of a vector

    * - :func:`rms`
      - .. image:: _static/MCONT.png 
           :width: 16px
      - Returns the root mean square of all the fields of a variable

    * - :func:`stdev`
      - .. image:: _static/MCONT.png 
           :width: 16px
      - Returns the standard deviation of all the fields of a variable

    * - :func:`stdev_a`
      - .. image:: _static/MCONT.png 
           :width: 16px
      - Computes the area-weighted standard deviation for each field in a fieldset

    * - :func:`sum`
      - .. image:: _static/MCONT.png 
           :width: 16px
      - Returns the sum or mean of the values in a geopoints variable

    * - :func:`var`
      - .. image:: _static/MCONT.png 
           :width: 16px
      - Returns the variance of all the fields of a variable

    * - :func:`var_a`
      - .. image:: _static/MCONT.png 
           :width: 16px
      - Computes the area-weighted variance for each field in a fieldset


Thermodynamics
-------------------------------

.. list-table::
    :widths: 20 10 70
    :header-rows: 0


    * - :func:`dewpoint_from_relative_humidity`
      - .. image:: _static/MCONT.png 
           :width: 16px
      - Computes the dewpoint for a given temperature and relative humidity

    * - :func:`dewpoint_from_specific_humidity`
      - .. image:: _static/MCONT.png 
           :width: 16px
      - Computes the dewpoint for a given specific humidity and pressure

    * - :func:`eqpott_m`
      - .. image:: _static/MCONT.png 
           :width: 16px
      - 

    * - :func:`eqpott_p`
      - .. image:: _static/MCONT.png 
           :width: 16px
      - 

    * - :func:`lifted_condensation_level`
      - .. image:: _static/MCONT.png 
           :width: 16px
      - Computes the Lifted Condensation Level (LCL) using the parcel method

    * - :func:`mixing_ratio`
      - .. image:: _static/MCONT.png 
           :width: 16px
      - Computes the mixing ratio from specific humidity

    * - :func:`potential_temperature`
      - .. image:: _static/MCONT.png 
           :width: 16px
      - computes the potential temperature for a given temperature and pressure

    * - :func:`pott_m`
      - .. image:: _static/MCONT.png 
           :width: 16px
      - 

    * - :func:`pott_p`
      - .. image:: _static/MCONT.png 
           :width: 16px
      - 

    * - :func:`relative_humidity_from_dewpoint`
      - .. image:: _static/MCONT.png 
           :width: 16px
      - Computes the relative humidity for a given temperature and dewpoint

    * - :func:`saturation_mixing_ratio`
      - .. image:: _static/MCONT.png 
           :width: 16px
      - Computes the saturation mixing ratio for a given temperature and pressure

    * - :func:`saturation_vapour_pressure`
      - .. image:: _static/MCONT.png 
           :width: 16px
      - Computes the saturation vapour pressure for a given temperature

    * - :func:`seqpott_m`
      - .. image:: _static/MCONT.png 
           :width: 16px
      - 

    * - :func:`seqpott_p`
      - .. image:: _static/MCONT.png 
           :width: 16px
      - 

    * - :func:`temperature_from_potential_temperature`
      - .. image:: _static/MCONT.png 
           :width: 16px
      - Computes the temperature from potential tempearture and pressure

    * - :func:`thermo_bufr`
      - .. image:: _static/MCONT.png 
           :width: 16px
      - 

    * - :func:`thermo_data_values`
      - .. image:: _static/MCONT.png 
           :width: 16px
      - extracts data and metadata from a thermo data object

    * - :func:`thermo_grib`
      - .. image:: _static/MCONT.png 
           :width: 16px
      - 

    * - :func:`thermo_parcel_area`
      - .. image:: _static/MCONT.png 
           :width: 16px
      - returns a set of coloured areas from a thermo parcel path

    * - :func:`thermo_parcel_path`
      - .. image:: _static/MCONT.png 
           :width: 16px
      - computes the path of an ascending thermodynamic parcel

    * - :func:`vapour_pressure`
      - .. image:: _static/MCONT.png 
           :width: 16px
      - Computes the vapour pressure for a given specific humidity and pressure


Geographic
-------------------------------

.. list-table::
    :widths: 20 10 70
    :header-rows: 0


    * - :func:`bearing`
      - .. image:: _static/MCONT.png 
           :width: 16px
      - Computes the bearings for all the gridpoints with respect to a reference point

    * - :func:`coslat`
      - .. image:: _static/MCONT.png 
           :width: 16px
      - Generates a field with the cosine of the gridpoint latitudes

    * - :func:`direction`
      - .. image:: _static/MCONT.png 
           :width: 16px
      - Computes meteorological wind direction using U and V wind components

    * - :func:`distance`
      - .. image:: _static/MCONT.png 
           :width: 16px
      - Computes the distances of all the gridpoints from a point

    * - :func:`geosort`
      - .. image:: _static/MCONT.png 
           :width: 16px
      - Sorts the geopoints North to South and West to East

    * - :func:`grid_cell_area`
      - .. image:: _static/MCONT.png 
           :width: 16px
      - Computes grid cell area for each gridpoints in a field

    * - :func:`latitudes`
      - .. image:: _static/MCONT.png 
           :width: 16px
      - Returns a list/vector of latitudes from the given geopoints.

    * - :func:`longitudes`
      - .. image:: _static/MCONT.png 
           :width: 16px
      - Returns a list/vector of longitudes from the given geopoints.

    * - :func:`nearest_gridpoint`
      - .. image:: _static/MCONT.png 
           :width: 16px
      - Returns the nearest grid point value from a field

    * - :func:`nearest_gridpoint_info`
      - .. image:: _static/MCONT.png 
           :width: 16px
      - Returns the nearest grid point value from a field

    * - :func:`offset`
      - .. image:: _static/MCONT.png 
           :width: 16px
      - Offsets the locations of geopoints

    * - :func:`sinlat`
      - .. image:: _static/MCONT.png 
           :width: 16px
      - Generates a field with the sine of the gridpoint latitudes

    * - :func:`tanlat`
      - .. image:: _static/MCONT.png 
           :width: 16px
      - Generates a field with the tangent of the gridpoint latitudes


Filtering
-------------------------------

.. list-table::
    :widths: 20 10 70
    :header-rows: 0


    * - :func:`bitmap`
      - .. image:: _static/MCONT.png 
           :width: 16px
      - Converts numbers to missing values in a vector

    * - :func:`bufr_picker`
      - .. image:: _static/MCONT.png 
           :width: 16px
      - 

    * - :func:`cleanfile`
      - .. image:: _static/MCONT.png 
           :width: 16px
      - 

    * - :func:`filter`
      - .. image:: _static/MCONT.png 
           :width: 16px
      - Filters a vector according to the values of a second vector

    * - :func:`nobitmap`
      - .. image:: _static/MCONT.png 
           :width: 16px
      - Converts missing values to numbers in a vector

    * - :func:`obsfilter`
      - .. image:: _static/MCONT.png 
           :width: 16px
      - 

    * - :func:`odb_filter`
      - .. image:: _static/MCONT.png 
           :width: 16px
      - 

    * - :func:`read`
      - .. image:: _static/MCONT.png 
           :width: 16px
      - 

    * - :func:`rmask`
      - .. image:: _static/MCONT.png 
           :width: 16px
      - Generates masks based on a radius around a point for fieldsets


Grid
-------------------------------

.. list-table::
    :widths: 20 10 70
    :header-rows: 0


    * - :func:`interpolate`
      - .. image:: _static/MCONT.png 
           :width: 16px
      - Interpolates field values to the specified location

    * - :func:`surrounding_points_indexes`
      - .. image:: _static/MCONT.png 
           :width: 16px
      - Returns the indexes of the four surrounding grid points


Vertical
-------------------------------

.. list-table::
    :widths: 20 10 70
    :header-rows: 0


    * - :func:`cross_sect`
      - .. image:: _static/MCONT.png 
           :width: 16px
      - 

    * - :func:`geostrophic_wind`
      - .. image:: _static/MCONT.png 
           :width: 16px
      - Computes geostrophic wind on pressure levels

    * - :func:`ml_to_hl`
      - .. image:: _static/MCONT.png 
           :width: 16px
      - Interpolates model level fields to height levels

    * - :func:`mvl_geopotential_on_ml`
      - .. image:: _static/MCONT.png 
           :width: 16px
      - Computes geopotential on model levels

    * - :func:`mvl_ml2hPa`
      - .. image:: _static/MCONT.png 
           :width: 16px
      - Interpolates a fieldset on model levels to pressure levels (in hPa)

    * - :func:`pressure`
      - .. image:: _static/MCONT.png 
           :width: 16px
      - Creates fields of pressure or thickness (input in lat/lon only).

    * - :func:`thickness`
      - .. image:: _static/MCONT.png 
           :width: 16px
      - Creates fields of pressure or thickness (input in lat/lon only).

    * - :func:`unipressure`
      - .. image:: _static/MCONT.png 
           :width: 16px
      - Creates fields of pressure or thickness (accepts several grid types)

    * - :func:`unithickness`
      - .. image:: _static/MCONT.png 
           :width: 16px
      - Creates fields of pressure or thickness (accepts several grid types)

    * - :func:`univertint`
      - .. image:: _static/MCONT.png 
           :width: 16px
      - Universal vertical integration, also for sparse vertical data

    * - :func:`vert_prof`
      - .. image:: _static/MCONT.png 
           :width: 16px
      - 

    * - :func:`vertint`
      - .. image:: _static/MCONT.png 
           :width: 16px
      - Performs vertical integration

    * - :func:`w_from_omega`
      - .. image:: _static/MCONT.png 
           :width: 16px
      - Computes the vertical velocity in m/s from pressure velocity
