
met3d
=========================

.. container::
    
    .. container:: leftside

        .. image:: /_static/MET3D.png
           :width: 48px

    .. container:: rightside

        This icon performs an ODB/SQL query on an ODB database (ODB-1) or file (ODB-2). The result is always an ODB file (in ODB-2 format).


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


.. minigallery:: metview.met3d
    :add-heading:

