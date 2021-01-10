
mxsectview
=========================

.. container::
    
    .. container:: leftside

        .. image:: /_static/MXSECTIONVIEW.png
           :width: 48px

    .. container:: rightside

		Specifies the view for cross section plots from a suitable GRIB data source . It can also take the output from :func:`mcross_sect` as an input. In this case, a consistency check is performed between the parameters that are common to both functions.
		
		In addition to the parameters required for the cross section computation, :func:`mxsectview` specifies the axis details as well as the plot positioning in the plot frame of the display window/paper sheet and the overlay of different data units in the same plot.
		
		When using :func:`mxsectview` the generated profile data cannot be accessed. If you need to access this data use :func:`mcross_sect` instead.
		
		If an orography is plotted it can be customised by applying :func:`mgraph`.
		
		For further details on the role and usage of views in the visualisation process, please see `Anaylis Views <https://confluence.ecmwf.int/display/METV/Analysis+Views>`_.
		


		.. note:: This function performs the same task as the `Cross Section View <https://confluence.ecmwf.int/display/METV/Cross+Section+View>`_ icon in Metview’s user interface. It accepts its parameters as keyword arguments, described below.


.. py:function:: mxsectview(**kwargs)
  
    Defines the view for a vertical cross section.


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

    :param bottom_level: Specifies the lower limit of the cross section, as a pressure value (hPa) or model level number (hybrid levels).
    :type bottom_level: number, default: 1100.0

    :param top_level: Specifies the upper limit of the cross section, as a pressure level (hPa) or model level number (hybrid levels).
    :type top_level: number, default: 0.01

    :param horizontal_axis: Specifies the plotting attributes of the horizontal axis.
    :type horizontal_axis: :func:`maxis`

    :param vertical_axis: Specifies the plotting attributes of the vertical axis.
    :type vertical_axis: :func:`maxis`

    :param subpage_clipping: Clips plot to subpage borders.
    :type subpage_clipping: {"on", "off"}, default: "off"

    :param subpage_x_position: Specifies the X offset of the plot from the left side of the plot frame (any subdivision of the display area). This is expressed as a percentage of the X-dimension of the plot frame.
    :type subpage_x_position: number, default: 7.5

    :param subpage_y_position: Specifies the Y offset of the plot from the bottom side of the plot frame (any subdivision of the display area). This is expressed as a percentage of the Y-dimension of the plot frame.
    :type subpage_y_position: number, default: 7

    :param subpage_x_length: Specifies the X length of the plot. This is expressed as a percentage of the X-dimension of the plot frame. Hence the sum of this X length plus the X offset cannot exceed 100 (it is advised that it does not exceed 95 since you need some margin on the right for things like axis or map grid labels).
    :type subpage_x_length: number, default: 85

    :param subpage_y_length: Same as ``subpage_x_length`` but for the Y length of the plot.
    :type subpage_y_length: number, default: 80

    :param page_frame: Toggles the plotting of a border line around the plot frame.
    :type page_frame: {"on", "off"}, default: "off"

    :param page_frame_colour: Colour of the page frame.
    :type page_frame_colour: str, default: "charcoal"

    :param page_frame_line_style: Line style of the page frame.
    :type page_frame_line_style: {"solid", "dot", "dash", "chain_dot", "chain_dash"}, default: "solid"

    :param page_frame_thickness: Line thickness of the page frame.
    :type page_frame_thickness: int, default: 2

    :param page_id_line: Toggles the plotting of plot identification line.
    :type page_id_line: {"on", "off"}, default: "off"

    :param page_id_line_user_text: Specifies user text to be added to the plot identification line. Only available when ``page_id_line`` is "on".
    :type page_id_line_user_text: str

    :param subpage_frame: Toggles the plotting of a border line around the plot itself. In most cases you will want this to be left "on". When "off" the sides of the plot not equipped with axis will not be plotted.
    :type subpage_frame: {"on", "off"}, default: "off"

    :param subpage_frame_colour: Colour of the subpage frame.
    :type subpage_frame_colour: str, default: "black"

    :param subpage_frame_line_style: Line style of the subpage frame.
    :type subpage_frame_line_style: {"solid", "dot", "dash", "chain_dot", "chain_dash"}, default: "solid"

    :param subpage_frame_thickness: Line thickness of the subpage frame.
    :type subpage_frame_thickness: int, default: 2

    :param subpage_background_colour: Specifies the colour of the background of the plot (i.e. not affected by visual definitions like contour shadings or lines).
    :type subpage_background_colour: str, default: "white"

    :rtype: :class:`Request`


.. minigallery:: metview.mxsectview
    :add-heading:

