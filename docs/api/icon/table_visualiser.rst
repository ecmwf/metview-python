
table_visualiser
=========================

.. container::
    
    .. container:: leftside

        .. image:: /_static/TABLE_VISUALISER.png
           :width: 48px

    .. container:: rightside

        This function represents the `Table Visualiser <https://confluence.ecmwf.int/display/METV/table+visualiser>`_ icon in Metview's user interface.


.. py:function:: table_visualiser(**kwargs)
  
    Description comes here!


    :param table_plot_type: 
    :type table_plot_type: str


    :param table_filename: Specifies the path to the ASCII table file to be used. Alternatively, drop an icon into the ``table_data`` field, which overrides ``table_filename``.
    :type table_filename: str


    :param table_data: Drop an ASCII Table icon into this field to specify the data to be used. A _Notes icon will also be accepted, since Metview cannot be expected to automatically discriminate any but the most common types of ASCII ``table_data`` from other ASCII files. Note that ``table_filename`` is an alternative way of specifying the file.
    :type table_data: str


    :param table_x_type: Specifies how the X values should be interpreted, as numbers or as dates. Only available for 'Xy' type plots.
    :type table_x_type: str


    :param table_y_type: Specifies how the Y values should be interpreted, as numbers or as dates. Only available for 'Xy' type plots.
    :type table_y_type: str


    :param table_variable_identifier_type: Specifies how to identify the columns to use: by Name or by Index (starting at 1).
    :type table_variable_identifier_type: str


    :param table_x_variable: Specifies which variable/column to use for the x co-ordinates of the points. Can be a name or an index - see ``table_variable_identifier_type``.  Only available for 'Xy' type plots when ``table_x_type`` is Number.
    :type table_x_variable: str


    :param table_y_variable: Specifies which variable/column to use for the x co-ordinates of the points. Can be a name or an index - see ``table_variable_identifier_type``.  Only available for 'Xy' type plots when ``table_y_type`` is Number.
    :type table_y_variable: str


    :param table_x_missing_value: Points with this value in their x co-ordinate will not be plotted.
    :type table_x_missing_value: number


    :param table_y_missing_value: Points with this value in their y co-ordinate will not be plotted.
    :type table_y_missing_value: number


    :param table_longitude_variable: Specifies which variable/column to use for the longitude co-ordinates of the points. Can be a name or an index - see ``table_variable_identifier_type``. Only available for 'Geo' type plots .
    :type table_longitude_variable: str


    :param table_latitude_variable: Specifies which variable/column to use for the latitude co-ordinates of the points. Can be a name or an index - see ``table_variable_identifier_type``. Only available for 'Geo' type plots .
    :type table_latitude_variable: str


    :param table_x_component_variable: When set to a 'Vectors' type plot, this parameter specifies which variable/column gives the magnitudes of the vectors in the X or longitude direction (e.g. U-component of wind). Can be a name or an index - see ``table_variable_identifier_type``.
    :type table_x_component_variable: str


    :param table_y_component_variable: When set to a 'Vectors' type plot, this parameter specifies which variable/column gives the magnitudes of the vectors in the Y or latitude direction (e.g. V-component of wind). Can be a name or an index - see ``table_variable_identifier_type``.
    :type table_y_component_variable: str


    :param table_value_variable: Specifies which variable/column supplies the values for the points. Can be a name or an index - see ``table_variable_identifier_type``.
    :type table_value_variable: str


    :param table_binning: Drop a :func:`binning` icon here. Only available for 'Binning' type plots.
    :type table_binning: str


    :param table_delimiter: 
    :type table_delimiter: str


    :param table_combine_delimiters: 
    :type table_combine_delimiters: str


    :param table_header_row: 
    :type table_header_row: str


    :param table_data_row_offset: 
    :type table_data_row_offset: str


    :param table_meta_data_rows: 
    :type table_meta_data_rows: str or list[str]


    :rtype: None
