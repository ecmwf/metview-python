
met3d
=========================

.. container::
    
    .. container:: leftside

        .. image:: /_static/MET3D.png
           :width: 48px

    .. container:: rightside

        This function performs the same task as the `Met3d <https://confluence.ecmwf.int/display/METV/met3d>`_ icon in Metview’s user interface. It accepts its parameters as keyword arguments, described below.


.. py:function:: met3d(**kwargs)
  
    Description comes here!


    :param source: Specifies the path to the input GRIB ``data``.
    :type source: str, default: "off"


    :param data: Specifies the input GRIB as an icon/set of icons. If both an icon (in ``data`` ) and a filename (in ``source`` ) are specified the icon takes precedence.
    :type data: str


    :param pipeline_file: Specifies the ``pipeline_file`` for the Met.3D session. The "default" value is "default" which means a pre-built ``pipeline_file`` will be used.
    :type pipeline_file: str, default: "default"


    :param frontend_file: Specifies the ``frontend_file`` for the Met.3D session. The "default" value is "default" which means a pre-built ``frontend_file`` will be used.
    :type frontend_file: str, default: "default"


    :rtype: None
