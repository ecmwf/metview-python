mvl_geopolyline
==================

.. py:function:: mvl_geopolyline(lat, lon, incr)

   Plots a polygon linearly sampled in lat-lon onto any map projections.
   
   :param lat: latitudes of the polygon points
   :type lat: list or ndarray
   :param lon: longituded of the polygon points
   :type lon: list or ndarray
   :param incr: increment in degrees for line segments to build up the lines between adjacent polygon points
   :type incr: number
   :rtype: :func:`input_visualiser`
   
   Internally, the lines between adjacent polygon points are split into a number of segments. The returned result is an :func:`input_visualiser` object which can be passed to :func:`plot` along with an optional :func:`mgraph` object.
   

.. mv-minigallery:: mvl_geopolyline