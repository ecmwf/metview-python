
ecfs
=========================

.. container::
    
    .. container:: leftside

        .. image:: /_static/ECFS.png
           :width: 48px

    .. container:: rightside

        This function represents the `Ecfs <https://confluence.ecmwf.int/display/METV/ecfs>`_ icon in Metview's user interface.


.. py:function:: ecfs(**kwargs)
  
    Description comes here!


    :param ecfs_domain: Specifies the ``ecfs_domain``. By default this is ec: and so far it is the only valid input.
    :type ecfs_domain: str


    :param file_name: Specifies the name of the file to be retrieved from ECFS. The name specified must not include the ec`: prefix, but should include the ECFS path, e.g.` /uid/dir1/.../filename`. If the file resides in the root ECFS directory, you can only specify the ``file_name``.

         Detailed information on ECFS can be obtained from the UNIX prompt. Given that ECFS commands mimic corresponding UNIX commands, you will obtain a man page for ECFS commands by entering :

           man ecfs
    :type file_name: str


    :rtype: None
