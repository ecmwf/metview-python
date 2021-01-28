
mxs_average
=========================

.. container::
    
    .. container:: leftside

        .. image:: /_static/MXAVERAGE.png
           :width: 48px

    .. container:: rightside

		Derives (and returns) a vertical average cross section data unit of upper air fields in GRIB format. For each upper air field, this average is taken along the North-South or East-West direction over a specified rectangular area and then interpolated horizontally along the direction perpendicular to the averaging direction with a spacing consistent with the resolution of the input GRIB data.
		
		The average cross section data can be plotted (using a default visualisation and with the plot area based on the range of data values) or saved as a NetCDF data file (:class:`NetCDF`) using :func:`write`. 
		
		If access to the output computed values is not required, or for more control of the plotting, use  :func:`maverageview`. 
		


		.. note:: This function performs the same task as the `Average Data <https://confluence.ecmwf.int/display/METV/Average+Data>`_ icon in Metview’s user interface. It accepts its parameters as keyword arguments, described below.


.. py:function:: mxs_average(**kwargs)
  
    Derives (and returns) vertical average cross section data.


    :param data: Specifies the GRIB data from which to derive the average view data. The input GRIB must specify a multi-level (pressure or model levels) upper air meteorological variable, in a latitude-longitude or Gaussian grid. If the input data is specified in model levels, you must include a Logarithm Of Surface Pressure (LNSP) field should you want the vertical axis of the plot in pressure levels rather than model levels when visualising the output. Note that the input fields should be on the same grid. If more than one time and/or forecast step is contained in ``data``, it returns a set of average cross sections in the resulting data, but note that currently only the first of these will be plotted with :func:`plot`.
    :type data: str

    :param area: Specifies the coordinates of the area (as [North, West, South, East]) over which the averages are calculated.
    :type area: list[float], default: [90, -180, -90, 180]

    :param direction: Specifies the direction along which the averaging of the variable is performed. Options are "ns" (North-South) and "ew" (East-West). For "ns", the averaging is weighted by the cosine of latitude.
    :type direction: {"ns", "ew"}, default: "ns"

    :rtype: :class:`NetCDF`


.. mv-minigallery:: mxs_average

