
mvert_prof
=========================

.. container::
    
    .. container:: leftside

        .. image:: /_static/MVPROFILE.png
           :width: 48px

    .. container:: rightside

        This icon represents the `Vertical Profile Data <https://confluence.ecmwf.int/display/METV/Vertical+Profile+Data>`_ icon in Metview's user interface.


.. py:function:: mvert_prof(**kwargs)
  
    Description comes here!


    :param data: 
    :type data: str


    :param input_mode: Specifies whether to derive the vertical profile for a ``point`` or an ``area``. In ``point`` mode the nearest grid``point`` to the ``point`` specified will be selected. The default value is ``point``.
    :type input_mode: str


    :param point: Specifies the coordinates of the ``point`` for which the vertical profile is calculated. Enter coordinates (lat/long) of a ``point`` separated by a "/". Alternatively, use the coordinate assist button.
    :type point: float or list[float]


    :param area: 
    :type area: float or list[float]


    :param output_mode: Specifies the output extraction mode. Valid values are Normal or Rttov. The Rttov option is only valid internally at ECMWF and it is used in the context of the RTTOV model application.
    :type output_mode: str


    :param water_type: Valid values are Fresh Water or Ocean Water. Available when ``output_mode`` is Rttov.
    :type water_type: str


    :param cloud_top_pressure: 
    :type cloud_top_pressure: number


    :param cloud_fraction: 
    :type cloud_fraction: number


    :rtype: None


.. minigallery:: metview.mvert_prof
    :add-heading:

