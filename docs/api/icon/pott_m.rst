
pott_m
=========================

.. container::
    
    .. container:: leftside

        .. image:: /_static/POTTF.png
           :width: 48px

    .. container:: rightside

		Computes the potential temperature for GRIB data on ECMWF model levels.


		.. note:: This function performs the same task as the `Potential Temperature <https://confluence.ecmwf.int/display/METV/Potential+Temperature>`_ icon in Metview’s user interface. It accepts its parameters as keyword arguments, described below.


.. py:function:: pott_m(**kwargs)
  
    Computes the potential temperature for GRIB data on ECMWF model levels.


    :param lnsp: Specifies the Logarithm of Surface Pressure (LNSP) GRIB field.
    :type lnsp: :class:`Fieldset`

    :param temperature: Specifies the temperature GRIB fields on model levels.
    :type temperature: :class:`Fieldset`

    :rtype: :class:`Fieldset`


.. mv-minigallery:: pott_m

