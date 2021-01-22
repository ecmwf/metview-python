set_stnids
=============

.. py:function:: set_stnids(gpt, ids)

    Creates a new :class:`Geopoints` with all the station id in ``gpt`` replaced by ``ids``.

    :param gpt: input geopoints
    :type gpt: :class:`Geopoints`
    :param ids: station ids to be written into ``gpt``
    :type ids: list of str
    :rtype: :class:`Geopoints`

    If ``ids`` is shorter than the geopoints count then only the first values that have a corresponding value in ``ids`` are changed.

    .. warning::
      :func:`set_stnids` only works for :class:`Geopoints` with 'ncols' type.


.. mv-minigallery:: set_stnids
