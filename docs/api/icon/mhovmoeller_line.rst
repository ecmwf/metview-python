
mhovmoeller_line
=========================

.. container::
    
    .. container:: leftside

        .. image:: /_static/MHOVMOELLERDATA.png
           :width: 48px

    .. container:: rightside

		Derives (and returns) a Hovmoeller diagram data unit for a given transect line for GRIB (:class:`Fieldset`) input. The generated data can be used to display a two-dimensional graph with latitude or longitude as one axis and time as the other. The point values for each field are interpolated along the transect line, with a spacing consistent with the resolution of the input GRIB data.
		
		The resulting data can be plotted (using a default visualisation and with the plot area based on the range of data values) or saved as a NetCDF data file using :func:`write`.
		
		If access to the computed values is not required, or for more control of the plotting, use :func:`mhovmoellerview`.


		.. note:: This function performs the same task as the `Hovmoeller Data <https://confluence.ecmwf.int/display/METV/Hovmoeller+Data>`_ icon in Metview’s user interface. It accepts its parameters as keyword arguments, described below.


.. py:function:: mhovmoeller_line(**kwargs)
  
    Provides input for Hovmoeller diagrams derived from a transect line.


    :param data: Specifies the GRIB data (:class:`Fieldset`) from which to derive the Hovmeller diagram. ``data`` must specify a time-series of a meteorological variable in a latitude-longitude or Gaussian grid. If ``data`` contains more than one parameter and/or level :func:`mhovmoeller_line` returns a set of Hovmoeller diagrams.
    :type data: :class:`Fieldset`

    :param line: Specifies the coordinates of a transect line along which the Hovmoeller diagram is calculated in [lat1, lon1, lat2, lon2] format.
    :type line: list[float], default: [0, -180, 0, 180]

    :param swap_axes: By default, the definition of the vertical and horizontal axes of the Hovmoeller diagrams follows pre-defined rules. However, if ``swap_axes`` is set to "yes" then the axes will be swapped around.
    :type swap_axes: {"no", "yes"}, default: "no"

    :param resolution: Used to interpolate the data onto a regular grid, and applies to both the horizontal and vertical axes where appropriate. This parameter is essential for creating a Hovmoeller diagram from satellite data.
    :type resolution: number, default: 1.0

    :rtype: :class:`Netcdf`
