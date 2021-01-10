
eqpott_m
=========================

.. container::
    
    .. container:: leftside

        .. image:: /_static/POTTF.png
           :width: 48px

    .. container:: rightside

		Computes the equivalent potential temperature for GRIB data on ECMWF model levels.


		.. note:: This function performs the same task as the `Potential Temperature <https://confluence.ecmwf.int/display/METV/Potential+Temperature>`_ icon in Metview’s user interface. It accepts its parameters as keyword arguments, described below.


.. py:function:: eqpott_m(**kwargs)
  
    Computes the equivalent  potential temperature for GRIB data on ECMWF model levels.


    :param lnsp: Specifies the Logarithm of Surface Pressure (LNSP) GRIB field. Specifies the temperature GRIB fields on model levels.
    :type lnsp: :class:`Fieldset`

    :param temperature: Specifies the temperature GRIB fields on model levels.
    :type temperature: :class:`Fieldset`

    :param humidity: Specifies the specific humidity GRIB fields on model levels.
    :type humidity: :class:`Fieldset`

    :rtype: :class:`Fieldset`
