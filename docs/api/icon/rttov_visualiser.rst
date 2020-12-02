
rttov_visualiser
=========================

.. container::
    
    .. container:: leftside

        .. image:: /_static/RTTOV_VISUALISER.png
           :width: 48px

    .. container:: rightside

        This function performs the same task as the `Rttov Visualiser <https://confluence.ecmwf.int/display/METV/rttov+visualiser>`_ icon in Metview’s user interface. It accepts its parameters as keyword arguments, described below.


.. py:function:: rttov_visualiser(**kwargs)
  
    Description comes here!


    :param rttov_plot_type: 
    :type rttov_plot_type: {"channel_tb_graph", "jacobian_channel_curve", "jacobian_matrix"}, default: "channel_tb_graph"


    :param rttov_data: 
    :type rttov_data: str


    :param rttov_filename: 
    :type rttov_filename: str, default: "off"


    :param rttov_jacobian_channel: 
    :type rttov_jacobian_channel: number, default: 1


    :rtype: None
