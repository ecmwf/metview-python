
odb_filter
=========================

.. container::
    
    .. container:: leftside

        .. image:: /_static/ODB_FILTER.png
           :width: 48px

    .. container:: rightside

		Performs an `ODB/SQL <https://confluence.ecmwf.int/display/ODBAPI/SQL>`_ query on an `ODB <https://confluence.ecmwf.int/display/METV/ODB+Overview>`_ database (ODB-1) or file (ODB-2 or ODC). The result is always an ODB file (in ODC format).
		
		.. tip:: A tutorial about using ODB in Metview can be found `here <https://confluence.ecmwf.int/display/METV/ODB+Tutorial>`_.


		.. note:: This function performs the same task as the `ODB Filter <https://confluence.ecmwf.int/display/METV/ODB+Filter>`_ icon in Metview’s user interface. It accepts its parameters as keyword arguments, described below.


.. py:function:: odb_filter(**kwargs)
  
    Performs an ODB/SQL query on an ODB.


    :param odb_filename: Specifies the path to the input ODB.
    :type odb_filename: str, default: "off"

    :param odb_data: Specifies the input as an :class:`Odb`. If both ``odb_data`` and ``odb_filename`` are specified ``odb_data`` takes precedence.
    :type odb_data: :class:`Odb`

    :param odb_query: Specifies the ODB/SQL query to run.
    :type odb_query: str

    :param odb_nb_rows: Specifies the maximum number of rows in the result. If -1 is given here the number of rows is not limited in the output.
    :type odb_nb_rows: number, default: -1

    :param fail_on_empty_output: Controls the behaviour when the resulting :class:`Odb` is empty. If it is set to "no" :func:`odb_filter` will return None, while if the value is "yes" the Python script running :func:`odb_filter` will abort.
    :type fail_on_empty_output: {"yes", "no"}, default: "yes"

    :rtype: :class:`Odb`


.. mv-minigallery:: odb_filter

