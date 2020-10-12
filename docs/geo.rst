Geographic functions
*********************

.. py:function:: distance(data, lat, lon)
.. py:function:: distance(data, coords)
   :noindex:

   Returns a new ``data`` with the value in each point being the distance in **metres** from a given geographical location (the reference). 
   
   :param data: input fieldset
   :type data: :class:`Fieldset` or :class:`Geopoints`
   :param float lat: latitude of the reference point 
   :param float lon: longitude of the reference point
   :param coords: coordinates of the reference point as [lat, lon]
   :type coords: list
   :rtype: the same type as ``data``.
   
   The reference location should be specified in degrees.