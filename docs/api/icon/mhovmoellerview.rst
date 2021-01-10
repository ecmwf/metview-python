
mhovmoellerview
=========================

.. container::
    
    .. container:: leftside

        .. image:: /_static/MHOVMOELLERVIEW.png
           :width: 48px

    .. container:: rightside

		Defines the **view** for Hovmoeller diagram plots from a suitable GRIB data source. It can also take the output from a hovmoeller data object as an input. In this case, a consistency check is performed between the parameters that are common to both functions.
		
		In addition to the parameters required for the Hovmoeller diagram computation, :func:`mhovmoellerview` specifies the axis details as well as the plot positioning in the plot frame of the display window/paper sheet and the overlay of different data units in the same plot.
		
		To access the computed output values use a hovmoeller data object.
		
		For further details on the role and usage of views in the visualisation process, please see `Anaylis Views <https://confluence.ecmwf.int/display/METV/Analysis+Views>`_.
		  


		.. note:: This function performs the same task as the `Hovmoeller View <https://confluence.ecmwf.int/display/METV/Hovmoeller+View>`_ icon in Metview’s user interface. It accepts its parameters as keyword arguments, described below.


.. py:function:: mhovmoellerview(**kwargs)
  
    Defines the view for Hovmoeller diagram plots.


    :param type: Specifies the type of the Hovmoeller diagram to be produced. Options are:
		
		* "area_hovm": diagram derived from an input rectangular area
		* "line_hovm": diagram derived from an input transect line.
		* "vertical_hovm": diagram derived from an input rectangular area and a set of levels.
    :type type: {"line_hovm", "area_hovm", "vertical_hovm"}, default: "line_hovm"

    :param line: Specifies the coordinates of a transect line along which the Hovmoeller diagram is calculated in [lat1, lon1, lat2, lon2] format. Enabled when ``type`` is "line_hovm".
    :type line: list[float], default: [0, -180, 0, 180]

    :param area: Specifies the coordinates of the area (as [north, west, south, east]) over which the Hovmoeller diagram is calculated. Enabled when ``type`` is "area_hovm" or "vertical_hovm".
    :type area: list[float], default: [30, -30, -30, 30]

    :param average_direction: Specifies the direction along which the averaging is performed. Options are "north_south" and "east_west". For "north_south" the averaging is weighted by the cosine of the latitudes.
    :type average_direction: {"east_west", "north_south"}, default: "east_west"

    :param time_axis_mode: Specifies the direction of the date/time axis. The options are as follows:
		
		* "user": left/bottom date is taken from ``date_min`` and the right/top date is taken from ``date_max``.
		* "automatic_forwards": date limits are taken from the data and plotted left to right or bottom to top.
		* "automatic_backwards": date limits are taken from the data and plotted right to left or top to bottom. This option has the same effect as "user" with default ``date_min`` and ``date_max``.
    :type time_axis_mode: {"automatic_forwards", "automatic_backwards", "user"}, default: "user"

    :param date_min: Specifies the horizontal date minimum value. Default value "automatic" indicates that the minimum value will be taken from the input data.
    :type date_min: str, default: "automatic"

    :param date_max: Specifies the horizontal date maximum value. Default value "automatic" indicates that the maximum value will be taken from the input data.
    :type date_max: str, default: "automatic"

    :param bottom_level: Specifies the vertical lower limit value, as a pressure level (hPa) or ECMWF model level.
    :type bottom_level: number, default: 1015.0

    :param top_level: Specifies the vertical upper limit value, as a pressure level (hPa) or ECMWF model level.
    :type top_level: number, default: 0.01

    :param swap_axes: By default, the definition of the vertical and horizontal axes of the Hovmoeller diagrams follows pre-defined rules. However, if ``swap_axes`` is set to "yes" then the axes will be swapped around.
    :type swap_axes: {"no", "yes"}, default: "no"

    :param resolution: Used to interpolate the data onto a regular grid, and applies to both the horizontal and vertical axes where appropriate. This parameter is essential for creating a Hovmoeller diagram from satellite data.
    :type resolution: number, default: 1.0

    :param time_axis: Specifies the characteristics of the time-series axis as an :func:`maxis` object to be used in the plotting of the data. The following :func:`maxis` parameters are defined by the application; therefore, users should not change their values directly: ``axis_type`` (set to "date"), ``axis_date_min_value`` and ``axis_date_max_value`` (set according to ``date_min`` and ``date_max``, respectively), and ``axis_orientation``. The ``axis_orientation`` parameter is defined according to the following rules:
		         
		* if the selected input pane is "line_hovm", the value is set to "horizontal".
		* if the selected input pane is "area_hovm" and `average_direction`` is "east_west", the value is set to "horizontal".
		* if the selected input pane is "area_hovm" and ``average_direction`` is "north_south", the value is set to "vertical".
		* if the selected input pane is "vertical_hovm", the value is set to "horizontal".
		However, it is possible to change ``axis_orientation`` value from its calculated default by setting ``swap_axes`` to "yes". This option is not available for "vertical_hovm".
    :type time_axis: :func:`maxis`

    :param geo_axis: Specifies the characteristics of the geographical axis as an :func:`maxis` object to be used in the plotting of the data. The following :func:`maxis` parameters are defined by the application; therefore, users should not change their values directly: ``axis_min_value`` and ``axis_max_value`` (set according to ``line`` or ``area`` ), ``axis_type``, ``axis_tick_label_type`` and ``axis_orientation``. The ``axis_type`` and ``axis_tick_label_type`` parameters are defined according to the following rules:
		
		* if the selected input pane is "line_hovm", ``axis_type`` is set to "geoline".
		* if the selected input pane is "area_hovm" and ``average_direction`` is "east_west", ``axis_type`` is set to "regular" and "axis_tick_label_type`` to "latitude".
		* if the selected input pane is "area_hovm" and ``average_direction`` is "north_south", ``axis_type`` is set to "regular" and ``axis_tick_label_type`` to "longitude".
		Moreover, ``axis_orientation`` parameter is defined according to the following rules:
		
		* if the selected input pane is "line_hovm", the value is set to "vertical".
		* if the selected input pane is "area_hovm" and ``average_direction`` is "east_west", the value is set to "vertical".
		* if the selected input pane is "area_hovm" and ``average_direction`` is "north_south" the value is set to "horizontal"
		However, it is possible to change the ``axis_orientation`` from its calculated default by setting ``swap_axes`` to "Yes".
    :type geo_axis: :func:`maxis`

    :param vertical_axis: Specifies the characteristics of the level-series axis to be used in the plotting of the data. The following :func:`maxis` parameters are defined by the application; therefore, users should  not change their values directly: ``axis_min_value`` and ``axis_max_value`` (set according to the input data set), ``axis_type``, ``axis_tick_label_type`` and ``axis_orientation``.
    :type vertical_axis: :func:`maxis`

    :param vertical_level_type: Specifies if a conversion from model level to pressure level needs to be performed. If it is "pressure" and the input data is specified on ECMWF model levels, the Logarithm of Surface Pressure (LNSP) field should be added to the input data.
    :type vertical_level_type: {"as_in_data", "pressure"}, default: "as_in_data"

    :param vertical_scaling: Specifies the type of the vertical axis .
    :type vertical_scaling: {"linear", "log"}, default: "linear"

    :param subpage_clipping: Clips plot to subpage borders.
    :type subpage_clipping: {"on", "off"}, default: "off"

    :param subpage_x_position: Specifies the X offset of the plot from the left side of the plot frame (any subdivision of the display area). This is expressed as a percentage of the X-dimension of the plot frame.
    :type subpage_x_position: number, default: 12

    :param subpage_y_position: Specifies the Y offset of the plot from the bottom side of the plot frame (any subdivision of the display area). This is expressed as a percentage of the Y-dimension of the plot frame.
    :type subpage_y_position: number, default: 10

    :param subpage_x_length: Specifies the X length of the plot. This is expressed as a percentage of the X-dimension of the plot frame. Hence the sum of this X length plus the X offset cannot exceed 100 (it is advised that it does not exceed 95 since you need some margin on the right for things like axis or map grid labels).
    :type subpage_x_length: number, default: 75

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


.. minigallery:: metview.mhovmoellerview
    :add-heading:

