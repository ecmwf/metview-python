mvl_geocircle
===============

.. py:function:: mvl_geocircle(lat, lon, radius, resolution)

   Plots a circle defined on the Earths surface with a given radius in km onto a map in any projections.
   
   :param lat: latitude of the centre of the circle
   :type lat: number
   :param lon: longitude of the centre of the circle
   :type lon: number
   :param radius: radius of the circle in km
   :type radius: number
   :param resolution: number of line segments to make up the circle
   :type resolution: number
   :rtype: :func:`input_visualiser`
   
   Internally, the circle is split into ``resolution`` number of segments and the returned result is an :func:`input_visualiser` object which can be passed to :func:`plot` along with an optional :func:`mgraph` object.
   

.. mv-minigallery:: mvl_geocircle
