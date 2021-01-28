
binning
=========================

.. container::
    
    .. container:: leftside

        .. image:: /_static/BINNING.png
           :width: 48px

    .. container:: rightside

		Defines 2D binning for input point data to construct gridded data for visualisation. The number of points occurring within each grid box is counted and becomes the value for that grid box. The resulting visualisation is therefore of this gridded data, and can be customised with :func:`mcont`.


		.. note:: This function performs the same task as the `Binning <https://confluence.ecmwf.int/display/METV/binning>`_ icon in Metview’s user interface. It accepts its parameters as keyword arguments, described below.


.. py:function:: binning(**kwargs)
  
    


    :param binning_x_method: 
    :type binning_x_method: {"count", "list", "interval"}, default: "count"

    :param binning_x_min_value: 
    :type binning_x_min_value: number, default: -1.0e+21

    :param binning_x_max_value: 
    :type binning_x_max_value: number, default: 1.0e+21

    :param binning_x_count: 
    :type binning_x_count: number, default: 10

    :param binning_x_list: 
    :type binning_x_list: float or list[float]

    :param binning_x_interval: 
    :type binning_x_interval: number, default: 10

    :param binning_x_reference: 
    :type binning_x_reference: number, default: 0

    :param binning_y_method: 
    :type binning_y_method: {"count", "list", "interval"}, default: "count"

    :param binning_y_min_value: 
    :type binning_y_min_value: number, default: -1.0e+21

    :param binning_y_max_value: 
    :type binning_y_max_value: number, default: 1.0e+21

    :param binning_y_count: 
    :type binning_y_count: number, default: 10

    :param binning_y_list: 
    :type binning_y_list: float or list[float]

    :param binning_y_interval: 
    :type binning_y_interval: number, default: 10

    :param binning_y_reference: 
    :type binning_y_reference: number, default: 0

    :rtype: :class:`Request`


.. mv-minigallery:: binning

