
eqpott_p
=========================

.. container::
    
    .. container:: leftside

        .. image:: /_static/POTTF.png
           :width: 48px

    .. container:: rightside

		Computes the equivalent potential temperature for GRIB data on pressure levels.


		.. note:: This function performs the same task as the `Potential Temperature <https://confluence.ecmwf.int/display/METV/Potential+Temperature>`_ icon in Metview’s user interface. It accepts its parameters as keyword arguments, described below.


.. py:function:: eqpott_p(**kwargs)
  
    Computes the equivalent potential temperature for GRIB data on pressure levels.


    :param temperature: Specifies the temperature GRIB fields on pressure levels.
    :type temperature: :class:`Fieldset`

    :param humidity: Specifies the specific humidity GRIB fields on model levels.
    :type humidity: :class:`Fieldset`

    :rtype: :class:`Fieldset`


.. mv-minigallery:: eqpott_p

