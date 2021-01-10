
pscairo_output
=========================

Defines a Postscript plot output driver based on the Cairo library.

.. py:function:: pscairo_output(**kwargs)
  
    Defines a Postscript plot output driver based on the Cairo library.


    :param output_title: 
    :type output_title: str, default: "magics++ plot"

    :param output_name_first_page_number: 
    :type output_name_first_page_number: {"on", "off"}, default: "on"

    :param output_file_minimal_width: 
    :type output_file_minimal_width: number, default: 1

    :param output_debug: 
    :type output_debug: {"on", "off"}, default: "off"

    :param output_filelist: 
    :type output_filelist: {"on", "off"}, default: "off"

    :param output_filelist_name: 
    :type output_filelist_name: str, default: "magics_outputs.lst"

    :param output_ps_colour_model: 
    :type output_ps_colour_model: {"rgb", "cmyk", "monochrome", "gray", "cmyk_monochrome", "cmyk_gray"}, default: "rgb"

    :param output_ps_scale: 
    :type output_ps_scale: number, default: 1.0

    :param output_ps_split: 
    :type output_ps_split: {"on", "off"}, default: "off"

    :rtype: :class:`Request`
