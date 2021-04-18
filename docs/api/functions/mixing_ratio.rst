mixing_ratio
================

..  py:function:: mixing_ratio(q)

    Computes the mixing ratio from the given specific humidity (``q``).

    :param q: specific humidity (kg/kg)
    :type q: number, ndarray or :class:`Fieldset`
    :rtype: same type as ``q`` or None
    
    The result is the mixing ratio in kg/kg units. On error None is returned. The computation is based on the following definition:

    .. math:: 
      
        w = \frac {q}{1-q}


.. mv-minigallery:: mixing_ratio
