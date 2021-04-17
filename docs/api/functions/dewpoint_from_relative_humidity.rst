dewpoint_from_relative_humidity
==================================


..  py:function:: dewpoint_from_relative_humidity(t, r)

    Computes the dewpoint temperature from the given temperature (``t``) and relative humidity (``r``).

    :param t: temperature (K)
    :type t: number, ndarray or :class:`Fieldset`
    :param r: relative humidity ([0-1])
    :type r: number, ndarray or :class:`Fieldset`
    :rtype: same type as ``t`` or None

    The result is the dewpoint temperature in K units. On error None is returned. The computation is based on the following formula:

    .. math:: 

        r = \frac{e_{wsat}(td)}{e_{wsat}(t)}

    where

        * e\ :sub:`wsat` is the saturation vapour pressure over water
        * td is the dewpoint temperature



.. mv-minigallery:: dewpoint_from_relative_humidity
