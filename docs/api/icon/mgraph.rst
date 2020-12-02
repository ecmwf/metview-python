
mgraph
=========================

.. container::
    
    .. container:: leftside

        .. image:: /_static/MGRAPH.png
           :width: 48px

    .. container:: rightside

        This function performs the same task as the `Graph Plotting <https://confluence.ecmwf.int/display/METV/Graph+Plotting>`_ icon in Metview’s user interface. It accepts its parameters as keyword arguments, described below.


.. py:function:: mgraph(**kwargs)
  
    Description comes here!


    :param legend: Turn "on"/"off" the legend for this graph (this parameter is new to Magics++)
    :type legend: {"on", "off"}, default: "off"


    :param legend_user_text: User-defined text for the legend of this graph
    :type legend_user_text: str


    :param graph_type: Defines the type of "curve" required
    :type graph_type: {"curve", "bar", "flag", "arrow", "area"}, default: "curve"


    :param graph_shade: Turn the shading onTurn the shading "on"
    :type graph_shade: {"on", "off"}, default: "on"


    :param graph_line: Plot the curve line
    :type graph_line: {"on", "off"}, default: "on"


    :param graph_line_style: Line style of the curve
    :type graph_line_style: {"solid", "dash", "dot", "chain_dot", "chain_dash"}, default: "solid"


    :param graph_line_colour: Colour of the curve
    :type graph_line_colour: str, default: "blue"


    :param graph_line_thickness: Thickness of the curve
    :type graph_line_thickness: int, default: 1


    :param graph_symbol: If symbols are to be drawn "on" the curves
    :type graph_symbol: {"on", "off"}, default: "off"


    :param graph_symbol_marker_index: The marker symbol to be used.
    :type graph_symbol_marker_index: number, default: 3


    :param graph_symbol_height: Height of  symbol
    :type graph_symbol_height: number, default: 0.2


    :param graph_symbol_colour: Colour of graph symbol
    :type graph_symbol_colour: str, default: "red"


    :param graph_symbol_outline: Add an outline to each symbol
    :type graph_symbol_outline: {"on", "off"}, default: "off"


    :param graph_symbol_outline_colour: Colour of the outline
    :type graph_symbol_outline_colour: str, default: "black"


    :param graph_symbol_outline_thickness: thickness of the outline
    :type graph_symbol_outline_thickness: int, default: 1


    :param graph_symbol_outline_style: Line Style of outline
    :type graph_symbol_outline_style: {"solid", "dash", "dot", "chain_dot", "chain_dash"}, default: "solid"


    :param graph_x_suppress_below: Value on the x  below which a point is considered missing
    :type graph_x_suppress_below: number, default: -1.0e+21


    :param graph_x_suppress_above: Value on the x  above which a point is considered missing
    :type graph_x_suppress_above: number, default: 1.0e+21


    :param graph_y_suppress_below: Value on the y  below which a point is considered missing
    :type graph_y_suppress_below: number, default: -1.0e+21


    :param graph_y_suppress_above: Value on the y  above which a point is considered missing
    :type graph_y_suppress_above: number, default: 1.0e+21


    :param graph_missing_data_mode: How to handle missing data
    :type graph_missing_data_mode: {"ignore", "join", "drop"}, default: "ignore"


    :param graph_missing_data_style: Line style of the missing data part of curve
    :type graph_missing_data_style: {"solid", "dash", "dot", "chain_dot", "chain_dash"}, default: "dash"


    :param graph_missing_data_colour: Colour of the missing data part of curve
    :type graph_missing_data_colour: str, default: "red"


    :param graph_missing_data_thickness: Thickness of the missing data part of curve
    :type graph_missing_data_thickness: int, default: 1


    :param graph_flag_colour: The colour of the Flags!
    :type graph_flag_colour: str, default: "black"


    :param graph_flag_length: Physical length of wind flag shaft
    :type graph_flag_length: number, default: 0.75


    :param graph_arrow_colour: The colour of the arrows
    :type graph_arrow_colour: str, default: "black"


    :param graph_arrow_unit_velocity: Wind speed in m/s represented by a unit vector (1.0 cm).
    :type graph_arrow_unit_velocity: number, default: 25.0


    :param graph_bar_orientation: Orientation of the bars : "vertical" or "horizontal"
    :type graph_bar_orientation: {"vertical", "horizontal"}, default: "vertical"


    :param graph_bar_justification: the bar will be centered on the value, or "left", "right" justify : useful for plotting any accumulated fields
    :type graph_bar_justification: {"left", "centre", "right"}, default: "centre"


    :param graph_bar_width: The width of a bar in a bar chart
    :type graph_bar_width: number, default: -1


    :param graph_bar_style: If candlestick, a line will be drawn at the position with 2 small perpendicular lines at top and bottom
    :type graph_bar_style: {"bar", "linebar"}, default: "bar"


    :param graph_bar_line_style: Line Style of the Bar Border
    :type graph_bar_line_style: {"solid", "dash", "dot", "chain_dot", "chain_dash"}, default: "solid"


    :param graph_bar_line_thickness: Thickness of the Bar Border
    :type graph_bar_line_thickness: int, default: 1


    :param graph_bar_line_colour: The colour of the  the Bar Border
    :type graph_bar_line_colour: str, default: "black"


    :param graph_bar_colour: The colour of the interiors of bars
    :type graph_bar_colour: str, default: "blue"


    :param graph_bar_clipping: whether or not to clip the bar if they go outside the view area.
    :type graph_bar_clipping: {"on", "off"}, default: "on"


    :param graph_bar_annotation: add annotation on the top box : List of strings to use
    :type graph_bar_annotation: str or list[str]


    :param graph_bar_annotation_font_size: Font size for annotation
    :type graph_bar_annotation_font_size: number, default: 0.25


    :param graph_bar_annotation_font_colour: Font size for annotation
    :type graph_bar_annotation_font_colour: str, default: "red"


    :param graph_bar_minimum_value: If set, defines the bottom of the bar
    :type graph_bar_minimum_value: number, default: 1.0e21


    :param graph_shade_style: Style of shading
    :type graph_shade_style: {"area_fill", "hatch", "dot"}, default: "area_fill"


    :param graph_shade_colour: The colour of the shaded part of bars
    :type graph_shade_colour: str, default: "blue"


    :param graph_shade_dot_density: Density per square cm. of shading dots
    :type graph_shade_dot_density: number, default: 20


    :param graph_shade_dot_size: Size of shading dots
    :type graph_shade_dot_size: number, default: 0.02


    :param graph_shade_hatch_index: Hatch index number
    :type graph_shade_hatch_index: number, default: 0


    :rtype: None


.. minigallery:: metview.mgraph
    :add-heading:

