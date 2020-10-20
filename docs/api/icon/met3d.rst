
met3d
=========================

.. container::
    
    .. container:: leftside

        .. image:: /_static/MET3D.png
           :width: 48px

    .. container:: rightside

        This function represents the `Met3d <https://confluence.ecmwf.int/display/METV/met3d>`_ icon in Metview's user interface.


.. py:function:: met3d(**kwargs)
  
    Description comes here!


    :param source: Specifies the path to the input GRIB ``data``.
    :type source: str


    :param data: Specifies the input GRIB as an icon/set of icons. If both an icon (in ``data`` ) and a filename (in ``source`` ) are specified the icon takes precedence.
    :type data: str


    :param pipeline_file: Specifies the ``pipeline_file`` for the Met.3D session. The default value is DEFAULT which means a pre-built ``pipeline_file`` will be used.
    :type pipeline_file: str


    :param frontend_file: Specifies the ``frontend_file`` for the Met.3D session. The default value is DEFAULT which means a pre-built ``frontend_file`` will be used.
    :type frontend_file: str


    :rtype: None
