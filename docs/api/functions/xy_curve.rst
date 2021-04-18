xy_curve
============

.. py:function:: xy_curve(x, y, colour, style, thickness)

   Convenience function to build a curve to be plotted in a :func:`cartesianview` with the given ``colour``, ``style`` and ``thickness``.
   
   :param x: x coordinates of the curve points
   :type x: list or ndarray
   :param y: y coordinates of the curve points
   :type y: list or ndarray
   :param colour: the colour of the curve
   :type colour: str
   :param style: the line style of the curve
   :type style: str
   :param thickness: the thickness of the curve
   :type thickness: number
   :rtype: list of :func:`input_visualiser` and :func:`mgraph`
   
   Returns a list containing an :func:`input_visualiser` and an :func:`mgraph`, which can be directly used in :func:`plot`.
   

.. mv-minigallery:: xy_curve
