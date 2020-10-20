
mgraph
=========================

.. container::
    
    .. container:: leftside

        .. image:: /_static/MGRAPH.png
           :width: 48px

    .. container:: rightside

        This icon represents the `Graph Plotting <https://confluence.ecmwf.int/display/METV/Graph+Plotting>`_ icon in Metview's user interface.


.. py:function:: mgraph(**kwargs)
  
    Description comes here!


    :param legend: Turn on/off the legend for this graph (this parameter is new to Magics++). The possible values:

        * on
        * off
        The default is: off.
    :type legend: str


    :param legend_user_text: User-defined text for the legend of this graph
    :type legend_user_text: str


    :param graph_type: Defines the type of curve required. The possible values:

        * curve
        * bar
        * flag
        * arrow
        * area
        The default is: curve.
    :type graph_type: str


    :param graph_shade: Turn the shading onTurn the shading on. The possible values:

        * on
        * off
        The default is: on.
    :type graph_shade: str


    :param graph_line: Plot the curve line. The possible values:

        * on
        * off
        The default is: on.
    :type graph_line: str


    :param graph_line_style: Line style of the curve. The possible values:

        * solid
        * dash
        * dot
        * chain_dot
        * chain_dash
        The default is: solid.
    :type graph_line_style: str


    :param graph_line_colour: Colour of the curve. The possible values:

        * background
        The default is: blue.
    :type graph_line_colour: str


    :param graph_line_thickness: Thickness of the curve. The default is: 1.
    :type graph_line_thickness: int


    :param graph_symbol: If symbols are to be drawn on the curves. The possible values:

        * on
        * off
        The default is: off.
    :type graph_symbol: str


    :param graph_symbol_marker_index: The marker symbol to be used. The default is: 3.
    :type graph_symbol_marker_index: number


    :param graph_symbol_height: Height of  symbol. The default is: 0.2.
    :type graph_symbol_height: number


    :param graph_symbol_colour: Colour of graph symbol. The possible values:

        * background
        The default is: red.
    :type graph_symbol_colour: str


    :param graph_symbol_outline: Add an outline to each symbol. The possible values:

        * on
        * off
        The default is: off.
    :type graph_symbol_outline: str


    :param graph_symbol_outline_colour: Colour of the outline. The possible values:

        * background
        The default is: black.
    :type graph_symbol_outline_colour: str


    :param graph_symbol_outline_thickness: thickness of the outline. The default is: 1.
    :type graph_symbol_outline_thickness: int


    :param graph_symbol_outline_style: Line Style of outline. The possible values:

        * solid
        * dash
        * dot
        * chain_dot
        * chain_dash
        The default is: solid.
    :type graph_symbol_outline_style: str


    :param graph_x_suppress_below: Value on the x  below which a point is considered missing. The default is: -1.0e+21.
    :type graph_x_suppress_below: number


    :param graph_x_suppress_above: Value on the x  above which a point is considered missing. The default is: 1.0e+21.
    :type graph_x_suppress_above: number


    :param graph_y_suppress_below: Value on the y  below which a point is considered missing. The default is: -1.0e+21.
    :type graph_y_suppress_below: number


    :param graph_y_suppress_above: Value on the y  above which a point is considered missing. The default is: 1.0e+21.
    :type graph_y_suppress_above: number


    :param graph_missing_data_mode: How to handle missing data. The possible values:

        * ignore
        * join
        * drop
        The default is: ignore.
    :type graph_missing_data_mode: str


    :param graph_missing_data_style: Line style of the missing data part of curve. The possible values:

        * solid
        * dash
        * dot
        * chain_dot
        * chain_dash
        The default is: dash.
    :type graph_missing_data_style: str


    :param graph_missing_data_colour: Colour of the missing data part of curve. The possible values:

        * background
        The default is: red.
    :type graph_missing_data_colour: str


    :param graph_missing_data_thickness: Thickness of the missing data part of curve. The default is: 1.
    :type graph_missing_data_thickness: int


    :param graph_flag_colour: The colour of the Flags!. The possible values:

        * background
        The default is: black.
    :type graph_flag_colour: str


    :param graph_flag_length: Physical length of wind flag shaft. The default is: 0.75.
    :type graph_flag_length: number


    :param graph_arrow_colour: The colour of the arrows. The possible values:

        * background
        The default is: black.
    :type graph_arrow_colour: str


    :param graph_arrow_unit_velocity: Wind speed in m/s represented by a unit vector (1.0 cm). The default is: 25.0.
    :type graph_arrow_unit_velocity: number


    :param graph_bar_orientation: Orientation of the bars : Vertical or horizontal. The possible values:

        * vertical
        * horizontal
        The default is: vertical.
    :type graph_bar_orientation: str


    :param graph_bar_justification: the bar will be centered on the value, or left, right justify : useful for plotting any accumulated fields. The possible values:

        * left
        * centre
        * right
        The default is: centre.
    :type graph_bar_justification: str


    :param graph_bar_width: The width of a bar in a bar chart. The default is: -1.
    :type graph_bar_width: number


    :param graph_bar_style: If candlestick, a line will be drawn at the position with 2 small perpendicular lines at top and bottom. The possible values:

        * bar
        * linebar
        The default is: bar.
    :type graph_bar_style: str


    :param graph_bar_line_style: Line Style of the Bar Border. The possible values:

        * solid
        * dash
        * dot
        * chain_dot
        * chain_dash
        The default is: solid.
    :type graph_bar_line_style: str


    :param graph_bar_line_thickness: Thickness of the Bar Border. The default is: 1.
    :type graph_bar_line_thickness: int


    :param graph_bar_line_colour: The colour of the  the Bar Border. The possible values:

        * background
        The default is: black.
    :type graph_bar_line_colour: str


    :param graph_bar_colour: The colour of the interiors of bars. The possible values:

        * background
        The default is: blue.
    :type graph_bar_colour: str


    :param graph_bar_clipping: whether or not to clip the bar if they go outside the view area. The possible values:

        * on
        * off
        The default is: on.
    :type graph_bar_clipping: str


    :param graph_bar_annotation: add annotation on the top box : List of strings to use
    :type graph_bar_annotation: str or list[str]


    :param graph_bar_annotation_font_size: Font size for annotation. The default is: 0.25.
    :type graph_bar_annotation_font_size: number


    :param graph_bar_annotation_font_colour: Font size for annotation. The possible values:

        * background
        The default is: red.
    :type graph_bar_annotation_font_colour: str


    :param graph_bar_minimum_value: If set, defines the bottom of the bar. The default is: 1.0e21.
    :type graph_bar_minimum_value: number


    :param graph_shade_style: Style of shading. The possible values:

        * area_fill
        * hatch
        * dot
        The default is: area_fill.
    :type graph_shade_style: str


    :param graph_shade_colour: The colour of the shaded part of bars. The possible values:

        * background
        The default is: blue.
    :type graph_shade_colour: str


    :param graph_shade_dot_density: Density per square cm. of shading dots. The default is: 20.
    :type graph_shade_dot_density: number


    :param graph_shade_dot_size: Size of shading dots. The default is: 0.02.
    :type graph_shade_dot_size: number


    :param graph_shade_hatch_index: Hatch index number. The default is: 0.
    :type graph_shade_hatch_index: number


    :rtype: None


.. minigallery:: metview.mgraph
    :add-heading:

