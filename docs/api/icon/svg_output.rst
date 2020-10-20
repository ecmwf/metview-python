
svg_output
=========================

.. py:function:: svg_output(**kwargs)
  
    Description comes here!


    :param output_title: Defines a title for the output which gets displayed if the format supports it. The default is: magics++ plot.
    :type output_title: str


    :param output_width: Defines the width of the image in pixels.(For GD and SVG). The default is: 800.
    :type output_width: number


    :param output_name_first_page_number: Determines whether, for the first page of multipage output, the number is included in the filename. The possible values:

        * on
        * off
        The default is: on.
    :type output_name_first_page_number: str


    :param output_file_minimal_width: Width of numbering of multi-file outputs (eg, 'plot.1.png' or 'plot.001.png'). The default is: 1.
    :type output_file_minimal_width: number


    :param output_debug: Defines if extra debug information are written in the output file (PS, EPS, SVG) or console (PNG). The possible values:

        * on
        * off
        The default is: off.
    :type output_debug: str


    :param output_filelist: Defines if a list of all generated files should be written. The possible values:

        * on
        * off
        The default is: off.
    :type output_filelist: str


    :param output_filelist_name: Defines the name of the file containing the list of generated files. The default is: magics_outputs.lst.
    :type output_filelist_name: str


    :param output_svg_desc: Defines a text describing the content of the SVG output.
    :type output_svg_desc: str


    :param output_svg_meta: Defining meta data in RDF to be added to the SVG output.
    :type output_svg_meta: str


    :param output_svg_use_external_files: Can the SVG driver use external files for cell and image plotting. External files will reduce the SVG file size but add an external dependency!. The possible values:

        * on
        * off
        The default is: on.
    :type output_svg_use_external_files: str


    :param output_svg_fix_size: Decides if the size is fixed in the SVG document. The possible values:

        * on
        * off
        The default is: off.
    :type output_svg_fix_size: str


    :param output_svg_logo_location: Sets where the (ECMWF) logo can be found. Possible values are 'inline'(default),'share' or 'local'. The default is: inline.
    :type output_svg_logo_location: str


    :rtype: None
