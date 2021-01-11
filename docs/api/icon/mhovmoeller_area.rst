
mhovmoeller_area
=========================

.. container::
    
    .. container:: leftside

        .. image:: /_static/MHOVMOELLERDATA.png
           :width: 48px

    .. container:: rightside

		Derives (and returns) a Hovmoeller diagram data unit for a given geographical area for GRIB (:class:`Fieldset`) input. The generated data can be used to display a two-dimensional graph with latitude or longitude as one axis and time as the other. The average values for each field are taken along the North-South or East-West direction.
		
		The resulting data can be plotted (using a default visualisation and with the plot area based on the range of data values) or saved as a NetCDF data file using :func:`write`.
		
		If access to the computed values is not required, or for more control of the plotting, use :func:`mhovmoellerview`.


		.. note:: This function performs the same task as the `Hovmoeller Data <https://confluence.ecmwf.int/display/METV/Hovmoeller+Data>`_ icon in Metview’s user interface. It accepts its parameters as keyword arguments, described below.


.. py:function:: mhovmoeller_area(**kwargs)
  
    Provides input for Hovmoeller diagrams derived from a geographical area.


    :param data: Specifies the GRIB data (:class:`Fieldset`) from which to derive the Hovmeller diagram. ``data`` must specify a time-series of a meteorological variable in a latitude-longitude or Gaussian grid. If ``data`` contains more than one parameter and/or level :func:`mhovmoeller_area` returns a set of Hovmoeller diagrams.
    :type data: :class:`Fieldset`

    :param area: Specifies the coordinates of the area (as [north, west, south, east]) over which the Hovmoeller diagram is calculated.
    :type area: list[float], default: [30, -30, -30, 30]

    :param average_direction: Specifies the direction along which the averaging is performed. Options are "north_south" and "east_west". For "north_south" the averaging is weighted by the cosine of the latitudes.
    :type average_direction: {"east_west", "north_south"}, default: "east_west"

    :param swap_axes: By default, the definition of the vertical and horizontal axes of the Hovmoeller diagrams follows pre-defined rules. However, if ``swap_axes`` is set to "yes" then the axes will be swapped around.
    :type swap_axes: {"no", "yes"}, default: "no"

    :param resolution: Used to interpolate the data onto a regular grid, and applies to both the horizontal and vertical axes where appropriate. This parameter is essential for creating a Hovmoeller diagram from satellite data.
    :type resolution: number, default: 1.0

    :rtype: :class:`NetCDF`
