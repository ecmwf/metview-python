
msymb
=========================

.. container::
    
    .. container:: leftside

        .. image:: /_static/MSYMB.png
           :width: 48px

    .. container:: rightside

        This function represents the `Symbol Plotting <https://confluence.ecmwf.int/display/METV/Symbol+Plotting>`_ icon in Metview's user interface.


.. py:function:: msymb(**kwargs)
  
    Description comes here!


    :param legend: Turn legend on or off (ON/OFF) : New Parameter!. The possible values:

        * on
        * off
        The default is: off.
    :type legend: str


    :param symbol_type: Defines the type of symbol plotting required. The possible values:

        * number
        * text
        * marker
        * wind
        The default is: number.
    :type symbol_type: str


    :param symbol_table_mode: Specifies if plotting is to be in advanced, table (on) or individual mode (off).                    Note:  The simple table mode is not recommended anymore, try to use the advanced mode instead,                this  should give you easier control of the plot. The possible values:

        * off
        * advanced
        * on
        The default is: off.
    :type symbol_table_mode: str


    :param symbol_format: Format used to plot values (MAGICS Format/(AUTOMATIC)). The default is: (automatic).
    :type symbol_format: str


    :param symbol_outline: Add an outline to each symbol. The possible values:

        * on
        * off
        The default is: off.
    :type symbol_outline: str


    :param symbol_outline_colour: Colour of the outline. The possible values:

        * background
        The default is: black.
    :type symbol_outline_colour: str


    :param symbol_outline_thickness: thickness of the outline. The default is: 1.
    :type symbol_outline_thickness: int


    :param symbol_outline_style: Line Style of outline. The possible values:

        * solid
        * dash
        * dot
        * chain_dot
        * chain_dash
        The default is: solid.
    :type symbol_outline_style: str


    :param symbol_connect_line: Connect all the symbols with a line. The possible values:

        * on
        * off
        The default is: off.
    :type symbol_connect_line: str


    :param symbol_connect_automatic_line_colour: if on, will use the colour of the symbol. The possible values:

        * on
        * off
        The default is: on.
    :type symbol_connect_automatic_line_colour: str


    :param symbol_connect_line_colour: Colour of the connecting line. The possible values:

        * background
        The default is: black.
    :type symbol_connect_line_colour: str


    :param symbol_connect_line_thickness: thickness of the  connecting line. The default is: 1.
    :type symbol_connect_line_thickness: int


    :param symbol_connect_line_style: Line Style of  connecting line. The possible values:

        * solid
        * dash
        * dot
        * chain_dot
        * chain_dash
        The default is: solid.
    :type symbol_connect_line_style: str


    :param legend_user_text: if set, the text to be shown for the symbol group in the legend
    :type legend_user_text: str


    :param symbol_colour: Colour of symbols. The possible values:

        * background
        The default is: blue.
    :type symbol_colour: str


    :param symbol_height: Height of symbols. The default is: 0.2.
    :type symbol_height: number


    :param symbol_marker_mode: Method to select a marker : by name, by index, by image : in that case, Magics will use an external image as marker.Method to select a marker : by name, by index, by image : in that case, Magics will use an external image as marker. The possible values:

        * index
        * name
        * image
        The default is: index.
    :type symbol_marker_mode: str


    :param symbol_marker_index: Marker indice:  An integer between 1 and 28. The default is: 1.
    :type symbol_marker_index: int


    :param symbol_marker_name: Symbol name. Choose in a list of available markers dot/circle/ww_00 ... The default is: dot.
    :type symbol_marker_name: str


    :param symbol_image_path: Path to the image
    :type symbol_image_path: str


    :param symbol_image_format: Format of the image file. If set to AUTOMATIC, the file extension will be used to determine the file type. The possible values:

        * automatic
        * png
        * svg
        The default is: automatic.
    :type symbol_image_format: str


    :param symbol_image_width: width of the image. The default is: -1.
    :type symbol_image_width: number


    :param symbol_image_height: height of the image. The default is: -1.
    :type symbol_image_height: number


    :param symbol_text_list: list of texts to plot
    :type symbol_text_list: str or list[str]


    :param symbol_text_position: Position of the text. The possible values:

        * right
        * left
        * bottom
        * top
        The default is: right.
    :type symbol_text_position: str


    :param symbol_text_font: Font to use. The possible values:

        * arial
        * courier
        * helvetica
        * times
        * serif
        * sansserif
        * symbol
        The default is: sansserif.
    :type symbol_text_font: str


    :param symbol_text_font_size: Font size. The default is: 0.25.
    :type symbol_text_font_size: number


    :param symbol_text_font_style: Font style. The possible values:

        * normal
        * bold
        * italic
        * bolditalic
        The default is: normal.
    :type symbol_text_font_style: str


    :param symbol_text_font_colour: Font colour. The possible values:

        * background
        * automatic
        The default is: automatic.
    :type symbol_text_font_colour: str


    :param symbol_text_blanking: blanking of the text. The possible values:

        * on
        * off
        The default is: off.
    :type symbol_text_blanking: str


    :param symbol_legend_height: If set, the height will be used to plot the symbols in the legend. The default is: -1.
    :type symbol_legend_height: number


    :param symbol_min_table: Table of minimum values.  The table is used in conjunction with ``symbol_max_table``
    :type symbol_min_table: float or list[float]


    :param symbol_max_table: Table of maximum values. The table is used in conjunction with ``symbol_min_table``
    :type symbol_max_table: float or list[float]


    :param symbol_marker_table: Table of MARKER indices. The table is to be used in conjunction with ``symbol_min_table`` and ``symbol_max_table``
    :type symbol_marker_table: float or list[float]


    :param symbol_name_table: Table of Symbol names. The table is to be used in conjunction with ``symbol_min_table`` and ``symbol_max_table``
    :type symbol_name_table: str or list[str]


    :param symbol_colour_table: Table of SYMBOL colours. T The table is to be used in conjunction with ``symbol_min_table`` and ``symbol_max_table``
    :type symbol_colour_table: str or list[str]


    :param symbol_height_table: Table of SYMBOL heights.  The table is to be used in conjunction with ``symbol_min_table`` and ``symbol_max_table``
    :type symbol_height_table: float or list[float]


    :param symbol_advanced_table_selection_type: Technique to use to calculate the shading band levels. The possible values:

        * count
        * interval
        * list
        The default is: count.
    :type symbol_advanced_table_selection_type: str


    :param symbol_advanced_table_min_value: Min value to plot. The default is: -1.e21.
    :type symbol_advanced_table_min_value: number


    :param symbol_advanced_table_max_value: Max value to plot. The default is: 1.e21.
    :type symbol_advanced_table_max_value: number


    :param symbol_advanced_table_level_count: Count or number of levels to be plotted. Magics will try to find "nice levels",            this means that the number of levels could be slightly different from the requested number of levels. The default is: 10.
    :type symbol_advanced_table_level_count: number


    :param symbol_advanced_table_level_tolerance: Tolerance: Do not use "nice levels" if the number of levels is really to different [count +/- tolerance]. The default is: 2.
    :type symbol_advanced_table_level_tolerance: number


    :param symbol_advanced_table_interval: Interval in data units between different bands of shading. The default is: 8.0.
    :type symbol_advanced_table_interval: number


    :param symbol_advanced_table_reference_level: Level from which the level interval is calculated. The default is: 0.0.
    :type symbol_advanced_table_reference_level: number


    :param symbol_advanced_table_level_list: List of shading band levels to be plotted
    :type symbol_advanced_table_level_list: float or list[float]


    :param symbol_advanced_table_colour_method: Method of generating the colours of the bands in polygon shading. The possible values:

        * calculate
        * list
        The default is: calculate.
    :type symbol_advanced_table_colour_method: str


    :param symbol_advanced_table_max_level_colour: Highest shading band colour. The possible values:

        * background
        The default is: blue.
    :type symbol_advanced_table_max_level_colour: str


    :param symbol_advanced_table_min_level_colour: Lowest shading band colour. The possible values:

        * background
        The default is: red.
    :type symbol_advanced_table_min_level_colour: str


    :param symbol_advanced_table_colour_direction: Direction of colour sequencing for plotting (CLOCKWISE/ ANTI_CLOCKWISE). The possible values:

        * clockwise
        * anti-clockwise
        The default is: anti-clockwise.
    :type symbol_advanced_table_colour_direction: str


    :param symbol_advanced_table_colour_list: List of colours to be used in symbol plotting
    :type symbol_advanced_table_colour_list: str or list[str]


    :param symbol_advanced_table_colour_list_policy: What to do if the list of colours is smaller than the list of intervals: lastone/cycle. The possible values:

        * lastone
        * cycle
        The default is: lastone.
    :type symbol_advanced_table_colour_list_policy: str


    :param symbol_advanced_table_marker_list: List of markers to be used in symbol plotting
    :type symbol_advanced_table_marker_list: float or list[float]


    :param symbol_advanced_table_marker_name_list: List of markers to be used in symbol plotting symbol
    :type symbol_advanced_table_marker_name_list: str or list[str]


    :param symbol_advanced_table_marker_list_policy: What to do if  the list of markers is smaller than the list of intervals: lastone/cycle. The possible values:

        * lastone
        * cycle
        The default is: lastone.
    :type symbol_advanced_table_marker_list_policy: str


    :param symbol_advanced_table_height_method: Method of generating the height. The possible values:

        * calculate
        * list
        The default is: list.
    :type symbol_advanced_table_height_method: str


    :param symbol_advanced_table_height_max_value: Maximum height to use. The default is: 0.2.
    :type symbol_advanced_table_height_max_value: number


    :param symbol_advanced_table_height_min_value: Mininimum height to use. The default is: 0.1.
    :type symbol_advanced_table_height_min_value: number


    :param symbol_advanced_table_height_list: List of heights to be used
    :type symbol_advanced_table_height_list: float or list[float]


    :param symbol_advanced_table_height_list_policy: What to do if the list of heights is smaller than the list of intervals: lastone/cycle. The possible values:

        * lastone
        * cycle
        The default is: lastone.
    :type symbol_advanced_table_height_list_policy: str


    :param symbol_advanced_table_text_list: Text to display
    :type symbol_advanced_table_text_list: str or list[str]


    :param symbol_advanced_table_text_list_policy: What to do if  the list of text is smaller that the list of intervalslastone: reuse the last one,cycle: return to the fisrt one. The possible values:

        * lastone
        * cycle
        The default is: cycle.
    :type symbol_advanced_table_text_list_policy: str


    :param symbol_advanced_table_text_font_name: 
    :type symbol_advanced_table_text_font_name: str


    :param symbol_advanced_table_text_font_size: Font size. The default is: 0.25.
    :type symbol_advanced_table_text_font_size: number


    :param symbol_advanced_table_text_font_style: Font Style. The possible values:

        * normal
        * bold
        * italic
        * bolditalic
        The default is: normal.
    :type symbol_advanced_table_text_font_style: str


    :param symbol_advanced_table_text_font_colour: Symbol Colour. The possible values:

        * background
        * automatic
        The default is: automatic.
    :type symbol_advanced_table_text_font_colour: str


    :param symbol_advanced_table_text_display_type: How to display text         none:do not display it         centre : display it instead of the symbol,         right : attached it to the right of the symbol,         top : attached it to the top of the symbol,         bottom:   attached it to the bottom of the symbol,. The possible values:

        * centre
        * none
        * right
        * left
        * top
        * bottom
        The default is: none.
    :type symbol_advanced_table_text_display_type: str


    :param symbol_advanced_table_outlayer_method: outlayer method. The possible values:

        * none
        The default is: none.
    :type symbol_advanced_table_outlayer_method: str


    :rtype: None


.. minigallery:: metview.msymb
    :add-heading:

