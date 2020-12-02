
cleanfile
=========================

.. container::
    
    .. container:: leftside

        .. image:: /_static/CLEANFILE.png
           :width: 48px

    .. container:: rightside

        This function performs the same task as the `Clean File <https://confluence.ecmwf.int/display/METV/Clean+File>`_ icon in Metview’s user interface. It accepts its parameters as keyword arguments, described below.


.. py:function:: cleanfile(**kwargs)
  
    Description comes here!


    :param path: Specifies the path to the input data.
    :type path: str


    :param data: Specifies the input as an object. If both ``data`` and ``path``  are specified ``data`` takes precedence.
    :type data: :class:`Fieldset` or :class:`BUFR`


    :param skip_hirlam_custom_record: Skips custom records for HIRLAM data.
    :type skip_hirlam_custom_record: {"no", "yes"}, default: "no"


    :rtype: None
