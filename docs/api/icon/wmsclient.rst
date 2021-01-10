
wmsclient
=========================

.. container::
    
    .. container:: leftside

        .. image:: /_static/WMS_CLIENT.png
           :width: 48px

    .. container:: rightside

		Implements a WMS (Web Map Service) client.
		
		.. note:: :func:`wmsclient` was primarily developed for Metview's user interface where it (as an icon) has a specialised editor that allows to inspect the GetCapabilities request and build and visualise the GetMap request. See the `Metview WMS Tutorial <https://confluence.ecmwf.int/display/METV/Metview+WMS+Tutorial>`_ for details.
		
		
		


		.. note:: This function performs the same task as the `WMS Client <https://confluence.ecmwf.int/display/METV/WMS+Client>`_ icon in Metview’s user interface. It accepts its parameters as keyword arguments, described below.


.. py:function:: wmsclient(**kwargs)
  
    Implements a WMS (Web Map Service) client.


    :param mode: 
    :type mode: {"expert", "interactive"}, default: "interactive"

    :param server: 
    :type server: str

    :param version: 
    :type version: str

    :param request: 
    :type request: str

    :param extra_getcap_par: 
    :type extra_getcap_par: str

    :param extra_getmap_par: 
    :type extra_getmap_par: str

    :param http_user: 
    :type http_user: str

    :param http_password: 
    :type http_password: str

    :param time_dimensions: 
    :type time_dimensions: str

    :rtype: :class:`Request`
