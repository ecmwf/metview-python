
png_output
=========================

Defines a PNG plot output driver.

.. py:function:: png_output(**kwargs)
  
    Defines a PNG plot output driver.


    :param output_title: Defines a title for the output.
    :type output_title: str, default: "magics++ plot"

    :param output_width: Defines the width of the image in pixels.
    :type output_width: number, default: 800

    :param output_name_first_page_number: Determines whether, for the first page of multipage output, the number is included in the filename.
    :type output_name_first_page_number: {"on", "off"}, default: "on"

    :param output_file_minimal_width: Width of numbering of multi-file outputs (eg. use 1 for 'plot.1.png', 3 for 'plot.001.png' etc).
    :type output_file_minimal_width: number, default: 1

    :param output_debug: Defines if extra debug information are written to the console (PNG).
    :type output_debug: {"on", "off"}, default: "off"

    :param output_filelist: Defines if a list of all the generated files should be written into a file.
    :type output_filelist: {"on", "off"}, default: "off"

    :param output_filelist_name: Defines the name of the file containing the list of generated files.
    :type output_filelist_name: str, default: "magics_outputs.lst"

    :param output_cairo_transparent_background: Defines the background to be transparent.
    :type output_cairo_transparent_background: {"on", "off"}, default: "off"

    :param output_cairo_antialias: Defines if lines are antialiased.
    :type output_cairo_antialias: {"on", "off"}, default: "on"

    :rtype: :class:`Request`
