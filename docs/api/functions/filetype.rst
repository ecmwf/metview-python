filetype
==============

.. py:function:: filetype(path)

    Returns the internal Metview type as a string of the specified file. 
    
    :param path: file path
    :type path: str
    :rtype: str

    When Metview cannot determine the type it returns the string "BAD". For Metview icons not representing data it returns "NOTE".

.. mv-minigallery:: filetype
