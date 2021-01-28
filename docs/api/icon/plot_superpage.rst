
plot_superpage
=========================

.. container::
    
    .. container:: leftside

        .. image:: /_static/DISPLAYWINDOW.png
           :width: 48px

    .. container:: rightside

		Defines the top level layout for plotting. It can contain multiple :func:`plot_pages`.


		.. note:: This function performs the same task as the `Display Window <https://confluence.ecmwf.int/display/METV/Display+Window>`_ icon in Metview’s user interface. It accepts its parameters as keyword arguments, described below.


.. py:function:: plot_superpage(**kwargs)
  
    Defines the top level layout for plotting.


    :param layout_size: 
    :type layout_size: {"a4", "a3", "custom"}, default: "a4"

    :param layout_orientation: 
    :type layout_orientation: {"landscape", "portrait"}, default: "landscape"

    :param custom_width: 
    :type custom_width: number, default: 29.7

    :param custom_height: 
    :type custom_height: number, default: 21.0

    :param pages: List of plot pages.
    :type pages: list of :func:`plot_page`

    :rtype: :class:`Request`


.. mv-minigallery:: plot_superpage

