remove_missing_values
========================

.. py:function:: remove_missing_values (gpt)

    Returns a new :class:`Geopoints` that contains just the non-missing values in ``gpt``.
    
    :param gpt: input geopoints
    :type gpt: :class:`Geopoints`
    :rtype: :class:`Geopoints`
    
    A geopoint (i.e. a row in a :class:`Geopoints`) is considered to be missing if either its **value** or **value2** members are missing.

.. mv-minigallery:: remove_missing_values
