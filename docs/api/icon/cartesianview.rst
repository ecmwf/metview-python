
cartesianview
=========================

.. container::
    
    .. container:: leftside

        .. image:: /_static/CARTESIANVIEW.png
           :width: 48px

    .. container:: rightside

        This function performs the same task as the `Cartesian View <https://confluence.ecmwf.int/display/METV/Cartesian+View>`_ icon in Metview’s user interface. It accepts its parameters as keyword arguments, described below.


.. py:function:: cartesianview(**kwargs)
  
    Description comes here!


    :param map_projection: 
    :type map_projection: {"cartesian", "tephigram", "skewt", "emagram", "taylor"}, default: "cartesian"


    :param x_automatic: Determines whether the x-coordinate system should be defined automatically based "on" the first data to be plotted in the view; if so, the axis will range, left to right, from the minimum to the maximum value in the data. If not, the minimum and maximum values should be specified.
    :type x_automatic: {"on", "off"}, default: "off"


    :param x_axis_type: Determines the type of coordinates on this axis:

         *  "regular" : the values are real-valued numbers
         *  "date" : the values are dates. When invoked from a macro, these can be supplied as "date" variables; when typing dates into the icon editor, use the Magics notation for writing dates
         *  "logarithmic" : the values are real-valued numbers, but the axis will be displayed on a "logarithmic" scale
         *  "geoline" : the axis limits should be provided as geographical coordinates; this can be used for displaying cross sections, or other plots where an axis represents a geographical line
    :type x_axis_type: {"regular", "date", "logarithmic", "geoline"}, default: "regular"


    :param x_min: The leftmost value of the x axis, this parameter is only used if the axis type is set to Regular or Logarithmic.
    :type x_min: number, default: 0


    :param x_max: The rightmost value of the x axis, this parameter is only used if the axis type is set to Regular or Logarithmic.
    :type x_max: number, default: 100


    :param x_min_latitude: The leftmost latitude value of the x axis, this parameter is only used if the axis type is set to Geoline.
    :type x_min_latitude: number, default: -90


    :param x_max_latitude: The rightmost latitude value of the x axis, this parameter is only used if the axis type is set to Geoline.
    :type x_max_latitude: number, default: 90


    :param x_min_longitude: The leftmost longitude value of the x axis, this parameter is only used if the axis type is set to Geoline.
    :type x_min_longitude: number, default: -180


    :param x_max_longitude: The rightmost longitude value of the x axis, this parameter is only used if the axis type is set to Geoline.
    :type x_max_longitude: number, default: 180


    :param x_date_min: The leftmost date value of the x axis, this parameter is only used if the axis type is set to Date.
    :type x_date_min: str, default: "2011-01-01"


    :param x_date_max: The rightmost date value of the x axis, this parameter is only used if the axis type is set to Date.
    :type x_date_max: str, default: "2011-01-31"


    :param x_automatic_reverse: 
    :type x_automatic_reverse: {"on", "off"}, default: "off"


    :param y_automatic: 
    :type y_automatic: {"on", "off"}, default: "off"


    :param y_axis_type: Determines the type of coordinates on this axis:

         *  "regular" : the values are real-valued numbers
         *  "date" : the values are dates. When invoked from a macro, these can be supplied as "date" variables; when typing dates into the icon editor, use the Magics notation for writing dates
         *  "logarithmic" : the values are real-valued numbers, but the axis will be displayed on a "logarithmic" scale
         *  "geoline" : the axis limits should be provided as geographical coordinates; this can be used for displaying cross sections, or other plots where an axis represents a geographical line
    :type y_axis_type: {"regular", "date", "logarithmic", "geoline"}, default: "regular"


    :param y_min: The bottom value of the y axis, this parameter is only used if the axis type is set to Regular or Logarithmic.
    :type y_min: number, default: 0


    :param y_max: The uppermost value of the y axis, this parameter is only used if the axis type is set to Regular or Logarithmic.
    :type y_max: number, default: 100


    :param y_min_latitude: The bottom latitude value of the y axis, this parameter is only used if the axis type is set to Geoline.
    :type y_min_latitude: number, default: -90


    :param y_max_latitude: The uppermost latitude value of the y axis, this parameter is only used if the axis type is set to Geoline.
    :type y_max_latitude: number, default: 90


    :param y_min_longitude: The bottom longitude value of the y axis, this parameter is only used if the axis type is set to Geoline.
    :type y_min_longitude: number, default: -180


    :param y_max_longitude: The uppermost longitude value of the x axis, this parameter is only used if the axis type is set to Geoline.
    :type y_max_longitude: number, default: 180


    :param y_date_min: The bottom date value of the y axis, this parameter is only used if the axis type is set to Date.
    :type y_date_min: str, default: "2011-01-01"


    :param y_date_max: The uppermost date value of the y axis, this parameter is only used if the axis type is set to Date.
    :type y_date_max: str, default: "2011-01-31"


    :param y_automatic_reverse: 
    :type y_automatic_reverse: {"on", "off"}, default: "off"


    :param horizontal_axis: Specifies the plotting attributes of the ``horizontal_axis``. An :func:`maxis` icon can be dropped here.
    :type horizontal_axis: str


    :param vertical_axis: Specifies the plotting attributes of the ``vertical_axis``. An :func:`maxis` icon can be dropped here.
    :type vertical_axis: str


    :param taylor_grid: 
    :type taylor_grid: str


    :param subpage_clipping: 
    :type subpage_clipping: {"on", "off"}, default: "off"


    :param subpage_x_position: Specifies the X offset of the plot from the left side of the plot frame (any subdivision of the display area). This is expressed as a percentage of the X-dimension of the plot frame.
    :type subpage_x_position: str, default: "7.5"


    :param subpage_y_position: Specifies the Y offset of the plot from the bottom side of the plot frame (any subdivision of the display area). This is expressed as a percentage of the Y-dimension of the plot frame.
    :type subpage_y_position: str, default: "7"


    :param subpage_x_length: Specifies the X length of the plot. This is expressed as a percentage of the X-dimension of the plot frame. Hence the sum of this X length plus the X offset cannot exceed 100 (it is advised that it does not exceed 95 since you need some margin on the right for things like axis or map grid labels).
    :type subpage_x_length: str, default: "85"


    :param subpage_y_length: As above but for the Y length of the plot.
    :type subpage_y_length: str, default: "80"


    :param subpage_vertical_axis_width: 
    :type subpage_vertical_axis_width: str, default: "1"


    :param subpage_horizontal_axis_height: 
    :type subpage_horizontal_axis_height: str, default: "1"


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


.. minigallery:: metview.cartesianview
    :add-heading:

