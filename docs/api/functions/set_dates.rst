set_dates
============

.. py:function:: set_dates(gpt, dates)

    Creates a new :class:`Geopoints` with all the dates (**only the date component** of the dates!) in ``gpt`` replaced by ``dates``.

    :param gpt: input geopoints
    :type gpt: :class:`Geopoints`
    :param dates: dates to be written into ``gpt``
    :type dates: datetime.datetime/date or list or ndarray of these
    :rtype: :class:`Geopoints`

    If ``dates`` is a single date all the dates are replaced with it.  If ``dates`` is a list or ndarray and is shorter than the geopoints count then only the first dates that have a corresponding value in ``dates`` are changed.


.. mv-minigallery:: set_dates
