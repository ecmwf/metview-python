
bufr_picker
=========================

.. container::
    
    .. container:: leftside

        .. image:: /_static/BUFRPICKER.png
           :width: 48px

    .. container:: rightside

        This icon performs an ODB/SQL query on an ODB database (ODB-1) or file (ODB-2). The result is always an ODB file (in ODB-2 format).


.. py:function:: bufr_picker(**kwargs)
  
    Description comes here!


    :param data: Drop any icon containing or returning BUFR ``data``. This may be, for example, a _MARS Retrieval (of observations) icon, a BUFR file icon or an Observation Filter icon (provided it ``output``s BUFR, not geopoints).
    :type data: str


    :param output: Specifies the ``output`` format you want. Specify one of the geopoints formats ( Geographical Points, Geographical Polar Vectors or Geographical X Y Vectors ).
    :type output: str


    :param parameter: 
    :type parameter: str or list[str]


    :param missing_data: If set to Ignore , missing ``data`` is not included in the ``output`` file; this is the default behaviour. If set to Include , missing ``data`` will be ``output`` to the geopoints file, its value being set to that specified by Missing ``data`` Value. Note that when the ``output`` format is one of the two geopoints vector formats, the observation is considered missing if one or both of the ``parameter``s are missing.
    :type missing_data: str


    :param missing_data_value: Available only for Missing ``data`` set to Include. Any missing observations will be ``output`` as this value (default 0). It is wise, therefore, to ensure that this value is outwith the range of possible values for the requested ``parameter``(s)
    :type missing_data_value: number


    :param coordinate_descriptors: 
    :type coordinate_descriptors: str or list[str]


    :param coordinate_values: 
    :type coordinate_values: str or list[str]


    :param fail_on_error: If set to Yes , then any error encountered when trying to decode the input ``data`` will result in the module failing (turn red and abort any dependent processes); if run inside a macro, the macro will also fail. If set to No , then any such errors will not be fatal, and an empty ``data`` file will be returned.
    :type fail_on_error: str


    :rtype: None


.. minigallery:: metview.bufr_picker
    :add-heading:

