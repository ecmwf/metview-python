
cleanfile
=========================

.. container::
    
    .. container:: leftside

        .. image:: /_static/CLEANFILE.png
           :width: 48px

    .. container:: rightside

		Removes padding or unwanted data transmission headers from the beginning of binary data files so that Metview could properly recognise them as a GRIB or BUFR file.


		.. note:: This function performs the same task as the `Clean File <https://confluence.ecmwf.int/display/METV/Clean+File>`_ icon in Metview’s user interface. It accepts its parameters as keyword arguments, described below.


.. py:function:: cleanfile(**kwargs)
  
    Removes padding or unwanted data transmission headers from the beginning of binary data files so that Metview could properly recognise them as a GRIB or BUFR file.


    :param path: Specifies the path to the input data.
    :type path: str

    :param data: Specifies the input as an object. If both ``data`` and ``path``  are specified ``data`` takes precedence.
    :type data: :class:`Binary`

    :param skip_hirlam_custom_record: Skips custom records for HIRLAM data.
    :type skip_hirlam_custom_record: {"no", "yes"}, default: "no"

    :rtype: :class:`Fieldset` or :class:`Bufr`


.. mv-minigallery:: cleanfile

