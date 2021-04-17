bearing
==========

.. py:function:: bearing (fs, lat, lon)
.. py:function:: bearing (fs, coords)
   :noindex:

   Computes the bearing for each grid point in ``fs`` with reference to the given location. 
   
   :param fs: input fieldset
   :type fs: :class:`Fieldset`
   :param lat: latitude of the reference point
   :type lat: number
   :param lon: longitude of the reference point
   :type lon: number
   :param coords: coordinates of the reference point as [lat, lon]
   :type coords: list
   :rtype: :class:`Fieldset`
   
   The **bearing** is the angle between the Northward meridian going through the reference point and the great circle connecting the reference point and the given gridpoint. It is measured in degrees clockwise from North. If a gridpoint is located on the same latitude as the reference point the bearing is regarded constant: it is either 90° (East) or 270° (West). If the gridpoint is co-located with the reference point the bearing is set to a missing value. The reference location should be specified in degrees.


.. mv-minigallery:: bearing
