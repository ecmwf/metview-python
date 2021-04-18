vapour_pressure
==================

..  py:function::  vapour_pressure(q, [p])

    Computes the vapour pressure for a given specific humidity (``q``) and pressure (``p``).
    
    :param q: specific humidity (kg/kg)
    :type q: number, ndarray or :class:`Fieldset`
    :param p: pressure (Pa)
    :type p: number, ndarray or :class:`Fieldset`
    :rtype: same type as ``q`` or None

    The result is the vapour pressure in Pa units. On error None is returned. The following rules are applied when ``q`` is a :class:`Fieldset`:

    * if ``q`` is a pressure level :class:`Fieldset` no ``p`` is needed
    * if ``q`` is defined on ECMWF model levels (hybrid/eta) ``p`` must be either a single LNSP (logarithm of surface pressure, identified by paramId=152) field or a :class:`Fieldset` defining the pressure on the same levels as ``q``
    * for other level types ``p`` must be a :class:`Fieldset` defining the pressure on the same levels as ``q``.

    The computation is based on the following formula:

    .. math:: 

        \frac{p\;q}{\epsilon\; (1 + q(\frac{1}{\epsilon} -1 )}

    with

    .. math:: 

        \epsilon = \frac{R_{dry}}{R_{vapour}} = 0.621981



.. mv-minigallery:: vapour_pressure
