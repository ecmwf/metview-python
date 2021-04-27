rmask
=========

.. py:function:: rmask(fs, circle)
.. py:function:: rmask(fs, lat, lon, radius)
   :noindex:

   For each field in ``fs`` creates a field containing grid point values of 0 or 1 according to whether their distance to a given geographical location is larger or smaller than a given radius. 0 is assigned to points outside the radius and 1 to points inside the radius.
   
   :param fs: input fieldset
   :type fs: :class:`Fieldset`
   :param circle: circle as a list of [lat, lon, radius]
   :type circle: list[number]
   :param number lat: latitude coordinate of the centre of the circle
   :param number lon: longitude coordinate of the centre of the circle
   :param number radius: radius of the circle in m
   :rtype: :class:`Fieldset`

   .. note::
      See also :func:`mask` to define a rectangular mask.  


.. mv-minigallery:: rmask
