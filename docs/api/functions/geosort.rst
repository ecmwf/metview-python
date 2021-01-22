geosort
==========

.. py:function:: geosort(gpt)

    Returns a new :class:`Geopoints` that contains ``gpt`` sorted geographically from North to South (and West to East in points with the same latitude value, then by height, with lowest numerical values first).

    :param fs: input geopoints
    :type fs: :class:`Geopoints`
    :rtype: :class:`Geopoints`

.. mv-minigallery:: geosort
