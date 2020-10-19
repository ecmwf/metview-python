write
==========

.. py:function write(path, *args)
.. py:function write(filehandler, *args)

    Writes output to a file specified by ``path`` or ``filehandler`` (previously assigned to it by the file() function). 
    
    :param path: file path
    :type path: str
    :rtype: None
    
    The output file type depends on the type that is being written - if it is a :class:`Fieldset` then it creates a GRIB file, if it is observations it creates a BUFR file, if geopoints creates a geopoints file, if it is anything else it will create a text file with the current value of the variable(s) - an icon (associated with the corresponding file type) is also created if the files are saved to the Metview directory structure.

    If you use write() sequentially, note that it will overwrite any previous output if called with a file name, but will add to previous output if called with a filehandler.

    Note that special characters such as newline and tab can be written to text files.