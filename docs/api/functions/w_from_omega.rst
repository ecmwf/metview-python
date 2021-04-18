w_from_omega
================

..  py:function:: w_from_omega(omega, t,  [p])

    Computes the hydrostatic vertical velocity from  pressure velocity (``omega``) for a given temperature (``t``) and pressure (``p``).

    :param omega: hydrostatic pressure velocity (Pa/s)
    :type omega: number, ndarray or :class:`Fieldset`
    :param t: temperature (K)
    :type t: number, ndarray or :class:`Fieldset`
    :param p: pressure (Pa)
    :type p: number, ndarray or :class:`Fieldset`
    :rtype: same type as ``omega`` or None

    The result is the vertical velocity in m/s units. On error None is returned. The following rules are applied when ``omega`` is a :class:`Fieldset`:

    * if ``omega`` is a pressure level :class:`Fieldset` no ``p`` is needed
    * if ``omega`` is defined on ECMWF model levels (hybrid/eta) ``p`` must be either a single LNSP (logarithm of surface pressure, identified by paramId=152) field or a :class:`Fieldset` defining the pressure on the same levels as ``omega``
    * for other level types ``omega`` must be a :class:`Fieldset` defining the pressure on the same levels as ``omega``.

    The computation is based on the following hydrostatic formula:

    .. math:: 

        w = - \frac{\omega T R_{d}}{p g}

    where

    * Rd is the specific gas constant for dry air (287.058 J/(kg K)).
    * g is the gravitational acceleration (9.81 m/s\ :sup:`2`)
    

.. mv-minigallery:: w_from_omega
