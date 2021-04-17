dewpoint_from_specific_humidity
===================================

..  py:function:: dewpoint_from_specific_humidity(q, [p])

    Computes the dewpoint temperature from the given specific humidity (``q``) and pressure (``p``). 

    :param q: specific humidity (kg/kg)
    :type q: number, ndarray or :class:`Fieldset`
    :param p: pressure (Pa)
    :type p: number, ndarray or :class:`Fieldset`
    :rtype: same type as ``q`` or None

    The result is the dewpoint temperature in K units. On error None is returned. The following rules are applied when ``q`` is a :class:`Fieldset`:

    * if ``q`` is a pressure level :class:`Fieldset` no ``p`` is needed
    * if ``q`` is defined on ECMWF model levels (hybrid/eta) ``p`` must be either a single LNSP (logarithm of surface pressure, identified by paramId=152) field or a :class:`Fieldset` defining the pressure on the same levels as ``q``
    * for other level types ``p`` must be a :class:`Fieldset` defining the pressure on the same levels as ``q``.

    The computation is based on the following equation:
    
    .. math:: 
    
        e(q, p) = e_{wsat}(td)

    where:
        * e is the vapour pressure
        * e\ :sub:`wsat` is the saturation vapour pressure over water
        * td is the dewpoint temperature



.. mv-minigallery:: dewpoint_from_specific_humidity