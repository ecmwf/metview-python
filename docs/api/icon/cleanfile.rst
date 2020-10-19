
cleanfile
=========================

.. container::
    
    .. container:: leftside

        .. image:: /_static/CLEANFILE.png
           :width: 48px

    .. container:: rightside

        This icon performs an ODB/SQL query on an ODB database (ODB-1) or file (ODB-2). The result is always an ODB file (in ODB-2 format).


.. py:function:: cleanfile(**kwargs)
  
    Description comes here!


    :param path: Specifies the ``path`` to the input ``data``.
    :type path: str


    :param data: Specifies the input as an icon. If both an icon (in ``data`` ) and a filename (in ``path`` ) are specified the icon takes precedence.
    :type data: str


    :param skip_hirlam_custom_record: The possible values are yes and no. The default is no.
    :type skip_hirlam_custom_record: str


    :rtype: None


.. minigallery:: metview.cleanfile
    :add-heading:

