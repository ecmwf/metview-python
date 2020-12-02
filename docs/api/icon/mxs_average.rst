
mxs_average
=========================

.. container::
    
    .. container:: leftside

        .. image:: /_static/MXAVERAGE.png
           :width: 48px

    .. container:: rightside

        This function performs the same task as the `Average Data <https://confluence.ecmwf.int/display/METV/Average+Data>`_ icon in Metview’s user interface. It accepts its parameters as keyword arguments, described below.


.. py:function:: mxs_average(**kwargs)
  
    Description comes here!


    :param data: 
    :type data: str


    :param area: 
    :type area: float or list[float], default: 90


    :param direction: Specifies the ``direction`` along which the averaging of the variable is performed. Options are North South and East West. For North South , the averaging is weighted by cos(latitude).
    :type direction: {"ns", "ew"}, default: "ns"


    :rtype: None
