set_value2s
===============

..  py:function:: set_value2s(gpt, values)

    Creates a new :class:`Geopoints` with the **value2** column in ``gpt`` replaced by ``values``.

    :param gpt: input geopoints
    :type gpt: :class:`Geopoints`
    :param values: values to be written into the value2 column of ``gpt``
    :type values: number or list or ndarray
    :rtype: :class:`Geopoints`

    If ``values`` is a number all the values are replaced with it. If ``values`` is a list or ndarray and is shorter than the geopoints count then only the first values that have a corresponding value in ``values`` are changed.

    .. warning::
        :func:`set_value2s` only works for :class:`Geopoints` with 'xy_vector' or 'polar_vector' type.



.. mv-minigallery:: set_value2s
