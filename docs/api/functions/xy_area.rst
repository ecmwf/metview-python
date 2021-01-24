xy_area
==================

.. py:function:: xy_area(x, y, colour)

   Convenience function to build an area (i.e. a polygon) to be plotted in a :func:`cartesianview` with the given ``colour``.
   
   :param x: x coordinates of the polygon points
   :type x: list or ndarray
   :param y: y coordinates of the polygon points
   :type y: list or ndarray
   :param colour: fill colour of the area
   :type colour: str
   :rtype: list of :func:`input_visualiser` and :func:`mgraph`
   
   Returns a list containing an :func:`input_visualiser` and an :func:`mgraph`, which can be directly used in :func:`plot`.
   

.. mv-minigallery:: xy_area
