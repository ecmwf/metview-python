append
************

..  py:function:: append(path, obj1, [obj2, ...])
..  py:function:: append(filehandler, obj1, [obj2, ...])
    :noindex:

    Appends output to a file specified by ``path`` or ``filehandler``.
    
    :param path: output file path
    :type path: str
    :param filehandler: Metview filehandler of the output file (has to be created with :func:`file`)
    :type filehandler: Metview filehandler object
    :param obj: data objects to be written into the output
    :type obj: Metview data object (see below)
    :rtype: None
    
    The output file format depends on the object type that is being written:
    
    ..  list-table::
        :header-rows: 1 
    
        * - Object
          - Output format
        * - :class:`Fieldset`
          - GRIB
        * - :class:`Geopoints`
          - Geopoints
        * - :class:`Bufr`
          - BUFR
        * - :class:`NetCDF`
          - NetCDF
        * - :class:`Odb`
          - ODB
        * - other types
          - text

    Note that special characters such as newline and tab can be written to text files.

    .. note::

        See also :func:`write`.

.. mv-minigallery:: write
