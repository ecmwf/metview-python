interpolate
=============


.. py:function:: interpolate(fs, lat, lon)
.. py:function:: interpolate(fs, locations)
   :noindex:

   Interpolate the values of ``fs`` to a given location(s) using **bilinear** interpolation. 
     
   :param fs: input fieldset
   :type fs: :class:`Fieldset`
   :param lat: latitude of target location
   :type lat: number
   :param lon: longitude of target location
   :type lon: number
   :param locations: multiple target locations
   :type locations: list or :class:`Geopoints`
   :rtype: number or ndarray or :class:`Geopoints` or None

   A **single target location** can be defined with ``lat`` and ``lon`` or by specifying a list of [lat, lon] as ``locations``. If ``fs`` has only one field, a number is returned; otherwise a 1D-ndarray is returned. Where it is not possible to generate a sensible value due to lack of valid data in ``fs``, None is returned.

   For multiple target locations ``locations`` must be a :class:`Geopoints` and in this case the first field in ``fs`` is interpolated for each position of the :class:`Geopoints`. The output is then another :class:`Geopoints` taking the date, time and level from ``fs``. Where it is not possible to generate a sensible value due to lack of valid data in the fieldset NaN is used (this can be removed from the output with :func:`remove_missing_values`). 
   
   .. note::
      A similar function, :func:`nearest_gridpoint`, also exists.


.. mv-minigallery:: interpolate
