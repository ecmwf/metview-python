
geo_to_kml
=========================

.. container::
    
    .. container:: leftside

        .. image:: /_static/GEOTOKML.png
           :width: 48px

    .. container:: rightside

		Converts :class:`Geopoints` into KML format.


		.. note:: This function performs the same task as the `Geopoints To KML <https://confluence.ecmwf.int/display/METV/Geopoints+To+KML>`_ icon in Metview’s user interface. It accepts its parameters as keyword arguments, described below.


.. py:function:: geo_to_kml(**kwargs)
  
    Converts :class:`Geopoints` into KML format.


    :param geopoints: 
    :type geopoints: str

    :param output_mode: 
    :type output_mode: {"poi", "tra", "pol"}, default: "poi"

    :param output_format: 
    :type output_format: {"kmz", "kml"}, default: "kml"

    :param area: 
    :type area: float or list[float], default: 90

    :rtype: :class:`Request`
