xs_build_curve
==================

.. py:function:: xs_build_curve(xs_d, fs, colour, style, thickness)

   Convenience function to build a curve to be plotted in a :func:`mxsectview` with the given ``colour``, ``style`` and ``thickness``.
   
   :param xs_d: cross section data object
   :type xs_d: :func:`mcross_sect`
   :param fs: the data from which the curve values will be extracted
   :type fs: :class:`Fieldset`
   :param colour: the colour of the curve
   :type colour: str
   :param style: the line style of the curve. The possible values are "solid", "dash", "dot", "chain_dot", "chain_dash".
   :type style: str
   :param thickness: the thickness of the curve
   :type thickness: number
   :rtype: list of :func:`input_visualiser` and :func:`mgraph`
   
   The curve values are extracted from the first field in ``fs`` and they must be in the same units as the vertical axis of the cross section. The cross section definition itself is taken from ``xs_d``. :func:`xs_build_curve` returns a list containing an :func:`input_visualiser` and an :func:`mgraph`, which can be directly used in :func:`plot`.
   

.. mv-minigallery:: xs_build_curve
