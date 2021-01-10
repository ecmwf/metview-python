
ps_output
=========================

Defines a Postscript plot output driver.

.. py:function:: ps_output(**kwargs)
  
    Defines a Postscript plot output driver.


    :param output_title: Defines a title for the output which gets displayed if the format supports it.
    :type output_title: str, default: "magics++ plot"

    :param output_name_first_page_number: Determines whether, for the first page of multipage output, the number is included in the filename.
    :type output_name_first_page_number: {"on", "off"}, default: "on"

    :param output_file_minimal_width: Width of numbering of multi-file outputs (eg, 'plot.1.png' or 'plot.001.png').
    :type output_file_minimal_width: number, default: 1

    :param output_debug: Defines if extra debug information are written in the output file (PS, EPS, SVG) or console (PNG).
    :type output_debug: {"on", "off"}, default: "off"

    :param output_filelist: Defines if a list of all generated files should be written to a file.
    :type output_filelist: {"on", "off"}, default: "off"

    :param output_filelist_name: Defines the name of the file containing the list of generated files.
    :type output_filelist_name: str, default: "magics_outputs.lst"

    :param output_ps_colour_model: Defines the PostScript colour model.
    :type output_ps_colour_model: {"rgb", "cmyk", "monochrome", "gray", "cmyk_monochrome", "cmyk_gray"}, default: "rgb"

    :param output_ps_scale: Defines the PostScript scale between 0.1 and 1.0 (1.0 being the full page size).
    :type output_ps_scale: number, default: 1.0

    :param output_ps_split: Enables the output to be split into different (single page) PostScript files.
    :type output_ps_split: {"on", "off"}, default: "off"

    :rtype: :class:`Request`
