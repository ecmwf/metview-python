
bufr_picker
=========================

.. container::
    
    .. container:: leftside

        .. image:: /_static/BUFRPICKER.png
           :width: 48px

    .. container:: rightside

        This function performs the same task as the `Bufr Picker <https://confluence.ecmwf.int/display/METV/bufr+picker>`_ icon in Metview’s user interface. It accepts its parameters as keyword arguments, described below.


.. py:function:: bufr_picker(**kwargs)
  
    Description comes here!


    :param data: Specifies the input data.
    :type data: :class:`Bufr`


    :param output: Specifies the output :class:`Geopoints` format.
    :type output: {"geopoints", "polar_vector", "xy_vector", "ncols"}, default: "geopoints"


    :param parameter: 
    :type parameter: str or list[str], default: "012163"


    :param missing_data: If set to "ignore", missing data is not included in the output file. If set to "include", missing data will be output to the geopoints file, its value being set to that specified by ``missing_data_value``. Note that when ``output`` is one of the two geopoints vector formats, the observation is considered missing if one or both of the parameters are missing.
    :type missing_data: {"ignore", "include"}, default: "ignore"


    :param missing_data_value: Available only for ``missing_data`` set to "include". Any missing observations will be output as this value (default 0). It is wise, therefore, to ensure that this value is outwith the range of possible values for the requested parameter(s).
    :type missing_data_value: number, default: 0


    :param coordinate_descriptors: 
    :type coordinate_descriptors: str or list[str], default: "5042"


    :param coordinate_values: 
    :type coordinate_values: str or list[str], default: "all"


    :param fail_on_error: If set to "yes", then any error encountered when trying to decode the input data will result in the module failing. If set to "no", then any such errors will not be fatal, and an empty data file will be returned.
    :type fail_on_error: {"yes", "no"}, default: "yes"


    :rtype: None
