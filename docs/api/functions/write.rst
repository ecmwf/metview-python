write
************

..  py:function:: write(path, obj1, [obj2, ...])
..  py:function:: write(filehandler, obj1, [obj2, ...])
    :noindex:

    Writes output to a file specified by ``path`` or ``filehandler``.
    
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

    If you use :func:`write` sequentially, note that it will overwrite any previous output if called with a ``path``, but will add to previous output if called with a ``filehandler``.
    
    Note that special characters such as newline and tab can be written to text files.

.. mv-minigallery:: write
