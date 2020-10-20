
Computation functions
===========================



Statistics
-------------------------------

.. list-table::
    :widths: 20 80
    :header-rows: 0


    * - :func:`accumulate`
      - Adds up the values per field in a :class:`Fieldset`

    * - :func:`average`
      - Computes the average per field in a :class:`Fieldset`

    * - :func:`average_ew`
      - Returns the zonal averages as a list (or list of lists) of numbers.

    * - :func:`average_ns`
      - Returns the meridional averages as a list (or list of lists) of numbers.

    * - :func:`corr_a`
      - Computes the area-weighted correlation for each field in a :class:`Fieldset`

    * - :func:`covar`
      - Returns the covariance of all two :class:`Fieldset`

    * - :func:`covar_a`
      - Computes the area-weighted covariance for each field in a :class:`Fieldset`

    * - :func:`frequencies`
      - Computes frequencies of a field

    * - :func:`integrate`
      - Computes the average weighted by the gridcell area for each field in :class:`Fieldset`

    * - :func:`max`
      - Maximum

    * - :func:`maxvalue`
      - Computes the maximum of all the values in a :class:`Fieldset`

    * - :func:`mean`
      - Returns the sum or mean of the values in a :class:`Geopoints` variable

    * - :func:`mean_ew`
      - Generates a :class:`Fieldset` out of East-West means

    * - :func:`min`
      - Minimum

    * - :func:`minvalue`
      - Minimum value of a variable

    * - :func:`percentile`
      - Computes a set of percentiles of GRIB data

    * - :func:`rms`
      - Returns the root mean square of all the fields of a variable

    * - :func:`stdev`
      - Returns the standard deviation of all the fields of a variable

    * - :func:`stdev_a`
      - Computes the area-weighted standard deviation for each field in a :class:`Fieldset`

    * - :func:`sum`
      - Returns the sum or mean of the values in a :class:`Geopoints` variable

    * - :func:`var`
      - Returns the variance of all the fields of a variable

    * - :func:`var_a`
      - Computes the area-weighted variance for each field in a :class:`Fieldset`


Geographic
-------------------------------

.. list-table::
    :widths: 20 80
    :header-rows: 0


    * - :func:`bearing`
      - Computes the bearings for all the gridpoints with respect to a reference point

    * - :func:`coslat`
      - Generates a field with the cosine of the gridpoint latitudes

    * - :func:`distance`
      - Computes the distances of all the gridpoints from a point

    * - :func:`geosort`
      - Sorts the :class:`Geopoints` North to South and West to East

    * - :func:`grid_cell_area`
      - Computes grid cell area for each gridpoints in a field

    * - :func:`latitudes`
      - Returns a list/vector of latitudes from the given :class:`Geopoints`.

    * - :func:`longitudes`
      - Returns a list/vector of longitudes from the given :class:`Geopoints`.

    * - :func:`nearest_gridpoint`
      - Returns the nearest grid point value from a field

    * - :func:`nearest_gridpoint_info`
      - Returns the nearest grid point value from a field

    * - :func:`offset`
      - Offsets the locations of :class:`Geopoints`

    * - :func:`reprojection`
      - Repoject satellite view GRIB data onto a latlon grid

    * - :func:`sinlat`
      - Generates a field with the sine of the gridpoint latitudes

    * - :func:`subsample`
      - Filters from the first :class:`Geopoints` variable points that exist in the second

    * - :func:`tanlat`
      - Generates a field with the tangent of the gridpoint latitudes


Filtering
-------------------------------

.. list-table::
    :widths: 20 80
    :header-rows: 0


    * - :func:`bufr_picker`
      - Filters BUFR data with complex structure

    * - :func:`cleanfile`
      - Removes unwanted header padding from GRIB and BUFR

    * - :func:`filter`
      - Filters a vector according to the values of a second vector

    * - :func:`obsfilter`
      - Filters BUFR data

    * - :func:`odb_filter`
      - Filters ODB data

    * - :func:`read`
      - Filters and interpolates GRIB data


Masking
-------------------------------

.. list-table::
    :widths: 20 80
    :header-rows: 0


    * - :func:`bitmap`
      - Converts numbers to missing values in a vector

    * - :func:`mask`
      - Generates masks for :class:`Geopoints`

    * - :func:`nobitmap`
      - Converts missing values to numbers in a vector

    * - :func:`remove_missing_latlons`
      - Copies a set of :class:`Geopoints`, removing missing lat/lons

    * - :func:`remove_missing_values`
      - Copies a set of :class:`Geopoints`, removing missing values

    * - :func:`rmask`
      - Generates masks based on a radius around a point for :class:`Fieldset`


Grid
-------------------------------

.. list-table::
    :widths: 20 80
    :header-rows: 0


    * - :func:`interpolate`
      - Interpolates field values to the specified location

    * - :func:`surrounding_points_indexes`
      - Returns the indexes of the four surrounding grid points


Wind
-------------------------------

.. list-table::
    :widths: 20 80
    :header-rows: 0


    * - :func:`direction`
      - Computes meteorological wind direction using U and V wind components

    * - :func:`divrot`
      - Computes the rotational wind from a vorticity :class:`Fieldset`

    * - :func:`divwind`
      - Computes the divergent wind from a divergence :class:`Fieldset`

    * - :func:`geostrophic_wind`
      - Computes geostrophic wind on pressure levels

    * - :func:`streamfn`
      - Computes the stream function from a vorticity :class:`Fieldset`

    * - :func:`uvwind`
      - Computes u/v from a vorticty and divegence :class:`Fieldset`

    * - :func:`velpot`
      - Computes the velocity potential from a divergence :class:`Fieldset`

    * - :func:`xy_from_polar`
      - Computes the x and y components from polar components


Vertical
-------------------------------

.. list-table::
    :widths: 20 80
    :header-rows: 0


    * - :func:`mcross_sect`
      - Generates input data for a cross section

    * - :func:`mhovmoeller_area`
      - Generates data for the Hovmoeller area mode

    * - :func:`mhovmoeller_expand`
      - Generates data for the Hovmoeller expand mode

    * - :func:`mhovmoeller_line`
      - Generates data for the Hovmoeller line mode

    * - :func:`mhovmoeller_vertical`
      - Generates data for the Hovmoeller vertical mode

    * - :func:`ml_to_hl`
      - Interpolates model level fields to height levels

    * - :func:`mvert_prof`
      - Generates data for the vertical profile view

    * - :func:`mvl_geopotential_on_ml`
      - Computes the geopotential on model levels

    * - :func:`mvl_ml2hPa`
      - Interpolates a :class:`Fieldset` on model levels to pressure levels (in hPa)

    * - :func:`mxs_average`
      - Defines the average view

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

    * - :func:`vertint`
      - Performs vertical integration

    * - :func:`w_from_omega`
      - Computes the vertical velocity in m/s from pressure velocity


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
      - Computes the equivalent potential temperature on model levels

    * - :func:`eqpott_p`
      - Computes the equivalent potential temperature on pressure levels

    * - :func:`lifted_condensation_level`
      - Computes the Lifted Condensation Level (LCL) using the parcel method

    * - :func:`mixing_ratio`
      - Computes the mixing ratio from specific humidity

    * - :func:`potential_temperature`
      - computes the potential temperature for a given temperature and pressure

    * - :func:`pott_m`
      - Computes the potential temperature on model levels

    * - :func:`pott_p`
      - Computes the potential temperature on pressure levels

    * - :func:`relative_humidity_from_dewpoint`
      - Computes the relative humidity for a given temperature and dewpoint

    * - :func:`relhum`
      - Computes relative humidity from specific humidity

    * - :func:`saturation_mixing_ratio`
      - Computes the saturation mixing ratio for a given temperature and pressure

    * - :func:`saturation_vapour_pressure`
      - Computes the saturation vapour pressure for a given temperature

    * - :func:`seqpott_m`
      - Computes the saturation equivalent potential temperature on model levels

    * - :func:`seqpott_p`
      - Computes the saturation equivalent potential temperature on pressure levels

    * - :func:`temperature_from_potential_temperature`
      - Computes the temperature from potential tempearture and pressure

    * - :func:`thermo_bufr`
      - Generates thermodynamical profile from BUFR

    * - :func:`thermo_data_info`
      - extracts information from a thermo data object

    * - :func:`thermo_data_values`
      - extracts data and metadata from a thermo data object

    * - :func:`thermo_grib`
      - Generates thermodynamical profile from GRIB

    * - :func:`thermo_parcel_area`
      - returns a set of coloured areas from a thermo parcel path

    * - :func:`thermo_parcel_path`
      - Computes the path of an ascending thermodynamic parcel

    * - :func:`vapour_pressure`
      - Computes the vapour pressure for a given specific humidity and pressure


Calculus
-------------------------------

.. list-table::
    :widths: 20 80
    :header-rows: 0


    * - :func:`divergence`
      - Computes the horizontal divergence of a vector :class:`Fieldset`

    * - :func:`first_derivative_x`
      - Computes first West-East derivative of a :class:`Fieldset`

    * - :func:`first_derivative_y`
      - Computes first South-North derivative of a :class:`Fieldset`

    * - :func:`gradient`
      - Computes horizontal gradient of a :class:`Fieldset`

    * - :func:`integral`
      - Computes the surface integral of a :class:`Fieldset`

    * - :func:`laplacian`
      - Computes the horizontal Laplacian of :class:`Fieldset`

    * - :func:`second_derivative_x`
      - Computes the second West-East derivative of a :class:`Fieldset`

    * - :func:`second_derivative_y`
      - Computes the econd South-North derivative of a :class:`Fieldset`

    * - :func:`vorticity`
      - Computes the relative vorticity of a vector :class:`Fieldset`


Basic mathematics
-------------------------------

.. list-table::
    :widths: 20 80
    :header-rows: 0


    * - :func:`abs`
      - Computes the absolute value

    * - :func:`acos`
      - Computes the arc cosine

    * - :func:`asin`
      - Computes the arc sine

    * - :func:`atan`
      - Computes the arc tangent

    * - :func:`atan2`
      - Computes the arc tangent of 2 variables

    * - :func:`cos`
      - Computes the cosine

    * - :func:`div`
      - Computes the integer part of a divison

    * - :func:`exp`
      - Computes the exponential

    * - :func:`intbits`
      - Returns ranges of bits

    * - :func:`log`
      - Computes the natural logarithm

    * - :func:`log10`
      - Computes the base 10 logarithm

    * - :func:`mod`
      - Computes the integer remainder of a divison

    * - :func:`sgn`
      - Computes the sign

    * - :func:`sin`
      - Computes the sine

    * - :func:`sqrt`
      - Computes the square root

    * - :func:`tan`
      - Computes the tangent
