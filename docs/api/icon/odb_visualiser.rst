
odb_visualiser
=========================

.. container::
    
    .. container:: leftside

        .. image:: /_static/ODB_VISUALISER.png
           :width: 48px

    .. container:: rightside

        This icon performs an ODB/SQL query on an ODB database (ODB-1) or file (ODB-2). The result is always an ODB file (in ODB-2 format).


.. py:function:: odb_visualiser(**kwargs)
  
    Description comes here!


    :param odb_plot_type: Specifies the plot type to be generated. The possible values are as follows:

         *  geo_points (points plotted onto a map)
         *  geo_vectors (vectors plotted onto a map)
         *  xy_points (points plotted into a :func:`cartesianview`
         *  xy_vectors (vectors plotted into a :func:`cartesianview`
         *  xy_binning (gridded values by binning plotted into a a :func:`cartesianview`

         The default value is: geo_points.
    :type odb_plot_type: str


    :param odb_filename: Specifies the path to the input ODB.
    :type odb_filename: str


    :param odb_data: Specifies the input ODB as an icon. If both an icon (in ``odb_data`` ) and a filename (in ``odb_filename`` ) are specified the icon takes precedence.
    :type odb_data: str


    :param odb_x_type: Specifies the type of the x coordinate when ``odb_plot_type`` is set to xy_points , xy_vectors or xy_binning. The possible values are: number and date. The default is number.
    :type odb_x_type: str


    :param odb_y_type: Specifies the type of the y coordinate when ``odb_plot_type`` is set to xy_points , xy_vectors or xy_binning. The possible values are: number and date. The default is number.
    :type odb_y_type: str


    :param odb_x_variable: Specifies the ODB column interpreted as the x coordinate when ``odb_plot_type`` is set to geo_vectors , xy_vectors or xy_binning. The default is an empty string.
    :type odb_x_variable: str


    :param odb_y_variable: Specifies the ODB column interpreted as the y coordinate when ``odb_plot_type`` is set to geo_vectors , xy_vectors or xy_binning. The default is an empty string.
    :type odb_y_variable: str


    :param odb_latitude_variable: Specifies the ODB column interpreted as latitude when ``odb_plot_type`` is set to geo_points or geo_vectors. The default is lat@hdr.
    :type odb_latitude_variable: str


    :param odb_longitude_variable: Specifies the ODB column interpreted as longitude when ``odb_plot_type`` is set to geo_points or geo_vectors. The default is lon@hdr.
    :type odb_longitude_variable: str


    :param odb_x_component_variable: Specifies the ODB column interpreted as the x component of the vector when ``odb_plot_type`` is set to geo_vectors or xy_vectors. The default is obsvalue@body.
    :type odb_x_component_variable: str


    :param odb_y_component_variable: Specifies the ODB column interpreted as the y component of the vector when ``odb_plot_type`` is set to geo_vectors or xy_vectors. The default is obsvalue@body#1.
    :type odb_y_component_variable: str


    :param odb_value_variable: Specifies the ODB column interpreted as the value in each plot type. The default is obsvalue@body.
    :type odb_value_variable: str


    :param odb_metadata_variables: Specifies the list of columns extracted and added to the resulting ODB file on top of the columns directly used for visualisation. This parameter accepts wildcards (e.g. *.hdr`), to add all the columns from the source ODB to the result use : *`. The default is an empty string (no extra columns added).
    :type odb_metadata_variables: str or list[str]


    :param odb_parameters: The default is an empty string.
    :type odb_parameters: str


    :param odb_from: Defines the FROM statement of the ODB/SQL query.
    :type odb_from: str


    :param odb_where: Defines the WHERE statement of the ODB/SQL query.
    :type odb_where: str


    :param odb_orderby: Defines the ORDERBY statement of the ODB/SQL query.
    :type odb_orderby: str


    :param odb_nb_rows: Specifies the maximum number of rows in the result. If -1 is given here the number of rows is not limited in the output. The default value is -1.
    :type odb_nb_rows: number


    :param odb_coordinates_unit: Specifies the units of the geographical co-ordinates in the input ODB. The possible values are: degrees and radians. The default is degrees.

         For older ODBs column latlon_rad@desc tells us the geographical co-ordinate units. Its 0 value indicates degrees while 1 means radians. Newer ODBs, especially the ones retrieved from MARS, as a generic rule, always use degrees as geographical co-ordinate units.
    :type odb_coordinates_unit: str


    :param odb_binning: Specifies the :func:`binning` to create gridded data out of scattered data when the ``odb_plot_type`` is xy_binning.
    :type odb_binning: str


    :param fail_on_empty_output: When it is set to Yes the icon will not fail if the resulting ODB is empty (in Macro the return value is nil while in Python it is None`). Otherwise when it is set to No the icon will ``fail_on_empty_output``. The default value is Yes.
    :type fail_on_empty_output: str


    :rtype: None


.. minigallery:: metview.odb_visualiser
    :add-heading:

