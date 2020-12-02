
mwind
=========================

.. container::
    
    .. container:: leftside

        .. image:: /_static/MWIND.png
           :width: 48px

    .. container:: rightside

        This function performs the same task as the `Wind Plotting <https://confluence.ecmwf.int/display/METV/Wind+Plotting>`_ icon in Metview’s user interface. It accepts its parameters as keyword arguments, described below.


.. py:function:: mwind(**kwargs)
  
    Description comes here!


    :param wind_field_type: Method of wind field plotting
    :type wind_field_type: {"flags", "arrows", "streamlines"}, default: "arrows"


    :param wind_thinning_factor: Controls the actual number of wind arrows or flags plotted. See main text for explanation. Needs to 1.0 or larger.
    :type wind_thinning_factor: number, default: 2.0


    :param legend: 
    :type legend: {"on", "off"}, default: "off"


    :param wind_legend_text: 
    :type wind_legend_text: str, default: "vector"


    :param wind_advanced_method: 
    :type wind_advanced_method: {"on", "off"}, default: "off"


    :param wind_advanced_colour_parameter: 
    :type wind_advanced_colour_parameter: {"speed", "parameter"}, default: "speed"


    :param wind_advanced_colour_selection_type: 
    :type wind_advanced_colour_selection_type: {"count", "interval", "list"}, default: "count"


    :param wind_advanced_colour_max_value: 
    :type wind_advanced_colour_max_value: number, default: 1.e21


    :param wind_advanced_colour_min_value: 
    :type wind_advanced_colour_min_value: number, default: -1.e21


    :param wind_advanced_colour_level_count: 
    :type wind_advanced_colour_level_count: number, default: 10


    :param wind_advanced_colour_level_tolerance: 
    :type wind_advanced_colour_level_tolerance: number, default: 2


    :param wind_advanced_colour_reference_level: 
    :type wind_advanced_colour_reference_level: number, default: 0.0


    :param wind_advanced_colour_level_interval: 
    :type wind_advanced_colour_level_interval: number, default: 8.0


    :param wind_advanced_colour_level_list: 
    :type wind_advanced_colour_level_list: float or list[float]


    :param wind_advanced_colour_table_colour_method: 
    :type wind_advanced_colour_table_colour_method: {"calculate", "list"}, default: "calculate"


    :param wind_advanced_colour_max_level_colour: 
    :type wind_advanced_colour_max_level_colour: str, default: "blue"


    :param wind_advanced_colour_min_level_colour: 
    :type wind_advanced_colour_min_level_colour: str, default: "red"


    :param wind_advanced_colour_direction: 
    :type wind_advanced_colour_direction: {"clockwise", "anti_clockwise"}, default: "anti_clockwise"


    :param wind_advanced_colour_list: 
    :type wind_advanced_colour_list: str or list[str]


    :param wind_advanced_colour_list_policy: 
    :type wind_advanced_colour_list_policy: {"lastone", "cycle"}, default: "lastone"


    :param wind_flag_calm_indicator: Plot calm indicator circle, if wind speed is less than 0.5 m/s ("on" / "off")
    :type wind_flag_calm_indicator: {"on", "off"}, default: "on"


    :param wind_flag_calm_indicator_size: The radius of the circle which indicates calm in centimeter
    :type wind_flag_calm_indicator_size: number, default: 0.3


    :param wind_flag_calm_below: Winds less than or equal to this value will be drawn as calm.
    :type wind_flag_calm_below: number, default: 0.5


    :param wind_flag_colour: Colour of wind flag shaft, barbs and pennants
    :type wind_flag_colour: str, default: "blue"


    :param wind_flag_length: Physical length of wind flag shaft
    :type wind_flag_length: number, default: 1.0


    :param wind_flag_max_speed: Highest value of wind speed to be plotted
    :type wind_flag_max_speed: number, default: 1.0e+21


    :param wind_flag_min_speed: Lowest value of wind speed to be plotted
    :type wind_flag_min_speed: number, default: -1.0e+21


    :param wind_flag_style: Controls the line style of the wind flag shaft.
    :type wind_flag_style: {"solid", "dash", "dot", "chain_dot", "chain_dash"}, default: "solid"


    :param wind_flag_origin_marker: Symbol for marking the exact location of the current grid point.
    :type wind_flag_origin_marker: {"dot", "circle", "off"}, default: "circle"


    :param wind_flag_origin_marker_size: 
    :type wind_flag_origin_marker_size: number, default: 0.3


    :param wind_flag_thickness: Thickness of wind flag shaft
    :type wind_flag_thickness: int, default: 1


    :param wind_arrow_calm_indicator: Plot calm indicator circle if wind speed is less than or equal to the value in ``wind_arrow_calm_below`` ("on" / "off")
    :type wind_arrow_calm_indicator: {"on", "off"}, default: "off"


    :param wind_arrow_calm_indicator_size: The radius of the circle which indicates calm
    :type wind_arrow_calm_indicator_size: number, default: 0.3


    :param wind_arrow_calm_below: Winds less than or equal to this value will be drawn as calm.
    :type wind_arrow_calm_below: number, default: 0.5


    :param wind_arrow_colour: Colour of wind arrow
    :type wind_arrow_colour: str, default: "blue"


    :param wind_arrow_head_shape: Table number, XY, indicating shape of arrowhead X
    :type wind_arrow_head_shape: int, default: 0


    :param wind_arrow_head_ratio: Table number, XY, indicating style and shape of arrowhead X
    :type wind_arrow_head_ratio: number, default: 0.3


    :param wind_arrow_max_speed: Highest value of wind speed to be plotted
    :type wind_arrow_max_speed: number, default: 1.0e+21


    :param wind_arrow_min_speed: Lowest value of wind speed to be plotted
    :type wind_arrow_min_speed: number, default: -1.0e+21


    :param wind_arrow_fixed_velocity: Fixed velocity arrows (m/s).
    :type wind_arrow_fixed_velocity: number, default: 0


    :param wind_arrow_thickness: Thickness of wind arrow shaft
    :type wind_arrow_thickness: int, default: 1


    :param wind_arrow_style: Controls the line style of the arrow flag shaft.
    :type wind_arrow_style: {"solid", "dash", "dot", "chain_dot", "chain_dash"}, default: "solid"


    :param wind_arrow_unit_velocity: Wind speed in m/s represented by a unit vector (1.0 cm or 1.0 user unit depending on the value of wind_arrow_unit_system ).
    :type wind_arrow_unit_velocity: number, default: 25.0


    :param wind_arrow_legend_text: Text to be used as units in the legend text
    :type wind_arrow_legend_text: str, default: "m"


    :param wind_streamline_min_density: The minimum number of streamlines to be plotted in one square cm of the user's subpage
    :type wind_streamline_min_density: number, default: 1


    :param wind_streamline_min_speed: Wind speed below which streamline plotting will be stopped
    :type wind_streamline_min_speed: number, default: 1


    :param wind_streamline_thickness: Thickness of streamlines
    :type wind_streamline_thickness: int, default: 2


    :param wind_streamline_colour: Colour of streamlines
    :type wind_streamline_colour: str, default: "blue"


    :param wind_streamline_style: Line style of streamlines
    :type wind_streamline_style: {"solid", "dash", "dot", "chain_dot", "chain_dash"}, default: "solid"


    :param wind_streamline_head_shape: Table number, XY, indicating shape of arrowhead X
    :type wind_streamline_head_shape: int, default: 0


    :param wind_streamline_head_ratio: Table number, XY, indicating style and shape of arrowhead X
    :type wind_streamline_head_ratio: number, default: 0.3


    :rtype: None


.. minigallery:: metview.mwind
    :add-heading:

