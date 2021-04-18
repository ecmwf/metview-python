set_levels
============

.. py:function:: set_levels(gpt, levels)

    Creates a new :class:`Geopoints` with all the levels in ``gpt`` replaced by ``levels``.

    :param gpt: input geopoints
    :type gpt: :class:`Geopoints`
    :param levels: levels to be written into ``gpt``
    :type levels: number or list or ndarray
    :rtype: :class:`Geopoints`

    If ``levels`` is a number all the levels are replaced with it.  If ``levels`` is a list or ndarray and is shorter than the geopoints count then only the first values that have a corresponding value in ``levels`` are changed.


.. mv-minigallery:: set_levels
