
met3d
=========================

.. container::
    
    .. container:: leftside

        .. image:: /_static/MET3D.png
           :width: 48px

    .. container:: rightside

		Starts up the Met.3D visualisation system with the specified input GRIB data and options.


		.. note:: This function performs the same task as the `Met3d <https://confluence.ecmwf.int/display/METV/met3d>`_ icon in Metview’s user interface. It accepts its parameters as keyword arguments, described below.


.. py:function:: met3d(**kwargs)
  
    Starts up the Met.3D visualisation system.


    :param source: Specifies the path to the input GRIB data.
    :type source: str, default: "off"

    :param data: Specifies the input GRIB as a :class:`Fieldset`. If both ``data`` ``source`` are specified ``data`` takes precedence.
    :type data: :class:`Fieldset`

    :param pipeline_file: Specifies the pipeline file for the Met.3D session. When it is set to "default" a pre-built pipeline file will be used.
    :type pipeline_file: str, default: "default"

    :param frontend_file: Specifies the frontend file for the Met.3D session. When it is set to "default" a pre-built frontend file will be used.
    :type frontend_file: str, default: "default"

    :rtype: :class:`Request`
