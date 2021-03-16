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

The ODB icon
^^^^^^^^^^^^^^^^^

   Metview automatically recognizes both ODB-1 and ODB-2 formats and assigns the same icon to both types of file in the user interface:

Examining ODB contents
^^^^^^^^^^^^^^^^^^^^^^^^

   The meta-data and data contents of an ODB can be inspected with the ODB Examiner, which can be started up from the user interface (right-click examine on the icon).

Filtering ODB
^^^^^^^^^^^^^^^^^^^^

   Filtering ODB data is performed with the ODB Filter icon, which can perform an ODB/SQL query resulting in a new ODB:

Visualising ODB
^^^^^^^^^^^^^^^^^^^^

   The ODB Visualiser icon is used to visualise (and optionally filter) ODB data using various techniques and plot types:


.. include:: /gen_files/toc/odb_obj.rst