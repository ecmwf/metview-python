
annotationview
=========================

.. container::
    
    .. container:: leftside

        .. image:: /_static/ANNOTATIONVIEW.png
           :width: 48px

    .. container:: rightside

        This icon represents the `Annotation View <https://confluence.ecmwf.int/display/METV/Annotation+View>`_ icon in Metview's user interface.


.. py:function:: annotationview(**kwargs)
  
    Description comes here!


    :param subpage_clipping: 
    :type subpage_clipping: str


    :param subpage_x_position: Specifies the X offset of the plot from the left side of the plot frame (any subdivision of the display area). This is expressed as a percentage of the X-dimension of the plot frame.
    :type subpage_x_position: number


    :param subpage_y_position: Specifies the Y offset of the plot from the bottom side of the plot frame (any subdivision of the display area). This is expressed as a percentage of the Y-dimension of the plot frame.
    :type subpage_y_position: number


    :param subpage_x_length: Specifies the X length of the plot. This is expressed as a percentage of the X-dimension of the plot frame. Hence the sum of this X length plus the X offset cannot exceed 100 (it is advised that it does not exceed 95 since you need some margin on the right for things like axis or map grid labels).
    :type subpage_x_length: number


    :param subpage_y_length: As above but for the Y length of the plot.
    :type subpage_y_length: number


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


.. minigallery:: metview.annotationview
    :add-heading:

