temperature_from_potential_temperature
=========================================

..  py:function:: temperature_from_potential_temperature(theta, p)

    Computes the temperature from a given potential temperature (``theta``) and pressure (``p``).

    :param theta: potential temperature (K)
    :type theta: float
    :param p: pressure (Pa)
    :type p: float
    :rtype: float or None

    The result is the temperature in K units. On error None is returned.