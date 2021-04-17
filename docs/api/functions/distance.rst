distance
=============


.. py:function:: distance(fs, lat, lon)
.. py:function:: distance(fs, coords)
   :noindex:

   Returns a :class:`Fieldset` with the value in each grid point being the distance in **metres** from a given geographical location (the reference). 
   
   :param fs: input fieldset
   :type fs: :class:`Fieldset`
   :param number lat: latitude of the reference point 
   :param number lon: longitude of the reference point
   :param coords: coordinates of the reference point as [lat, lon]
   :type coords: list
   :rtype: :class:`Fieldset`
   
   The reference location should be specified in degrees.



.. py:function:: distance(gpt, lat, lon)
.. py:function:: distance(gpt, coords)
   :noindex:

   Returns a :class:`Geopoints` with the value in each grid point being the distance in **metres** from a given geographical location (the reference). 
   
   :param fs: input geopoints
   :type fs: :class:`Geopoints`
   :param number lat: latitude of the reference point 
   :param number lon: longitude of the reference point
   :param coords: coordinates of the reference point as [lat, lon]
   :type coords: list
   :rtype: :class:`Geopoints`
   
   The reference location should be specified in degrees. A geopoint with either latitude or longitude set to missing value will have a distance of missing value.


.. mv-minigallery:: distance
