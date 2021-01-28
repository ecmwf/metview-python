
mhovmoeller_vertical
=========================

.. container::
    
    .. container:: leftside

        .. image:: /_static/MHOVMOELLERDATA.png
           :width: 48px

    .. container:: rightside

		Derives (and returns) a vertical Hovmoeller diagram data unit for a given geographical area for GRIB (:class:`Fieldset`) input. The generated data can be used to display a two-dimensional graph with levels as one axis and time as the other. 
		
		The resulting data can be plotted (using a default visualisation and with the plot area based on the range of data values) or saved as a NetCDF data file using :func:`write`.
		
		If access to the computed values is not required, or for more control of the plotting, use :func:`mhovmoellerview`.


		.. note:: This function performs the same task as the `Hovmoeller Data <https://confluence.ecmwf.int/display/METV/Hovmoeller+Data>`_ icon in Metview’s user interface. It accepts its parameters as keyword arguments, described below.


.. py:function:: mhovmoeller_vertical(**kwargs)
  
    Provides input for Hovemoeller diagrams derived from an input geographical area and a set of levels.


    :param data: Specifies the GRIB data (:class:`Fieldset`) from which to derive the Hovmeller diagram. ``data`` must specify a time-series of a meteorological variable in a latitude-longitude or Gaussian grid. The GRIB data should contain a set of levels for each parameter. Also, if the input data is specified on ECMWF model levels, you must include the parameter LNSP should you want the vertical axis of the plot in pressure levels rather than ECMWF model levels when visualising the output.
    :type data: :class:`Fieldset`

    :param area: Specifies the coordinates of the area (as [north, west, south, east]) over which the Hovmoeller diagram is calculated.
    :type area: list[float], default: [30, -30, -30, 30]

    :param vertical_level_type: Specifies if a conversion from ECMWF model level to pressure level needs to be performed. If it is set to "pressure" and the input data is specified on ECMWF model levels, the LNSP field should be added to the input data.
    :type vertical_level_type: {"as_in_data", "pressure"}, default: "as_in_data"

    :rtype: :class:`NetCDF`


.. mv-minigallery:: mhovmoeller_vertical

