
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


    :param url: Provide a ``url`` that  will return a file. This can be, for instance, a ``url`` that points directly to a particular file, or a request to a web service that generates and returns some data.
    :type url: str


    :param target: This parameter is optional. If set, the downloaded file will be copied to the given location. The ``target`` path can be absolute or relative, but must include the file name, and the parent directory must already exist. If running from an interactive session, a relative path will be relative to the folder containing the macro; when running in batch mode, the path will be relative to where the metview command was run from.  

         ## Example usage

           # download the data and assign to a variable data = download(``url`` : "http://download.ecmwf.org/test-data/metview/gallery/2m_temperature.grib") print('Values range from ', minvalue(data), ' to ', maxvalue(data)) write('local_copy_of_file.grib', data)  # example which uses the ``target`` parameter to directly save the file download(``url``: "http://download.ecmwf.org/test-data/grib_api/data/budg.md5", ``target``: 'local_md5.txt')
    :type target: str


    :rtype: None
