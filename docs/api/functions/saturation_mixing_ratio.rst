
saturation_mixing_ratio
=========================

..  py:function:: saturation_mixing_ratio(t, p, [phase])

    Computes the saturation mixing ratio for a given temperature (``t``), pressure (``p``) and ``phase``.

    :param t: temperature (K)
    :type t: number or ndarray
    :param p: pressure (Pa)
    :type p: number or ndarray
    :param phase: is either "water", "ice" or "mixed". When it is not specified the "water" phase is used.
    :type phase: str
    :rtype: same type as ``t`` or None

    The result is the saturation mixing ratio in kg/kg units. On error None is returned. The computation is implemented via calling :func:`mixing_ratio` and :func:`saturation_vapour_pressure`:

    .. code-block:: python

        ws = mv.mixing_ratio(p, mv.saturation_vapour_pressure(t, phase))

.. mv-minigallery:: saturation_mixing_ratio
