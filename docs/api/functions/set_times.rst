set_times
============

.. py:function:: set_times(gpt, times)

    Creates a new :class:`Geopoints` with all the times in ``gpt`` replaced by ``times``.

    :param gpt: input geopoints
    :type gpt: :class:`Geopoints`
    :param times: dates to be written into ``gpt``
    :type times: number or list/ndarray of numbers
    :rtype: :class:`Geopoints`

    A time value has to specified as a number in the format of **hhmm** (without leading zeros).

    If ``times`` is a single time all the times are replaced with it. If ``times`` is a list or ndarray and is shorter than the geopoints count then only the first times that have a corresponding value in ``times`` are changed.

.. mv-minigallery:: set_times
