.. _read_fn:

read
************

.. py:function:: read(path)
    :noindex:

    Reads a data file specified by ``path``. 

    :param path: file path
    :type path: str
    :rtype: Metview data object (see below)

    The resulting object type depends on the file format that is being read:

    ..  list-table::
        :header-rows: 1 

        * - Input format
          - Object
        * - GRIB
          - :class:`Fieldset`
        * - Geopoints
          - :class:`Geopoints`
        * - BUFR
          - :class:`Bufr`
        * - NetCDF
          - :class:`NetCDF`
        * - ODB
          - :class:`Odb`
        * - text
          - list (one item per line)
        * - other
          - object of the corresponding type 
  

.. mv-minigallery:: read_fn

