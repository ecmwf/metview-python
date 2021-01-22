
maverageview
=========================

.. container::
    
    .. container:: leftside

        .. image:: /_static/MXAVERAGEVIEW.png
           :width: 48px

    .. container:: rightside

		Defines the **view** for average (zonal or meridional) cross-section plots from a suitable GRIB data source. It can also take the output from :func:`mxs_average` as an input. In this case, a consistency check is performed between the parameters that are common to both functions.
		
		In addition to the parameters required for the average cross section computation, :func:`maverageview` specifies the axis details as well as the plot positioning in the plot frame of the display window / paper sheet.
		
		For further details on the role and usage of views in the visualisation process, please see `Anaylis Views <https://confluence.ecmwf.int/display/METV/Analysis+Views>`_.
		


		.. note:: This function performs the same task as the `Average View <https://confluence.ecmwf.int/display/METV/Average+View>`_ icon in Metview’s user interface. It accepts its parameters as keyword arguments, described below.


.. py:function:: maverageview(**kwargs)
  
    Defines the view for average (zonal or meridional) cross-section plots.


    :param bottom_level: Specifies the lower limit of the average cross section, as a pressure value (hPa) or ECMWF model level number (hybrid levels).
    :type bottom_level: number, default: 1015.0

    :param top_level: Specifies the upper limit of the average cross section, as a pressure value (hPa) or ECMWF model level number (hybrid levels).
    :type top_level: number, default: 0.01

    :param vertical_scaling: Specifies the type of the vertical axis.
    :type vertical_scaling: {"linear", "log"}, default: "linear"

    :param area: Specifies the coordinates of the area (as [north, west, south, east]) over which the averages cross section is calculated.
    :type area: list[float], default: [90, -180, -90, 180]

    :param direction: Specifies the direction along which the averaging is performed. Options are "ns" (north-south) and "ew" (east-west). For "ns" the averaging is weighted by the cosine of the latitudes.
    :type direction: {"ns", "ew"}, default: "ns"

    :param horizontal_axis: Specifies the plotting attributes of the horizontal axis.
    :type horizontal_axis: :func:`maxis`

    :param vertical_axis: Specifies the plotting attributes of the vertical axis.
    :type vertical_axis: :func:`maxis`

    :param subpage_clipping: Clips plot to subpage borders.
    :type subpage_clipping: {"on", "off"}, default: "off"

    :param subpage_x_position: Specifies the X offset of the plot from the left side of the plot frame (any subdivision of the display area). This is expressed as a percentage of the X-dimension of the plot frame.
    :type subpage_x_position: number, default: 0

    :param subpage_y_position: Specifies the Y offset of the plot from the bottom side of the plot frame (any subdivision of the display area). This is expressed as a percentage of the Y-dimension of the plot frame.
    :type subpage_y_position: number, default: 0

    :param subpage_x_length: Specifies the X length of the plot. This is expressed as a percentage of the X-dimension of the plot frame. Hence the sum of this X length plus the X offset cannot exceed 100 (it is advised that it does not exceed 95 since you need some margin on the right for things like axis or map grid labels).
    :type subpage_x_length: number, default: 100

    :param subpage_y_length: Same as ``subpage_x_length`` but for the Y length of the plot.
    :type subpage_y_length: number, default: 100

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
.. include:: /gallery/backref/maverageview.rst