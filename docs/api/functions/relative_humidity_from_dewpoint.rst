relative_humidity_from_dewpoint
==================================

..  py:function::  relative_humidity_from_dewpoint(t, td)

    Computes the relative humidity from the given temperature (``t``) and dewpoint temperature (``td``).

    :param t: temperature (K)
    :type t: float, ndarray or :class:`Fieldset`
    :param td: dewpoint temperature (K)
    :type td: float, ndarray or :class:`Fieldset`
    :rtype: same type as ``t`` or None

    The result is the relative humidity in the range of [0, 1]. On error None is returned. The computation is based on the following formula:

    .. math:: 
      
        r = \frac {e_{wsat}(Td)}{e_{wsat}(T)}

    where e w\ :sub:`sat` is the saturation vapour pressure over water.

.. mv-minigallery:: relative_humidity_from_dewpoint
