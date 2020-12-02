
download
=========================

.. container::
    
    .. container:: leftside

        .. image:: /_static/DOWNLOAD.png
           :width: 48px

    .. container:: rightside

        This function performs the same task as the `Download from URL <https://confluence.ecmwf.int/display/METV/Download+from+URL>`_ icon in Metview’s user interface. It accepts its parameters as keyword arguments, described below.


.. py:function:: download(**kwargs)
  
    Description comes here!


    :param url: Provide a URL that will return a file. This can be, for instance, a URL that points directly to a particular file, or a request to a web service that generates and returns some data.

    :type url: str


    :param target: This parameter is optional. If set, the downloaded file will be copied to the given location. The target path can be absolute or relative, but must include the file name, and the parent directory must already exist. If running from an interactive session, a relative path will be relative to the folder containing the script; when running in batch mode, the path will be relative to where the :command:`metview` command was run from.  
    :type target: str


    :rtype: None
