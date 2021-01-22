
thermo_bufr
=========================

.. container::
    
    .. container:: leftside

        .. image:: /_static/THERMODATA.png
           :width: 48px

    .. container:: rightside

		Derives (and returns) a Thermodynamic diagram data unit from :class:`Bufr` data. In such a diagram, temperature, humidity (represented by the dew point) and wind values are displayed with respect to pressure. All the three major thermodynamic diagrams types re supported in Metview: Tephigram, Skew-T and Emagram.
		
		The resulting data can plotted (using a default visualisation and with the plot area based on the range of data values) or saved as a :class:`NetCDF` data file using :func:`write`.
		
		If access to the output computed values is not required, or for more control of the plotting, use :func:`thermoview`.


		.. note:: This function performs the same task as the `Thermo Data <https://confluence.ecmwf.int/display/METV/Thermo+Data>`_ icon in Metview’s user interface. It accepts its parameters as keyword arguments, described below.


.. py:function:: thermo_bufr(**kwargs)
  
    Derives (and returns) a Thermodynamic diagram data unit from BUFR data.


    :param data: Specifies the BUFR data to be used in the plotting of a thermodynamic diagram. The data should be upper air sounding data. Please note that PILOT observations (winds only) do not have enough data for plotting a thermodynamic diagram.
    :type data: :class:`Bufr`

    :param station: Specifies the location as a :func:`stations` object for which the diagram is to be plotted.
    :type station: :func:`stations``

    :rtype: :class:`NetCDF`
.. include:: /gallery/backref/thermo_bufr.rst