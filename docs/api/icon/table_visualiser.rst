
table_visualiser
=========================

.. container::
    
    .. container:: leftside

        .. image:: /_static/TABLEVISUALISER.png
           :width: 48px

    .. container:: rightside

		Controls the parsing and plotting of `ASCII Tables <https://confluence.ecmwf.int/display/METV/ASCII+Tables>`_ such as CSV. The columns used for plotting can be selected by name (if there is a header row) or by index, starting at 1. The points may be interpreted as either geographic co-ordinates or as generic X/Y co-ordinates. The generated object can directly be used in :func:`plot`.


		.. note:: This function performs the same task as the `Table Visualiser <https://confluence.ecmwf.int/display/METV/table+visualiser>`_ icon in Metview’s user interface. It accepts its parameters as keyword arguments, described below.


.. py:function:: table_visualiser(**kwargs)
  
    Defines the visualisation of ASCII tables (e.g. CSV).


    :param table_plot_type: Specifies the type of plot to be generated. This also implicitly specifies the type of data which will be entered. The available modes are as follows:
		
		* "xy_points"
		* "geo_points"
		* "xy_vectors"
		* "geo_vectors"
		* "xy_binning": the points will be gridded specified by ``binning``.
		* "geo_binning": the points will be gridded specified by ``binning``.
    :type table_plot_type: str, default: "xy_points"

    :param table_filename: Specifies the path to the ASCII table file to be used. Alternatively, use ``table_data`` field, which overrides ``table_filename``.
    :type table_filename: str, default: "off"

    :param table_data: Specifies the input data by :func:`tablereader`.
    :type table_data: :func:`tablereader`

    :param table_x_type: Specifies how the X values should be interpreted. Only available when ``table_plot_type`` is "xy_*".
    :type table_x_type: {"number", "date"}, default: "number"

    :param table_y_type: Specifies how the Y values should be interpreted. Only available when ``table_plot_type`` is "xy_*". type plots.
    :type table_y_type: {"number", "date"}, default: "number"

    :param table_variable_identifier_type: Specifies how to identify the columns to use: by "name" or by "index" (starting at 1).
    :type table_variable_identifier_type: {"name", "index"}, default: "name"

    :param table_x_variable: Specifies which variable/column to use for the x co-ordinates of the points. Can be a name or an index - see ``table_variable_identifier_type``. Only available when ``table_plot_type`` is 'xy_*' and ``table_x_type`` is "number".
    :type table_x_variable: str

    :param table_y_variable: Specifies which variable/column to use for the y co-ordinates of the points. Can be a name or an index - see ``table_variable_identifier_type``. Only available when ``table_plot_type`` is 'xy_*' and ``table_y_type`` is "number".
    :type table_y_variable: str

    :param table_x_missing_value: Points with this value in their x co-ordinate will not be plotted.
    :type table_x_missing_value: number, default: -21.e6

    :param table_y_missing_value: Points with this value in their y co-ordinate will not be plotted.
    :type table_y_missing_value: number, default: -21.e6

    :param table_longitude_variable: Specifies which variable/column to use for the longitude co-ordinates of the points. Can be a name or an index - see ``table_variable_identifier_type``. Only available when ``table_plot_type`` is 'geo_*'.
    :type table_longitude_variable: str

    :param table_latitude_variable: Specifies which variable/column to use for the latitude co-ordinates of the points. Can be a name or an index - see ``table_variable_identifier_type``. Only available when ``table_plot_type`` is 'geo_*'.
    :type table_latitude_variable: str

    :param table_x_component_variable: When ``table_plot_type`` is '*_vectors', this parameter specifies which variable/column gives the magnitudes of the vectors in the X or longitude direction (e.g. U-component of wind). Can be a name or an index - see ``table_variable_identifier_type``.
    :type table_x_component_variable: str

    :param table_y_component_variable: When ``table_plot_type`` is '*_vectors', this parameter specifies which variable/column gives the magnitudes of the vectors in the Y or latitude direction (e.g. V-component of wind). Can be a name or an index - see ``table_variable_identifier_type``.
    :type table_y_component_variable: str

    :param table_value_variable: Specifies which variable/column supplies the values for the points. Can be a name or an index - see ``table_variable_identifier_type``.
    :type table_value_variable: str

    :param table_binning: Specifies the binning. Available when ``table_plot_type`` id "*_binning".
    :type table_binning: :func:`binning`

    :param table_delimiter: Specifies the (single) character that separates values in the table.
    :type table_delimiter: str, default: ","

    :param table_combine_delimiters: If it is set to "on", then consecutive delimiters will be considered as one. This is often the case when whitespace is used to separate values which are aligned in columns. Note that in this case, it is not possible to represent missing values in the table. If "off", then a delimiter not surrounded by two data values indicates there is a missing value on at least one side of it. See `ASCII Tables <https://confluence.ecmwf.int/display/METV/ASCII+Tables>`_ for more details.
    :type table_combine_delimiters: {"on", "off"}, default: "off"

    :param table_header_row: Specifies which row of the table file contains the names of the columns. This row, if present, should contain the one entry for each data column, separated with the same delimiter as the data. The first row of the table is number 1. Set this parameter to 0 in order to indicate that there is no header row.
    :type table_header_row: int, default: 1

    :param table_data_row_offset: Specifies how many rows after the header row the first data row appears. Normally this is 1, since data tends to start on the row after the column headers. If there is no header row, then this number is equivalent to the first data row (e.g. if the data starts on row 3, then set this parameter to 3).'
    :type table_data_row_offset: int, default: 1

    :param table_meta_data_rows: Specifies the rows (if any) which contain meta-data in a form which can be parsed by Metview. See `ASCII Tables <https://confluence.ecmwf.int/display/METV/ASCII+Tables>`_ for more details.
    :type table_meta_data_rows: int or list[int]

    :rtype: :class:`Request`
