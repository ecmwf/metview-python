
read_table
=========================

.. container::
    
    .. container:: leftside

        .. image:: /_static/TABLEREADER.png
           :width: 48px

    .. container:: rightside

		Reads ASCII table file with various formatting and reading options allowing a wide variety of ASCII data tables to be parsed. See `ASCII Tables <https://confluence.ecmwf.int/display/METV/ASCII+Tables>`_ for more details.


		.. note:: This function performs the same task as the `Table Reader <https://confluence.ecmwf.int/display/METV/Table+Reader>`_ icon in Metview’s user interface. It accepts its parameters as keyword arguments, described below.


.. py:function:: read_table(**kwargs)
  
    Reads ASCII table data with various formatting and reading options allowing a wide variety of ASCII data tables to be parsed.


    :param data: Object representing an ASCII table file.
    :type data: :class:`Table`, :class:`Geopoints` or :class:`Note`

    :param table_filename: Specifies the path to the input table file. This parameter, if filled, overrides ``data``.
    :type table_filename: str

    :param table_delimiter: Specifies the (single) character that separates values in the table.
    :type table_delimiter: str, default: ","

    :param table_combine_delimiters: If "on", then consecutive delimiters will be considered as one. This is often the case when whitespace is used to separate values which are aligned in columns. Note that in this case, it is not possible to represent missing values in the table. If "off", then a delimiter not surrounded by two data values indicates there is a missing value on at least one side of it. See the discussion in `ASCII Tables <https://confluence.ecmwf.int/display/METV/ASCII+Tables>`_ for more details.
    :type table_combine_delimiters: {"on", "off"}, default: "off"

    :param table_header_row: Specifies which row of the table file contains the names of the columns. This row, if present, should contain the one entry for each data column, separated with the same delimiter as the data. The first row of the table is number 1. Set this parameter to 0 in order to indicate that there is no header row.
    :type table_header_row: number, default: 1

    :param table_data_row_offset: Specifies how many rows after the header row the first data row appears. Normally this is 1, since data tends to start on the row after the column headers. If there is no header row, then this number is equivalent to the first data row (e.g. if the data starts on row 3, then set this parameter to 3).
    :type table_data_row_offset: number, default: 1

    :param table_meta_data_rows: Specifies the rows (if any) which contain meta-data in a form which can be parsed by Metview. See ASCII Tables for more details.
    :type table_meta_data_rows: list

    :param table_columns: In order to conserve resources, it is possible to choose to load only a specified set of data columns. The first column is numbered 1.
    :type table_columns: list

    :param table_column_types: If Metview does not correctly determine the data types of the columns, this parameter makes it possible to specify the data types as a list of type names. Possible type names are "number" and "string". If ``table_columns`` is set, only that subset of columns should be represented by the list of types.
    :type table_column_types: list

    :rtype: :class:`Table`


.. mv-minigallery:: read_table

