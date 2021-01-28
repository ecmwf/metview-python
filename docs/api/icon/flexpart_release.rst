
flexpart_release
=========================

.. container::
    
    .. container:: leftside

        .. image:: /_static/FLEXPART_RELEASE.png
           :width: 48px

    .. container:: rightside

		Defines release conditions for running the `FLEXPART <https://confluence.ecmwf.int/display/METV/The+FLEXPART+interface>`_ Lagrangian particle dispersion model via :func:`flexpart_run`.


		.. note:: This function performs the same task as the `Flexpart Release <https://confluence.ecmwf.int/display/METV/flexpart+release>`_ icon in Metview’s user interface. It accepts its parameters as keyword arguments, described below.


.. py:function:: flexpart_release(**kwargs)
  
    Defines release conditions for :func:`flexpart_run`.


    :param name: Specifies the ``name`` of the release (maximum 40 characters).
    :type name: str

    :param starting_date: Specifies the beginning date of the release in YYYYMMDD format.  Relative dates with respect to the run date of the FLEXPART simulation (see parameter ``starting_date`` in :func:`flexpart_run`) are allowed: e.g. 0 means run date, 1 means the day after the run date, etc.
    :type starting_date: str, default: "0"

    :param starting_time: Specifies the beginning time of the release in HH[:MM[:SS]] format.
    :type starting_time: str

    :param ending_date: Specifies the ending date of the release in YYYYMMDD format.  Relative dates with respect to the run date of the FLEXPART simulation (see parameter ``starting_date`` in :func:`flexpart_run`) are allowed: e.g. 0 means run date, 1 means the day after the run date, etc.
    :type ending_date: str, default: "0"

    :param ending_time: Specifies the ending time of the release in HH[:MM[:SS]] format.
    :type ending_time: str

    :param area: Specifies the area for the release in degrees in S/W/N/E format.
    :type area: list[float], default: [-90, -180, 90, 180]

    :param level_units: Specifies the units for the release vertical extent. The possible values are:
		
		* "agl": metres above ground level
		* "asl": metres above sea level
		* "hpa": pressure in hPa
    :type level_units: {"agl", "asl", "hpa"}, default: "agl"

    :param top_level: Specifies the top level of the release.
    :type top_level: number

    :param bottom_level: Specifies the bottom level of the release.
    :type bottom_level: number

    :param particle_count: Specifies the number of particles released.
    :type particle_count: number

    :param masses: Specifies the list of total masses of the released species. The number of masses given here must match the number of species defined via the ``release_species`` parameter of :func:`flexpart_run`. The actual units of ``masses`` is defined by the ``release_units`` parameter of :func:`flexpart_run`. Please note that for backward simulations any non-zero positive value can stand here because the output is normalised by this value!
    :type masses: float or list[float]

    :rtype: :class:`Request`


.. mv-minigallery:: flexpart_release

