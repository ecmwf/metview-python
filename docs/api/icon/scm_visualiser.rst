
scm_visualiser
=========================

.. container::
    
    .. container:: leftside

        .. image:: /_static/SCM_VIS.png
           :width: 48px

    .. container:: rightside

		Visualises the results of the IFS Single Column Model.
		
		.. warning:: :func:`scm_visualiser` is only available and intended to be used at ECMWF.
		
		.. tip:: A tutorial about using the Single Column Model in Metview can be found `here <https://confluence.ecmwf.int/display/METV/The+SCM+Interface+in+Metview+-+Tutorial>`_.


		.. note:: This function performs the same task as the `Scm Visualiser <https://confluence.ecmwf.int/display/METV/scm+visualiser>`_ icon in Metview’s user interface. It accepts its parameters as keyword arguments, described below.


.. py:function:: scm_visualiser(**kwargs)
  
    Visualises the results of the IFS Single Column Model.


    :param scm_plot_type: 
    :type scm_plot_type: {"time_value_curve", "time_height_matrix", "profile"}, default: "time_value_curve"

    :param scm_data_filename: 
    :type scm_data_filename: str, default: "off"

    :param scm_data: 
    :type scm_data: str

    :param scm_data_title: 
    :type scm_data_title: str, default: "data"

    :param scm_data_type: 
    :type scm_data_type: {"input", "output"}, default: "output"

    :param scm_compare_data: 
    :type scm_compare_data: {"on", "off"}, default: "off"

    :param scm_comparison_data_filename: 
    :type scm_comparison_data_filename: str, default: "off"

    :param scm_comparison_data: 
    :type scm_comparison_data: str

    :param scm_comparison_data_title: 
    :type scm_comparison_data_title: str, default: "comparison data"

    :param scm_comparison_mode: 
    :type scm_comparison_mode: {"overlay", "difference"}, default: "overlay"

    :param scm_output_1d_variables: 
    :type scm_output_1d_variables: str or list[str], default: "t_skin"

    :param scm_output_2d_variables: 
    :type scm_output_2d_variables: str or list[str], default: "t"

    :param scm_input_1d_variables: 
    :type scm_input_1d_variables: str or list[str], default: "t_skin"

    :param scm_input_2d_variables: 
    :type scm_input_2d_variables: str or list[str], default: "t"

    :param scm_times: 
    :type scm_times: str or list[str], default: "0"

    :param scm_x_min_list: 
    :type scm_x_min_list: float or list[float]

    :param scm_x_max_list: 
    :type scm_x_max_list: float or list[float]

    :param scm_y_min_list: 
    :type scm_y_min_list: float or list[float]

    :param scm_y_max_list: 
    :type scm_y_max_list: float or list[float]

    :param scm_value_min_list: 
    :type scm_value_min_list: float or list[float]

    :param scm_value_max_list: 
    :type scm_value_max_list: float or list[float]

    :param scm_grid: 
    :type scm_grid: {"on", "off"}, default: "off"

    :param scm_output_mode: 
    :type scm_output_mode: {"screen", "postscript", "png", "pdf"}, default: "screen"

    :param scm_output_file_path: 
    :type scm_output_file_path: str, default: "scm_out.ps"

    :rtype: :class:`Request`


.. mv-minigallery:: scm_visualiser

