
thermoview
=========================

.. container::
    
    .. container:: leftside

        .. image:: /_static/THERMOVIEW.png
           :width: 48px

    .. container:: rightside

        This function performs the same task as the `Thermo View <https://confluence.ecmwf.int/display/METV/Thermo+View>`_ icon in Metview’s user interface. It accepts its parameters as keyword arguments, described below.


.. py:function:: thermoview(**kwargs)
  
    Description comes here!


    :param type: Specifies the ``type`` of the Thermodynamic diagram to be produced. Only "tephigram" is currently implemented.
    :type type: {"tephigram", "skewt", "emagram"}, default: "tephigram"


    :param bottom_pressure: Specifies the value at the bottom of the pressure axis of the thermodynamic diagram.
    :type bottom_pressure: number, default: 1015.0


    :param top_pressure: Specifies the value at the top of the pressure axis of the thermodynamic diagram.
    :type top_pressure: number, default: 100


    :param minimum_temperature: Specifies the minimum value on the temperature axis of the thermodynamic diagram.
    :type minimum_temperature: number, default: -90


    :param maximum_temperature: Specifies the maximum value on the temperature axis of the thermodynamic diagram.
    :type maximum_temperature: number, default: 50


    :param thermo_grid: Configures the background attributes of the thermodynamic diagram, please see ```thermo_grid`` <https://confluence.ecmwf.int/display/METV/Thermo+Grid>`_.
    :type thermo_grid: str


    :param point_selection: Specifies how the geographical location, for which the diagram is to be plotted, will be selected. Options are: ``"coordinates"`` , ``"area_average"`` and ``"station"``.
    :type point_selection: {"coordinates", "area_average", "station"}, default: "coordinates"


    :param coordinates: Specifies the geographical location for which the diagram is to be plotted. Enter the ``coordinates`` (lat/long) of a point separated by a "/" (lat/long). Alternatively, use the coordinate assist button. Only available if ``point_selection`` is ``coordinates``.
    :type coordinates: float or list[float], default: 0


    :param area_average: Specifies a geographical area over which an ``area_average`` value will be used, instead of a point value, to produce the diagram. Enter the ``coordinates`` (lat/long) of an area separated by a "/" (top left lat and long, bottom right lat and long). Alternatively, use the coordinate assist button. Only available if ``point_selection`` is ``area_average``.
    :type area_average: float or list[float], default: 30


    :param station: 
    :type station: str


    :param point_extraction: Specifies the way to calculate values at the point location for GRIB thermodynamic diagrams. Options are:

         "interpolate" \- "interpolate" values from the four surrounding grid points (default)

         Nearest Gridpoint \- use the data from the nearest grid point
    :type point_extraction: {"interpolate", "nearest_gridpoint"}, default: "interpolate"


    :param dew_point_formulation: Specifies the equation to compute the Dew Point parameter. Options are: Saturation Over Water and Mixed Phase 0 to -23.
    :type dew_point_formulation: {"saturation_over_water", "mixed_phase_0_to_-23"}, default: "saturation_over_water"


    :param temperature_param: Specifies the parameter number of the temperature, if the data is a non-ECMWF. ECMWF uses specific parameter numbers different from the WMO ones.
    :type temperature_param: number, default: 130


    :param specific_humidity_param: Specifies the parameter number of the specific humidity, if the data is a non- ECMWF. ECMWF uses specific parameter numbers different from the WMO ones.
    :type specific_humidity_param: number, default: 133


    :param lnsp_param: Specifies the parameter number of the Lnsp, if the data is a non-ECMWF. ECMWF uses specific parameter numbers different from the WMO ones.
    :type lnsp_param: number, default: 152


    :param u_wind_param: Specifies the parameter number of the U wind component, if the data is a non- ECMWF. ECMWF uses specific parameter numbers different from the WMO ones.
    :type u_wind_param: number, default: 131


    :param v_wind_param: Specifies the parameter number of the V wind component, if the data is a non- ECMWF. ECMWF uses specific parameter numbers different from the WMO ones.
    :type v_wind_param: number, default: 132


    :param map_overlay_control: Specifies details of the overlaying of data units in the same plot. Options are "always" (default), By Date , By Level , "never".
    :type map_overlay_control: {"always", "by_date", "by_level", "never"}, default: "always"


    :param subpage_clipping: 
    :type subpage_clipping: {"on", "off"}, default: "off"


    :param subpage_x_position: Specifies the X offset of the plot from the left side of the plot frame (any subdivision of the display area). This is expressed as a percentage of the X-dimension of the plot frame.
    :type subpage_x_position: str, default: "12"


    :param subpage_y_position: Specifies the Y offset of the plot from the bottom side of the plot frame (any subdivision of the display area). This is expressed as a percentage of the Y-dimension of the plot frame.
    :type subpage_y_position: str, default: "10"


    :param subpage_x_length: Specifies the X length of the plot. This is expressed as a percentage of the X-dimension of the plot frame. Hence the sum of this X length plus the X offset cannot exceed 100 (it is advised that it does not exceed 95 since you need some margin on the right for things like axis or map grid labels).
    :type subpage_x_length: str, default: "75"


    :param subpage_y_length: As above but for the Y length of the plot.
    :type subpage_y_length: str, default: "80"


    :param page_frame: Toggles the plotting of a border line around the plot frame "on" / "off" .
    :type page_frame: {"on", "off"}, default: "off"


    :param page_frame_colour: 
    :type page_frame_colour: str, default: "charcoal"


    :param page_frame_line_style: 
    :type page_frame_line_style: {"solid", "dot", "dash", "chain_dot", "chain_dash"}, default: "solid"


    :param page_frame_thickness: 
    :type page_frame_thickness: int, default: 2


    :param page_id_line: Toggles the plotting of plot identification line "on" / "off" .
    :type page_id_line: {"on", "off"}, default: "off"


    :param page_id_line_user_text: Specifies user text to be added to the plot identification line. Only available when ``page_id_line`` is On .
    :type page_id_line_user_text: str


    :param subpage_frame: Toggles the plotting of a border line around the plot itself "on" / "off" . In most cases you will want this to be left "on" . When "off" the sides of the plot not equipped with axis will not be plotted.
    :type subpage_frame: {"on", "off"}, default: "on"


    :param subpage_frame_colour: 
    :type subpage_frame_colour: str, default: "black"


    :param subpage_frame_line_style: 
    :type subpage_frame_line_style: {"solid", "dot", "dash", "chain_dot", "chain_dash"}, default: "solid"


    :param subpage_frame_thickness: 
    :type subpage_frame_thickness: int, default: 2


    :param subpage_background_colour: Specifies the colour of the background of the plot (i.e. not affected by visual definitions like contour shadings or lines).
    :type subpage_background_colour: str, default: "none"


    :rtype: None


.. minigallery:: metview.thermoview
    :add-heading:

