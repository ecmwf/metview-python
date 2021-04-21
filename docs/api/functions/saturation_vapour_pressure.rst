saturation_vapour_pressure
=============================

..  py:function:: saturation_vapour_pressure(t, [phase])

    Computes the saturation vapour pressure for a given temperature (``t``) and ``phase``.
    
    :param t: temperature (K)
    :type t: number or ndarray
    :param phase: is either "water", "ice" or "mixed". When it is not specified the "water" phase is used.
    :type phase: str
    :rtype: same type as ``t`` or None

    The result is the saturation vapour pressure in Pa units. On error None is returned. The computations for saturation over "water" and "ice" are based on the Tetens formula:

    .. math:: 

        e_{sat} = a_{1}\;exp \left(a_{3}\frac{T-273.16}{T-a_{4}}\right)

    where the parameters are set as follows:

    * "water": a\ :sub:`1` =611.21 Pa, a\ :sub:`3` =17.502 and a\ :sub:`4` =32.19 K
    * "ice": a\ :sub:`1` =611.21 Pa, a\ :sub:`3` =22.587 and a\ :sub:`4` =-0.7 K

    For the "mixed" phase the linear combination of the "water" and "ice" phases is used as described in the IFS documentation (see `here <https://www.ecmwf.int/en/elibrary/18714-part-iv-physical-processes>`_ on p116 for details for model cycle CY45R1).

.. mv-minigallery:: saturation_vapour_pressure
