mvl_geopolyline
==================

.. py:function:: mvl_geopolyline(lat, lon, incr)

   Plots a polygon linearly sampled on cylindrical projection onto any map projections.
   
   :param lat: latitudes of the polygon waypoints
   :type lat: list or ndarray
   :param lon: longituded of the waypoints
   :type lon: list or ndarray
   :param incr: increment in degrees for line segments to build up the line between two waypoints between two waypoints
   :type incr: int
   :rtype: :func:`input_visualiser`
   
   Internally, the each line between two waypoints is split into a number of segments and the returned result is an :func:`input_visualiser` object which can be passed to :func:`plot` along with an optional :func:`mgraph` object.
   

.. mv-minigallery:: mvl_geopolyline