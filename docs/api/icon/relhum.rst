
relhum
=========================

.. container::
    
    .. container:: leftside

        .. image:: /_static/RELHUM.png
           :width: 48px

    .. container:: rightside

        This function performs the same task as the `Relative Humidity <https://confluence.ecmwf.int/display/METV/Relative+Humidity>`_ icon in Metview’s user interface. It accepts its parameters as keyword arguments, described below.


.. py:function:: relhum(**kwargs)
  
    Description comes here!


    :param data: Specifies the temperature and specific humidity `GRIB <https://confluence.ecmwf.int/display/METV/Thermo+``data``#Thermo``data``-GRIB``data``>`_ ``data`` required for the application. If the input is on (hybrid) model levels it must contain the lnsp field as well.
    :type data: str


    :rtype: None
