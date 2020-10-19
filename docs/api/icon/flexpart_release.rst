
flexpart_release
=========================

.. container::
    
    .. container:: leftside

        .. image:: /_static/FLEXPART_RELEASE.png
           :width: 48px

    .. container:: rightside

        This icon performs an ODB/SQL query on an ODB database (ODB-1) or file (ODB-2). The result is always an ODB file (in ODB-2 format).


.. py:function:: flexpart_release(**kwargs)
  
    Description comes here!


    :param name: Specifies the ``name`` of the release (maximum 40 characters).
    :type name: str


    :param starting_date: Specifies the beginning date of the release in YYYYMMDD format.  Relative dates with respect to the run date of the FLEXPART simulation (defined by parameter ``starting_date`` in :func:`flexpart_run` are allowed: e.g. 0 means run date, 1 means the day after the run date, etc. The default value is 0.
    :type starting_date: str


    :param starting_time: Specifies the beginning time of the release in HH[:MM[:SS]] format.
    :type starting_time: str


    :param ending_date: Specifies the ``ending_date`` of the release in YYYYMMDD format.  Relative dates with respect to the run date of the FLEXPART simulation (defined by parameter ``starting_date`` in :func:`flexpart_run` are allowed: e.g. 0 means run date, 1 means the day after the run date, etc. The default value is 0.
    :type ending_date: str


    :param ending_time: Specifies the ``ending_time`` of the release in HH[:MM[:SS]] format.
    :type ending_time: str


    :param area: Specifies the ``area`` for the release in degrees in S/W/N/E format. The default value is -90/-180/90/180.
    :type area: float or list[float]


    :param level_units: Specifies the units for the release vertical extent. The possible values are agl (metres above ground level), asl (metres above sea level) and hPa. The default value is agl.
    :type level_units: str


    :param top_level: Specifies the ``top_level`` of the release.
    :type top_level: number


    :param bottom_level: Specifies the ``bottom_level`` of the release.
    :type bottom_level: number


    :param particle_count: Specifies the number of particles released.
    :type particle_count: number


    :param masses: Specifies the list of total ``masses`` of the released species. The number of ``masses`` given here must match the number of species defined via the Release Species parameter of :func:`flexpart_run`. The actual units of the ``masses`` is defined by the Release Units parameter of :func:`flexpart_run`. Please note that for backward simulations any non-zero positive value can stand here because the output is normalised by this value!
    :type masses: float or list[float]


    :rtype: None


.. minigallery:: metview.flexpart_release
    :add-heading:

