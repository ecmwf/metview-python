
odb_filter
=========================

.. container::
    
    .. container:: leftside

        .. image:: /_static/ODB_FILTER.png
           :width: 48px

    .. container:: rightside

        This function performs the same task as the `ODB Filter <https://confluence.ecmwf.int/display/METV/ODB+Filter>`_ icon in Metview’s user interface. It accepts its parameters as keyword arguments, described below.


.. py:function:: odb_filter(**kwargs)
  
    Description comes here!


    :param odb_filename: Specifies the path to the input ODB
    :type odb_filename: str, default: "off"


    :param odb_data: Specifies the input ODB as an icon. If both an icon (in ``odb_data`` ) and a filename (in ``odb_filename`` ) are specified the icon takes precedence.
    :type odb_data: str


    :param odb_query: Specifies the [ODB/SQL](/display/ODBAPI/SQL) query to run.
    :type odb_query: str


    :param odb_nb_rows: Specifies the maximum number of rows in the result. If -1 is given here the number of rows is not limited in the output. The default value is -1.
    :type odb_nb_rows: number, default: -1


    :param fail_on_empty_output: When it is set to "no" the icon will not fail if the resulting ODB is empty (in Macro the return value is nil while in Python it is None`). Otherwise when it is set to "yes" the icon will ``fail_on_empty_output``. The default value is "yes".
    :type fail_on_empty_output: {"yes", "no"}, default: "yes"


    :rtype: None


.. minigallery:: metview.odb_filter
    :add-heading:

