
msymb
=========================

.. container::
    
    .. container:: leftside

        .. image:: /_static/MSYMB.png
           :width: 48px

    .. container:: rightside

		This is the visual definition for specifying how symbols (e.g. circles and crosses) are displayed. This can be used with non-gridded data, such as :func:`Geopoints` or CSV.


		.. note:: This function performs the same task as the `Symbol Plotting <https://confluence.ecmwf.int/display/METV/Symbol+Plotting>`_ icon in Metview’s user interface. It accepts its parameters as keyword arguments, described below.


.. py:function:: msymb(**kwargs)
  
    Defines the style for symbol plotting of non-gridded data.


    :param legend: Enables the legend.
    :type legend: {"on", "off"}, default: "off"

    :param symbol_type: Defines the type of symbol plotting required.
    :type symbol_type: {"number", "text", "marker", "wind"}, default: "number"

    :param symbol_table_mode: Specifies the table mode. Note: the simple table mode ("on") is not recommended  any more, try to use the "advanced" mode instead, this  should give you easier control of the plot.
    :type symbol_table_mode: {"off", "advanced", "on"}, default: "off"

    :param symbol_format: Specifies the format for value plotting.
    :type symbol_format: str, default: "(automatic)"

    :param symbol_outline: Adds an outline to each symbol.
    :type symbol_outline: {"on", "off"}, default: "off"

    :param symbol_outline_colour: Colour of the outline.
    :type symbol_outline_colour: str, default: "black"

    :param symbol_outline_thickness: Thickness of the outline.
    :type symbol_outline_thickness: int, default: 1

    :param symbol_outline_style: Line style of the outline.
    :type symbol_outline_style: {"solid", "dash", "dot", "chain_dot", "chain_dash"}, default: "solid"

    :param symbol_connect_line: Connects all the symbols with a line.
    :type symbol_connect_line: {"on", "off"}, default: "off"

    :param symbol_connect_automatic_line_colour: If it is "on", the lines connecting the symbols will have the same colour as the symbols.
    :type symbol_connect_automatic_line_colour: {"on", "off"}, default: "on"

    :param symbol_connect_line_colour: Colour of the connecting line.
    :type symbol_connect_line_colour: str, default: "black"

    :param symbol_connect_line_thickness: Thickness of the connecting line.
    :type symbol_connect_line_thickness: int, default: 1

    :param symbol_connect_line_style: Line style of connecting line.
    :type symbol_connect_line_style: {"solid", "dash", "dot", "chain_dot", "chain_dash"}, default: "solid"

    :param legend_user_text: If set, this text will be shown for the symbol group in the legend.
    :type legend_user_text: str

    :param symbol_colour: Colour of symbols.
    :type symbol_colour: str, default: "blue"

    :param symbol_height: Height (cm) of symbols.
    :type symbol_height: number, default: 0.2

    :param symbol_marker_mode: Method to select a marker. If it is set to "image" an external image specified in ``symbol_image_path`` will be used as a marker.
    :type symbol_marker_mode: {"index", "name", "image"}, default: "index"

    :param symbol_marker_index: Marker index. An integer between 1 and 28.
    :type symbol_marker_index: int, default: 1

    :param symbol_marker_name: Marker name.
    :type symbol_marker_name: str, default: "dot"

    :param symbol_image_path: Path to the symbol maker image.
    :type symbol_image_path: str

    :param symbol_image_format: Format of the image file. If set to "automatic", the file extension will be used to determine the file type.
    :type symbol_image_format: {"automatic", "png", "svg"}, default: "automatic"

    :param symbol_image_width: Width of the image.
    :type symbol_image_width: number, default: -1

    :param symbol_image_height: Height of the image.
    :type symbol_image_height: number, default: -1

    :param symbol_text_list: List of text to plot.
    :type symbol_text_list: str or list[str]

    :param symbol_text_position: Relative position of the text items.
    :type symbol_text_position: {"right", "left", "bottom", "top"}, default: "right"

    :param symbol_text_font: Font of the text items.
    :type symbol_text_font: {"arial", "courier", "helvetica", "times", "serif", "sansserif", "symbol"}, default: "sansserif"

    :param symbol_text_font_size: Font size of text items.
    :type symbol_text_font_size: number, default: 0.25

    :param symbol_text_font_style: Font style of text items.
    :type symbol_text_font_style: {"normal", "bold", "italic", "bolditalic"}, default: "normal"

    :param symbol_text_font_colour: Font colour of text items.
    :type symbol_text_font_colour: {"background", "automatic"}, default: "automatic"

    :param symbol_text_blanking: Blanking of the text.
    :type symbol_text_blanking: {"on", "off"}, default: "off"

    :param symbol_legend_height: If set, the height will be used to plot the symbols in the legend.
    :type symbol_legend_height: number, default: -1

    :param symbol_min_table: Table of minimum values.  The table is used in conjunction with ``symbol_max_table``.
    :type symbol_min_table: float or list[float]

    :param symbol_max_table: Table of maximum values. The table is used in conjunction with ``symbol_min_table``.
    :type symbol_max_table: float or list[float]

    :param symbol_marker_table: Table of marker indices. The table is to be used in conjunction with ``symbol_min_table`` and ``symbol_max_table``.
    :type symbol_marker_table: float or list[float]

    :param symbol_name_table: Table of symbol names. The table is to be used in conjunction with ``symbol_min_table`` and ``symbol_max_table``.
    :type symbol_name_table: str or list[str]

    :param symbol_colour_table: Table of symbol colours. The table is to be used in conjunction with ``symbol_min_table`` and ``symbol_max_table``.
    :type symbol_colour_table: str or list[str]

    :param symbol_height_table: Table of symbol heights (cm). The table is to be used in conjunction with ``symbol_min_table`` and ``symbol_max_table``.
    :type symbol_height_table: float or list[float]

    :param symbol_advanced_table_selection_type: Technique to use to calculate the symbol table values.
    :type symbol_advanced_table_selection_type: {"count", "interval", "list"}, default: "count"

    :param symbol_advanced_table_min_value: Minimum value to plot.
    :type symbol_advanced_table_min_value: number, default: -1.e21

    :param symbol_advanced_table_max_value: Maximum value to plot.
    :type symbol_advanced_table_max_value: number, default: 1.e21

    :param symbol_advanced_table_level_count: Number of levels to be plotted when ``symbol_advanced_table_selection_type`` is "count". The plotting library will try to find a "nice" set of levels, which means that the number of levels could be slightly different than specified here.
    :type symbol_advanced_table_level_count: number, default: 10

    :param symbol_advanced_table_level_tolerance: Do not use nice levels if the number of levels differs from ``symbol_advanced_table_level_count`` by more than ``symbol_advanced_table_level_tolerance``.
    :type symbol_advanced_table_level_tolerance: number, default: 2

    :param symbol_advanced_table_interval: Interval in data units between two table values when ``symbol_advanced_table_selection_type`` is "interval".
    :type symbol_advanced_table_interval: number, default: 8.0

    :param symbol_advanced_table_reference_level: The level from which the symbol table interval is calculated.
    :type symbol_advanced_table_reference_level: number, default: 0.0

    :param symbol_advanced_table_level_list: List of symbol table values.
    :type symbol_advanced_table_level_list: float or list[float]

    :param symbol_advanced_table_colour_method: Method of generating the colours for the symbol table entries.
    :type symbol_advanced_table_colour_method: {"calculate", "list"}, default: "calculate"

    :param symbol_advanced_table_max_level_colour: Highest symbol table entry colour.
    :type symbol_advanced_table_max_level_colour: str, default: "blue"

    :param symbol_advanced_table_min_level_colour: Lowest symbol table entry colour.
    :type symbol_advanced_table_min_level_colour: str, default: "red"

    :param symbol_advanced_table_colour_direction: Direction of colour sampling along the colour wheel for plotting when ``symbol_advanced_table_colour_method`` is "calculate".
    :type symbol_advanced_table_colour_direction: {"clockwise", "anti-clockwise"}, default: "anti-clockwise"

    :param symbol_advanced_table_colour_list: List of colours to be used in symbol plotting.
    :type symbol_advanced_table_colour_list: str or list[str]

    :param symbol_advanced_table_colour_list_policy: Specifies what to do if there are fewer colours in ``symbol_advanced_table_colour_list`` than there are symbol table intervals.
    :type symbol_advanced_table_colour_list_policy: {"lastone", "cycle"}, default: "lastone"

    :param symbol_advanced_table_marker_list: List of markers to be used in symbol plotting.
    :type symbol_advanced_table_marker_list: float or list[float]

    :param symbol_advanced_table_marker_name_list: List of symbol names to be used in symbol plotting.
    :type symbol_advanced_table_marker_name_list: str or list[str]

    :param symbol_advanced_table_marker_list_policy: Specifies what to do if there are fewer markers specified than the number of symbol table intervals.
    :type symbol_advanced_table_marker_list_policy: {"lastone", "cycle"}, default: "lastone"

    :param symbol_advanced_table_height_method: Method of generating the height (cm) for symbol table intervals.
    :type symbol_advanced_table_height_method: {"calculate", "list"}, default: "list"

    :param symbol_advanced_table_height_max_value: Maximum height to use.
    :type symbol_advanced_table_height_max_value: number, default: 0.2

    :param symbol_advanced_table_height_min_value: Minimum height to use.
    :type symbol_advanced_table_height_min_value: number, default: 0.1

    :param symbol_advanced_table_height_list: List of heights to be used.
    :type symbol_advanced_table_height_list: float or list[float]

    :param symbol_advanced_table_height_list_policy: Specifies what to do if there are fewer entries in ``symbol_advanced_table_height_list`` than there are symbol table intervals.
    :type symbol_advanced_table_height_list_policy: {"lastone", "cycle"}, default: "lastone"

    :param symbol_advanced_table_text_list: Text to display
    :type symbol_advanced_table_text_list: str or list[str]

    :param symbol_advanced_table_text_list_policy: Specifies what to do if there are fewer entries in ``symbol_advanced_table_text_list`` than there are symbol table intervals.
    :type symbol_advanced_table_text_list_policy: {"lastone", "cycle"}, default: "cycle"

    :param symbol_advanced_table_text_font_name: Font name.
    :type symbol_advanced_table_text_font_name: {"arial", "courier", "helvetica", "times", "serif", "sansserif", "symbol"}, default: "sansserif"

    :param symbol_advanced_table_text_font_size: Font size.
    :type symbol_advanced_table_text_font_size: number, default: 0.25

    :param symbol_advanced_table_text_font_style: Font style.
    :type symbol_advanced_table_text_font_style: {"normal", "bold", "italic", "bolditalic"}, default: "normal"

    :param symbol_advanced_table_text_font_colour: Font colour.
    :type symbol_advanced_table_text_font_colour: {"background", "automatic"}, default: "automatic"

    :param symbol_advanced_table_text_display_type: How to display text:         
		
		* "none": do not display it
		* "centre": display it instead of the symbol
		* "right": attach it to the right of the symbol
		* "top": attach it to the top of the symbol
		* "bottom": attach it to the "bottom" of the symbol
    :type symbol_advanced_table_text_display_type: {"centre", "none", "right", "left", "top", "bottom"}, default: "none"

    :param symbol_advanced_table_outlayer_method: Outlayer method.
    :type symbol_advanced_table_outlayer_method: {"none"}, default: "none"

    :rtype: :class:`Request`
.. include:: /gallery/backref/msymb.rst