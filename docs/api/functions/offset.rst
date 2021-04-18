
offset
===========

.. py:function:: offset(gpt, lat_offset, lon_offset)
.. py:function:: offset(gpt, offset)

    Creates a new :class:`Geopoints` from ``gpt`` with the locations offset by the specified amounts.

    :param gpt: input geopoints
    :type gpt: :class:`Geopoints`
    :param number lat_offset: latitude offset
    :param number lon_offset: longitude offset
    :type list offset:  latitude and longitude offsets as [lat_offset, lon_offset]
    :rtype: :class:`Geopoints`


.. mv-minigallery:: offset
