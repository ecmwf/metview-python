nearest_gridpoint
=======================

.. py:function:: nearest_gridpoint(fs, lats, lons, [mode])
.. py:function:: nearest_gridpoint(fs, location, [mode])
.. py:function:: nearest_gridpoint(fs, gpt, [mode])
   :noindex:

   Returns the nearest gridpoint value from ``fs`` for a given location (or locations).
   
   :param fs: input fieldset
   :type fs: :class:`Fieldset`
   :param lats: target latitude(s)
   :type lats: number or ndarray
   :param lons: target longitudes(s)
   :type lons: number or ndarray
   :param location: single target location defined as a list of [lat, lon]
   :type location: list
   :param gpt: input geopoints
   :type gpt: :class:`Geopoints`
   :param str mode: specifies the way missing values are handled. The only allowed value is "valid".
   :rtype: number or ndarray or :class:`Geopoints`
  
   ``fs`` must be a gridded field. 

   The nearest gridpoint extraction depends on the arguments:

   * ``location`` defines a single location. The return value is a number when ``fs`` only contains one field, and list otherwise.
   * ``lats`` and ``lons`` can define either a single location (as number) or multiple locations (as ndarray). If a single location is specified the return value is the same as for ``location``. For multiple locations an ndarray is returned.
   * when ``gpt`` is specified only the first field of ``fs`` is used. The result is a :class:`Geopoints` containing the the nearest gridpoint values for all the locations in ``gpt``.  Where it is not possible to generate a sensible value due to lack of valid data in ``fs``, the internal geopoints missing value is used (this value can be checked for with the built-in variable geo_missing_value or removed with the function :func:`remove_missing_values`).

   Parameter ``mode`` controls the return value when the nearest gridpoint value is a missing value or the location is out of the grid area:

   * by default, None is returned for a single location and nan for multiple locations. 
   * if ``mode`` is 'valid' then from out of the surrounding gridpoints the nearest valid one is returned; None or nan will still be returned if all the surrounding points are missing.

.. note::
      A similar function, :func:`interpolate`, also exists.

.. mv-minigallery:: nearest_gridpoint