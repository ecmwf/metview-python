
mtext
=========================

.. container::
    
    .. container:: leftside

        .. image:: /_static/MTEXT.png
           :width: 48px

    .. container:: rightside

		This is the visual definition for specifying how plot titles and text boxes are displayed.


		.. note:: This function performs the same task as the `Text Plotting <https://confluence.ecmwf.int/display/METV/Text+Plotting>`_ icon in Metview’s user interface. It accepts its parameters as keyword arguments, described below.


.. py:function:: mtext(**kwargs)
  
    Defines the plot title and text boxes.


    :param text_line_count: The number of lines of text to be plotted.
    :type text_line_count: number, default: 1

    :param text_line_1: Text for line 1.
    :type text_line_1: str, default: ["<magics_title, >"]

    :param text_line_2: Text for line 2.
    :type text_line_2: str

    :param text_line_3: Text for line 3.
    :type text_line_3: str

    :param text_line_4: Text for line 4.
    :type text_line_4: str

    :param text_line_5: Text for line 5.
    :type text_line_5: str

    :param text_line_6: Text for line 6.
    :type text_line_6: str

    :param text_line_7: Text for line 7.
    :type text_line_7: str

    :param text_line_8: Text for line 8.
    :type text_line_8: str

    :param text_line_9: Text for line 9.
    :type text_line_9: str

    :param text_line_10: Text for line 10.
    :type text_line_10: str

    :param text_colour: Colour of the text.
    :type text_colour: str, default: "navy"

    :param text_font: Font name.
    :type text_font: {"arial", "courier", "helvetica", "times", "serif", "sansserif", "symbol"}, default: "sansserif"

    :param text_font_style: Font style.
    :type text_font_style: {"normal", "bold", "italic", "bolditalic"}, default: "normal"

    :param text_font_size: Font size, specified in cm.
    :type text_font_size: str, default: "0.3"

    :param text_justification: How text is to be positioned in each line.
    :type text_justification: {"left", "centre", "right"}, default: "centre"

    :param text_orientation: Orientation of the text.
    :type text_orientation: {"horizontal", "top_bottom", "bottom_top"}, default: "horizontal"

    :param text_lines: Specifies all the text lines in one go as a list. When it is set ``text_line_count`` and ``text_line_N`` are ignored.
    :type text_lines: str or list[str]

    :param text_mode: Specifies whether text will be a title or user positioned.
    :type text_mode: {"title", "positional"}, default: "title"

    :param text_box_x_position: X coordinate of lower left corner of text box. (Relative to ``page_x_position`` in the parent view).
    :type text_box_x_position: number, default: -1

    :param text_box_y_position: Y coordinate of lower left corner of text box. (Relative to ``page_Y_position`` in the parent view).
    :type text_box_y_position: number, default: -1

    :param text_box_x_length: Length of text box in X direction.
    :type text_box_x_length: number, default: -1

    :param text_box_y_length: Length of text box in Y direction.
    :type text_box_y_length: number, default: -1

    :param text_box_blanking: Enables blanking in the text box.
    :type text_box_blanking: {"on", "off"}, default: "off"

    :param text_border: Plots border around text box.
    :type text_border: {"on", "off"}, default: "off"

    :param text_border_line_style: Line style of border around text box.
    :type text_border_line_style: {"solid", "dash", "dot", "chain_dot", "chain_dash"}, default: "solid"

    :param text_border_colour: Colour of border around text box.
    :type text_border_colour: str, default: "blue"

    :param text_border_thickness: Thickness of text box border.
    :type text_border_thickness: int, default: 1

    :rtype: :class:`Request`


.. mv-minigallery:: mtext

