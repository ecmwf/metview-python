
mlegend
=========================

.. container::
    
    .. container:: leftside

        .. image:: /_static/MLEGEND.png
           :width: 48px

    .. container:: rightside

        This icon represents the `Legend <https://confluence.ecmwf.int/display/METV/Legend>`_ icon in Metview's user interface.


.. py:function:: mlegend(**kwargs)
  
    Description comes here!


    :param legend_text_colour: Legend text colour. The possible values:

        * background
        The default is: navy.
    :type legend_text_colour: str


    :param legend_title: plot legend title text. The possible values:

        * on
        * off
        The default is: off.
    :type legend_title: str


    :param legend_title_text: Text to plot as legend title. The default is: legend.
    :type legend_title_text: str


    :param legend_title_orientation: Orientation of legend title, if automatic the title will be    horizontal for horizontal legend and vertical for vertical. The possible values:

        * vertical
        * horizontal
        * automatic
        The default is: automatic.
    :type legend_title_orientation: str


    :param legend_title_font_size: Font size used for the title: The default is the same as text_entry. The default is: -1.
    :type legend_title_font_size: number


    :param legend_title_font_colour: Font Colour used for the title: The defaut is the same as the text_entry. The possible values:

        * background
        The default is: automatic.
    :type legend_title_font_colour: str


    :param legend_title_position: relative title position. The possible values:

        * automatic
        * top
        * bottom
        * left
        * right
        The default is: automatic.
    :type legend_title_position: str


    :param legend_title_position_ratio: percentage of the legend box used for the title. The default is: 25.
    :type legend_title_position_ratio: number


    :param legend_units_text: Text to plot as units
    :type legend_units_text: str


    :param legend_user_minimum: Use of user tailored text for minimum. The possible values:

        * on
        * off
        The default is: off.
    :type legend_user_minimum: str


    :param legend_user_minimum_text: User tailored text for minimum
    :type legend_user_minimum_text: str


    :param legend_user_maximum: Use of user tailored text for maximum. The possible values:

        * on
        * off
        The default is: off.
    :type legend_user_maximum: str


    :param legend_user_maximum_text: User tailored text for maximum
    :type legend_user_maximum_text: str


    :param legend_display_type: type of shaded legend required. The possible values:

        * disjoint
        * continuous
        * histogram
        The default is: continuous.
    :type legend_display_type: str


    :param legend_text_format: Format of automatic text (MAGICS Format/(AUTOMATIC)). The default is: (automatic).
    :type legend_text_format: str


    :param legend_box_mode: Whether legend box is positioned automatically or by the user. The possible values:

        * automatic
        * positional
        The default is: automatic.
    :type legend_box_mode: str


    :param legend_automatic_position: Whether legend box is positioned on the top or on the right of the drawing area. The possible values:

        * top
        * right
        The default is: top.
    :type legend_automatic_position: str


    :param legend_automatic_box_margin: margin in % of the legend box [top/bottom] for vertical layout and [left/right] for horizontal layout. The default is: 5.
    :type legend_automatic_box_margin: number


    :param legend_text_font: Font name - please make sure this font is installed!. The possible values:

        * arial
        * courier
        * helvetica
        * times
        * serif
        * sansserif
        * symbol
        The default is: sansserif.
    :type legend_text_font: str


    :param legend_text_font_style: Font style. Set this to an empty string in order to remove all styling. The possible values:

        * normal
        * bold
        * italic
        * bolditalic
        The default is: normal.
    :type legend_text_font_style: str


    :param legend_text_font_size: Font size, specified in cm or in % ex: 0.5cm or 10%. The default is: 0.2.
    :type legend_text_font_size: str


    :param legend_text_orientation: Orientation of the text : horizontal by default. The default is: 0.
    :type legend_text_orientation: number


    :param legend_text_composition: Determines whether to use automatically-generated or user-generated text (or both) in the legend. The possible values:

        * automatic_text_only
        * user_text_only
        * both
        The default is: automatic_text_only.
    :type legend_text_composition: str


    :param legend_user_lines: List of text for legend entries
    :type legend_user_lines: str or list[str]


    :param legend_values_list: List of values to show in the legend
    :type legend_values_list: float or list[float]


    :param legend_column_count: Number of columns in the legend. The default is: 1.
    :type legend_column_count: number


    :param legend_entry_plot_direction: Method of filling in legend entries. The possible values:

        * automatic
        * row
        * column
        The default is: automatic.
    :type legend_entry_plot_direction: str


    :param legend_entry_plot_orientation: going from bootom to top ot top to bottom in column mode!. The possible values:

        * bottom_top
        * top_bottom
        The default is: bottom_top.
    :type legend_entry_plot_orientation: str


    :param legend_symbol_height_factor: Factor to apply to the symbol_height in the legend. The default is: 1.
    :type legend_symbol_height_factor: number


    :param legend_box_x_position: X coordinate of lower left corner of legend box (Relative to page_x_position). The default is: -1.
    :type legend_box_x_position: number


    :param legend_box_y_position: Y coordinate of lower left corner of legend box (Relative to page_y_position). The default is: -1.
    :type legend_box_y_position: number


    :param legend_box_x_length: Length of legend box in X direction. The default is: -1.
    :type legend_box_x_length: number


    :param legend_box_y_length: Length of legend box in Y direction. The default is: 0.
    :type legend_box_y_length: number


    :param legend_box_blanking: blanking of legend box. The possible values:

        * on
        * off
        The default is: off.
    :type legend_box_blanking: str


    :param legend_border: Plot border around legend box. The possible values:

        * on
        * off
        The default is: off.
    :type legend_border: str


    :param legend_border_line_style: Line style of border around legend box. The possible values:

        * solid
        * dash
        * dot
        * chain_dot
        * chain_dash
        The default is: solid.
    :type legend_border_line_style: str


    :param legend_border_colour: Colour of border around text box (Full choice of colours). The possible values:

        * background
        The default is: blue.
    :type legend_border_colour: str


    :param legend_border_thickness: Thickness of legend box border. The default is: 1.
    :type legend_border_thickness: int


    :param legend_entry_text_width: Width in percent used for the text part of a legend Entry. The default is: 60.
    :type legend_entry_text_width: number


    :param legend_entry_border: add a border to the graphical part of each legend entry. The possible values:

        * on
        * off
        The default is: on.
    :type legend_entry_border: str


    :param legend_entry_border_colour: border colour. The possible values:

        * background
        The default is: black.
    :type legend_entry_border_colour: str


    :param legend_label_frequency: Frequency of the labels.Frequency of the labels. The default is: 1.
    :type legend_label_frequency: number


    :param legend_histogram_border: add a border to the the bars. The possible values:

        * on
        * off
        The default is: on.
    :type legend_histogram_border: str


    :param legend_histogram_border_colour: border colour of the bars. The possible values:

        * background
        The default is: black.
    :type legend_histogram_border_colour: str


    :param legend_histogram_mean_value: show the mean value. The possible values:

        * on
        * off
        The default is: off.
    :type legend_histogram_mean_value: str


    :param legend_histogram_mean_value_marker: show the mean value. The default is: 15.
    :type legend_histogram_mean_value_marker: number


    :param legend_histogram_mean_value_marker_colour: show the mean value. The possible values:

        * background
        The default is: black.
    :type legend_histogram_mean_value_marker_colour: str


    :param legend_histogram_mean_value_marker_size: show the mean value. The default is: 0.4.
    :type legend_histogram_mean_value_marker_size: number


    :param legend_histogram_max_value: show the max value. The possible values:

        * on
        * off
        The default is: on.
    :type legend_histogram_max_value: str


    :param legend_histogram_grid_colour: Colour of the grids. The possible values:

        * background
        The default is: black.
    :type legend_histogram_grid_colour: str


    :param legend_histogram_grid_line_style: Line Style of the grids. The possible values:

        * solid
        * dash
        * dot
        * chain_dot
        * chain_dash
        The default is: solid.
    :type legend_histogram_grid_line_style: str


    :param legend_histogram_grid_thickness: thickness of the grids. The default is: 1.
    :type legend_histogram_grid_thickness: int


    :rtype: None


.. minigallery:: metview.mlegend
    :add-heading:

