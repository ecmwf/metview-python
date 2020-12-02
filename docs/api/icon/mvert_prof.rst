
mvert_prof
=========================

.. container::
    
    .. container:: leftside

        .. image:: /_static/MVPROFILE.png
           :width: 48px

    .. container:: rightside

        This function performs the same task as the `Vertical Profile Data <https://confluence.ecmwf.int/display/METV/Vertical+Profile+Data>`_ icon in Metview’s user interface. It accepts its parameters as keyword arguments, described below.


.. py:function:: mvert_prof(**kwargs)
  
    Description comes here!


    :param data: 
    :type data: str


    :param input_mode: Specifies whether to derive the vertical profile for a ``"point"`` or an ``"area"``. In ``"point"`` mode the nearest grid``"point"`` to the ``"point"`` specified will be selected. The default value is ``"point"``.
    :type input_mode: {"point", "nearest_gridpoint", "area"}, default: "point"


    :param point: Specifies the coordinates of the ``point`` for which the vertical profile is calculated. Enter coordinates (lat/long) of a ``point`` separated by a "/". Alternatively, use the coordinate assist button.
    :type point: float or list[float], default: 0


    :param area: 
    :type area: float or list[float], default: 30


    :param output_mode: Specifies the output extraction mode. Valid values are "normal" or "rttov". The "rttov" option is only valid internally at ECMWF and it is used in the context of the "rttov" model application.
    :type output_mode: {"normal", "rttov"}, default: "normal"


    :param water_type: Valid values are Fresh Water or Ocean Water. Available when ``output_mode`` is Rttov.
    :type water_type: {"0", "1"}, default: "0"


    :param cloud_top_pressure: 
    :type cloud_top_pressure: number, default: 0.0


    :param cloud_fraction: 
    :type cloud_fraction: number, default: 0.0


    :rtype: None
