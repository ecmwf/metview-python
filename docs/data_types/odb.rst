ODB object
******************

.. py:class:: Odb

What is ODB?
^^^^^^^^^^^^^^^^^

   ODB (Observation DataBase) is a file-based database-like system developed at ECMWF to store and retrieve large volumes of meteorological observational and feedback data efficiently for use within the IFS.

   Currently, ODB files come in two flavours:

   * ODB-1 (the original hierarchical table format capable of running in a parallel environment within IFS)
   * ODB-2 (a flat format with a modern API used for archiving in MARS).

   Data from ODB can be extracted using the ODB/SQL query language, which is generally a small subset of SQL with some useful extensions.

   Metview uses ECMWF's ODC library for handling ODB-2 data. The documentation for how to construct
   queries with it can be found in the documentation of its predecessor, `ODB API <https://confluence.ecmwf.int/display/ODBAPI>`_.

   
Construction
^^^^^^^^^^^^^^^^^

   A ODB can be read from disk using :ref:`read() <read_fn>`:
   
      .. code-block:: python
   
         import metview as mv
   
         d = mv.read("mydata.odb")
         
Examining ODB contents
^^^^^^^^^^^^^^^^^^^^^^^^

   If Metview has been built with its graphical user interface, the contents of an ODB 
   can be inspected with the ODB Examiner, which can be started up from the user interface (right-click examine on the icon).

Filtering ODB
^^^^^^^^^^^^^^^^^^^^

   Filtering ODB data is performed with :func:`odb_filter`, which can perform an ODB/SQL query resulting in a new ODB:

Visualising ODB
^^^^^^^^^^^^^^^^^^^^

   The :func:`odb_visualiser` is used to visualise (and optionally filter) ODB data using various techniques and plot types.


.. include:: /gen_files/toc/odb_obj.rst
.. include:: /gen_files/toc/odb.rst
