db_info
===========

.. py:function:: db_info(gpt, key, [column_name])

    Returns metadata about the database retrieval which generated ``gpt``. 
    
    :param gpt: input geopoints
    :type gpt: :class:`Geopoints`
    :param str key: the metadata key
    :param str column_name: name of the column if ``key`` is "column"
    :rtype: str or list of str

    ``key`` specifies the piece of information to extract; possible values are:

    * "name": the name of the database system, e.g. ODB
    * "path": the path to the database
    * "query": a list of str containing the multi-line data query
    * "column": the name of the database column used to populate a given element of the geopoints. In this case ``column_name`` must be provided, naming the geopoints element of interest - possible values are "lat", "lon", "level", "date", "time", "value" and "value".
    * "alias": similar to "column" above, but returns the name of the database alias used instead of the full column name

    .. note::
        This information is derived from the **DB_INFO** section (if it exists) in the geopoints file
        header. See :ref:`geopoints_db_info`.


.. mv-minigallery:: db_info
