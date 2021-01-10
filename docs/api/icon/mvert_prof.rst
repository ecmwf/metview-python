
mvert_prof
=========================

.. container::
    
    .. container:: leftside

        .. image:: /_static/MVPROFILE.png
           :width: 48px

    .. container:: rightside

		Derives (and returns) a vertical profile data unit of upper air fields in GRIB format for a particular point location (or small area). For each upper air field, values are interpolated at the point location (or integrated over the small area).
		
		The vertical profile data can be plotted (using a default visualisation based on the range of data values) or saved as a NetCDF data file (:class:`Netcdf`) using :func:`write`.
		
		If access to the output computed values is not required, or for more control of the plotting, use  :func:`mvertprofview`. 
		


		.. note:: This function performs the same task as the `Vertical Profile Data <https://confluence.ecmwf.int/display/METV/Vertical+Profile+Data>`_ icon in Metview’s user interface. It accepts its parameters as keyword arguments, described below.


.. py:function:: mvert_prof(**kwargs)
  
    Derives (and returns) vertical profile data.


    :param data: Specifies the GRIB data from which to derive the vertical profile data. The input GRIB must specify a multi-level (pressure or model levels) upper air meteorological variable, in a latitude-longitude or Gaussian grid. If the input data is specified in model levels, you must include a Logarithm Of Surface Pressure (LNSP) field should you want the vertical axis of the plot in pressure levels rather than model levels when visualising the output. Note that the input fields should be on the same grid. If more than one time and/or forecast step is contained in ``data``, it returns a set of vertical profiles in the resulting data, but note that currently only the first of these will be plotted with :func:`plot`.
    :type data: :class:`Fieldset`

    :param input_mode: Specifies whether to derive the vertical profile for a "point" or an "area". Option "nearest_gridpoint" will take the nearest gridpoint to the ``point`` specified.
    :type input_mode: {"point", "nearest_gridpoint", "area"}, default: "point"

    :param point: Specifies the coordinates (as [lat, lon]) of the point for which the vertical profile is calculated. Enabled when ``input_mode`` is "point" or "nearest_gridpoint".
    :type point: list[float], default: [0, 0]

    :param area: Specifies the coordinates of the area (as [north, west, south, east]) over which the averages composing the vertical profile are calculated. Enabled when ``input_mode`` is "area".
    :type area: list[float], default: [30, -30, -30, 30]

    :param output_mode: Specifies the output extraction mode. The "rttov" option is only valid internally at ECMWF and it is used in the contex of the RTTOV Model application.
    :type output_mode: {"normal", "rttov"}, default: "normal"

    :param water_type: Valid values are "fresh_water" or "ocean_water". Available when ``output_mode`` is "rttov.
    :type water_type: {"fresh_water", "ocean_water"}, default: "fresh_water"

    :param cloud_top_pressure: Pressure of the cloud top in hPa. Available when ``output_mode`` is "rttov".
    :type cloud_top_pressure: number, default: 0.0

    :param cloud_fraction: Available when ``output_mode`` is "rttov".
    :type cloud_fraction: number, default: 0.0

    :rtype: :class:`Netcdf`
