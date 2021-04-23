thermo_parcel_path
=====================

..  py:function:: thermo_parcel_path(t, td, p, options)
..  py:function:: thermo_parcel_path(profile, options)
    :noindex:

    Computes the path of an ascending thermodynamic parcel with the given start condition for the given vertical profile. 
    
    :param t: temperature profile (°C)
    :type t: ndarray
    :param td: dewpoint temperature profile (°C)
    :type td: ndarray
    :param p: pressure profile (hPa)
    :type p: ndarray
    :param profile: profile data extracted from a :class:`Fieldset` or :class:`Bufr` for a thermodynamic diagram
    :type profile: :func:`thermo_bufr` or :func:`thermo_grib`
    :param options: options
    :type options: dict
    :rtype: dict
    
    It returns a dict containing all the data to plot the parcel path, buoyancy areas and related data into a thermodynamic diagram.

    ``options`` specifies the various settings for the parcel computations. The members of this dict are as follows (temperature values are in °C and pressure values are in hPa):

    * **mode**: the start condition mode. The possible values are 'surface', 'custom', 'mean_layer' and 'most_unstable' (see  below for details)
    * **start_t**: the start temperature (see  below for details)
    * **start_td**: the start dewpoint (see  below for details)
    * **start_p**: the start pressure (see  below for details)
    * **top_p**: the top pressure of the start layer (see below for details)
    * **bottom_p**: the bottom pressure of the start layer (see below for details)
    * **stop_at_el**: if it is defined and set to 1 the parcel computations will stop at the Equilibrium Level.

    The start condition ``mode`` can have these values:

    * **surface**: the parcel ascends from the surface, i.e. the lowest point of the profile. The format is as follows:

        .. code-block:: python
            
            {mode: "surface"}

    * **custom**: the parcel ascends from a given temperature, dewpoint and pressure. The format is as follows:
    
        .. code-block:: python
            
            {mode: 'custom', 
             start_t: start_temperature, 
             start_td: start_dewpoint,
             start_p: start_pressure}

    * **mean layer**: the parcel ascends from the mean temperature, dew point and pressure of a given pressure layer. The format is as follows:
    
        .. code-block:: python
            
            {mode: 'mean_layer',
             top_p: layer_top,
             bottom_p: layer_bottom}

        When bottom_p is omitted the layer starts at the surface.
    
    * **most unstable**: the parcel ascends from the most unstable condition. To determine this, a parcel is started from all the points along the profile in the specified pressure layer. The start level of the parcel that results in the highest CAPE value will define the most unstable start condition. The format is as follows:
        
        .. code-block:: python

            {mode: 'most_unstable', 
             top_p: layer_top, 
             bottom_p: layer_bottom}

        When bottom_p is omitted the pressure layer starts at the surface.

    :func:`thermo_parcel_path` returns a dict to describe all the parameters related to the ascend of the parcel. The members of this definition are as follows (temperature values are in °C and pressure values are in hPa) :

    * path: path of the parcel. It is itself a dict with two members: t and p, both containing a list of values.

    * area: positive and negative buoyancy areas between the parcel path and the profile. It is a list of dictionaries describing the areas.

    * cape: value of the CAPE (Convective Available Potential Energy)  (J/kg)

    * cin: value the CIN (Convective Inhibition) (J/kg)

    * lcl: Lifted Condensation Level. It is a definition with two members: t and p. If no LCL exists it is set to None.

    * lfc: Level of Free Convention. It is a definition with two members: t and p. If no LFC exists it is set to None.

    * el: Equilibrium Level. It is a definition with two members: t and p. If no EL exists it is set to None.

    * top: Cloud Top Level. It is a definition with two members: t and p. If no TOP exists it is set to None.

    * start: start conditions of the parcel with four members: mode, t, td and p.


.. mv-minigallery:: thermo_parcel_path