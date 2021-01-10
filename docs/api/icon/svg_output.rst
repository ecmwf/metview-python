
svg_output
=========================

Defines an SVG plot output driver.

.. py:function:: svg_output(**kwargs)
  
    Defines an SVG plot output driver.


    :param output_title: Defines a title for the output which gets displayed if the format supports it.
    :type output_title: str, default: "magics++ plot"

    :param output_width: Defines the width of the image in pixels.
    :type output_width: number, default: 800

    :param output_name_first_page_number: Determines whether, for the first page of multipage output, the number is included in the filename.
    :type output_name_first_page_number: {"on", "off"}, default: "on"

    :param output_file_minimal_width: Width of numbering of multi-file outputs (eg, 'plot.1.png' or 'plot.001.png').
    :type output_file_minimal_width: number, default: 1

    :param output_debug: Defines if extra debug information are written in the output file.
    :type output_debug: {"on", "off"}, default: "off"

    :param output_filelist: Defines if a list of all generated files should be written into a file.
    :type output_filelist: {"on", "off"}, default: "off"

    :param output_filelist_name: Defines the name of the file containing the list of generated files.
    :type output_filelist_name: str, default: "magics_outputs.lst"

    :param output_svg_desc: Defines a text describing the content of the SVG output.
    :type output_svg_desc: str

    :param output_svg_meta: Defining meta data in RDF to be added to the SVG output.
    :type output_svg_meta: str

    :param output_svg_use_external_files: Can the SVG driver use external files for cell and image plotting. External files will reduce the SVG file size but add an external dependency!
    :type output_svg_use_external_files: {"on", "off"}, default: "on"

    :param output_svg_fix_size: Decides if the size is fixed in the SVG document.
    :type output_svg_fix_size: {"on", "off"}, default: "off"

    :param output_svg_logo_location: Sets where the (ECMWF) logo can be found.
    :type output_svg_logo_location: {"inline", "share", "local"}, default: "inline"

    :rtype: :class:`Request`
