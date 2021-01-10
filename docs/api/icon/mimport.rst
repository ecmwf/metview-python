
mimport
=========================

.. container::
    
    .. container:: leftside

        .. image:: /_static/MIMPORT.png
           :width: 48px

    .. container:: rightside

		Adds an image to the plot at the specified position, which is given in plot device coordinates in cm units.


		.. note:: This function performs the same task as the `Mimport <https://confluence.ecmwf.int/display/METV/mimport>`_ icon in Metview’s user interface. It accepts its parameters as keyword arguments, described below.


.. py:function:: mimport(**kwargs)
  
    Adds an image to the plot at the specified position, which is given in plot device coordinates in cm units.


    :param import_file_name: 
    :type import_file_name: str

    :param import_file: 
    :type import_file: str

    :param import_format: 
    :type import_format: {"png", "jpeg", "gif"}, default: "png"

    :param import_x_position: 
    :type import_x_position: number, default: 0

    :param import_y_position: 
    :type import_y_position: number, default: 0

    :param import_width: 
    :type import_width: number, default: -1

    :param import_height: 
    :type import_height: number, default: -1

    :rtype: :class:`Request`
