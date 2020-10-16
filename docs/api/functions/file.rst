I/O functions
******************

.. py:function:: filetype(path)

    Returns the internal Metview type as a string of the specified file. 
    
    :param path: file path
    :type path: str
    :rtype: str

    When Metview cannot determine the type it returns the string "BAD". For Metview icons not representing data it returns "NOTE".


.. py:function:: newpage(dw)

    Forces a new page to be taken in the current PostScript/PDF file.


.. py:function print(*args)

    Prints all its arguments to the output area of the main user interface (and to that of any opened macro editor window). Note that special characters such as newline and tab can be used here.

.. py:function read(path)

    Reads a data file specified by ``path``. 

    :param path: file path
    :type path: str
    :rtype: :class:`Fieldset` or :class:`Geopoints` or :class:`Bufr` or :class:`NetCDF` or :class:`ODB`

    The function returns an object of the corresponding type.

    The variable of type list is used to hold the contents of an ASCII file - the elements of this list variable are themselves lists, each holding a line of text. The elements of these sub lists are the text line tokens (component strings) arising from the parsing of the text.


.. py:function read_table(**kwargs)

    Reads an ASCII table-based file such as a comma separated value (CSV) file. This is a Metview icon function, for detailed documentation please see Table Reader.
    

.. py:function tmpfile()

    Reserves and returns a unique file name (inside the Metview cache directory) for a temporary file. Returned filenames are unique even when there are several copies of the same macro being executed simultaneously.


.. py:function write(path, *args)
.. py:function write(filehandler, *args)

    Writes output to a file specified by ``path`` or ``filehandler`` (previously assigned to it by the file() function). 
    
    :param path: file path
    :type path: str
    :rtype: None
    
    The output file type depends on the type that is being written - if it is a :class:`Fieldset` then it creates a GRIB file, if it is observations it creates a BUFR file, if geopoints creates a geopoints file, if it is anything else it will create a text file with the current value of the variable(s) - an icon (associated with the corresponding file type) is also created if the files are saved to the Metview directory structure.

    If you use write() sequentially, note that it will overwrite any previous output if called with a file name, but will add to previous output if called with a filehandler.

    Note that special characters such as newline and tab can be written to text files.