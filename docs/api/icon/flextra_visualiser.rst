
flextra_visualiser
=========================

.. container::
    
    .. container:: leftside

        .. image:: /_static/FLEXTRA_VISUALISER.png
           :width: 48px

    .. container:: rightside

        This function performs the same task as the `Flextra Visualiser <https://confluence.ecmwf.int/display/METV/flextra+visualiser>`_ icon in Metview’s user interface. It accepts its parameters as keyword arguments, described below.


.. py:function:: flextra_visualiser(**kwargs)
  
    Description comes here!


    :param flextra_plot_type: 
    :type flextra_plot_type: str, default: "geo_points"


    :param flextra_plot_content: 
    :type flextra_plot_content: str, default: "trajectory"


    :param flextra_filename: 
    :type flextra_filename: str, default: "off"


    :param flextra_data: 
    :type flextra_data: str


    :param flextra_group_index: 
    :type flextra_group_index: number, default: 1


    :param flextra_x_variable: 
    :type flextra_x_variable: str, default: "date"


    :param flextra_y_variable: 
    :type flextra_y_variable: str, default: "pressure"


    :param flextra_label_variable: 
    :type flextra_label_variable: {"time", "latitude", "longitude", "eta", "pressure", "height", "heght_agl", "pv", "theta"}, default: "time"


    :param flextra_label_period: 
    :type flextra_label_period: {"6h", "12h", "24h", "48h"}, default: "12h"


    :rtype: None


.. minigallery:: metview.flextra_visualiser
    :add-heading:

