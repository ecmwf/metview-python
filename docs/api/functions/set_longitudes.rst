set_longitudes
=================

.. py:function:: set_longitudes(gpt, longitudes)

    Creates a new :class:`Geopoints` with all the longitudes in ``gpt`` replaced by ``longitudes``.

    :param gpt: input geopoints
    :type gpt: :class:`Geopoints`
    :param latitudes: longitudes to be written into ``gpt``
    :type latitudes: float or list or ndarray
    :rtype: :class:`Geopoints`

    If ``longitudes`` is a number all the longitudes are replaced with it. If ``longitudes`` is a list or ndarray and is shorter than the geopoints count then only the first values that have a corresponding value in ``longitudes`` are changed.


.. mv-minigallery:: set_longitudes
