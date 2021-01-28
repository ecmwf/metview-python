
mwind
=========================

.. container::
    
    .. container:: leftside

        .. image:: /_static/MWIND.png
           :width: 48px

    .. container:: rightside

		This is the visual definition for specifying how vector data is displayed. It controls features such as wind arrows and wind flags. Note that Metview will automatically interpret certain pairs of GRIB parameters as vector components, for example u/v and 10u/10v. Use :func:`grib_vectors` to plot an arbitrary pair of scalar fields as a vector field.


		.. note:: This function performs the same task as the `Wind Plotting <https://confluence.ecmwf.int/display/METV/Wind+Plotting>`_ icon in Metview’s user interface. It accepts its parameters as keyword arguments, described below.


.. py:function:: mwind(**kwargs)
  
    Defines the style for wind plotting.


    :param wind_field_type: Method of wind plotting.
    :type wind_field_type: {"flags", "arrows", "streamlines"}, default: "arrows"

    :param wind_thinning_factor: Controls the actual number of wind arrows/flags plotted. If it is 1 all the wind arrows/flags will be plotted. Otherwise a spatial thinning will be applied. Values have to greater than or equal to 1.
    :type wind_thinning_factor: number, default: 2.0

    :param legend: Enables the legend.
    :type legend: {"on", "off"}, default: "off"

    :param wind_legend_text: Defines the legend entry text.
    :type wind_legend_text: str, default: "vector"

    :param wind_advanced_method: Enables the advanced wind plotting method ("on") when wind flag/arrow colours can be defined for a set of bands. If it is "off" all the wind flags/arrows will have the same colour.
    :type wind_advanced_method: {"on", "off"}, default: "off"

    :param wind_advanced_colour_parameter: Specifies the parameter defining the magnitude of the flags/arrows when plotting GRIB fields. Only use "parameter" when you want to colour the wind field by another (scalar) field. See :func:`grib_vectors` for details.
    :type wind_advanced_colour_parameter: {"speed", "parameter"}, default: "speed"

    :param wind_advanced_colour_selection_type: Technique to calculate the wind bands in advanced mode.
    :type wind_advanced_colour_selection_type: {"count", "interval", "list"}, default: "count"

    :param wind_advanced_colour_max_value: Highest value to be plotted in advanced mode.
    :type wind_advanced_colour_max_value: number, default: 1.e21

    :param wind_advanced_colour_min_value: Lowest value to be plotted in advanced mode.
    :type wind_advanced_colour_min_value: number, default: -1.e21

    :param wind_advanced_colour_level_count: Number of levels to be plotted when ``wind_advanced_colour_selection_type`` is "count". The plotting library will try to find a "nice" set of levels, which means that the number of levels could be slightly different than specified here.
    :type wind_advanced_colour_level_count: number, default: 10

    :param wind_advanced_colour_level_tolerance: Do not use nice levels if the number of levels differs from ``wind_advanced_colour_level_count`` by more than ``wind_advanced_colour_level_tolerance``.
    :type wind_advanced_colour_level_tolerance: number, default: 2

    :param wind_advanced_colour_reference_level: The value from which the wind bands are calculated.
    :type wind_advanced_colour_reference_level: number, default: 0.0

    :param wind_advanced_colour_level_interval: Interval between two wind values when ``wind_advanced_colour_selection_type`` is "interval".
    :type wind_advanced_colour_level_interval: number, default: 8.0

    :param wind_advanced_colour_level_list: List of wind band values.
    :type wind_advanced_colour_level_list: float or list[float]

    :param wind_advanced_colour_table_colour_method: Method of generating the colours for the wind bands.
    :type wind_advanced_colour_table_colour_method: {"calculate", "list"}, default: "calculate"

    :param wind_advanced_colour_max_level_colour: Highest wind band entry colour.
    :type wind_advanced_colour_max_level_colour: str, default: "blue"

    :param wind_advanced_colour_min_level_colour: Lowest wind band entry colour.
    :type wind_advanced_colour_min_level_colour: str, default: "red"

    :param wind_advanced_colour_direction: Direction of colour sampling along the colour wheel for plotting when ``wind_advanced_colour_table_colour_method`` is "calculate".
    :type wind_advanced_colour_direction: {"clockwise", "anti_clockwise"}, default: "anti_clockwise"

    :param wind_advanced_colour_list: List of colours for the wind bands.
    :type wind_advanced_colour_list: str or list[str]

    :param wind_advanced_colour_list_policy: Specifies what to do if there are fewer colours in ``wind_advanced_colour_list`` than there are wind bands.
    :type wind_advanced_colour_list_policy: {"lastone", "cycle"}, default: "lastone"

    :param wind_flag_calm_indicator: Plots calm indicator circle, if wind speed is less than or equal to ``wind_flag_calm_below``.
    :type wind_flag_calm_indicator: {"on", "off"}, default: "on"

    :param wind_flag_calm_indicator_size: The radius (cm) of the calm indicator circle.
    :type wind_flag_calm_indicator_size: number, default: 0.3

    :param wind_flag_calm_below: Winds less than or equal to this value will be drawn as calm.
    :type wind_flag_calm_below: number, default: 0.5

    :param wind_flag_colour: Colour of the wind flag shaft, barbs and pennants.
    :type wind_flag_colour: str, default: "blue"

    :param wind_flag_length: Physical length (cm) of wind flag shaft.
    :type wind_flag_length: number, default: 1.0

    :param wind_flag_max_speed: Highest value of the wind flags to be plotted.
    :type wind_flag_max_speed: number, default: 1.0e+21

    :param wind_flag_min_speed: Lowest value of the wind flags to be plotted.
    :type wind_flag_min_speed: number, default: -1.0e+21

    :param wind_flag_style: Controls the line style of the wind flag shaft.
    :type wind_flag_style: {"solid", "dash", "dot", "chain_dot", "chain_dash"}, default: "solid"

    :param wind_flag_origin_marker: Symbol for marking the exact location of the current grid point for wind flags.
    :type wind_flag_origin_marker: {"dot", "circle", "off"}, default: "circle"

    :param wind_flag_origin_marker_size: 
    :type wind_flag_origin_marker_size: number, default: 0.3

    :param wind_flag_thickness: Thickness of the wind flag shaft.
    :type wind_flag_thickness: int, default: 1

    :param wind_arrow_calm_indicator: Plots the calm indicator circle if the wind speed is less than or equal to ``wind_arrow_calm_below``.
    :type wind_arrow_calm_indicator: {"on", "off"}, default: "off"

    :param wind_arrow_calm_indicator_size: The radius (cm) of the calm indicator circle.
    :type wind_arrow_calm_indicator_size: number, default: 0.3

    :param wind_arrow_calm_below: Winds less than or equal to this value will be drawn as calm.
    :type wind_arrow_calm_below: number, default: 0.5

    :param wind_arrow_colour: Colour of the wind arrow.
    :type wind_arrow_colour: str, default: "blue"

    :param wind_arrow_head_shape: Indicates the shape of the arrow head.
    :type wind_arrow_head_shape: int, default: 0

    :param wind_arrow_head_ratio: Indicates the shape of the arrow head.
    :type wind_arrow_head_ratio: number, default: 0.3

    :param wind_arrow_max_speed: Highest value of the wind arrows to be plotted.
    :type wind_arrow_max_speed: number, default: 1.0e+21

    :param wind_arrow_min_speed: Lowest value of the wind arrows to be plotted.
    :type wind_arrow_min_speed: number, default: -1.0e+21

    :param wind_arrow_fixed_velocity: Plots fixed velocity arrows (m/s). See ``wind_arrow_unit_velocity``.
    :type wind_arrow_fixed_velocity: number, default: 0

    :param wind_arrow_thickness: Thickness of the wind arrow shaft.
    :type wind_arrow_thickness: int, default: 1

    :param wind_arrow_style: Controls the line style of the arrow shaft.
    :type wind_arrow_style: {"solid", "dash", "dot", "chain_dot", "chain_dash"}, default: "solid"

    :param wind_arrow_unit_velocity: Wind speed in m/s that will be plotted as a 1 cm long wind arrow.
    :type wind_arrow_unit_velocity: number, default: 25.0

    :param wind_arrow_legend_text: Text to be used as units in the legend text.
    :type wind_arrow_legend_text: str, default: "m"

    :param wind_streamline_min_density: The minimum number of streamlines to be plotted in one square cm of the user's subpage.
    :type wind_streamline_min_density: number, default: 1

    :param wind_streamline_min_speed: Wind speed below which streamline plotting will be stopped.
    :type wind_streamline_min_speed: number, default: 1

    :param wind_streamline_thickness: Thickness of streamlines.
    :type wind_streamline_thickness: int, default: 2

    :param wind_streamline_colour: Colour of streamlines.
    :type wind_streamline_colour: str, default: "blue"

    :param wind_streamline_style: Line style of streamlines.
    :type wind_streamline_style: {"solid", "dash", "dot", "chain_dot", "chain_dash"}, default: "solid"

    :param wind_streamline_head_shape: Indicates the shape of the arrow heads on the streamlines.
    :type wind_streamline_head_shape: int, default: 0

    :param wind_streamline_head_ratio: Indicates the shape of the arrow heads on the streamlines.
    :type wind_streamline_head_ratio: number, default: 0.3

    :rtype: :class:`Request`


.. mv-minigallery:: mwind

