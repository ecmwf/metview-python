
mhovmoellerview
=========================

.. container::
    
    .. container:: leftside

        .. image:: /_static/MHOVMOELLERVIEW.png
           :width: 48px

    .. container:: rightside

        This function performs the same task as the `Mhovmoellerview <https://confluence.ecmwf.int/display/METV/mhovmoellerview>`_ icon in Metview’s user interface. It accepts its parameters as keyword arguments, described below.


.. py:function:: mhovmoellerview(**kwargs)
  
    Description comes here!


    :param type: 
    :type type: {"line_hovm", "area_hovm", "vertical_hovm"}, default: "line_hovm"


    :param line: 
    :type line: float or list[float], default: 0


    :param area: 
    :type area: float or list[float], default: 30


    :param average_direction: 
    :type average_direction: {"east_west", "north_south"}, default: "east_west"


    :param time_axis_mode: 
    :type time_axis_mode: {"automatic_forwards", "automatic_backwards", "user"}, default: "user"


    :param date_min: 
    :type date_min: str, default: "automatic"


    :param date_max: 
    :type date_max: str, default: "automatic"


    :param bottom_level: 
    :type bottom_level: number, default: 1015.0


    :param top_level: 
    :type top_level: number, default: 0.01


    :param swap_axes: 
    :type swap_axes: {"no", "yes"}, default: "no"


    :param resolution: 
    :type resolution: number, default: 1.0


    :param time_axis: 
    :type time_axis: str


    :param geo_axis: 
    :type geo_axis: str


    :param vertical_axis: 
    :type vertical_axis: str


    :param vertical_level_type: 
    :type vertical_level_type: {"as_in_data", "pressure"}, default: "as_in_data"


    :param vertical_scaling: 
    :type vertical_scaling: {"linear", "log"}, default: "linear"


    :param subpage_clipping: 
    :type subpage_clipping: {"on", "off"}, default: "off"


    :param subpage_x_position: 
    :type subpage_x_position: str, default: "12"


    :param subpage_y_position: 
    :type subpage_y_position: str, default: "10"


    :param subpage_x_length: 
    :type subpage_x_length: str, default: "75"


    :param subpage_y_length: 
    :type subpage_y_length: str, default: "80"


    :param page_frame: 
    :type page_frame: {"on", "off"}, default: "off"


    :param page_frame_colour: 
    :type page_frame_colour: str, default: "charcoal"


    :param page_frame_line_style: 
    :type page_frame_line_style: {"solid", "dot", "dash", "chain_dot", "chain_dash"}, default: "solid"


    :param page_frame_thickness: 
    :type page_frame_thickness: int, default: 2


    :param page_id_line: 
    :type page_id_line: {"on", "off"}, default: "off"


    :param page_id_line_user_text: 
    :type page_id_line_user_text: str


    :param subpage_frame: 
    :type subpage_frame: {"on", "off"}, default: "on"


    :param subpage_frame_colour: 
    :type subpage_frame_colour: str, default: "black"


    :param subpage_frame_line_style: 
    :type subpage_frame_line_style: {"solid", "dot", "dash", "chain_dot", "chain_dash"}, default: "solid"


    :param subpage_frame_thickness: 
    :type subpage_frame_thickness: int, default: 2


    :param subpage_background_colour: 
    :type subpage_background_colour: str, default: "none"


    :rtype: None


.. minigallery:: metview.mhovmoellerview
    :add-heading:

