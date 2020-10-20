
cartesianview
=========================

.. container::
    
    .. container:: leftside

        .. image:: /_static/CARTESIANVIEW.png
           :width: 48px

    .. container:: rightside

        This icon represents the `Cartesian View <https://confluence.ecmwf.int/display/METV/Cartesian+View>`_ icon in Metview's user interface.


.. py:function:: cartesianview(**kwargs)
  
    Description comes here!


    :param map_projection: 
    :type map_projection: str


    :param x_automatic: Determines whether the x-coordinate system should be defined automatically based on the first data to be plotted in the view; if so, the axis will range, left to right, from the minimum to the maximum value in the data. If not, the minimum and maximum values should be specified.
    :type x_automatic: str


    :param x_axis_type: Determines the type of coordinates on this axis:

         *  Regular : the values are real-valued numbers
         *  Date : the values are dates. When invoked from a macro, these can be supplied as date variables; when typing dates into the icon editor, use the Magics notation for writing dates
         *  Logarithmic : the values are real-valued numbers, but the axis will be displayed on a logarithmic scale
         *  Geoline : the axis limits should be provided as geographical coordinates; this can be used for displaying cross sections, or other plots where an axis represents a geographical line
    :type x_axis_type: str


    :param x_min: The leftmost value of the x axis, this parameter is only used if the axis type is set to Regular or Logarithmic.
    :type x_min: number


    :param x_max: The rightmost value of the x axis, this parameter is only used if the axis type is set to Regular or Logarithmic.
    :type x_max: number


    :param x_min_latitude: The leftmost latitude value of the x axis, this parameter is only used if the axis type is set to Geoline.
    :type x_min_latitude: number


    :param x_max_latitude: The rightmost latitude value of the x axis, this parameter is only used if the axis type is set to Geoline.
    :type x_max_latitude: number


    :param x_min_longitude: The leftmost longitude value of the x axis, this parameter is only used if the axis type is set to Geoline.
    :type x_min_longitude: number


    :param x_max_longitude: The rightmost longitude value of the x axis, this parameter is only used if the axis type is set to Geoline.
    :type x_max_longitude: number


    :param x_date_min: The leftmost date value of the x axis, this parameter is only used if the axis type is set to Date.
    :type x_date_min: str


    :param x_date_max: The rightmost date value of the x axis, this parameter is only used if the axis type is set to Date.
    :type x_date_max: str


    :param x_automatic_reverse: 
    :type x_automatic_reverse: str


    :param y_automatic: 
    :type y_automatic: str


    :param y_axis_type: Determines the type of coordinates on this axis:

         *  Regular : the values are real-valued numbers
         *  Date : the values are dates. When invoked from a macro, these can be supplied as date variables; when typing dates into the icon editor, use the Magics notation for writing dates
         *  Logarithmic : the values are real-valued numbers, but the axis will be displayed on a logarithmic scale
         *  Geoline : the axis limits should be provided as geographical coordinates; this can be used for displaying cross sections, or other plots where an axis represents a geographical line
    :type y_axis_type: str


    :param y_min: The bottom value of the y axis, this parameter is only used if the axis type is set to Regular or Logarithmic.
    :type y_min: number


    :param y_max: The uppermost value of the y axis, this parameter is only used if the axis type is set to Regular or Logarithmic.
    :type y_max: number


    :param y_min_latitude: The bottom latitude value of the y axis, this parameter is only used if the axis type is set to Geoline.
    :type y_min_latitude: number


    :param y_max_latitude: The uppermost latitude value of the y axis, this parameter is only used if the axis type is set to Geoline.
    :type y_max_latitude: number


    :param y_min_longitude: The bottom longitude value of the y axis, this parameter is only used if the axis type is set to Geoline.
    :type y_min_longitude: number


    :param y_max_longitude: The uppermost longitude value of the x axis, this parameter is only used if the axis type is set to Geoline.
    :type y_max_longitude: number


    :param y_date_min: The bottom date value of the y axis, this parameter is only used if the axis type is set to Date.
    :type y_date_min: str


    :param y_date_max: The uppermost date value of the y axis, this parameter is only used if the axis type is set to Date.
    :type y_date_max: str


    :param y_automatic_reverse: 
    :type y_automatic_reverse: str


    :param horizontal_axis: Specifies the plotting attributes of the ``horizontal_axis``. An :func:`maxis` icon can be dropped here.
    :type horizontal_axis: str


    :param vertical_axis: Specifies the plotting attributes of the ``vertical_axis``. An :func:`maxis` icon can be dropped here.
    :type vertical_axis: str


    :param taylor_grid: 
    :type taylor_grid: str


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


    :param subpage_vertical_axis_width: 
    :type subpage_vertical_axis_width: str


    :param subpage_horizontal_axis_height: 
    :type subpage_horizontal_axis_height: str


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


.. minigallery:: metview.cartesianview
    :add-heading:

