
scm_run
=========================

.. container::
    
    .. container:: leftside

        .. image:: /_static/SCM_RUN.png
           :width: 48px

    .. container:: rightside

		Runs the IFS Single Column Model.
		
		.. warning:: :func:`scm_run` is only available and intended to be used at ECMWF.
		
		.. tip:: A tutorial about using the Single Column Model in Metview can be found `here <https://confluence.ecmwf.int/display/METV/The+SCM+Interface+in+Metview+-+Tutorial>`_.


		.. note:: This function performs the same task as the `Scm Run <https://confluence.ecmwf.int/display/METV/scm+run>`_ icon in Metview’s user interface. It accepts its parameters as keyword arguments, described below.


.. py:function:: scm_run(**kwargs)
  
    Runs the IFS Single Column Model.


    :param scm_exe_path: 
    :type scm_exe_path: str

    :param scm_input_data: 
    :type scm_input_data: str

    :param scm_input_data_path: 
    :type scm_input_data_path: str

    :param scm_namelist: 
    :type scm_namelist: str

    :param scm_namelist_path: 
    :type scm_namelist_path: str

    :param scm_vtable: 
    :type scm_vtable: str

    :param scm_vtable_path: 
    :type scm_vtable_path: str

    :param scm_rclim_path: 
    :type scm_rclim_path: str

    :param scm_copy_output_data: 
    :type scm_copy_output_data: {"on", "off"}, default: "off"

    :param scm_output_data_path: 
    :type scm_output_data_path: str, default: "scm_out.nc"

    :rtype: :class:`Request`


.. mv-minigallery:: scm_run

