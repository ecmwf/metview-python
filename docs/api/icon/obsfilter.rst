
obsfilter
=========================

.. container::
    
    .. container:: leftside

        .. image:: /_static/OBSFILTER.png
           :width: 48px

    .. container:: rightside

        This icon represents the `Observation Filter <https://confluence.ecmwf.int/display/METV/Observation+Filter>`_ icon in Metview's user interface.


.. py:function:: obsfilter(**kwargs)
  
    Description comes here!


    :param data: Drop any icon containing or returning BUFR ``data``. This may be a MARS Retrieval (of BUFR) icon, a BUFR file icon or an Observation Filter icon (provided it ``output``s BUFR, not geopoints). The default icon is a MARS Retrieval for 4 day old 12 UTC synoptic observations for the whole globe.
    :type data: str


    :param output: Specifies the ``output`` format you want. Specify one of the geopoints formats ( Geographical Points , Geographical Polar Vectors or Geographical X Y Vectors ) if you want to plot just one or two ``parameter``s or if you want to do calculations (including calculations with GRIB fields - combining geopoints with GRIB fields ``output``s geopoints). The ``parameter``s that follow - ``parameter`` , ``level`` , First ``level`` , Second ``level`` and Ocurrence Index - are not available if you specify BUFR ``output``, as BUFR ``output`` must be formed by whole messages (of a given type).
    :type output: str


    :param parameter: Available only for ``output`` set to one of the geopoints formats (see above). To specify a ``parameter`` enter its unique descriptor value (a numerical code). Geographical Polar Vectors and Geographical XY Vectors require two descriptors, separated by a slash ( / ). The descriptor value is of the form XXYYY , where XX defines the class (e.g. 12 = Temperature class) and YYY the ``parameter`` within that class (e.g. 12004 = Dry bulb Temperature at 2m). These descriptor values are different from the ones of the GRIB format. If you do not know the descriptor value, click-left on the assist button to obtain a check list of ``parameter``s and associated descriptors. This list only contains the most common ``parameter``s. If the one you need is not on the list you have to look up its descriptor value in the "BUFR User Guide and Reference Manual" (ECMWF Meteorological Bulletin M1.4/4) - see "BUFR Table B", pages 99-108. The significance of code and flag values for non-quantitative ``parameter``s are given in the same reference, in "BUFR code table", pages 111-154.
    :type parameter: str or list[str]


    :param missing_data: Available only for ``output`` set to one of the geopoints formats (see above). If set to Ignore , missing ``data`` is not included in the ``output`` file; this is the default behaviour. If set to Include , missing ``data`` will be ``output`` to the geopoints file, its value being set to that specified by Missing ``data`` Value . Note that when the ``output`` format is one of the two geopoints vector formats, the test for missing ``data`` is only performed on the first ``parameter``.
    :type missing_data: str


    :param missing_data_value: Available only for ``output`` set to one of the geopoints formats and Missing ``data`` set to Include . Any missing observations will be ``output`` as this value (default 0). It is wise, therefore, to ensure that this value is outwith the range of possible values for the requested ``parameter``(s). Note that when the out- put format is one of the two geopoints vector formats, the test for missing ``data`` is only performed on the first ``parameter``.
    :type missing_data_value: number


    :param level: Available only for ``output`` set to one of the geopoints formats (see above). Specify one of Surface , Single ``level`` , Layer and Occurrence . What you specify here must be consistent with the ``parameter`` you specified for filtering.
    :type level: str


    :param level_descriptor: 
    :type level_descriptor: str


    :param first_level: Available only for ``output`` set to one of the geopoints formats (see above) and ``level`` set to Single ``level`` or Layer. Specify the ``level`` of the observation in hPa. If Layer was chosen for ``level`` , the value will specify the bottom ``level`` of the layer. The assist button gives you a check list of most common pressure ``level``s in hPa.
    :type first_level: str


    :param second_level: Available only for ``output`` set to one of the geopoints formats (see above) and ``level`` set to Layer . Specify the top ``level`` of the layer in hPa.
    :type second_level: str


    :param occurrence_index: Only available if ``level`` set to Occurrence. Specify the numerical index of a ``parameter`` that has several values within one observation (e.g. cloud amount on different ``level``s or water temperature at

         different depths).
    :type occurrence_index: number


    :param observation_types: Specifies the numerical code or text string for the desired observation type. The assist button provides a partial list of available text strings and associated types. ``observation_types`` are standardised by WMO and are fixed from place to place. See the "BUFR User Guide and Reference Manual" (ECMWF Meteorological Bulletin M1.4/4) - "BUFR Table A", page 97 - for a complete list of numerical codes.
    :type observation_types: str or list[str]


    :param observation_subtypes: Specifies the numerical code or text string for the desired observation subtype. The assist button provides a list of available numerical codes and associated subtypes. Note that institutions are free to define their own subtypes hence these are not an international standard.
    :type observation_subtypes: str or list[str]


    :param date_and_time_from: 
    :type date_and_time_from: str


    :param date: Specifies observation(s) ``date``. It is not possible to specify a range of ``date``s. If you are filtering a new MARS Retrieval, remember that archived observations are always a couple of days old - trying to retrieve yesterday’s observations is likely to fail. Allowed formats for the ``date`` are as follows :

         * Absolute as YYYYMMDD
         * Relative as -n ; n is the number of days before today ( -1 = yesterday)
         * To specify a number of different ``date``s use : YYYYMMDD1/YYYYMMDD2/...

         Specifying a value for ``date`` requires setting a value for ``time`` (if both are set to ANY , changing ``date`` will change ``time`` from ANY to 12).
    :type date: str


    :param time: Specifies ``time`` of the observation(s). Required format is HHMM. It is not possible to specify a range of ``time``s.
    :type time: str


    :param resolution_in_mins: Specifies a ``time`` window in minutes around the value chosen for ``time`` .
    :type resolution_in_mins: number


    :param wmo_blocks: Specifies a WMO block number. These identify a geographical region, e.g. 02 for Sweden and Finland, 16 for Italy and Greece.
    :type wmo_blocks: str or list[str]


    :param wmo_stations: Specifies a list of ``wmo_stations``, using the five digit station identifier (the first two of which are the WMO block number).
    :type wmo_stations: str or list[str]


    :param location_filter: Specifies one of No ``location_filter`` , ``area`` , Cross-Section ``line``. This allows you to filter observations contained within a geographical ``area`` or within a given proximity to a geographical ``line`` between two points.
    :type location_filter: str


    :param area: Specifies the coordinates of the ``area`` of interest. Enter coordinates (lat/long) of an ``area`` separated by a "/" (top left lat and long, bottom right lat and long); alternatively, use the coordinate assist button.
    :type area: float or list[float]


    :param line: Specifies the coordinates of a transect ``line``. Enter coordinates (lat/long) of a ``line`` separated by a "/" (easternmost lat and long, westernmost lat and long); alternatively, use the coordinate assist button. This will filter all stations close enough to the ``line`` - how close is defined by ``delta_in_km`` .
    :type line: float or list[float]


    :param delta_in_km: Specifies the width of the cross section ``line`` defined in ``line``.
    :type delta_in_km: number


    :param custom_filter: This allows you to filter observations of a given ``parameter`` according to its value. You can select observations equal to a value ( Filter by Value ) or within/outside a given range of values ( Filter by Range / Filter by Exclude Range ). Note that naturally you must specify one observed ``parameter`` to be filtered in this way.
    :type custom_filter: str


    :param custom_parameter: Specifies the descriptor value of the ``parameter`` you want to filter according to value.
    :type custom_parameter: str


    :param custom_values: Specifies the desired numerical values for filtering by value. You may specify more than one value, separated by a forward slash (e.g. n1/n2 ). If you Filter by Value, observations of the selected ``parameter`` with the value equal to n1 or n2 are selected (you may specify more than two values). If you Filter by Range , observations of the selected ``parameter`` with the value within the n1 to n2 interval are selected. If you Filter by Exclude Range, observations of the selected ``parameter`` with the value outside the n1 to n2 interval are selected.
    :type custom_values: float or list[float]


    :param fail_on_error: 
    :type fail_on_error: str


    :param fail_on_empty_output: 
    :type fail_on_empty_output: str


    :rtype: None


.. minigallery:: metview.obsfilter
    :add-heading:

