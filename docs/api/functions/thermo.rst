Thermodynamic functions
************************


.. ..  py:function:: dewpoint_from_relative_humidity(t, r)

..     Computes the dewpoint temperature from the given temperature (``t``) and relative humidity (``r``).

..     :param t: temperature (K)
..     :type t: float, ndarray or :class:`Fieldset`
..     :param r: relative humidity ([0-1])
..     :type r: float, ndarray or :class:`Fieldset`
..     :rtype: same type as ``t`` or None

..     The result is the dewpoint temperature in K units. On error None is returned. The computation is based on the following formula:

..     .. math:: 

..         r = \frac{e_{wsat}(td)}{e_{wsat}(t)}

..     where

..         * e\ :sub:`wsat` is the saturation vapour pressure over water
..         * td is the dewpoint temperature


.. ..  py:function:: dewpoint_from_specific_humidity(q, [p])

..     Computes the dewpoint temperature from the given specific humidity (``q``) and pressure (``p``). 

..     :param q: specific humidity (kg/kg)
..     :type q: float, ndarray or :class:`Fieldset`
..     :param p: pressure (Pa)
..     :type p: float, ndarray or :class:`Fieldset`
..     :rtype: same type as ``q`` or None

..     The result is the dewpoint temperature in K units. On error None is returned. The following rules are applied when ``q`` is a :class:`Fieldset`:

..     * if ``q`` is a pressure level :class:`Fieldset` no ``p`` is needed
..     * if ``q`` is defined on ECMWF model levels (hybrid/eta) ``p`` must be either a single LNSP (logarithm of surface pressure, identified by paramId=152) field or a :class:`Fieldset` defining the pressure on the same levels as ``q``
..     * for other level types ``p`` must be a :class:`Fieldset` defining the pressure on the same levels as ``q``.

..     The computation is based on the following equation:
    
..     .. math:: 
    
..         e(q, p) = e_{wsat}(td)

..     where

..         e is the vapour pressure
..         e\ :sub:`wsat` is the saturation vapour pressure over water
..         td is the dewpoint temperature


..  py:function:: eqpott_m(**kwargs)

    Computes the equivalent potential temperature from a :class:`Fieldset` on (hybrid) model levels. This is a Metview icon function, for detailed documentation please see Potential Temperature.


..  py:function:: eqpott_pl(**kwargs)

    Computes the equivalent potential temperature from a :class:`Fieldset` on pressure levels. This is a Metview icon function, for detailed documentation please see Potential Temperature.

.. ..  py:function:: lifted_condensation_level(t, td, p)

..     Computes the Lifted Condensation Level (LCL) of a parcel ascending from a given temperature, dewpoint and pressure.
   
..     :param t: initial temperature (K)
..     :type t: float
..     :param td: initial dew point temperature (K)
..     :type td: float
..     :param p: initial pressure (Pa)
..     :type p: float
..     :rtype: dict or None

..     The LCL is the level where the parcel becomes saturated and it is computed with an iterative method along the dry adiabat of the ascending parcel.

..     The result is a dict with two members: t and p, containing the temperature and pressure of the LCL, in K and Pa units, respectively. On error or if the LCL does not exist None is returned.


.. ..  py:function:: mixing_ratio(q)

..     Computes the mixing ratio from the given specific humidity (``q``).

..     :param q: specific humidity (kg/kg)
..     :type q: float, ndarray or :class:`Fieldset`
..     :rtype: same type as ``q`` or None
    
..     The result is the mixing ratio in kg/kg units. On error None is returned. The computation is based on the following definition:

..     .. math:: 
      
..         w = \frac {q}{1-q}


.. ..  py:function:: potential_temperature(t, p)

..     Computes the potential temperature for a given temperature (``t``) and pressure (``p``).

..     :param t: temperature (K)
..     :type t: float
..     :param p: pressure (Pa)
..     :type : float
..     :rtype: float or None
    
..     The result is the potential temperature in K units. On error None is returned.


..  py:function:: pott_m(**kwargs)

    Computes the potential temperature from a :class:`Fieldset` on (hybrid) model levels. This is a Metview icon function, for detailed documentation please see Potential Temperature.


..  py:function:: pott_pl(**kwargs)

    Computes the potential temperature from a :class:`Fieldset` on pressure levels. This is a Metview icon function, for detailed documentation please see Potential Temperature.


..  py:function:: relhum(**kwargs)

    Computes the relative humidity from a specific humidity :class:`Fieldset`. This is a Metview icon function, for detailed documentation please see Relative Humidity.


.. ..  py:function::  relative_humidity_from_dewpoint(t, td)

..     Computes the relative humidity from the given temperature (``t``) and dewpoint temperature (``td``).

..     :param t: temperature (K)
..     :type t: float, ndarray or :class:`Fieldset`
..     :param td: dewpoint temperature (K)
..     :type td: float, ndarray or :class:`Fieldset`
..     :rtype: same type as ``t`` or None

..     The result is the relative humidity in the range of [0, 1]. On error None is returned. The computation is based on the following formula:

..     .. math:: 
      
..         r = \frac {e_{wsat}(Td)}{e_{wsat}(T)}

..     where e w\ :sub:`sat` is the saturation vapour pressure over water.


.. ..  py:function:: saturation_mixing_ratio(t, p, [phase])

..     Computes the saturation mixing ratio for a given temperature (``t``), pressure (``p``) and ``phase``.

..     :param t: temperature (K)
..     :type t: float or ndarray
..     :param p: pressure (Pa)
..     :type p: float or ndarray
..     :param phase: is either "water", "ice" or "mixed". When it is not specified the "water" phase is used.
..     :type phase: str
..     :rtype: same type as ``t`` or None

..     The result is the saturation mixing ratio in kg/kg units. On error None is returned. The computation is implemented via calling :func:`mixing_ratio` and :func:`saturation_vapour_pressure`:

..     .. code-block:: python

..         ws = mv.mixing_ratio(p, mv.saturation_vapour_pressure(t, phase))

.. ..  py:function:: saturation_vapour_pressure(t, [phase])

..     Computes the saturation vapour pressure for a given temperature (``t``) and ``phase``.
    
..     :param t: temperature (K)
..     :type t: float or ndarray
..     :param phase: is either "water", "ice" or "mixed". When it is not specified the "water" phase is used.
..     :type phase: str
..     :rtype: same type as ``t`` or None

..     The result is the saturation vapour pressure in Pa units. On error None is returned. The computations for saturation over "water" and "ice" are based on the Tetens formula:

..     .. math:: 

..         e_{sat} = a_{1}\;exp \left(a_{3}\frac{T-273.16}{T-a_{4}}\right)

..     where the parameters are set as follows:

..     * "water": a\ :sub:`1` =611.21 Pa, a\ :sub:`3` =17.502 and a\ :sub:`4` =32.19 K
..     * "ice": a\ :sub:`1` =611.21 Pa, a\ :sub:`3` =22.587 and a\ :sub:`4` =-0.7 K

..     For the "mixed" phase the linear combination of the "water" and "ice" phases are used as described in the IFS documentation (see here on p116 for details for model cycle CY45R1).

..  py:function:: seqpott_m(**kwargs)

    Computes the saturation equivalent potential temperature for a :class:`Fieldset` on (hybrid) model levels. This is a Metview icon function, for detailed documentation please see Potential Temperature.


..  py:function:: seqpott_pl(**kwargs)

    Computes the saturation equivalent potential temperature for a :class:`Fieldset` on pressure levels. This is a Metview icon function, for detailed documentation please see Potential Temperature.

.. ..  py:function:: temperature_from_potential_temperature(theta, p)

..     Computes the temperature from a given potential temperature (``theta``) and pressure (``p``).

..     :param theta: potential temperature (K)
..     :type theta: float
..     :param p: pressure (Pa)
..     :type p: float
..     :rtype: float or None

..     The result is the temperature in K units. On error None is returned.

..  py:function:: thermo_bufr(**kwargs)

    Extracts vertical profiles from BUFR data in a suitable format suitable for thermodynamic diagrams (defined by Thermo View). This is a Metview icon function, for detailed documentation please see Thermo Data.


.. ..  py:function:: thermo_data_info(data)

..     Convenience function to extract metadata from ``data``. 

..     :param data: thermo data object containing vertical profiles
..     :type data: thermo data
..     :rtype: dict
    
..     :func:`thermo_data_info` returns a dict that can be used to e.g. build the title for thermodynamic diagrams. See the Parcel method on Skew-T Example from the Gallery for its usage.


.. ..  py:function:: thermo_data_values(data, time_dim_index)

..     Convenience function to access profiles from ``data`` for a given ``time_dimension_index``.
    
..     :param data: thermo data object containing vertical profiles
..     :type data: thermo data
..     :param time_dim_index: the (zero-based) index of the selected time dimension from ``data``
..     :type time_dim_index: int
..     :rtype: dict
    
..     See the Parcel method on Skew-T Example from the Gallery for its usage.


..  py:function:: thermo_grib(**kwargs)

    Extracts vertical profiles from GRIB data in a suitable format for thermodynamic diagrams (defined by Thermo View). This is a Metview icon function, for detailed documentation please see Thermo Data.

.. ..  py:function:: thermo_parcel_path(t, td, p, options)
.. ..  py:function:: thermo_parcel_path(profile, options)
..     :noindex:

..     Computes the path of an ascending thermodynamic parcel with the given start condition for the given vertical profile. 
    
..     :param t: temperature profile (°C)
..     :type t: ndarray
..     :param td: dewpoint temperature profile (°C)
..     :type td: ndarray
..     :param p: pressure profile (hPa)
..     :type p: ndarray
..     :param profile: the result of a vertical profile extraction from GRIB or BUFR with the thermo_grib() or thermo_bufr() functions (see Thermo Data ), respectively.
..     :type profile: thermo_data
..     :param options: options
..     :type options: dict
..     :rtype: dict
    
..     It returns a dict containing all the data to plot the parcel path, buoyancy areas and related data into a thermodynamic diagram.

..     ``options`` specifies the various settings for the parcel computations. The members of this dict are as follows (temperature values are in °C and pressure values are in hPa):

..     * **mode**: the start condition mode. The possible values are 'surface', 'custom', 'mean_layer' and 'most_unstable' (see  below for details)
..     * **start_t**: the start temperature (see  below for details)
..     * **start_td**: the start dewpoint (see  below for details)
..     * **start_p**: the start pressure (see  below for details)
..     * **top_p**: the top pressure of the start layer (see below for details)
..     * **bottom_p**: the bottom pressure of the start layer (see below for details)
..     * **stop_at_el**: if it is defined and set to 1 the parcel computations will stop at the Equilibrium Level.

..     There are four different modes available for the parcel start conditions:

..     * **Surface**: the parcel ascends from the surface, i.e. the lowest point of the profile. The format is as follows:

..         .. code-block:: python
            
..             {mode: "surface"}

..     * **Custom**: the parcel ascends from a given temperature, dewpoint and pressure. The format is as follows:
    
..         .. code-block:: python
            
..             {mode: 'custom', 
..              start_t: start_temperature, 
..              start_td: start_dewpoint,
..              start_p: start_pressure}

..     * **Mean layer**: the parcel ascends from the mean temperature, dew point and pressure of a given pressure layer. The format is as follows:
    
..         .. code-block:: python
            
..             {mode: 'mean_layer',
..              top_p: layer_top,
..              bottom_p: layer_bottom}

..         When bottom_p is omitted the layer starts at the surface.
    
..     * **Most unstable**: the parcel ascends from the most unstable condition. To determine this, a parcel is started from all the points along the profile in the specified pressure layer. The start level of the parcel that results in the highest CAPE value will define the most unstable start condition. The format is as follows:
        
..         .. code-block:: python

..             {mode: 'most_unstable', 
..              top_p: layer_top, 
..              bottom_p: layer_bottom}

..         When bottom_p is omitted the pressure layer starts at the surface.

..     :func:`thermo_parcel_path` returns a dict to describe all the parameters related to the ascend of the parcel. The members of this definition are as follows (temperature values are in °C and pressure values are in hPa) :

..     * path: path of the parcel. It is itself a definition with two members: t and p, each containing a list of values.

..     * area: positive and negative buoyancy areas between the parcel path and the profile. It is a list of definitions describing the areas.

..     * cape: value of the CAPE (Convective Available Potential Energy)  (J/kg)

..     * cin: value the CIN (Convective Inhibition) (J/kg)

..     * lcl: Lifted Condensation Level. It is a definition with two members: t and p. If no LCL exists it is set to None.

..     * lfc: Level of Free Convention. It is a definition with two members: t and p. If no LFC exists it is set to None.

..     * el: Equilibrium Level. It is a definition with two members: t and p. If no EL exists it is set to None.

..     * top: Cloud Top Level. It is a definition with two members: t and p. If no TOP exists it is set to None.

..     * start: start conditions of the parcel with four members: mode, t, td and p.


.. ..  py:function::  vapour_pressure(q, [p])

..     Computes the vapour pressure for a given specific humidity (``q``) and pressure (``p``).
    
..     :param q: specific humidity (kg/kg)
..     :type q: float, ndarray or :class:`Fieldset`
..     :param p: pressure (Pa)
..     :type p: float, ndarray or :class:`Fieldset`
..     :rtype: same type as ``q`` or None

..     The result is the vapour pressure in Pa units. On error None is returned. The following rules are applied when ``q`` is a :class:`Fieldset`:

..     * if ``q`` is a pressure level :class:`Fieldset` no ``p`` is needed
..     * if ``q`` is defined on ECMWF model levels (hybrid/eta) ``p`` must be either a single LNSP (logarithm of surface pressure, identified by paramId=152) field or a :class:`Fieldset` defining the pressure on the same levels as ``q``
..     * for other level types ``p`` must be a :class:`Fieldset` defining the pressure on the same levels as ``q``.

..     The computation is based on the following formula:

..     .. math:: 

..         \frac{p\;q}{\epsilon\; (1 + q(\frac{1}{\epsilon} -1 )}

..     with

..     .. math:: 

..         \epsilon = \frac{R_{dry}}{R_{vapour}} = 0.621981


.. ..  py:function:: w_from_omega(omega, t,  [p])

..     Computes the hydrostatic vertical velocity from  pressure velocity (``omega``) for a given temperature (``t``) and pressure (``p``).

..     :param omega: hydrostatic pressure velocity (Pa/s)
..     :type omega: float, ndarray or :class:`Fieldset`
..     :param t: temperature (K)
..     :type t: float, ndarray or :class:`Fieldset`
..     :param p: pressure (Pa)
..     :type p: float, ndarray or :class:`Fieldset`
..     :rtype: same type as ``omega`` or None

..     The result is the vertical velocity in m/s units. On error None is returned. The following rules are applied when ``omega`` is a :class:`Fieldset`:

..     * if ``omega`` is a pressure level :class:`Fieldset` no ``p`` is needed
..     * if ``omega`` is defined on ECMWF model levels (hybrid/eta) ``p`` must be either a single LNSP (logarithm of surface pressure, identified by paramId=152) field or a :class:`Fieldset` defining the pressure on the same levels as ``omega``
..     * for other level types ``omega`` must be a :class:`Fieldset` defining the pressure on the same levels as ``omega``.

..     The computation is based on the following hydrostatic formula:

..     .. math:: 

..         w = - \frac{\omega T R_{d}}{p g}

..     where

..     * Rd is the specific gas constant for dry air (287.058 J/(kg K)).
..     * g is the gravitational acceleration (9.81 m/s\ :sup:`2`)
    
