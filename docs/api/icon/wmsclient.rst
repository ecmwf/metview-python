
wmsclient
=========================

.. container::
    
    .. container:: leftside

        .. image:: /_static/WMS_CLIENT.png
           :width: 48px

    .. container:: rightside

        This function performs the same task as the `WMS Client <https://confluence.ecmwf.int/display/METV/WMS+Client>`_ icon in Metview’s user interface. It accepts its parameters as keyword arguments, described below.


.. py:function:: wmsclient(**kwargs)
  
    Description comes here!


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


    :rtype: None
