
input_visualiser
=========================

.. container::
    
    .. container:: leftside

        .. image:: /_static/INPUTVISUALISER.png
           :width: 48px

    .. container:: rightside

        This function performs the same task as the `Input Visualiser <https://confluence.ecmwf.int/display/METV/input+visualiser>`_ icon in Metview’s user interface. It accepts its parameters as keyword arguments, described below.


.. py:function:: input_visualiser(**kwargs)
  
    Description comes here!


    :param input_plot_type: Specifies the type of plot to be generated. This also implicitly specifies the type of data which will be entered. The available modes follow a set format: the first part is either 'Geo' (geographical coordinates) or 'Xy' (more generic coordinates); the second part is 'Points' (individual points), 'Vectors' (individual points with vector information) or 'Binning' (the points will be gridded – see :func:`binning`.
    :type input_plot_type: {"xy_points", "geo_points", "xy_area", "xy_vectors", "geo_vectors", "xy_binning", "geo_binning", "xy_boxplot"}, default: "xy_points"


    :param input_x_type: Specifies how the X values should be interpreted. Only available for 'Xy' type plots.
    :type input_x_type: {"number", "date"}, default: "number"


    :param input_y_type: Specifies how the Y values should be interpreted. Only available for 'Xy' type plots.
    :type input_y_type: {"number", "date"}, default: "number"


    :param input_x_values: A list of x-coordinate values separated by a “/” or a vector (in Macro) or a numpy array (Python) of numbers. Only available for 'Xy' type plots when ``input_x_type`` is Number.
    :type input_x_values: str or list[str]


    :param input_y_values: A list of y-coordinate values separated by a “/” or a vector (in Macro) or a numpy array (Python) of numbers. Only available for 'Xy' type plots when ``input_y_type`` is Number.
    :type input_y_values: str or list[str]


    :param input_x2_values: A list of x-coordinate values separated by a “/” or a vector (in Macro) or a numpy array (Python) of numbers. Only available for XY Area type plots.
    :type input_x2_values: str or list[str]


    :param input_y2_values: A list of y-coordinate values separated by a “/” or a vector (in Macro) or a numpy array (Python) of numbers. Only available for XY Area type plots.
    :type input_y2_values: str or list[str]


    :param input_x_missing_value: Specifies the value which will be considered 'missing' when plotting. Only available for 'Xy' type plots when ``input_x_type`` is Number.
    :type input_x_missing_value: number, default: -21.e6


    :param input_y_missing_value: Specifies the value which will be considered 'missing' when plotting. Only available for 'Xy' type plots when ``input_y_type`` is Number.
    :type input_y_missing_value: number, default: -21.e6


    :param input_date_x_values: A list of dates to be used as x-coordinate values separated by a “/”. See  on page 6 for details on how to specify dates to the visualiser icons. Only available for 'Xy' type plots when ``input_x_type`` is Date.
    :type input_date_x_values: str or list[str]


    :param input_date_y_values: A list of dates to be used as x-coordinate values separated by a “/”. See  on page 6 for details on how to specify dates to the visualiser icons. Only available for 'Xy' type plots when ``input_y_type`` is Date.
    :type input_date_y_values: str or list[str]


    :param input_date_x2_values: 
    :type input_date_x2_values: str or list[str]


    :param input_date_y2_values: 
    :type input_date_y2_values: str or list[str]


    :param input_longitude_values: A list of longitude values separated by a “/” or a vector (in Macro) or a numpy array (Python) of numbers. Only available for 'Geo' type plots.
    :type input_longitude_values: str or list[str]


    :param input_latitude_values: A list of latitude values separated by a “/” or a vector (in Macro) or a numpy array (Python) of numbers. Only available for 'Geo' type plots.
    :type input_latitude_values: str or list[str]


    :param input_x_component_values: A list of x vector component values separated by a “/”. Only available for 'Vectors' type plots.
    :type input_x_component_values: str or list[str]


    :param input_y_component_values: 
    :type input_y_component_values: str or list[str]


    :param input_values: 
    :type input_values: str or list[str]


    :param input_minimum_values: 
    :type input_minimum_values: float or list[float]


    :param input_maximum_values: 
    :type input_maximum_values: float or list[float]


    :param input_median_values: 
    :type input_median_values: float or list[float]


    :param input_box_upper_values: 
    :type input_box_upper_values: float or list[float]


    :param input_box_lower_values: 
    :type input_box_lower_values: float or list[float]


    :param input_binning: 
    :type input_binning: str


    :rtype: None


.. minigallery:: metview.input_visualiser
    :add-heading:

