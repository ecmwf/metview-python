
thermo_grib
=========================

.. container::
    
    .. container:: leftside

        .. image:: /_static/THERMODATA.png
           :width: 48px

    .. container:: rightside

		Derives (and returns) a Thermodynamic diagram data unit from GRIB data (:class:`Fieldset`). In such a diagram, temperature, humidity (represented by the dew point) and wind values are displayed with respect to pressure. All the three major thermodynamic diagrams types re supported in Metview: Tephigram, Skew-T and Emagram.
		
		The resulting data can plotted (using a default visualisation and with the plot area based on the range of data values) or saved as a :class:`NetCDF` data file using :func:`write`.
		
		If access to the output computed values is not required, or for more control of the plotting, use :func:`thermoview`.


		.. note:: This function performs the same task as the `Thermo Data <https://confluence.ecmwf.int/display/METV/Thermo+Data>`_ icon in Metview’s user interface. It accepts its parameters as keyword arguments, described below.


.. py:function:: thermo_grib(**kwargs)
  
    Derives (and returns) a Thermodynamic diagram data unit from GRIB data.


    :param data: Specifies the GRIB data to be used in the plotting of a thermodynamic diagram. The data should include gridded fields of temperature and specific humidity. These parameters must have the same number of levels and they will be used to compute the dew point parameter. :class:`Fieldset` u and v wind components are optional, but if given a wind profile will be plotted in the thermodynamic view. These two components must have the same number of levels, but not necessarily have the same number of levels of temperature and specific humidity. If the data is given on ECMWF model levels then a Logarithm of Surface Pressure (LNSP) field must be provided too.
    :type data: :class:`Fieldset`

    :param point_selection: Specifies how the geographical location, for which the diagram is to be plotted, will be selected.
    :type point_selection: {"coordinates", "area_average", "station"}, default: "coordinates"

    :param coordinates: Specifies the geographical location (as [lat, lon]) for which the diagram is to be plotted. Available when ``point_selection`` is "coordinates".
    :type coordinates: list[float], default: [0, 0]

    :param area_average: Specifies a geographical area over which an area average value will be used, instead of a point value, to produce the diagram.  The area is defined as [north, west, south, east]. Available when ``point_selection`` is "area_average".
    :type area_average: list[float], default: [30, -30, -30, 30]

    :param station: Specifies the location as a :func:`stations`` object for which the diagram is to be plotted. Available if ``point_selection` is "station".
    :type station: :func:`stations``

    :param point_extraction: Specifies the way to calculate values at the point location for GRIB thermodynamic diagrams. The possible options are:
		
		* "interpolate": interpolate values from the four surrounding grid points.
		* "nearest_gridpoint": use the data from the nearest grid point.
    :type point_extraction: {"interpolate", "nearest_gridpoint"}, default: "interpolate"

    :param dew_point_formulation: Specifies the equation to compute the dew point.
    :type dew_point_formulation: {"saturation_over_water", "mixed_phase_0_to\_\-23"}, default: "saturation_over_water"

    :param temperature_param: Specifies the ecCodes paramId used to identify the temperature in the input data.
    :type temperature_param: number, default: 130

    :param specific_humidity_param: Specifies the ecCodes paramId used to identify the specific humidity in the input data.
    :type specific_humidity_param: number, default: 133

    :param lnsp_param: Specifies the ecCodes paramId used to identify the Logarithm of Surface Pressure (LNSP) in the input data.
    :type lnsp_param: number, default: 152

    :param u_wind_param: Specifies the ecCodes paramId used to identify the U wind component in the input data.
    :type u_wind_param: number, default: 131

    :param v_wind_param: Specifies the ecCodes paramId used to identify the V wind component in the input data.
    :type v_wind_param: number, default: 132

    :rtype: :class:`NetCDF`
.. include:: /gallery/backref/thermo_grib.rst