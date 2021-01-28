
relhum
=========================

.. container::
    
    .. container:: leftside

        .. image:: /_static/RELHUM.png
           :width: 48px

    .. container:: rightside

		Computes the relative humidity from temperature, specific humidity and logarithm of surface pressure (LNSP) GRIB data. LNSP is only required if the input data is specified on ECMWF model levels. The computations are based on a mixed-phase Tetens formula used by IFS for diagnostic purposes (see `here <https://www.ecmwf.int/en/elibrary/18714-part-iv-physical-processes>`_ on p116 for details from the latest model cycle (CY45R1, at the time of the writing of this documentation).


		.. note:: This function performs the same task as the `Relative Humidity <https://confluence.ecmwf.int/display/METV/Relative+Humidity>`_ icon in Metview’s user interface. It accepts its parameters as keyword arguments, described below.


.. py:function:: relhum(**kwargs)
  
    Computes the relative humidity from temperature and specific humidity GRIB data.


    :param data: Specifies the temperature and specific humidity input GRIB data required for the application. If the input is defined on ECMWF (hybrid/eta) model levels it must contain a Logarithm of Surface Pressure field as well (it must have the ecCodes paramId of 152).
    :type data: :class:`Fieldset`

    :rtype: :class:`fieldset`


.. mv-minigallery:: relhum

