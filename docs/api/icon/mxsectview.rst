
mxsectview
=========================

.. container::
    
    .. container:: leftside

        .. image:: /_static/MXSECTIONVIEW.png
           :width: 48px

    .. container:: rightside

        This icon represents the `Cross Section View <https://confluence.ecmwf.int/display/METV/Cross+Section+View>`_ icon in Metview's user interface.


.. py:function:: mxsectview(**kwargs)
  
    Description comes here!


    :param bottom_level: Specifies the lower limit of the cross section, as a pressure level (hPa) or model level (η levels).
    :type bottom_level: number


    :param top_level: Specifies the upper limit of the cross section, as a pressure level (hPa) or model level (η levels).
    :type top_level: number


    :param line: 
    :type line: float or list[float]


    :param wind_parallel: When this option is On , the wind components are projected onto the cross section plane. For 2D wind the result is a signed scalar data (a contour plot). When 3D wind data are available a vector plot is produced with the vertical component scaled/computed as specified in parameter ``w_wind_scaling_factor_mode``. Valid values are On / Off.
    :type wind_parallel: str


    :param wind_perpendicular: When this option is On , the wind components are projected onto the normal vector of the cross section plane. The result is a signed scalar data (a contour plot). Valid values are On / Off. This cannot be set to On if ``wind_parallel`` is also On.
    :type wind_perpendicular: str


    :param wind_intensity: When this option is On the result depends on other settings:

         * When both ``wind_parallel`` and ``wind_perpendicular`` are Off , the result is the length of the 2D/3D wind vector at the cross section plane
         * When ``wind_parallel`` is On , the result is the absolute value of the projected wind onto the cross section plane
         * When ``wind_perpendicular`` is On , the result is the absolute value of the wind projected onto the normal vector of the cross section plane

         Valid values are On / Off.
    :type wind_intensity: str


    :param lnsp_param: Specifies the ecCodes paramId of the LNSP data. The default value is 152 (as used by ECMWF).
    :type lnsp_param: number


    :param u_wind_param: Specifies the ecCodes paramId of the U wind component data. The default value is 131 (as used by ECMWF).
    :type u_wind_param: number


    :param v_wind_param: Specifies the ecCodes paramId of the V wind component data. The default value is 132 (as used by ECMWF).
    :type v_wind_param: number


    :param w_wind_param: Specifies the ecCodes paramId of the vertical wind component data. The default value is 135 i.e. pressure velocity (as used by ECMWF).
    :type w_wind_param: number


    :param t_param: Specifies the ecCodes paramId of the temperature data used in the vertical wind computations when ``w_wind_scaling_factor_mode`` is set to Compute. The default value is 130 (as used by ECMWF).
    :type t_param: number


    :param horizontal_point_mode: Specifies how the geographical points along the input transect ``line`` will be computed. Valid values are Interpolate and Nearest Gridpoint. Setting this option to Interpolate will create a regular set of interpolated geographical points along the transect ``line``. Setting this option to Nearest Gridpoint will instead select the nearest points from the data.
    :type horizontal_point_mode: str


    :param vertical_coordinates: Setting this option to User will enable the use of general height-based coordinates. In this mode, additional GRIB fields should be supplied (one per level) where the values of the grid points represent the heights of their locations. Valid values are Default and _User.The default value is Default.
    :type vertical_coordinates: str


    :param vertical_coordinate_param: Specifies the ecCodes paramId of the general height-based coordinates if ``vertical_coordinates`` is set to User.
    :type vertical_coordinate_param: str


    :param w_wind_scaling_factor_mode: Specifies the representation of the vertical wind component (defined as ``w_wind_param`` ). The valid values are as follows:

         *  Automatic : the values are scaled by a factor based on the geographical area, the top/bottom pressure levels and the size of the plot window.
         *  User : the values are scaled by the factor defined via parameter ``w_wind_scaling_factor``.
         *  Compute : in this mode, supposing that ``w_wind_param`` defines the the pressure velocity , the vertical wind component in m/s is computed using the following hydrostatic formula:

         \\[ w = - \frac{\omega R T}{p g} \\]

         where:

         * ω: pressure velocity (Pa/s)
         * p : pressure on (Pa)
         * T: temperature (K)
         * R: gas constant, 287.058 J kg-1 K-1
         * g: gravitational acceleration, 9.81 m/s2

         To make this formula work, the input data have to be specified either on pressure levels or on model levels together with LNSP. The temperature's paramId is defined by ``t_param``. When temperature is not available, the computations still work but T is replaced by a constant 273.16 K value in the formula. Having computed the vertical wind component, a scaling with the factor defined by ``w_wind_scaling_factor`` is still applied to the resulting values.

         The default value is Automatic.
    :type w_wind_scaling_factor_mode: str


    :param w_wind_scaling_factor: Specifies the vertical wind scaling factor if ``w_wind_scaling_factor_mode`` is set to User or Compute. The default value is -100.
    :type w_wind_scaling_factor: number


    :param level_selection_type: 
    :type level_selection_type: str


    :param level_list: Specifies the list of output pressure levels. Only available if ``level_selection_type`` is set to ``level_list``.
    :type level_list: float or list[float]


    :param level_count: Specifies the number of output pressure levels if ``level_selection_type`` is set to Count.
    :type level_count: number


    :param vertical_scaling: Specifies the type of ``vertical_axis`` - ``line``ar or Logarithmic.
    :type vertical_scaling: str


    :param horizontal_axis: Specifies the plotting attributes of the ``horizontal_axis``. An :func:`maxis` icon can be dropped here.
    :type horizontal_axis: str


    :param vertical_axis: Specifies the plotting attributes of the ``vertical_axis``. An :func:`maxis` icon can be dropped here.
    :type vertical_axis: str


    :param subpage_clipping: 
    :type subpage_clipping: str


    :param subpage_x_position: Specifies the X offset of the plot from the left side of the plot frame (any subdivision of the display area). This is expressed as a percentage of the X-dimension of the plot frame.
    :type subpage_x_position: str


    :param subpage_y_position: Specifies the Y offset of the plot from the bottom side of the plot frame (any subdivision of the display area). This is expressed as a percentage of the Y-dimension of the plot frame.
    :type subpage_y_position: str


    :param subpage_x_length: Specifies the X length of the plot. This is expressed as a percentage of the X-dimension of the plot frame. Hence the sum of this X length plus the X offset cannot exceed 100 (it is advised that it does not exceed 95 since you need some margin on the right for things like axis or map grid labels).
    :type subpage_x_length: str


    :param subpage_y_length: As above but for the Y length of the plot.
    :type subpage_y_length: str


    :param page_frame: Toggles the plotting of a border ``line`` around the plot frame On / Off .
    :type page_frame: str


    :param page_frame_colour: 
    :type page_frame_colour: str


    :param page_frame_line_style: 
    :type page_frame_line_style: str


    :param page_frame_thickness: 
    :type page_frame_thickness: str


    :param page_id_line: Toggles the plotting of plot identification ``line`` On / Off .
    :type page_id_line: str


    :param page_id_line_user_text: Specifies user text to be added to the plot identification ``line``. Only available when Page Id ``line`` is On .
    :type page_id_line_user_text: str


    :param subpage_frame: Toggles the plotting of a border ``line`` around the plot itself On / Off . In most cases you will want this to be left On . When Off the sides of the plot not equipped with axis will not be plotted.
    :type subpage_frame: str


    :param subpage_frame_colour: 
    :type subpage_frame_colour: str


    :param subpage_frame_line_style: 
    :type subpage_frame_line_style: str


    :param subpage_frame_thickness: 
    :type subpage_frame_thickness: str


    :param subpage_background_colour: Specifies the colour of the background of the plot (i.e. not affected by visual definitions like contour shadings or ``line``s).
    :type subpage_background_colour: str


    :rtype: None


.. minigallery:: metview.mxsectview
    :add-heading:

