
thermoview
=========================

.. container::
    
    .. container:: leftside

        .. image:: /_static/THERMOVIEW.png
           :width: 48px

    .. container:: rightside

        This icon represents the `Thermo View <https://confluence.ecmwf.int/display/METV/Thermo+View>`_ icon in Metview's user interface.


.. py:function:: thermoview(**kwargs)
  
    Description comes here!


    :param type: Specifies the ``type`` of the Thermodynamic diagram to be produced. Only Tephigram is currently implemented.
    :type type: str


    :param bottom_pressure: Specifies the value at the bottom of the pressure axis of the thermodynamic diagram.
    :type bottom_pressure: number


    :param top_pressure: Specifies the value at the top of the pressure axis of the thermodynamic diagram.
    :type top_pressure: number


    :param minimum_temperature: Specifies the minimum value on the temperature axis of the thermodynamic diagram.
    :type minimum_temperature: number


    :param maximum_temperature: Specifies the maximum value on the temperature axis of the thermodynamic diagram.
    :type maximum_temperature: number


    :param thermo_grid: Configures the background attributes of the thermodynamic diagram, please see ```thermo_grid`` <https://confluence.ecmwf.int/display/METV/Thermo+Grid>`_.
    :type thermo_grid: str


    :param point_selection: Specifies how the geographical location, for which the diagram is to be plotted, will be selected. Options are: ``coordinates`` , ``area_average`` and ``station``.
    :type point_selection: str


    :param coordinates: Specifies the geographical location for which the diagram is to be plotted. Enter the ``coordinates`` (lat/long) of a point separated by a "/" (lat/long). Alternatively, use the coordinate assist button. Only available if ``point_selection`` is ``coordinates``.
    :type coordinates: float or list[float]


    :param area_average: Specifies a geographical area over which an ``area_average`` value will be used, instead of a point value, to produce the diagram. Enter the ``coordinates`` (lat/long) of an area separated by a "/" (top left lat and long, bottom right lat and long). Alternatively, use the coordinate assist button. Only available if ``point_selection`` is ``area_average``.
    :type area_average: float or list[float]


    :param station: 
    :type station: str


    :param point_extraction: Specifies the way to calculate values at the point location for GRIB thermodynamic diagrams. Options are:

         Interpolate \- interpolate values from the four surrounding grid points (default)

         Nearest Gridpoint \- use the data from the nearest grid point
    :type point_extraction: str


    :param dew_point_formulation: Specifies the equation to compute the Dew Point parameter. Options are: Saturation Over Water and Mixed Phase 0 to -23.
    :type dew_point_formulation: str


    :param temperature_param: Specifies the parameter number of the temperature, if the data is a non-ECMWF. ECMWF uses specific parameter numbers different from the WMO ones.
    :type temperature_param: number


    :param specific_humidity_param: Specifies the parameter number of the specific humidity, if the data is a non- ECMWF. ECMWF uses specific parameter numbers different from the WMO ones.
    :type specific_humidity_param: number


    :param lnsp_param: Specifies the parameter number of the Lnsp, if the data is a non-ECMWF. ECMWF uses specific parameter numbers different from the WMO ones.
    :type lnsp_param: number


    :param u_wind_param: Specifies the parameter number of the U wind component, if the data is a non- ECMWF. ECMWF uses specific parameter numbers different from the WMO ones.
    :type u_wind_param: number


    :param v_wind_param: Specifies the parameter number of the V wind component, if the data is a non- ECMWF. ECMWF uses specific parameter numbers different from the WMO ones.
    :type v_wind_param: number


    :param map_overlay_control: Specifies details of the overlaying of data units in the same plot. Options are Always (default), By Date , By Level , Never.
    :type map_overlay_control: str


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


    :param page_frame: Toggles the plotting of a border line around the plot frame On / Off .
    :type page_frame: str


    :param page_frame_colour: 
    :type page_frame_colour: str


    :param page_frame_line_style: 
    :type page_frame_line_style: str


    :param page_frame_thickness: 
    :type page_frame_thickness: str


    :param page_id_line: Toggles the plotting of plot identification line On / Off .
    :type page_id_line: str


    :param page_id_line_user_text: Specifies user text to be added to the plot identification line. Only available when ``page_id_line`` is On .
    :type page_id_line_user_text: str


    :param subpage_frame: Toggles the plotting of a border line around the plot itself On / Off . In most cases you will want this to be left On . When Off the sides of the plot not equipped with axis will not be plotted.
    :type subpage_frame: str


    :param subpage_frame_colour: 
    :type subpage_frame_colour: str


    :param subpage_frame_line_style: 
    :type subpage_frame_line_style: str


    :param subpage_frame_thickness: 
    :type subpage_frame_thickness: str


    :param subpage_background_colour: Specifies the colour of the background of the plot (i.e. not affected by visual definitions like contour shadings or lines).
    :type subpage_background_colour: str


    :rtype: None


.. minigallery:: metview.thermoview
    :add-heading:

