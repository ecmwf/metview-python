
regrid
=========================

.. container::
    
    .. container:: leftside

        .. image:: /_static/REGRID.png
           :width: 48px

    .. container:: rightside

		Takes data from a GRIB source and performs a variety of operations on it, including spectral to grid conversion, regridding using a large variety of powerful and flexible interpolation techniques, nabla operators and special consideration of wind fields. :func:`regrid` is designed with re-use in mind. The first time a particular interpolation is performed, it might take some time to compute, but it will create cache files that can be re-used, meaning that the same interpolation will be much faster on subsequent runs.


		.. note:: This function performs the same task as the `Regrid <https://confluence.ecmwf.int/display/METV/regrid>`_ icon in Metview’s user interface. It accepts its parameters as keyword arguments, described below.


.. py:function:: regrid(**kwargs)
  
    Performs a variety of operations on GRIB data, including spectral to grid conversion, regridding using a large variety of powerful and flexible interpolation techniques, nabla operators and special consideration of wind fields.


    :param source: 
    :type source: str

    :param data: 
    :type data: :class:`Filedset`

    :param grid_definition_mode: 
    :type grid_definition_mode: {"grid", "lambert_azimuthal_equal_area", "lambert_conformal", "template", "filter"}, default: "grid"

    :param template_source: 
    :type template_source: str

    :param template_data: 
    :type template_data: str

    :param grid: 
    :type grid: str or list[str]

    :param first_point: 
    :type first_point: float or list[float], default: 0

    :param dx_in_metres: 
    :type dx_in_metres: number

    :param dy_in_metres: 
    :type dy_in_metres: number

    :param nx: 
    :type nx: number

    :param ny: 
    :type ny: number

    :param lad_in_degrees: 
    :type lad_in_degrees: number

    :param lov_in_degrees: 
    :type lov_in_degrees: number

    :param latin_1_in_degrees: 
    :type latin_1_in_degrees: number, default: 0

    :param latin_2_in_degrees: 
    :type latin_2_in_degrees: number, default: 0

    :param standard_parallel_in_degrees: 
    :type standard_parallel_in_degrees: number

    :param central_longitude_in_degrees: 
    :type central_longitude_in_degrees: number

    :param wind_processing: 
    :type wind_processing: {"off", "uv_to_uv", "vod_to_uv"}, default: "off"

    :param nabla: 
    :type nabla: str, default: "off"

    :param nabla_poles_missing_values: Due to the supporting differential operators calculation method, values aren't well defined at the poles (singularities). This option allows forcing missing value at the poles.
    :type nabla_poles_missing_values: {"on", "off"}, default: "off"

    :param area: Supply a grid definition as described  here: `area - keyword in MARS/Dissemination request <https://confluence.ecmwf.int/pages/viewpage.action?pageId=151520973>`_ (swapping north/south). Specifies the geographical area  as [south, west, north, east] that the output fields will cover, the default being for the whole globe. 
    :type area: list[float], default: [-90, -180, 90, 180]

    :param rotation: Position of the South Pole (as [lat, lon]) of the intended rotated grid as lat/lon in degree, as described here: `rotation - keyword in MARS/Dissemination request <https://confluence.ecmwf.int/pages/viewpage.action?pageId=168664701>`_. This is applicable to regular lat/lon or regular/reduced Gaussian grids.
    :type rotation: list[float], default: [-90, 0]

    :param truncation: 
    :type truncation: str, default: "automatic"

    :param intgrid: 
    :type intgrid: str, default: "automatic"

    :param frame: Specifies the width of a frame within a given sub-area, as described here `frame - keyword in MARS/Dissemination request <https://confluence.ecmwf.int/pages/viewpage.action?pageId=118841732>`_. The width of the frame is specified as an (integer) number of grid points inwards from a given area.
    :type frame: number

    :param interpolation: 
    :type interpolation: str, default: "automatic"

    :param nearest_method: Available for any of the 'nearest' interpolation methods. Supports Interpolation K-Nearest Neighbours or Nearest LSM. Possible values are:
		
		* "distance": input points with radius (option ``distance``) of output point
		* "nclosest": n-closest input points (option ``nclosest``) to output point (default 4)
		* "distance_and_nclosest": input points respecting ``distance`` :math:`\cap` ``nclosest``.
		* "distance_or_nclosest": input points respecting ``distance`` :math:`\cup` ``nclosest``    
		* "nclosest_or_nearest": n-closest input points (option ``nclosest``), if all are at the same distance (within option ``distance_tolerance``) return all points within that distance (robust interpolation of pole values)
		* "nearest_neighbour_with_lowest_index": nearest input point, if at the same distance to other points (option ``nclosest``) chosen by lowest index 
		* "sample": sample of n-closest points (option ``nclosest``) out of input points with radius (option ``distance``) of output point, not sorted by distance
		* "sorted_sample": as above, sorted by distance
    :type nearest_method: str, default: "automatic"

    :param distance_weighting: 
    :type distance_weighting: str, default: "inverse_distance_weighting_squared"

    :param nclosest: 
    :type nclosest: number, default: 4

    :param distance: 
    :type distance: number, default: 1

    :param climate_filter_delta: 
    :type climate_filter_delta: number, default: 1000

    :param distance_weighting_gaussian_stddev: 
    :type distance_weighting_gaussian_stddev: number, default: 1

    :param distance_weighting_shepard_power: 
    :type distance_weighting_shepard_power: number, default: 2

    :param distance_tolerance: 
    :type distance_tolerance: number, default: 1

    :param distance_weighting_with_lsm: Only available if ``interpolation`` is "nearest_lsm". Possible values are:
		
		* "nearest_lsm": chose the closest input point (no disambiguation if there is more than one closest point at the same distance)
		* "nearest_lsm_with_lowest_index": cross-platform compatible version (of the above Nearest LSM) with disambiguation of closest input points at the same distance of output points
		* "off": use internal defaults (currently set to "nearest_lsm_with_lowest_index")
    :type distance_weighting_with_lsm: {"nearest_lsm", "nearest_lsm_with_lowest_index", "off"}, default: "off"

    :param lsm_weight_adjustment: Only available if ``lsm`` is "on", this is the factor adjusting input point weights if they are not of the same type (land/sea) as related output point; On application, all contributing input point weights are re-normalised (linearly) to :math:`\sum_{i}w_{i}=1`.
    :type lsm_weight_adjustment: number, default: 0.2

    :param lsm_interpolation_input: If input is not on the same grid (geometry) as provided input LSM (respectively), interpolate with this method to a temporary LSM with required geometry.
    :type lsm_interpolation_input: str, default: "nearest_neighbour"

    :param lsm_selection_input: Specifies whether input LSM file will come from ``lsm_named_input`` ("named") or ``lsm_file_input`` ("file").
    :type lsm_selection_input: {"file", "named"}, default: "named"

    :param lsm_named_input: Select one of the predefined names from the following:
		
		* "1km": binary-based LSM sourced from MODIS Land Water Mask MOD44W (see `reference <https://lpdaac.usgs.gov/products/mod44wv006/>`_)
		* "10min": binary-based LSM at high resolution (legacy, pre-climate files version 15)
		* "O1280": GRIB-based IFS supporting climate files version 15, on this specific grid
		* "O640": as above, for this grid
		* "O320": as above, for this grid
		* "N320": as above, for this grid
		* "N256": as above, for this grid
		* "N128": as above, for this grid
    :type lsm_named_input: {"1km", "10min", "o1280", "o640", "o320", "n320", "n256", "n128"}, default: "1km"

    :param lsm_file_input: Provide the path to an input LSM GRIB file.
    :type lsm_file_input: str

    :param lsm_value_threshold_input: For GRIB-based LSM (so excluding '1km' and '10min'), the threshold for condition (value ≥ threshold) to distinguish land (true) from sea (false).
    :type lsm_value_threshold_input: number, default: 0.5

    :param lsm_interpolation_output: If output is not on the same grid (geometry) as provided output LSM (respectively), interpolate with this method to a temporary LSM with required geometry.
    :type lsm_interpolation_output: str, default: "nearest_neighbour"

    :param lsm_selection_output: Specifies whether output LSM file will come from ``lsm_named_output`` ("named") or ``lsm_file_output`` ("file").
    :type lsm_selection_output: {"file", "named"}, default: "named"

    :param lsm_named_output: Select one of the predefined names from the following:
		
		* "1km": binary-based LSM sourced from MODIS Land Water Mask MOD44W (see `reference <https://lpdaac.usgs.gov/products/mod44wv006/>`_)
		* "10min": binary-based LSM at high resolution (legacy, pre-climate files version 15)
		* "O1280": GRIB-based IFS supporting climate files version 15, on this specific grid
		* "O640": as above, for this grid
		* "O320": as above, for this grid
		* "N320": as above, for this grid
		* "N256": as above, for this grid
		* "N128": as above, for this grid
    :type lsm_named_output: {"1km", "10min", "o1280", "o640", "o320", "n320", "n256", "n128"}, default: "1km"

    :param lsm_file_output: Provide the path to an output LSM GRIB file.
    :type lsm_file_output: str

    :param lsm_value_threshold_output: For GRIB-based LSM (so excluding '1km' and '10min'), the threshold for condition (value ≥ threshold) to distinguish land (true) from sea (false).
    :type lsm_value_threshold_output: number, default: 0.5

    :param non_linear: 
    :type non_linear: str, default: "missing_if_heaviest_missing"

    :param simulated_missing_value: 
    :type simulated_missing_value: number, default: 9999

    :param simulated_missing_value_epsilon: 
    :type simulated_missing_value_epsilon: number, default: 0

    :param accuracy: Specifies the output GRIB bitsPerValue, as described  here: `accuracy - keyword in MARS/Dissemination request <https://confluence.ecmwf.int/pages/viewpage.action?pageId=168664760>`_.  If left empty, this will take the value from the input fields. This option can also be used to simply change the number of bits per value in a :class:`Fieldset` if no other processing options are given. Note that if ``packing`` is set to "ieee", then the only valid values for this parameter are 32 and 64.
    :type accuracy: number

    :param packing: Specifies the output GRIB packingType, as described  here: `accuracy - keyword in MARS/Dissemination request <https://confluence.ecmwf.int/pages/viewpage.action?pageId=168664760>`_. Possible values are depending on build-time configuration.
    :type packing: {"av", "co", "grid_jpeg", "so", "simple", "ieee", "as_input"}, default: "as_input"

    :param edition: Specifies the output GRIB edition (or format). Note that format conversion is not supported.
    :type edition: {"1", "2", "as_input"}, default: "as_input"

    :rtype: :class:`Fieldset`
