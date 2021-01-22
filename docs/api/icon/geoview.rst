
geoview
=========================

.. container::
    
    .. container:: leftside

        .. image:: /_static/GEOVIEW.png
           :width: 48px

    .. container:: rightside

		Defines a geographical view. For further details on the role and usage of views in the visualisation process, please see `Anaylis Views <https://confluence.ecmwf.int/display/METV/Analysis+Views>`_.


		.. note:: This function performs the same task as the `Geographical View <https://confluence.ecmwf.int/display/METV/Geographical+View>`_ icon in Metview’s user interface. It accepts its parameters as keyword arguments, described below.


.. py:function:: geoview(**kwargs)
  
    Defines a geographical view.


    :param coastlines: 
    :type coastlines: :func:`mcoast`

    :param area_mode: 
    :type area_mode: {"name", "user"}, default: "user"

    :param area_name: 
    :type area_name: str, default: "europe"

    :param map_projection: 
    :type map_projection: str, default: "cylindrical"

    :param map_area_definition: 
    :type map_area_definition: {"corners", "centre", "full"}, default: "full"

    :param area: 
    :type area: list[float], default: [-90, -180, 90, 180]

    :param map_hemisphere: 
    :type map_hemisphere: {"north", "south"}, default: "north"

    :param map_vertical_longitude: 
    :type map_vertical_longitude: number, default: 0

    :param map_centre_latitude: 
    :type map_centre_latitude: str, default: "45.0"

    :param map_centre_longitude: 
    :type map_centre_longitude: str, default: "0.0"

    :param map_scale: 
    :type map_scale: str, default: "130.0e4"

    :param map_projection_height: 
    :type map_projection_height: str, default: "42164000"

    :param map_projection_tilt: 
    :type map_projection_tilt: str, default: "0.0"

    :param map_projection_azimuth: 
    :type map_projection_azimuth: str, default: "20.0"

    :param map_projection_view_latitude: 
    :type map_projection_view_latitude: str, default: "20.0"

    :param map_projection_view_longitude: 
    :type map_projection_view_longitude: str, default: "-60.0"

    :param map_overlay_control: 
    :type map_overlay_control: {"always", "by_date", "by_level", "never"}, default: "always"

    :param subpage_clipping: Clips plot to subpage borders.
    :type subpage_clipping: {"on", "off"}, default: "off"

    :param subpage_x_position: Specifies the X offset of the plot from the left side of the plot frame (any subdivision of the display area). This is expressed as a percentage of the X-dimension of the plot frame.
    :type subpage_x_position: number, default: 7.5

    :param subpage_y_position: Specifies the Y offset of the plot from the bottom side of the plot frame (any subdivision of the display area). This is expressed as a percentage of the Y-dimension of the plot frame.
    :type subpage_y_position: number, default: 5

    :param subpage_x_length: Specifies the X length of the plot. This is expressed as a percentage of the X-dimension of the plot frame. Hence the sum of this X length plus the X offset cannot exceed 100 (it is advised that it does not exceed 95 since you need some margin on the right for things like axis or map grid labels).
    :type subpage_x_length: number, default: 85

    :param subpage_y_length: Same as ``subpage_x_length`` but for the Y length of the plot.
    :type subpage_y_length: number, default: 85

    :param subpage_metadata_info: 
    :type subpage_metadata_info: {"on", "off"}, default: "off"

    :param subpage_metadata_javascript_path: 
    :type subpage_metadata_javascript_path: str, default: "map.js"

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
.. include:: /gallery/backref/geoview.rst