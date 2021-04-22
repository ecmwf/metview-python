surrounding_points_indexes
============================

.. py:function:: surrounding_points_indexes(fs, lats, lons, [mode])
.. py:function:: surrounding_points_indexes(fs, location, [mode])

   Returns the indexes of the gridpoints surrounding the given location (or locations) in ``fs``.
  
   :param fs: input fieldset
   :type fs: :class:`Fieldset`
   :param lats: target latitude(s)
   :type lats: number or ndarray
   :param lons: target longitudes(s)
   :type lons: number or ndarray
   :param location: single target location defined as a list of [lat, lon]
   :type location: list
   :param str mode: specifies the way missing values are handled. The only allowed value is "all".
   :rtype: ndarray
  
   ``fs`` must be a gridded field. 

   The location(s) can be specified in the following ways:

   * ``location`` defines a single location.
   * ``lats`` and ``lons`` can define either a single location (as number) or multiple locations (as ndarray).

   By default the 4 surrounding gridpoint indexes are returned. The only exception is when a field is defined on a **reduced Gaussian grid** and the input location is at the North or South pole, beyond the most extreme row of points. In this case there will be a 'circle' of surrounding points, and all of these indexes are returned.
   
   If any of the surrounding points are **missing**, :func:`surrounding_points_indexes` will return nan. To prevent this, and to return all the points regardless, option ``mode`` has to be set to "all".
   

.. mv-minigallery:: surroundin_point_indexes
