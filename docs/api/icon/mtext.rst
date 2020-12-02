
mtext
=========================

.. container::
    
    .. container:: leftside

        .. image:: /_static/MTEXT.png
           :width: 48px

    .. container:: rightside

        This function performs the same task as the `Text Plotting <https://confluence.ecmwf.int/display/METV/Text+Plotting>`_ icon in Metview’s user interface. It accepts its parameters as keyword arguments, described below.


.. py:function:: mtext(**kwargs)
  
    Description comes here!


    :param text_line_count: The number of lines of text to be plotted
    :type text_line_count: number, default: 1


    :param text_line_1: Character string for holding lines of text (n=1,10)
    :type text_line_1: str, default: "<magics_title/>"


    :param text_line_2: Character string for holding lines of text (n=1,10)
    :type text_line_2: str


    :param text_line_3: Character string for holding lines of text (n=1,10)
    :type text_line_3: str


    :param text_line_4: Character string for holding lines of text (n=1,10)
    :type text_line_4: str


    :param text_line_5: Character string for holding lines of text (n=1,10)
    :type text_line_5: str


    :param text_line_6: Character string for holding lines of text (n=1,10)
    :type text_line_6: str


    :param text_line_7: Character string for holding lines of text (n=1,10)
    :type text_line_7: str


    :param text_line_8: Character string for holding lines of text (n=1,10)
    :type text_line_8: str


    :param text_line_9: Character string for holding lines of text (n=1,10)
    :type text_line_9: str


    :param text_line_10: Character string for holding lines of text (n=1,10)
    :type text_line_10: str


    :param text_colour: Colour of text in text block (Full choice of colours)
    :type text_colour: str, default: "navy"


    :param text_font: Font name - please make sure this font is installed!
    :type text_font: {"arial", "courier", "helvetica", "times", "serif", "sansserif", "symbol"}, default: "sansserif"


    :param text_font_style: Font style. Set this to an empty string in order to remove all styling.
    :type text_font_style: {"normal", "bold", "italic", "bolditalic"}, default: "normal"


    :param text_font_size: Font size, specified in cm.
    :type text_font_size: str, default: "0.3"


    :param text_justification: How text is to be positioned in each line ("left"/"centre"/"right")
    :type text_justification: {"left", "centre", "right"}, default: "centre"


    :param text_orientation: Orientation of the text
    :type text_orientation: {"horizontal", "top_bottom", "bottom_top"}, default: "horizontal"


    :param text_lines: text block to be plotted
    :type text_lines: str or list[str]


    :param text_mode: Whether text is to be a "title" or user positioned ("title"/"positional")
    :type text_mode: {"title", "positional"}, default: "title"


    :param text_box_x_position: X coordinate of lower left corner of text box (Relative to PAGE_X_POSITION)
    :type text_box_x_position: number, default: -1


    :param text_box_y_position: Y coordinate of lower left corner of text box (Relative to PAGE_Y_POSITION)
    :type text_box_y_position: number, default: -1


    :param text_box_x_length: Length of text box in X direction
    :type text_box_x_length: number, default: -1


    :param text_box_y_length: 
    :type text_box_y_length: number, default: -1


    :param text_box_blanking: All plotting in the text box previous to PTEXT call will be blanked out. Plotting after PTEXT call will not be affected. ("on"/"off")
    :type text_box_blanking: {"on", "off"}, default: "off"


    :param text_border: Plot border around text box ("on"/"off")
    :type text_border: {"on", "off"}, default: "off"


    :param text_border_line_style: Line style of border around text box ("solid"/"dash"/"dot"/"chain_dash"/"chain_dot")
    :type text_border_line_style: {"solid", "dash", "dot", "chain_dot", "chain_dash"}, default: "solid"


    :param text_border_colour: Colour of border around text box (Full choice of colours)
    :type text_border_colour: str, default: "blue"


    :param text_border_thickness: Thickness of text box border
    :type text_border_thickness: int, default: 1


    :rtype: None


.. minigallery:: metview.mtext
    :add-heading:

