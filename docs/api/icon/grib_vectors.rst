
grib_vectors
=========================

.. container::
    
    .. container:: leftside

        .. image:: /_static/GRIBVECTORS.png
           :width: 48px

    .. container:: rightside

        This icon performs an ODB/SQL query on an ODB database (ODB-1) or file (ODB-2). The result is always an ODB file (in ODB-2 format).


.. py:function:: grib_vectors(**kwargs)
  
    Description comes here!


    :param type: 
    :type type: str


    :param u_component: 
    :type u_component: str


    :param v_component: 
    :type v_component: str


    :param intensity: Specifies the field to be used as the vector field ``intensity`` component. The parameter accepts any GRIB icon as input. Available when ``type`` is Polar Field.
    :type intensity: str


    :param direction: Specifies the field to be used as the vector field ``direction`` component. The parameter accepts any GRIB icon as input. Available when ``type`` is Polar Field.
    :type direction: str


    :param colouring_field: Specifies the field to be used as the colouring key. If not supplied, the computed magnitude of the vector components will be used for colouring. The parameter accepts any GRIB icon as input.
    :type colouring_field: str


    :rtype: None


.. minigallery:: metview.grib_vectors
    :add-heading:

