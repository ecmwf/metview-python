mvl_geoline
===============

.. py:function:: mvl_geoline(lat1, lon1, lat2, lon2, incrm)

   Plots a straight line linearly sampled in lat-lon onto any map projections.
   
   :param lat1: start latitude of the line
   :type lat1: number
   :param lon1: start longitude of the line
   :type lon1: number
   :param lat2: end latitude of the line
   :type lat2: number
   :param lon2: end longitude of the line
   :type lon2: number
   :param incr: increment in degrees for the line segments to make up the line
   :type incr: number
   :rtype: :func:`input_visualiser`
   
   Internally, the line is split into a number of segments and the returned result is an :func:`input_visualiser` object which can be passed to :func:`plot` along with an optional :func:`mgraph` object.
   

.. mv-minigallery:: mvl_geoline