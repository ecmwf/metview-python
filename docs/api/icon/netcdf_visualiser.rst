
netcdf_visualiser
=========================

.. container::
    
    .. container:: leftside

        .. image:: /_static/NETCDFVIS.png
           :width: 48px

    .. container:: rightside

		Defines the visualisation of NetCDF data allowing to specify which variables in the file should be used, and how to interpret themThe generated object can directly be used in :func:`plot`.


		.. note:: This function performs the same task as the `Netcdf Visualiser <https://confluence.ecmwf.int/display/METV/netcdf+visualiser>`_ icon in Metview’s user interface. It accepts its parameters as keyword arguments, described below.


.. py:function:: netcdf_visualiser(**kwargs)
  
    Defines the visualisation of NetCDF data.


    :param netcdf_plot_type: 
    :type netcdf_plot_type: str, default: "geo_points"

    :param netcdf_filename: 
    :type netcdf_filename: str, default: "off"

    :param netcdf_data: 
    :type netcdf_data: str

    :param netcdf_latitude_variable: 
    :type netcdf_latitude_variable: str

    :param netcdf_longitude_variable: 
    :type netcdf_longitude_variable: str

    :param netcdf_x_variable: 
    :type netcdf_x_variable: str

    :param netcdf_y_variable: 
    :type netcdf_y_variable: str

    :param netcdf_x_position_variable: 
    :type netcdf_x_position_variable: str

    :param netcdf_y_position_variable: 
    :type netcdf_y_position_variable: str

    :param netcdf_x2_variable: 
    :type netcdf_x2_variable: str

    :param netcdf_y2_variable: 
    :type netcdf_y2_variable: str

    :param netcdf_value_variable: 
    :type netcdf_value_variable: str

    :param netcdf_x_component_variable: 
    :type netcdf_x_component_variable: str

    :param netcdf_y_component_variable: 
    :type netcdf_y_component_variable: str

    :param netcdf_dimension_setting_method: 
    :type netcdf_dimension_setting_method: {"index", "value"}, default: "value"

    :param netcdf_dimension_setting: 
    :type netcdf_dimension_setting: str or list[str]

    :param netcdf_matrix_primary_index: 
    :type netcdf_matrix_primary_index: {"latitude", "longitude"}, default: "longitude"

    :param netcdf_position_type: 
    :type netcdf_position_type: {"array", "matrix"}, default: "array"

    :param netcdf_missing_attribute: 
    :type netcdf_missing_attribute: str, default: "_fillvalue"

    :rtype: :class:`Request`
.. include:: /gallery/backref/netcdf_visualiser.rst