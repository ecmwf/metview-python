
grib_to_geo
=========================

.. container::
    
    .. container:: leftside

        .. image:: /_static/GRIB_TO_GEO.png
           :width: 48px

    .. container:: rightside

        This icon represents the `Grib To Geopoints <https://confluence.ecmwf.int/display/METV/Grib+To+Geopoints>`_ icon in Metview's user interface.


.. py:function:: grib_to_geo(**kwargs)
  
    Description comes here!


    :param data: Specifies the ``data`` to be converted. Only the first field will be converted. Drop any icon containing or returning GRIB ``data``. This may be, for example, a GRIB file, a MARS Retrieval (of observations) icon or a Macro which returns GRIB ``data``.
    :type data: str


    :param geopoints_format: Specifies which of two ``geopoints_format``s should be used for the output - either Traditional (6 columns including date, time and level) or XYV (just 3 columns - longitude, latitude and value). See `Geopoints <https://confluence.ecmwf.int/display/METV/Geopoints>`_ for details of these formats.
    :type geopoints_format: str


    :param missing_data: 
    :type missing_data: str


    :rtype: None


.. minigallery:: metview.grib_to_geo
    :add-heading:

