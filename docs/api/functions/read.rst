read
========

.. py:function read(path)

    Reads a data file specified by ``path``. 

    :param path: file path
    :type path: str
    :rtype: :class:`Fieldset` or :class:`Geopoints` or :class:`Bufr` or :class:`NetCDF` or :class:`Odb`

    The function returns an object of the corresponding type.

    The variable of type list is used to hold the contents of an ASCII file - the elements of this list variable are themselves lists, each holding a line of text. The elements of these sub lists are the text line tokens (component strings) arising from the parsing of the text.
