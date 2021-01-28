
mhovmoeller_expand
=========================

.. container::
    
    .. container:: leftside

        .. image:: /_static/MHOVMOELLERDATA.png
           :width: 48px

    .. container:: rightside

		Allows the production of Hovmoeller diagrams to be computed incrementally. This could be useful, for example, if the input data is too large or the Hovmoeller diagram needs to be updated periodically (e.g. to produce a diagram operationally during a certain period of time).
		
		The resulting data can be plotted (using a default visualisation and with the plot area based on the range of data values) or saved as a NetCDF data file using :func:`write`.
		
		If access to the computed values is not required, or for more control of the plotting, use :func:`mhovmoellerview`.


		.. note:: This function performs the same task as the `Hovmoeller Data <https://confluence.ecmwf.int/display/METV/Hovmoeller+Data>`_ icon in Metview’s user interface. It accepts its parameters as keyword arguments, described below.


.. py:function:: mhovmoeller_expand(**kwargs)
  
    Provides input for expanding Hovmoeller diagrams that have been derived previously.


    :param netcdf_path: Specifies the NetCDF file path and name. Alternatively, ``netcdf_data`` can be used.
    :type netcdf_path: str

    :param netcdf_data: Specifies the data (:class:`NetCDF`) from which to expand the Hovmoeller diagram. Takes precedence over ``netcdf_path``.
    :type netcdf_data: class:`NetCDF`

    :param data_path: Specifies the input GRIB file path and name. Alternatively, ``data`` can be used.
    :type data_path: str

    :param data: Specifies the GRIB data (:class:`Fieldset`) from which to derive the Hovmeller diagram. ``data`` must specify a time-series of a meteorological variable in a latitude-longitude or Gaussian grid.
    :type data: :class:`Fieldset`

    :rtype: :class:`NetCDF`


.. mv-minigallery:: mhovmoeller_expand

