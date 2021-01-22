stnids
========

.. py:function:: stnids(gpt)

    Returns the station id column of ``gpt`` as a list.
    
    :param fs: input geopoints
    :type fs: :class:`Geopoints`
    :rtype: list of str

    If a given point does not have a station id, then a None will be returned in its place in the list.

.. mv-minigallery:: stnids