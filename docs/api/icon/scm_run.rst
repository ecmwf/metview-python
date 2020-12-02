
scm_run
=========================

.. container::
    
    .. container:: leftside

        .. image:: /_static/SCM_RUN.png
           :width: 48px

    .. container:: rightside

        This function performs the same task as the `Scm Run <https://confluence.ecmwf.int/display/METV/scm+run>`_ icon in Metview’s user interface. It accepts its parameters as keyword arguments, described below.


.. py:function:: scm_run(**kwargs)
  
    Description comes here!


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


    :rtype: None
