
maverageview
=========================

.. container::
    
    .. container:: leftside

        .. image:: /_static/MXAVERAGEVIEW.png
           :width: 48px

    .. container:: rightside

        This function performs the same task as the `Average View <https://confluence.ecmwf.int/display/METV/Average+View>`_ icon in Metview’s user interface. It accepts its parameters as keyword arguments, described below.


.. py:function:: maverageview(**kwargs)
  
    Description comes here!


    :param bottom_level: Specifies the lower limit of the average cross section, as a pressure level (hPa) or model level (η levels).
    :type bottom_level: number, default: 1015.0


    :param top_level: Specifies the upper limit of the average cross section, as a pressure level (hPa) or model level (η levels).
    :type top_level: number, default: 0.01


    :param vertical_scaling: Specifies the type of ``vertical_axis`` - "linear" or Logarithmic.
    :type vertical_scaling: {"linear", "log"}, default: "linear"


    :param area: 
    :type area: float or list[float], default: 90


    :param direction: Specifies the ``direction`` along which the averaging of the variable is performed. Options are North South and East West. For North South, the averaging is weighted by cos(latitude).
    :type direction: {"ns", "ew"}, default: "ns"


    :param horizontal_axis: Specifies the plotting attributes of the ``horizontal_axis``. An :func:`maxis` icon can be dropped here.
    :type horizontal_axis: str


    :param vertical_axis: Specifies the plotting attributes of the ``vertical_axis``. An :func:`maxis` icon can be dropped here.
    :type vertical_axis: str


    :param subpage_clipping: 
    :type subpage_clipping: {"on", "off"}, default: "off"


    :param subpage_x_position: Specifies the X offset of the plot from the left side of the plot frame (any subdivision of the display ``area``). This is expressed as a percentage of the X-dimension of the plot frame.
    :type subpage_x_position: str, default: "7.5"


    :param subpage_y_position: Specifies the Y offset of the plot from the bottom side of the plot frame (any subdivision of the display ``area``). This is expressed as a percentage of the Y-dimension of the plot frame.
    :type subpage_y_position: str, default: "7"


    :param subpage_x_length: Specifies the X length of the plot. This is expressed as a percentage of the X-dimension of the plot frame. Hence the sum of this X length plus the X offset cannot exceed 100 (it is advised that it does not exceed 95 since you need some margin on the right for things like axis or map grid labels).
    :type subpage_x_length: str, default: "85"


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


.. minigallery:: metview.maverageview
    :add-heading:

