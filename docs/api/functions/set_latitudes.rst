set_latitudes
================

.. py:function:: set_latitudes(gpt, latitudes)

    Creates a new :class:`Geopoints` with all the latitudes in ``gpt`` replaced by ``latitudes``.

    :param gpt: input geopoints
    :type gpt: :class:`Geopoints`
    :param latitudes: latitudes to be written into ``gpt``
    :type latitudes: number or list or ndarray
    :rtype: :class:`Geopoints`

    If ``latitudes`` is a number all the latitudes are replaced with it. If ``latitudes`` is a list or ndarray and is shorter than the geopoints count then only the first values that have a corresponding value in ``latitudes`` are changed.

.. mv-minigallery:: set_latitudes
