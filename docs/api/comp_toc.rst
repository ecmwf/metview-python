
Computation functions
=======================



Statistics
------------


.. list-table::
    :widths: 20 80
    :header-rows: 0


    * - :func:`accumulate`
      - Adds up the values per field in a :class:`Fieldset`

    * - :func:`average`
      - Computes the average per field in a :class:`Fieldset`

    * - :func:`average_ew`
      - Computes the zonal averages for each field in a :class:`Fieldset`

    * - :func:`average_ns`
      - Computes the meridional averages for each field in a :class:`Fieldset`

    * - :func:`corr_a`
      - Computes the area-weighted correlation for each field in a :class:`Fieldset`

    * - :func:`covar`
      - Returns the covariance of two :class:`Fieldset` objects

    * - :func:`covar_a`
      - Computes the area-weighted covariance for each field in a :class:`Fieldset`

    * - :func:`frequencies`
      - Computes the frequencies of a :class:`Fieldset`

    * - :func:`integrate`
      - Computes the average weighted by the gridcell area for each field in :class:`Fieldset`

    * - :func:`max`
      - Maximum

    * - :func:`maxvalue`
      - Maximum value of a :class:`Fieldset`

    * - :func:`mean`
      - Returns the mean of the values in a :class:`Fieldset` or :class:`Geopoints`

    * - :func:`mean_ew`
      - Generates a :class:`Fieldset` out of East-West means

    * - :func:`min`
      - Minimum

    * - :func:`minvalue`
      - Minimum value of a :class:`Fieldset` or :class:`Geopoints`

    * - :func:`percentile`
      - Computes a set of percentiles in a :class:`Fieldset`

    * - :func:`rms`
      - Returns the root mean square of all the fields in a :class:`Fieldset`

    * - :func:`stdev`
      - Returns the standard deviation of all the fields in a :class:`Fieldset`

    * - :func:`stdev_a`
      - Computes the area-weighted standard deviation for each field in a :class:`Fieldset`

    * - :func:`sum`
      - Computes the sum of the values in a :class:`Fieldset` or :class:`Geopoints`

    * - :func:`var`
      - Returns the variance of all the fields in a :class:`Fieldset`

    * - :func:`var_a`
      - Computes the area-weighted variance for each field in a :class:`Fieldset`


Geographic
------------


.. list-table::
    :widths: 20 80
    :header-rows: 0


    * - :func:`bearing`
      - Computes the bearings with respect to a reference in a :class:`Fieldset` point

    * - :func:`coslat`
      - Generates a field with the cosine of the latitudes in a :class:`Fieldset`

    * - :func:`distance`
      - Computes the distances in a :class:`Fieldset` or :class:`Geopoints` to a reference point

    * - :func:`geosort`
      - Sorts a :class:`Geopoints` North to South and West to East

    * - :func:`grid_cell_area`
      - Computes the grid cell area in a :class:`Fieldset`

    * - :func:`interpolate`
      - Interpolates :class:`Fieldset` values to the specified location

    * - :func:`latitudes`
      - Returns the latitudes of a :class:`Fieldset` or :class:`Geopoints`

    * - :func:`longitudes`
      - Returns the longitudes from a :class:`Fieldset` or :class:`Geopoints`

    * - :func:`nearest_gridpoint`
      - Returns the nearest grid point value from a :class:`Fieldset`

    * - :func:`nearest_gridpoint_info`
      - Returns the nearest grid point value from a :class:`Fieldset`

    * - :func:`offset`
      - Offsets the locations of :class:`Geopoints`

    * - :func:`read`
      - Filters and interpolates :class:`Fieldset` data

    * - :func:`regrid`
      - Regridding and derivatives

    * - :func:`reprojection`
      - Repoject satellite view GRIB data onto a latlon grid

    * - :func:`sinlat`
      - Generates a field with the cosine of the latitudes in a :class:`Fieldset`

    * - :func:`subsample`
      - Filters the points of the first :class:`Geopoints` that exist in the second one

    * - :func:`surrounding_points_indexes`
      - Returns the indexes of the four surrounding grid points in a :class:`Fieldset`

    * - :func:`tanlat`
      - Generates a field with the tangent of the latitudes in a :class:`Fieldset`


Masking
---------


.. list-table::
    :widths: 20 80
    :header-rows: 0


    * - :func:`bitmap`
      - Converts numbers to missing values in a :class:`Fieldset`

    * - :func:`mask`
      - Generates masks for a :class:`Fieldset` or :class:`Geopoints`

    * - :func:`nobitmap`
      - Converts missing values to numbers in a :class:`Fieldset`

    * - :func:`remove_missing_latlons`
      - Removing missing lat/lons form a :class:`Geopoints`

    * - :func:`remove_missing_values`
      - Removes missing values from a :class:`Geopoints`

    * - :func:`rmask`
      - Generates masks based on a radius around a point for :class:`Fieldset`


Wind
------


.. list-table::
    :widths: 20 80
    :header-rows: 0


    * - :func:`direction`
      - Computes the wind direction

    * - :func:`divrot`
      - Computes the rotational wind from a spectral vorticity :class:`Fieldset`

    * - :func:`divwind`
      - Computes the divergent wind from a spectral divergence :class:`Fieldset`

    * - :func:`geostrophic_wind`
      - Computes the geostrophic wind on pressure levels in a :class:`Fieldset`

    * - :func:`streamfn`
      - Computes the stream function from a spectral vorticity :class:`Fieldset`

    * - :func:`uvwind`
      - Computes u/v from a spectral vorticty and divegence :class:`Fieldset`

    * - :func:`velpot`
      - Computes the velocity potential from a spectral divergence :class:`Fieldset`

    * - :func:`xy_from_polar`
      - Computes the x and y components from polar components


Vertical
----------


.. list-table::
    :widths: 20 80
    :header-rows: 0


    * - :func:`mcross_sect`
      - Generates data for the cross section view

    * - :func:`mhovmoeller_area`
      - Generates data for the Hovmoeller area mode

    * - :func:`mhovmoeller_expand`
      - Generates data for the Hovmoeller expand mode

    * - :func:`mhovmoeller_line`
      - Generates data for the Hovmoeller line mode

    * - :func:`mhovmoeller_vertical`
      - Generates data for the Hovmoeller vertical mode

    * - :func:`ml_to_hl`
      - Interpolates a model level :class:`Fieldset` to height levels

    * - :func:`mvert_prof`
      - Generates data for the vertical profile view

    * - :func:`mvl_geopotential_on_ml`
      - Computes the geopotential on model levels for a :class:`Fieldset`

    * - :func:`mvl_ml2hPa`
      - Interpolates a :class:`Fieldset` on model levels to pressure levels (in hPa)

    * - :func:`mxs_average`
      - Generates data for the average view

    * - :func:`pressure`
      - Computes the pressure on model levels in a :class:`Fieldset` (deprecated)

    * - :func:`thickness`
      - Computes the pressure thickness on model levels in a :class:`Fieldset` (deprecated)

    * - :func:`unipressure`
      - Computes the pressure on model levels in a :class:`Fieldset`

    * - :func:`unithickness`
      - Computes the pressure thickness of model levels in a :class:`Fieldset`

    * - :func:`univertint`
      - Performs a vertical integration for a :class:`Fieldset`

    * - :func:`vertint`
      - Performs a vertical integration for a :class:`Fieldset` (deprecated)

    * - :func:`w_from_omega`
      - Computes the vertical velocity in m/s from pressure velocity


Thermodynamics
----------------


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
      - Generates thermodynamical profile from :class:`Bufr`

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
----------


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
-------------------


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
      - Computes the arc tangent of 2 :class:`Fieldset` objects

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
