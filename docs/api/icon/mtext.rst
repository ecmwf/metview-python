
mtext
=========================

.. container::
    
    .. container:: leftside

        .. image:: /_static/MTEXT.png
           :width: 48px

    .. container:: rightside

        This function represents the `Text Plotting <https://confluence.ecmwf.int/display/METV/Text+Plotting>`_ icon in Metview's user interface.


.. py:function:: mtext(**kwargs)
  
    Description comes here!


    :param text_line_count: The number of lines of text to be plotted. The default is: 1.
    :type text_line_count: number


    :param text_line_1: Character string for holding lines of text (n=1,10). The default is: <magics_title/>.
    :type text_line_1: str


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


    :param text_colour: Colour of text in text block (Full choice of colours). The possible values:

        * background
        The default is: navy.
    :type text_colour: str


    :param text_font: Font name - please make sure this font is installed!. The possible values:

        * arial
        * courier
        * helvetica
        * times
        * serif
        * sansserif
        * symbol
        The default is: sansserif.
    :type text_font: str


    :param text_font_style: Font style. Set this to an empty string in order to remove all styling. The possible values:

        * normal
        * bold
        * italic
        * bolditalic
        The default is: normal.
    :type text_font_style: str


    :param text_font_size: Font size, specified in cm. The default is: 0.3.
    :type text_font_size: str


    :param text_justification: How text is to be positioned in each line (LEFT/CENTRE/RIGHT). The possible values:

        * left
        * centre
        * right
        The default is: centre.
    :type text_justification: str


    :param text_orientation: Orientation of the text. The possible values:

        * horizontal
        * top_bottom
        * bottom_top
        The default is: horizontal.
    :type text_orientation: str


    :param text_lines: text block to be plotted
    :type text_lines: str or list[str]


    :param text_mode: Whether text is to be a title or user positioned (TITLE/POSITIONAL). The possible values:

        * title
        * positional
        The default is: title.
    :type text_mode: str


    :param text_box_x_position: X coordinate of lower left corner of text box (Relative to PAGE_X_POSITION). The default is: -1.
    :type text_box_x_position: number


    :param text_box_y_position: Y coordinate of lower left corner of text box (Relative to PAGE_Y_POSITION). The default is: -1.
    :type text_box_y_position: number


    :param text_box_x_length: Length of text box in X direction. The default is: -1.
    :type text_box_x_length: number


    :param text_box_y_length: 
    :type text_box_y_length: number


    :param text_box_blanking: All plotting in the text box previous to PTEXT call will be blanked out. Plotting after PTEXT call will not be affected. (ON/OFF). The possible values:

        * on
        * off
        The default is: off.
    :type text_box_blanking: str


    :param text_border: Plot border around text box (ON/OFF). The possible values:

        * on
        * off
        The default is: off.
    :type text_border: str


    :param text_border_line_style: Line style of border around text box (SOLID/DASH/DOT/CHAIN_DASH/CHAIN_DOT). The possible values:

        * solid
        * dash
        * dot
        * chain_dot
        * chain_dash
        The default is: solid.
    :type text_border_line_style: str


    :param text_border_colour: Colour of border around text box (Full choice of colours). The possible values:

        * background
        The default is: blue.
    :type text_border_colour: str


    :param text_border_thickness: Thickness of text box border. The default is: 1.
    :type text_border_thickness: int


    :rtype: None


.. minigallery:: metview.mtext
    :add-heading:

