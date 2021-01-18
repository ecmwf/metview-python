
ecfs
=========================

.. container::
    
    .. container:: leftside

        .. image:: /_static/ECFS.png
           :width: 48px

    .. container:: rightside

        Retrieves files from ECFS (European Centre File Store).
				
		.. warning:: Only available and intented to be used at ECMWF.

        .. note:: This function performs the same task as the `Ecfs <https://confluence.ecmwf.int/display/METV/ecfs>`_ icon in Metview’s user interface. It accepts its parameters as keyword arguments, described below.


.. py:function:: ecfs(**kwargs)
  
    Retrieves files from ECFS.


    :param ecfs_domain: Specifies the ECFS domain. By default this is "ec:" and so far it is the only valid input.
    :type ecfs_domain: str, default: "ec:"

    :param file_name: Specifies the name of the file to be retrieved from ECFS. The name specified must not include the "ec:" prefix, but should include the ECFS path, e.g. "/uid/dir1/.../filename". If the file resides in the root ECFS directory, you can only specify the file name.
    :type file_name: str

    :rtype: Metview object representing the type of the retrieved data.
