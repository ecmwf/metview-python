
input_visualiser
=========================

.. container::
    
    .. container:: leftside

        .. image:: /_static/INPUTVISUALISER.png
           :width: 48px

    .. container:: rightside

		Defines the visualisation of list/ndarray data. The generated object can directly be used in :func:`plot`.


		.. note:: This function performs the same task as the `Input Visualiser <https://confluence.ecmwf.int/display/METV/input+visualiser>`_ icon in Metview’s user interface. It accepts its parameters as keyword arguments, described below.


.. py:function:: input_visualiser(**kwargs)
  
    Defines the visualisation of list/ndarray data.


    :param input_plot_type: Specifies the type of plot to be generated. This also implicitly specifies the type of data which will be entered. The available modes are as follows:
		
		* "xy_points"
		* "geo_points"
		* "xy_area"
		* "xy_vectors"
		* "geo_vectors"
		* "xy_binning": the points will be gridded specified by ``binning``.
		* "geo_binning": the points will be gridded specified by ``binning``.
		* "xy_boxplot"
    :type input_plot_type: str, default: "xy_points"

    :param input_x_type: Specifies how the X values should be interpreted. Only available when ``input_plot_type`` is "xy_*".
    :type input_x_type: {"number", "date"}, default: "number"

    :param input_y_type: Specifies how the Y values should be interpreted. Only available when ``input_plot_type`` is "xy_*". type plots.
    :type input_y_type: {"number", "date"}, default: "number"

    :param input_x_values: The x-coordinate values. Only available when ``input_plot_type`` is "xy_*" and ``input_x_type`` is "number".
    :type input_x_values: ndarray

    :param input_y_values: The y-coordinate values. Only available  when ``input_plot_type`` is "xy_*" and ``input_y_type`` is "number".
    :type input_y_values: ndarray

    :param input_x2_values: The second x-coordinate values. Only available when ``input_plot_type`` is "xy_area" and ``input_x_type`` is "number".
    :type input_x2_values: ndarray

    :param input_y2_values: The second y-coordinate values. Only available when ``input_plot_type`` is "xy_area" and ``input_y_type`` is "number".
    :type input_y2_values: ndarray

    :param input_x_missing_value: Specifies the value which will be considered "missing" when plotting. Only available when ``input_plot_type`` is "xy_*" and ``input_x_type`` is "number".
    :type input_x_missing_value: number, default: -21.e6

    :param input_y_missing_value: Specifies the value which will be considered "missing" when plotting. Only available when ``input_plot_type`` is "xy_*" and ``input_y_type`` is "number".
    :type input_y_missing_value: number, default: -21.e6

    :param input_date_x_values: The dates used as x-coordinate values. Only available when ``input_plot_type`` is "xy_*" and``input_x_type`` is "date".
    :type input_date_x_values: list of datetime.datetime

    :param input_date_y_values: The dates used as y-coordinate values. Only available when ``input_plot_type`` is "xy_*" and ``input_y_type`` is "date".
    :type input_date_y_values: list of datetime.datetime

    :param input_date_x2_values: 
    :type input_date_x2_values: list of datetime.datetime

    :param input_date_y2_values: 
    :type input_date_y2_values: list of datetime.datetime

    :param input_longitude_values: The longitude values. Only available when ``input_plot_type`` is "geo_*".
    :type input_longitude_values: ndarray

    :param input_latitude_values: The latitude values. Only available when ``input_plot_type`` is "geo_*".
    :type input_latitude_values: ndarray

    :param input_x_component_values: The x vector component values. Only available when ``input_plot_type`` is "*_vectors".
    :type input_x_component_values: ndarray

    :param input_y_component_values: The y vector component values. Only available when ``input_plot_type`` is "*_vectors".
    :type input_y_component_values: ndarray

    :param input_values: Specifies the actual values at the points whose coordinates are given in the other parameters.
    :type input_values: ndarray

    :param input_minimum_values: The minimum values when ``input_plot_type`` is "xy_boxplot".
    :type input_minimum_values: ndarray

    :param input_maximum_values: The maximum values when ``input_plot_type`` is "xy_boxplot".
    :type input_maximum_values: ndarray

    :param input_median_values: The median values when ``input_plot_type`` is "xy_boxplot".
    :type input_median_values: ndarray

    :param input_box_upper_values: The upper quartile (75%) values when ``input_plot_type`` is "xy_boxplot".
    :type input_box_upper_values: ndarray

    :param input_box_lower_values: The lower quartile (25%) values when ``input_plot_type`` is "xy_boxplot".
    :type input_box_lower_values: ndarray

    :param input_binning: Specifies the binning. Available when ``table_plot_type`` id "*_binning".
    :type input_binning: :func:`binning`

    :rtype: :class:`Request`
.. include:: /gallery/backref/input_visualiser.rst