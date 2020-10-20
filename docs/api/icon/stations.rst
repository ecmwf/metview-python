
stations
=========================

.. container::
    
    .. container:: leftside

        .. image:: /_static/STATIONS.png
           :width: 48px

    .. container:: rightside

        This icon represents the `stations <https://confluence.ecmwf.int/display/METV/stations>`_ icon in Metview's user interface.


.. py:function:: stations(**kwargs)
  
    Description comes here!


    :param search_stations_database: Selects the type of station location to be entered. The possible values are as follows:

         *  Yes - Wmo Station allows you to choose a station from the WMO station database.
         *  No - Location allows you to choose instead an arbitrary location.
    :type search_stations_database: str


    :param search_key: Specifies which parameter should be used in the search of the stations database. Only available for ``search_stations_database`` set to Yes - Wmo Station. Options are ``name`` , ``ident`` , ``wmo_block`` , ``position`` and ``area``. Each option when selected activates the parameter of the same ``name`` that follows in the editor.
    :type search_key: str


    :param name: Specifies the location ``name``. If ``search_stations_database`` is set to No - Location you are dealing with an arbitrary location and you may enter any ``name`` of your choice. If ``search_stations_database`` is set to Yes - WMO Station this should be the ``name`` of the required station. You need the exact ``name`` of the station so you should be careful with the spelling which is in accordance to WMO. This tries to match the original language spelling, hence an English speaking user should not look for Copenhagen or Oporto, but rather Kobenhavn and Porto.

         If you are in doubt about the spelling or know only part of the ``name`` you can enter a guess string (e.g. "kobe" or "port") and hit return. Then click the stations help button to the left of the text field - you will see a list of stations whose ``name`` starts with the guess string.

         ![](/download/attachments/133238824/image2019-2-21_10-47-32.png?version=1&modificationDate=1550746052318&api=v2)

         Click the one you want and its ``name`` will replace the guess string in the input field.
    :type name: str or list[str]


    :param position: Specifies the exact geographical coordinates of the location of interest. Enter latitude and longitude separated by a "/". To choose a location interactively use the coordinate assist button. If ``search_stations_database`` is set to No - Location you specify the coordinates of an arbitrary location. If ``search_stations_database`` is set to Yes -WMO Station you specify the location of a meteorological station.

         It may happen that you do not know the exact coordinates of the station. In this case, you can specify a geographical tolerance in the following parameter, ``threshold``. If you need to use the Stations database search tool, run it from the main User Interface or from one of the other parameter’s station assist button (which you must select in ``search_key`` ).
    :type position: float or list[float]


    :param height: Specifies the ``height`` of the station. If ``search_stations_database`` is set to No - Location then you can specify the ``height`` here; otherwise the station’s ``height`` is retrieved automatically from the database.
    :type height: number


    :param threshold: Specifies a geographical tolerance in degrees for the coordinates of a meteorological station specified in ``position``. This is only available for ``search_stations_database`` set to Yes - WMO Station and ``search_key`` set to ``position``.
    :type threshold: number


    :param ident: Specifies the station’s WMO numerical ``ident``ifier which is a 5 digit number. If you are in doubt about the ``ident``ifier, use the assist button. This is a station assist button and it launches the Stations database search tool. Only available if ``search_stations_database`` is set to Yes - WMO Station and ``search_key`` to ``ident``.
    :type ident: number


    :param wmo_block: Specifies the station’s ``wmo_block`` which is a 2 digit number corresponding to a geographical ``area``. If you are in doubt about the ``wmo_block``, use the assist button. This is a station assist button and it launches the Stations database search tool. Only available if ``search_stations_database`` is set to Yes - WMO Station and ``search_key`` to ``wmo_block``.
    :type wmo_block: number


    :param area: Specifies the coordinates of an ``area`` where meteorological stations of interest are located. Enter coordinates (lat/long) of an ``area`` separated by a "/" (top left lat and long, bottom right lat and long); alternatively, use the coordinate assist button. Only available if ``search_stations_database`` is set to Yes - WMO Station and ``search_key`` to ``area``. If you need to use the Stations database search tool, run it from the main User Interface or from one of the other parameter’s station assist button (which you must select in ``search_key`` ).
    :type area: float or list[float]


    :param fail_on_error: 
    :type fail_on_error: str


    :rtype: None


.. minigallery:: metview.stations
    :add-heading:

