
reprojection
=========================

.. container::
    
    .. container:: leftside

        .. image:: /_static/REPROJECTION.png
           :width: 48px

    .. container:: rightside

		Interpolates gridded data in GRIB format into a lat-lon grid. In the past it was used to visualise data on certain geometries. At present, all these data can be directly visualised, so :func:`reprojection` is need not be used.


		.. note:: This function performs the same task as the `Reprojection <https://confluence.ecmwf.int/display/METV/reprojection>`_ icon in Metview’s user interface. It accepts its parameters as keyword arguments, described below.


.. py:function:: reprojection(**kwargs)
  
    Interpolates gridded data in GRIB format into a lat-lon grid.


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

    :rtype: :class:`fieldset`


.. mv-minigallery:: reprojection

