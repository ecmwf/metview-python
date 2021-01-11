
odb_visualiser
=========================

.. container::
    
    .. container:: leftside

        .. image:: /_static/ODB_VISUALISER.png
           :width: 48px

    .. container:: rightside

		Defines the visualisation for `ODB <https://confluence.ecmwf.int/display/METV/ODB+Overview>`_ data using various plot types. Optionally it can perform an `ODB/SQL <https://confluence.ecmwf.int/display/ODBAPI/SQL>`_ query on the input ODB and visualises the resulting data. It works for both databases (ODB-1) and files (ODB-2 or ODC).
		
		.. tip:: A tutorial about using ODB in Metview can be found `here <https://confluence.ecmwf.int/display/METV/ODB+Tutorial>`_.
		
		**How can ODB/SQL queries be used in odb_visualiser?**
		
		The queries cannot directly be used but have to be mapped for a specific set of arguments. We illustrate it with a simple example. Let us suppose we want to perform this ODB/SQL query on our data:
		
		.. code-block:: sql
		
		    SELECT
		        lat@hdr,
		        lon@hdr,
		        fg_depar@body
		    WHERE
		        vertco_reference_1@body = 5
		    ORDERBY
		        obsvalue@body
		
		and want to plot the results as points (symbols) on a map. To achieve this we need to use the following code:
		
		.. code-block:: python
		
		    import metview as mv
		
		    db = mv.read("my_data.odb")
		
		    vis = mv.odb_viusaliser(
		        odb_data=db,
		        odb_latitude_variable="lat@hdr",
		        odb_longitude_variable="lon@hdr",
		        odb_value_variable="fg_depar@body",
		        odb_where="vertco_reference_1@body = 5",
		        odb_orderby="obsvalue@body")
		    
		    mv.plot(vis)


		.. note:: This function performs the same task as the `ODB Visualiser <https://confluence.ecmwf.int/display/METV/ODB+Visualiser>`_ icon in Metview’s user interface. It accepts its parameters as keyword arguments, described below.


.. py:function:: odb_visualiser(**kwargs)
  
    Defines the visualisation for ODB data.


    :param odb_plot_type: Specifies the plot type to be generated. The possible values are as follows:
		
		* "geo_points": points plotted onto a map
		* "geo_vectors": vectors plotted onto a map
		* "xy_points": points plotted into a :func:`cartesianview`
		* "xy_vectors": vectors plotted into a :func:`cartesianview`
		* "xy_binning": gridded values by binning plotted into a :func:`cartesianview`
    :type odb_plot_type: {"geo_points", "geo_vectors", "xy_points", "xy_vectors", "xy_binning"}, default: "geo_points"

    :param odb_filename: Specifies the path to the input ODB.
    :type odb_filename: str, default: "off"

    :param odb_data: Specifies the input :class:`Odb`. If both ``odb_data`` and ``odb_filename`` are specified ``odb_data`` takes precedence.
    :type odb_data: :class:`Odb`

    :param odb_x_type: Specifies the type of the x coordinate when ``odb_plot_type`` is set to "xy_points", "xy_vectors" or "xy_binning".
    :type odb_x_type: {"number", "date"}, default: "number"

    :param odb_y_type: Specifies the type of the y coordinate when ``odb_plot_type`` is set to "xy_points", "xy_vectors" or "xy_binning".
    :type odb_y_type: {"number", "date"}, default: "number"

    :param odb_x_variable: Specifies the ODB column interpreted as the x coordinate when ``odb_plot_type`` is set to "geo_vectors", "xy_vectors" or "xy_binning". The default is an empty string.
    :type odb_x_variable: str

    :param odb_y_variable: Specifies the ODB column interpreted as the y coordinate when ``odb_plot_type`` is set to "geo_vectors", "xy_vectors" or "xy_binning". The default is an empty string.
    :type odb_y_variable: str

    :param odb_latitude_variable: Specifies the ODB column interpreted as latitude when ``odb_plot_type`` is set to "geo_points" or "geo_vectors".
    :type odb_latitude_variable: str, default: "lat\@hdr"

    :param odb_longitude_variable: Specifies the ODB column interpreted as longitude when ``odb_plot_type`` is set to "geo_points" or "geo_vectors".
    :type odb_longitude_variable: str, default: "lon\@hdr"

    :param odb_x_component_variable: Specifies the ODB column interpreted as the x component of the vector when ``odb_plot_type`` is set to "geo_vectors" or "xy_vectors".
    :type odb_x_component_variable: str, default: "obsvalue\@body"

    :param odb_y_component_variable: Specifies the ODB column interpreted as the y component of the vector when ``odb_plot_type`` is set to "geo_vectors" or "xy_vectors".
    :type odb_y_component_variable: str, default: "obsvalue\@body#1"

    :param odb_value_variable: Specifies the ODB column interpreted as the value in each plot type.
    :type odb_value_variable: str, default: "obsvalue\@body"

    :param odb_metadata_variables: Specifies the list of columns extracted and added to the resulting ODB file on top of the columns directly used for visualisation. This parameter accepts wildcards (e.g. "\*.hdr"), to add all the columns from the source ODB to the result use "\*". The default is an empty string (no extra columns added).
    :type odb_metadata_variables: str or list[str]

    :param odb_parameters: 
    :type odb_parameters: str

    :param odb_from: Defines the FROM statement of the ODB/SQL query.
    :type odb_from: str

    :param odb_where: Defines the WHERE statement of the ODB/SQL query.
    :type odb_where: str

    :param odb_orderby: Defines the ORDERBY statement of the ODB/SQL query.
    :type odb_orderby: str

    :param odb_nb_rows: Specifies the maximum number of rows in the result. If -1 is given here the number of rows is not limited in the output.
    :type odb_nb_rows: number, default: -1

    :param odb_coordinates_unit: Specifies the units of the geographical co-ordinates in the input ODB. For older ODBs column "latlon_rad\@desc" tells us the geographical co-ordinate units. Its 0 value indicates "degrees" while 1 means radians. Newer ODBs, especially the ones retrieved from MARS, as a generic rule, always "degrees" as geographical co-ordinate units.
    :type odb_coordinates_unit: {"degrees", "radians"}, default: "degrees"

    :param odb_binning: Specifies the :func:`binning` to create gridded data out of scattered data when the ``odb_plot_type`` is "xy_binning".
    :type odb_binning: :class:`Request`

    :param fail_on_empty_output: Controls the behaviour when the resulting :class:`Odb` is empty. If it is set to "no" :func:`odb_visualiser` will return None, while if the value is "yes" the Python script running :func:`odb_visualiser` will abort.
    :type fail_on_empty_output: {"yes", "no"}, default: "yes"

    :rtype: :class:`Request`


.. minigallery:: metview.odb_visualiser
    :add-heading:

