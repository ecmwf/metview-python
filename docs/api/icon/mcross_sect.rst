
mcross_sect
=========================

.. container::
    
    .. container:: leftside

        .. image:: /_static/MXSECTION.png
           :width: 48px

    .. container:: rightside

		Derives (and returns) a vertical cross section data unit of upper air fields along a specified transect line. For each upper air field, point values are interpolated along the transect line, with a spacing consistent with the resolution of the input GRIB data.
		
		The cross section data can be plotted (using a default visualisation based on the range of data values) or saved as a NetCDF data file (:class:`Netcdf`) using :func:`write`.
		
		If an orography is plotted it can be customised by applying an :func:`mgraph` visual definition.
		
		If access to the output computed values is not required, or for more control of the plotting, use :func:`mxsectview`.


		.. note:: This function performs the same task as the `Cross Section Data <https://confluence.ecmwf.int/display/METV/Cross+Section+Data>`_ icon in Metview’s user interface. It accepts its parameters as keyword arguments, described below.


.. py:function:: mcross_sect(**kwargs)
  
    Derives (and returns) vertical cross section data.


    :param data: Specifies the GRIB data (:class:`Fieldset`) from which to derive the cross-section profile. The input GRIB icon must specify a multi-level meteorological variable, in a latitude-longitude or Gaussian grid. The following vertical coordinates are supported:
		
		* pressure levels
		* ECMWF model levels (hybrid levels used by the IFS). In this case you must include parameter LNSP (logarithm of surface pressure) should you want the orography and the vertical axis of the plot in pressure levels rather than model levels when visualising the output.
		* general coordinates defined by ``vertical_coordinates``
		
		 If wind arrows are to be plotted, then the input data should include three-dimensional wind data, i.e. the u/v/w wind components should all be present. If more than one time and/or forecast step is contained in ``data``, :func:`mcross_sect` returns a set of cross sections.
    :type data: :class:`Fieldset`

    :param line: Specifies the coordinates of a transect line along which the cross-section is calculated in [lat1, lon1, lat2, lon2] format. The cross section is calculated from a set of geographical points taken along the input transect line. The point selection takes into consideration the resolution of the data and assures that a minimum of 64 points will be used. Note that it is possible to define a line through either pole by describing the line’s coordinates as follows:
		
		* First, when specifying the latitudes of the two points, imagine that the latitude values go above 90 when you cross the North Pole and below -90 when you cross the South Pole.
		*  Next, if you wish a straight line, ensure that the two longitude values are the same as each other.
		
		An example demonstrates this. Say you wanted to defined a straight-line cross-section from 60S/25E to 60S/155W. This would be specified as -60/25/-120/25. The fact that one of the latitude values is below -90 indicates to Metview that a cross-section going through the South Pole is desired. Once this has been established, the fact that the two longitude values are identical tells Metview to use a straight line through the pole. If this is the intent, then only one unique longitude value is required, as the other one can be deduced. Giving Metview two different longitude values will cause a cross-section consisting of two curves to be produced.
    :type line: list[float], default: [0, -180, 0, 180]

    :param wind_parallel: When this option is "on", the wind components are projected onto the cross section plane. For 2D wind the result is a signed scalar data (a contour plot). When 3D wind data are available a vector plot is produced with the vertical component scaled/computed as specified in parameter ``w_wind_scaling_factor_mode``.
    :type wind_parallel: {"on", "off"}, default: "on"

    :param wind_perpendicular: When this option is "on", the wind components are projected onto the normal vector of the cross section plane. The result is a signed scalar data (a contour plot). ``wind_perpendicular`` cannot be set to "on" if ``wind_parallel`` is also "on".
    :type wind_perpendicular: {"on", "off"}, default: "off"

    :param wind_intensity: When this option is "on" the result depends on other settings:
		
		* When both ``wind_parallel`` and ``wind_perpendicular`` are "off", the result is the length of the 2D/3D wind vector at the cross section plane.
		* When ``wind_parallel`` is "on", the result is the absolute value of the projected wind onto the cross section plane.
		* When ``wind_perpendicular`` is "on", the result is the absolute value of the wind projected onto the normal vector of the cross section plane.
    :type wind_intensity: {"on", "off"}, default: "off"

    :param lnsp_param: Specifies the ecCodes paramId used to identify the Logarithm of Surface Pressure (LNSP) in the input data.
    :type lnsp_param: number, default: 152

    :param u_wind_param: Specifies the ecCodes paramId used to identify the U wind component in the input data.
    :type u_wind_param: number, default: 131

    :param v_wind_param: Specifies the ecCodes paramId used to identify the V wind component in the input data.
    :type v_wind_param: number, default: 132

    :param w_wind_param: Specifies the ecCodes paramId used to identify the vertical wind component in the input data. The default value is 135 i.e. pressure velocity in Pa/s (as used by ECMWF).
    :type w_wind_param: number, default: 135

    :param t_param: Specifies the ecCodes paramId used to identify the temperature in the input data. Used in the vertical wind computations when ``w_wind_scaling_factor_mode`` is set to "compute".
    :type t_param: number, default: 130

    :param horizontal_point_mode: Specifies how the geographical points along the input transect ``line`` will be computed. Setting this option to "interpolate" will create a regular set of interpolated geographical points along the transect ``line``. Setting this option to "nearest_gridpoint" will instead select the nearest points from the data.
    :type horizontal_point_mode: {"interpolate", "nearest_gridpoint"}, default: "interpolate"

    :param vertical_coordinates: Setting this option to "user" will enable the use of general height-based coordinates. In this mode, additional GRIB fields should be supplied (one per level) where the values of the grid points represent the heights of their locations.
    :type vertical_coordinates: {"default", "user"}, default: "default"

    :param vertical_coordinate_param: Specifies the ecCodes paramId of the general height-based coordinates if ``vertical_coordinates`` is set to "user".
    :type vertical_coordinate_param: str

    :param w_wind_scaling_factor_mode: Specifies the representation of the vertical wind component (defined as ``w_wind_param`` ). The valid values are as follows:
		
		* "automatic": the values are scaled by a factor based on the geographical area, the top/bottom pressure levels and the size of the plot window. This option was kept to provide compatibility with earlier Metview versions.
		* "user": the values are scaled by the factor defined via parameter ``w_wind_scaling_factor``.
		* "compute": in this mode, supposing that ``w_wind_param`` defines the the pressure velocity, the vertical wind component in m/s is computed by :func:`w_from_omega`. To make it work, the input data have to be specified either on pressure levels or on model levels together with LNSP. The temperature's paramId is defined by ``t_param``. When temperature is not available, the computations will use a constant temperature  value of 273.16 K. Having computed the vertical wind component, a scaling with the factor defined by ``w_wind_scaling_factor`` is still applied to the resulting values.
    :type w_wind_scaling_factor_mode: {"automatic", "user", "compute"}, default: "automatic"

    :param w_wind_scaling_factor: Specifies the vertical wind scaling factor if ``w_wind_scaling_factor_mode`` is set to 'user" or "compute".
    :type w_wind_scaling_factor: number, default: -100

    :param level_selection_type: Specifies the method to define the output pressure levels when converting model level data to pressure levels. The possible values are:
		
		* "from_data": compute the absolute bottom pressure level from the data for each model level, compute the average pressure along the cross section line and then use this mean pressure as the vertical pressure co-ordinate for that level compute extra levels at the bottom by adding an offset (10 hPa) until it reaches the bottom pressure level, computed previously. This will avoid blank areas in the plot near the orography line.
		* "count": calculate the output pressure levels by taking into account the bottom and top pressure levels (Bottom Level and Top Level) and the given number of levels (Level Count). The computed levels will be evenly spaced on either a linear or a logarithmic scale depending on the value of ``vertical_scaling``.
		* "level_list": use the given list of pressure levels in ``level_list``
    :type level_selection_type: {"from_data", "count", "level_list"}, default: "from_data"

    :param level_list: Specifies the list of output pressure levels. Only available if ``level_selection_type`` is set to "level_list".
    :type level_list: float or list[float], default: 0.01

    :param level_count: Specifies the number of output pressure levels if ``level_selection_type`` is set to "count".
    :type level_count: number, default: 100

    :param vertical_scaling: Specifies the type of the vertical_axis.
    :type vertical_scaling: {"linear", "log"}, default: "linear"

    :param bottom_level: Specifies the lower limit of the cross section, as a pressure value (hPa) or model level number (hybrid levels). Available when "level_selection_type" is "count".
    :type bottom_level: number, default: 1100.0

    :param top_level: Specifies the upper limit of the cross section, as a pressure level (hPa) or model level number (hybrid levels). Available when "level_selection_type" is "count".
    :type top_level: number, default: 0.01

    :rtype: :class:`Netcdf`


.. minigallery:: metview.mcross_sect
    :add-heading:

