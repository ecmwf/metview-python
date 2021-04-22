subsample
===============

.. py:function:: subsample(gpt_value, gpt_location)

    Returns a :class:`Geopoints` containing the same locations (latitude, longitude and height) as in ``gpt_location``, but whose values are from ``gpt_value`` (or a missing value if the point is not found in ``gpt_value``).

    :param gpt_value: geopoints defining the values
    :type gpt_value: :class:`Geopoints`
    :param gpt_locations: geopoints defining the locations
    :type gpt_locations: :class:`Geopoints`
    :rtype: :class:`Geopoints`

    The resulting :class:`Geopoints` is sorted in the same way as with :func:`geosort`. This means that extra care is needed to perform operations between the results of :func:`subsample` and another :class:`Geopoints`: make sure you call :func:`geosort` on the other :class:`Geopoints` beforehand so that the points could be aligned.
    
    Points with missing latitudes or longitudes will still be in the output, but the rule is that such a point is defined not to be at the same location as another point, even if its lat/lon are also missing. Use :func:`remove_missing_values` to get rid of the missing valued points in the returned :class:`Geopoints`.
    
    .. note::
        It is advised to remove missing lat/lon points using :func:`remove_missing_latlons` before using :func:`subsample` or :func:`geosort`.


.. mv-minigallery:: subsample
