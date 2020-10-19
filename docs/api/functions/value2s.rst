value2s
=============

.. py:function:: value2s(gpt)

    Returns the values in the **value2** column of ``gpt``.
    
    :param fs: input geopoints
    :type fs: :class:`Geopoints`
    :rtype: ndarray

    .. warning::
        :func:`set_value2s` only works for :class:`Geopoints` with 'xy_vector' or 'polar_vector' type.

