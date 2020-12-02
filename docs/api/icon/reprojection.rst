
reprojection
=========================

.. container::
    
    .. container:: leftside

        .. image:: /_static/REPROJECTION.png
           :width: 48px

    .. container:: rightside

        This function performs the same task as the `Reprojection <https://confluence.ecmwf.int/display/METV/reprojection>`_ icon in Metview’s user interface. It accepts its parameters as keyword arguments, described below.


.. py:function:: reprojection(**kwargs)
  
    Description comes here!


    :param source: 
    :type source: str, default: "off"


    :param data: 
    :type data: str


    :param area: 
    :type area: float or list[float], default: -90


    :param resolution: 
    :type resolution: float or list[float], default: 1


    :param projection: 
    :type projection: {"latlong"}, default: "latlong"


    :param interpolation: 
    :type interpolation: {"nearest_neighbour"}, default: "nearest_neighbour"


    :rtype: None
