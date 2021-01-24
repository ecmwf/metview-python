mvl_geoline
===============

.. py:function:: mvl_geoline(lat1, lon1, lat2, lon2, incrm)

   Plots a straight line linearly sampled on the cylindrical projection onto any map projections.
   
   :param lat1: start latitude of the line
   :type lat1: float
   :param lon1: start longitude of the line
   :type lon1: float
   :param lat2: end latitude of the line
   :type lat2: float
   :param lon2: end longitude of the line
   :type lon2: float
   :param incr: increment in degrees for the line segments to make up the line
   :type incr: int
   :rtype: :func:`input_visualiser`
   
   Internally, the line is split into a number of segments and the returned result is an :func:`input_visualiser` object which can be passed to :func:`plot` along with an optional :func:`mgraph` object.
   

.. mv-minigallery:: mvl_geoline