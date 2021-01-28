
grib_to_geo
=========================

.. container::
    
    .. container:: leftside

        .. image:: /_static/GRIB_TO_GEO.png
           :width: 48px

    .. container:: rightside

		Converts the first field in GRIB data (:class:`Fieldset`) into :class:`Geopoints`. The result is in ASCII format, and is stored as a set of separate points rather than as a grid. Note that :func:`grib_to_geo` can only converts GRIB data which is in a supported gridded format - for example, data in spherical harmonics cannot be converted. For the reverse computation, see :func:`geo_to_grib`.


		.. note:: This function performs the same task as the `Grib To Geopoints <https://confluence.ecmwf.int/display/METV/Grib+To+Geopoints>`_ icon in Metview’s user interface. It accepts its parameters as keyword arguments, described below.


.. py:function:: grib_to_geo(**kwargs)
  
    Converts GRIB data (:class:`Fieldset`) into :class:`Geopoints`.


    :param data: Specifies the GRIB data to be converted. Only the first field will be converted. In the user interface any icon containing or returning GRIB data can be used here (e.g. a GRIB icon or a MARS Retrieval icon etc).
    :type data: :class:`Fieldset`

    :param geopoints_format: Specifies which of two geopoints_formats should be used for the output - either "traditional" (6 columns including date, time and level) or "xyv" (just 3 columns - longitude, latitude and value). See `Geopoints <https://confluence.ecmwf.int/display/METV/Geopoints>`_ for details of these formats.
    :type geopoints_format: {"traditional", "xyv"}, default: "traditional"

    :param missing_data: 
    :type missing_data: {"ignore", "include"}, default: "include"

    :rtype: :class:`Geopoints`


.. mv-minigallery:: grib_to_geo

