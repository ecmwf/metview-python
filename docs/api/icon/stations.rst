
stations
=========================

.. container::
    
    .. container:: leftside

        .. image:: /_static/STATIONS.png
           :width: 48px

    .. container:: rightside

		Allows to specify a geographical location which may coincide with a meteorological (WMO) station. It is also equipped with a search facility applicable to the ECMWF’s station database. If the location is a meteorological station, you can search the database of stations by ``name``, ``ident``, ``wmo_block``, ``position`` or ``area``.


		.. note:: This function performs the same task as the `Stations <https://confluence.ecmwf.int/display/METV/stations>`_ icon in Metview’s user interface. It accepts its parameters as keyword arguments, described below.


.. py:function:: stations(**kwargs)
  
    Defines a geographical location which may coincide with a meteorological (WMO) station.


    :param search_stations_database: Selects the type of station location to be entered. When the value is "wmo" a station can be chosen from Metview's built-in WMO station database. If the value is "no" you can set an arbitrary location.
    :type search_stations_database: {"wmo", "no"}, default: "wmo"

    :param search_key: Specifies which parameter should be used in the search of the WMO stations database. Only available when ``search_stations_database`` is "wmo".
    :type search_key: {"name", "ident", "wmo_block", "position", "area"}, default: "name"

    :param name: Specifies the location name. If ``search_stations_database`` is set to "no" you are dealing with an arbitrary location and you may enter any name of your choice. If ``search_stations_database`` is set to "wmo" this should be the name of the required station. You need the exact name of the station so you should be careful with the spelling which is in accordance to WMO. This tries to match the original language spelling, hence an English speaking user should not look for Copenhagen, but rather Kobenhavn.
    :type name: str or list[str], default: "heathrow"

    :param position: Specifies the exact geographical coordinates (as [lat, lon]) of the location of interest. If ``search_stations_database`` is set to "no" you specify the coordinates of an arbitrary location, while if it is set to "wmo" you specify the location of a meteorological station. It may happen that you do not know the exact coordinates of the station. In this case, you can specify a geographical tolerance in ``threshold``.
    :type position: float or list[float], default: [51.38, -0.78]

    :param height: Specifies the height of the station. If ``search_stations_database`` is set to "no" you can specify the ``height`` here, otherwise the station's height is retrieved automatically from the database.
    :type height: number, default: 0

    :param threshold: Specifies a geographical tolerance in degrees for the coordinates of a meteorological station specified in ``position``. This is only available when ``search_stations_database`` is "wmo" and ``search_key`` is "position".
    :type threshold: number, default: 0.1

    :param ident: Specifies the station's WMO numerical identifier which is a 5 digit number. If you are in doubt about the identifier, use the assist button. This is a station assist button and it launches the Stations database search tool. Only available if ``search_stations_database`` is "wmo" and ``search_key`` is "ident".
    :type ident: number, default: 03772

    :param wmo_block: Specifies the station's WMO block which is a 2 digit number corresponding to a geographical area. If you are in doubt about the WMO block, use the assist button. This is a station assist button and it launches the Stations database search tool. Only available if ``search_stations_database`` is "wmo" and ``search_key`` is "wmo_block".
    :type wmo_block: number, default: 03

    :param area: Specifies the coordinates of an area (as [north, west, south, east]) where meteorological stations of interest are located. Only available if ``search_stations_database`` is "wmo" and ``search_key`` is "area".
    :type area: list[float], default: [52, -1, 51, 0]

    :param fail_on_error: 
    :type fail_on_error: {"yes", "no"}, default: "yes"

    :rtype: :class:`Request`
.. include:: /gallery/backref/stations.rst