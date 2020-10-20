
mwind
=========================

.. container::
    
    .. container:: leftside

        .. image:: /_static/MWIND.png
           :width: 48px

    .. container:: rightside

        This function represents the `Wind Plotting <https://confluence.ecmwf.int/display/METV/Wind+Plotting>`_ icon in Metview's user interface.


.. py:function:: mwind(**kwargs)
  
    Description comes here!


    :param wind_field_type: Method of wind field plotting. The possible values:

        * flags
        * arrows
        * streamlines
        The default is: arrows.
    :type wind_field_type: str


    :param wind_thinning_factor: Controls the actual number of wind arrows or flags plotted. See main text for explanation. Needs to 1.0 or larger. The default is: 2.0.
    :type wind_thinning_factor: number


    :param legend: 
    :type legend: str


    :param wind_legend_text: 
    :type wind_legend_text: str


    :param wind_advanced_method: 
    :type wind_advanced_method: str


    :param wind_advanced_colour_parameter: 
    :type wind_advanced_colour_parameter: str


    :param wind_advanced_colour_selection_type: 
    :type wind_advanced_colour_selection_type: str


    :param wind_advanced_colour_max_value: 
    :type wind_advanced_colour_max_value: number


    :param wind_advanced_colour_min_value: 
    :type wind_advanced_colour_min_value: number


    :param wind_advanced_colour_level_count: 
    :type wind_advanced_colour_level_count: number


    :param wind_advanced_colour_level_tolerance: 
    :type wind_advanced_colour_level_tolerance: number


    :param wind_advanced_colour_reference_level: 
    :type wind_advanced_colour_reference_level: number


    :param wind_advanced_colour_level_interval: 
    :type wind_advanced_colour_level_interval: number


    :param wind_advanced_colour_level_list: 
    :type wind_advanced_colour_level_list: float or list[float]


    :param wind_advanced_colour_table_colour_method: 
    :type wind_advanced_colour_table_colour_method: str


    :param wind_advanced_colour_max_level_colour: 
    :type wind_advanced_colour_max_level_colour: str


    :param wind_advanced_colour_min_level_colour: 
    :type wind_advanced_colour_min_level_colour: str


    :param wind_advanced_colour_direction: 
    :type wind_advanced_colour_direction: str


    :param wind_advanced_colour_list: 
    :type wind_advanced_colour_list: str or list[str]


    :param wind_advanced_colour_list_policy: 
    :type wind_advanced_colour_list_policy: str


    :param wind_flag_calm_indicator: Plot calm indicator circle, if wind speed is less than 0.5 m/s (ON / OFF). The possible values:

        * on
        * off
        The default is: on.
    :type wind_flag_calm_indicator: str


    :param wind_flag_calm_indicator_size: The radius of the circle which indicates calm in centimeter. The default is: 0.3.
    :type wind_flag_calm_indicator_size: number


    :param wind_flag_calm_below: Winds less than or equal to this value will be drawn as calm. The default is: 0.5.
    :type wind_flag_calm_below: number


    :param wind_flag_colour: Colour of wind flag shaft, barbs and pennants. The possible values:

        * background
        The default is: blue.
    :type wind_flag_colour: str


    :param wind_flag_length: Physical length of wind flag shaft. The default is: 1.0.
    :type wind_flag_length: number


    :param wind_flag_max_speed: Highest value of wind speed to be plotted. The default is: 1.0e+21.
    :type wind_flag_max_speed: number


    :param wind_flag_min_speed: Lowest value of wind speed to be plotted. The default is: -1.0e+21.
    :type wind_flag_min_speed: number


    :param wind_flag_style: Controls the line style of the wind flag shaft. The possible values:

        * solid
        * dash
        * dot
        * chain_dot
        * chain_dash
        The default is: solid.
    :type wind_flag_style: str


    :param wind_flag_origin_marker: Symbol for marking the exact location of the current grid point. The possible values:

        * dot
        * circle
        * off
        The default is: circle.
    :type wind_flag_origin_marker: str


    :param wind_flag_origin_marker_size: 
    :type wind_flag_origin_marker_size: number


    :param wind_flag_thickness: Thickness of wind flag shaft. The default is: 1.
    :type wind_flag_thickness: int


    :param wind_arrow_calm_indicator: Plot calm indicator circle if wind speed is less than or equal to the value in ``wind_arrow_calm_below`` (ON / OFF). The possible values:

        * on
        * off
        The default is: off.
    :type wind_arrow_calm_indicator: str


    :param wind_arrow_calm_indicator_size: The radius of the circle which indicates calm. The default is: 0.3.
    :type wind_arrow_calm_indicator_size: number


    :param wind_arrow_calm_below: Winds less than or equal to this value will be drawn as calm. The default is: 0.5.
    :type wind_arrow_calm_below: number


    :param wind_arrow_colour: Colour of wind arrow. The possible values:

        * background
        The default is: blue.
    :type wind_arrow_colour: str


    :param wind_arrow_head_shape: Table number, XY, indicating shape of arrowhead X. The default is: 0.
    :type wind_arrow_head_shape: int


    :param wind_arrow_head_ratio: Table number, XY, indicating style and shape of arrowhead X. The default is: 0.3.
    :type wind_arrow_head_ratio: number


    :param wind_arrow_max_speed: Highest value of wind speed to be plotted. The default is: 1.0e+21.
    :type wind_arrow_max_speed: number


    :param wind_arrow_min_speed: Lowest value of wind speed to be plotted. The default is: -1.0e+21.
    :type wind_arrow_min_speed: number


    :param wind_arrow_fixed_velocity: Fixed velocity arrows (m/s). The default is: 0.
    :type wind_arrow_fixed_velocity: number


    :param wind_arrow_thickness: Thickness of wind arrow shaft. The default is: 1.
    :type wind_arrow_thickness: int


    :param wind_arrow_style: Controls the line style of the arrow flag shaft. The possible values:

        * solid
        * dash
        * dot
        * chain_dot
        * chain_dash
        The default is: solid.
    :type wind_arrow_style: str


    :param wind_arrow_unit_velocity: Wind speed in m/s represented by a unit vector (1.0 cm or 1.0 user unit depending on the value of wind_arrow_unit_system ). The default is: 25.0.
    :type wind_arrow_unit_velocity: number


    :param wind_arrow_legend_text: Text to be used as units in the legend text. The default is: m.
    :type wind_arrow_legend_text: str


    :param wind_streamline_min_density: The minimum number of streamlines to be plotted in one square cm of the user's subpage. The default is: 1.
    :type wind_streamline_min_density: number


    :param wind_streamline_min_speed: Wind speed below which streamline plotting will be stopped. The default is: 1.
    :type wind_streamline_min_speed: number


    :param wind_streamline_thickness: Thickness of streamlines. The default is: 2.
    :type wind_streamline_thickness: int


    :param wind_streamline_colour: Colour of streamlines. The possible values:

        * background
        The default is: blue.
    :type wind_streamline_colour: str


    :param wind_streamline_style: Line style of streamlines. The possible values:

        * solid
        * dash
        * dot
        * chain_dot
        * chain_dash
        The default is: solid.
    :type wind_streamline_style: str


    :param wind_streamline_head_shape: Table number, XY, indicating shape of arrowhead X. The default is: 0.
    :type wind_streamline_head_shape: int


    :param wind_streamline_head_ratio: Table number, XY, indicating style and shape of arrowhead X. The default is: 0.3.
    :type wind_streamline_head_ratio: number


    :rtype: None


.. minigallery:: metview.mwind
    :add-heading:

