ODB filter
******************

What is ODB?

ODB is a database developed at ECMWF to store and retrieve large volumes of meteorological observational and feedback data efficiently for use within the IFS.

Currently, ODB comes in two flavours:

    * ODB-1 (the original hierarchical table format capable of running in a parallel environment within IFS)
    * ODB-2 (a new flat format with a modern API used for archiving in MARS).

Gallery Examples using ODB Filter

.. py:function:: odb_filter(**kwargs)
  
   This icon performs an ODB/SQL query on an ODB database (ODB-1) or file (ODB-2). The result is always an ODB file (in ODB-2 format).

   :param str odb_filename: Specifies the path to the input ODB
   :param object odb_data: Specifies the input ODB as an object. If both ``odb_data`` and ``odb_filename`` are specified ``odb_data`` takes precedence. (default: None)
   :param str odb_query: Specifies the ODB/SQL query to run.
   :param int odb_nb_rows: Specifies the maximum number of rows in the result. If -1 is given here the number of rows is not limited in the output. (default: -1)
   :param str fail_on_empty_output: When it is set to "no" :func:`odb_filter` will not fail if the resulting ODB is empty (i.e. it is None). Otherwise when it is set to "yes" the :func:`odb_filter` fail on empty output. (default: "yes")
   :rtype: :class:`Odb_db`


