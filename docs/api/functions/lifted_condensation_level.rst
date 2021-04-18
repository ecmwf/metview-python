lifted_condensation_level
===========================

..  py:function:: lifted_condensation_level(t, td, p)

    Computes the Lifted Condensation Level (LCL) of a parcel ascending from a given temperature, dewpoint and pressure.
   
    :param t: initial temperature (K)
    :type t: number
    :param td: initial dew point temperature (K)
    :type td: number
    :param p: initial pressure (Pa)
    :type p: number
    :rtype: dict or None

    The LCL is the level where the parcel becomes saturated and it is computed with an iterative method along the dry adiabat of the ascending parcel.

    The result is a dict with two members: t and p, containing the temperature and pressure of the LCL, in K and Pa units, respectively. On error or if the LCL does not exist None is returned.

.. mv-minigallery:: lifted_condensation_level
