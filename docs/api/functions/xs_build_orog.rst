xs_build_orog
==================

.. py:function:: xs_build_orog(xs_d, orog_fs, bottom_level, colour)

   Convenience function to build an orography area to be plotted in a :func:`mxsectview` with the given ``colour``.
   
   :param xs_d: cross section data object
   :type xs_d: :func:`mcross_sect`
   :param orog_fs: the orography data
   :type orog_fs: :class:`Fieldset`
   :param bottom_level: the bottom level of the orography area in the same units  as the vertical axis of the cross section
   :type bottom_level: number
   :param colour: the colour of the orography area
   :type colour: str
   :rtype: list of :func:`input_visualiser` and :func:`mgraph`
   
    The orography values are extracted from the first field in ``orog_fs`` and they must be in the same units as the vertical axis of the cross section. The cross section definition itself is taken from ``xs_d``. :func:`xs_build_curve` returns a list containing an :func:`input_visualiser` and an :func:`mgraph`, which can be directly used in :func:`plot`.
   

.. mv-minigallery:: xs_build_orog
