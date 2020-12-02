
mlegend
=========================

.. container::
    
    .. container:: leftside

        .. image:: /_static/MLEGEND.png
           :width: 48px

    .. container:: rightside

        This function performs the same task as the `Legend <https://confluence.ecmwf.int/display/METV/Legend>`_ icon in Metview’s user interface. It accepts its parameters as keyword arguments, described below.


.. py:function:: mlegend(**kwargs)
  
    Description comes here!


    :param legend_text_colour: Legend text colour
    :type legend_text_colour: str, default: "navy"


    :param legend_title: plot legend title text
    :type legend_title: {"on", "off"}, default: "off"


    :param legend_title_text: Text to plot as "legend" title
    :type legend_title_text: str, default: "legend"


    :param legend_title_orientation: Orientation of legend title, if "automatic" the title will be    "horizontal" for "horizontal" legend and "vertical" for "vertical"
    :type legend_title_orientation: {"vertical", "horizontal", "automatic"}, default: "automatic"


    :param legend_title_font_size: Font size used for the title: The default is the same as text_entry
    :type legend_title_font_size: number, default: -1


    :param legend_title_font_colour: Font Colour used for the title: The defaut is the same as the text_entry
    :type legend_title_font_colour: str, default: "automatic"


    :param legend_title_position: relative title position
    :type legend_title_position: {"automatic", "top", "bottom", "left", "right"}, default: "automatic"


    :param legend_title_position_ratio: percentage of the legend box used for the title
    :type legend_title_position_ratio: number, default: 25


    :param legend_units_text: Text to plot as units
    :type legend_units_text: str


    :param legend_user_minimum: Use of user tailored text for minimum
    :type legend_user_minimum: {"on", "off"}, default: "off"


    :param legend_user_minimum_text: User tailored text for minimum
    :type legend_user_minimum_text: str


    :param legend_user_maximum: Use of user tailored text for maximum
    :type legend_user_maximum: {"on", "off"}, default: "off"


    :param legend_user_maximum_text: User tailored text for maximum
    :type legend_user_maximum_text: str


    :param legend_display_type: type of shaded legend required
    :type legend_display_type: {"disjoint", "continuous", "histogram"}, default: "continuous"


    :param legend_text_format: Format of "(automatic)" text (MAGICS Format/("(automatic)"))
    :type legend_text_format: str, default: "(automatic)"


    :param legend_box_mode: Whether legend box is positioned automatically or by the user
    :type legend_box_mode: {"automatic", "positional"}, default: "automatic"


    :param legend_automatic_position: Whether legend box is positioned on the "top" or on the "right" of the drawing area
    :type legend_automatic_position: {"top", "right"}, default: "top"


    :param legend_automatic_box_margin: margin in % of the legend box [top/bottom] for vertical layout and [left/right] for horizontal layout
    :type legend_automatic_box_margin: number, default: 5


    :param legend_text_font: Font name - please make sure this font is installed!
    :type legend_text_font: {"arial", "courier", "helvetica", "times", "serif", "sansserif", "symbol"}, default: "sansserif"


    :param legend_text_font_style: Font style. Set this to an empty string in order to remove all styling.
    :type legend_text_font_style: {"normal", "bold", "italic", "bolditalic"}, default: "normal"


    :param legend_text_font_size: Font size, specified in cm or in % ex: 0.5cm or 10%
    :type legend_text_font_size: str, default: "0.2"


    :param legend_text_orientation: Orientation of the text : horizontal by default
    :type legend_text_orientation: number, default: 0


    :param legend_text_composition: Determines whether to use automatically-generated or user-generated text (or "both") in the legend
    :type legend_text_composition: {"automatic_text_only", "user_text_only", "both"}, default: "automatic_text_only"


    :param legend_user_lines: List of text for legend entries
    :type legend_user_lines: str or list[str]


    :param legend_values_list: List of values to show in the legend
    :type legend_values_list: float or list[float]


    :param legend_column_count: Number of columns in the legend
    :type legend_column_count: number, default: 1


    :param legend_entry_plot_direction: Method of filling in legend entries
    :type legend_entry_plot_direction: {"automatic", "row", "column"}, default: "automatic"


    :param legend_entry_plot_orientation: going from bootom to top ot top to bottom in column mode!
    :type legend_entry_plot_orientation: {"bottom_top", "top_bottom"}, default: "bottom_top"


    :param legend_symbol_height_factor: Factor to apply to the symbol_height in the legend
    :type legend_symbol_height_factor: number, default: 1


    :param legend_box_x_position: X coordinate of lower left corner of legend box (Relative to page_x_position)
    :type legend_box_x_position: number, default: -1


    :param legend_box_y_position: Y coordinate of lower left corner of legend box (Relative to page_y_position)
    :type legend_box_y_position: number, default: -1


    :param legend_box_x_length: Length of legend box in X direction
    :type legend_box_x_length: number, default: -1


    :param legend_box_y_length: Length of legend box in Y direction
    :type legend_box_y_length: number, default: 0


    :param legend_box_blanking: blanking of legend box
    :type legend_box_blanking: {"on", "off"}, default: "off"


    :param legend_border: Plot border around legend box
    :type legend_border: {"on", "off"}, default: "off"


    :param legend_border_line_style: Line style of border around legend box
    :type legend_border_line_style: {"solid", "dash", "dot", "chain_dot", "chain_dash"}, default: "solid"


    :param legend_border_colour: Colour of border around text box (Full choice of colours)
    :type legend_border_colour: str, default: "blue"


    :param legend_border_thickness: Thickness of legend box border
    :type legend_border_thickness: int, default: 1


    :param legend_entry_text_width: Width in percent used for the text part of a legend Entry
    :type legend_entry_text_width: number, default: 60


    :param legend_entry_border: add a border to the graphical part of each legend entry
    :type legend_entry_border: {"on", "off"}, default: "on"


    :param legend_entry_border_colour: border colour
    :type legend_entry_border_colour: str, default: "black"


    :param legend_label_frequency: Frequency of the labels.Frequency of the labels.
    :type legend_label_frequency: number, default: 1


    :param legend_histogram_border: add a border to the the bars
    :type legend_histogram_border: {"on", "off"}, default: "on"


    :param legend_histogram_border_colour: border colour of the bars
    :type legend_histogram_border_colour: str, default: "black"


    :param legend_histogram_mean_value: show the mean value
    :type legend_histogram_mean_value: {"on", "off"}, default: "off"


    :param legend_histogram_mean_value_marker: show the mean value
    :type legend_histogram_mean_value_marker: number, default: 15


    :param legend_histogram_mean_value_marker_colour: show the mean value
    :type legend_histogram_mean_value_marker_colour: str, default: "black"


    :param legend_histogram_mean_value_marker_size: show the mean value
    :type legend_histogram_mean_value_marker_size: number, default: 0.4


    :param legend_histogram_max_value: show the max value
    :type legend_histogram_max_value: {"on", "off"}, default: "on"


    :param legend_histogram_grid_colour: Colour of the grids
    :type legend_histogram_grid_colour: str, default: "black"


    :param legend_histogram_grid_line_style: Line Style of the grids
    :type legend_histogram_grid_line_style: {"solid", "dash", "dot", "chain_dot", "chain_dash"}, default: "solid"


    :param legend_histogram_grid_thickness: thickness of the grids
    :type legend_histogram_grid_thickness: int, default: 1


    :rtype: None


.. minigallery:: metview.mlegend
    :add-heading:

