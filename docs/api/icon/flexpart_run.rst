
flexpart_run
=========================

.. container::
    
    .. container:: leftside

        .. image:: /_static/FLEXPART_RUN.png
           :width: 48px

    .. container:: rightside

        This function performs the same task as the `Flexpart Run <https://confluence.ecmwf.int/display/METV/flexpart+run>`_ icon in Metview’s user interface. It accepts its parameters as keyword arguments, described below.


.. py:function:: flexpart_run(**kwargs)
  
    Description comes here!


    :param output_path: Specifies the location of the output data files. Both an absolute and relative path can be given here. Please note that Metview converts FLEXPART output into other formats and only these converted results are copied from the work directory into ``output_path``. For further details about the output formats click `here <https://confluence.ecmwf.int/display/METV/FLEXPART+output>`_.
    :type output_path: str


    :param input_data: Specifies the location of the ``input_data`` files and the AVAILABLE file using a :func:`flexpart_prepare` icon. Please note that if an icon is set here it takes precedence over the path specified in ``input_path``.
    :type input_data: str


    :param input_path: Specifies the location of the ``input_data`` files and the AVAILABLE file. Both an absolute and relative path can be given here. Please note that when an icon is specified in ``input_data`` this path is ignored.
    :type input_path: str


    :param user_exe_path: Specifies a user defined FLEXPART executable. Both absolute and relative path can be given here. If it is left blank (this is the default) Metview will use the MV_FLEXPART_EXE environment variable to locate the executable.
    :type user_exe_path: str


    :param user_resources_path: Specifies the location of the user defined parameter files (IGBP_int1.dat, OH_7lev_agl.dat, surfdata.t, surfdepo.t ) needed to run FLEXPART. Both an absolute and relative path can be given here. If it is left blank (this is the default) Metview will use the MV_FLEXPART_RESOURCES environment variable to locate the resources. For further details about the resources `click here <https://confluence.ecmwf.int/display/METV/FLEXPART+setup>`_.
    :type user_resources_path: str


    :param simulation_direction: Specifies the FLEXPART ``simulation_direction`` in time. The possible values are: "forward" and Backward. The default value is "forward".
    :type simulation_direction: str, default: "forward"


    :param starting_date: Specifies the beginning date of the simulation in YYYYMMDD format. Relative dates are allowed: e.g. -1 means yesterday, 0 means today, etc.
    :type starting_date: str


    :param starting_time: Specifies the beginning time of the simulation in HH[:MM[:SS]] format.
    :type starting_time: str


    :param ending_date: Specifies the ``ending_date`` of the simulation in YYYYMMDD format.  Relative dates are allowed: e.g. -1 means yesterday, 0 means today, etc.
    :type ending_date: str


    :param ending_time: Specifies the ``ending_time`` of the simulation in HH[:MM[:SS]] format.
    :type ending_time: str


    :param output_interval: 
    :type output_interval: str, default: "3"


    :param output_averaging_interval: Specifies the averaging interval for the output generation in HHHH[:MM[:SS]]` format. If 0 is given here instantaneous values are written into the output files. The default value is "3" (hours).
    :type output_averaging_interval: str, default: "3"


    :param output_sampling_rate: Specifies the sampling rate used for the averaging of the output. This period must be shorter than the ``output_averaging_interval``. The format is `HHHH[:MM[:SS]]`. The default value is 1 (hour).
    :type output_sampling_rate: str, default: "0:15"


    :param output_field_type: Specifies the type of the gridded output fields. The possible values are:

         for forward simulations :  

         *  none (no gridded output)
         *  "conc" (concentration)
         *  mixr (mass mixing ratio)
         *  both (concentration and mass mixing ratio)

         for backward simulations:_

         *  none (no gridded output)
         *  rtime (residence time/response function)  

         The default value is "conc". For more details about gridded output `click here. <https://confluence.ecmwf.int/display/METV/FLEXPART+output>`_
    :type output_field_type: str, default: "conc"


    :param output_flux: Specifies if the fluxes should be computed and written out as a gridded output ( "on" or "off" ). Fluxes corresponding to northward, southward, eastward, westward, upward and downward directions are calculated for each grid cell of the ``output_grid``.The control surfaces are placed in the middle of each ``output_grid`` cell. The default value is "off". For more details about flux output `click here. <https://confluence.ecmwf.int/display/METV/FLEXPART+output>`_
    :type output_flux: {"on", "off"}, default: "off"


    :param output_trajectory: Specifies if the plume trajectories should be computed ( "on" or "off" ). The default value is "off". For more details about trajectory output `click here. <https://confluence.ecmwf.int/display/METV/FLEXPART+output>`_
    :type output_trajectory: {"on", "off"}, default: "off"


    :param output_area: Specifies the area for the gridded output in degrees in S/W/N/E format. The default value is -90/-180/90/180.
    :type output_area: float or list[float], default: -90


    :param output_grid: Specifies the grid resolution for the gridded output in degrees as `east_west_resolution/north_south_resolution`. The default value is 1/1.
    :type output_grid: float or list[float], default: 1


    :param output_levels: Specifies the list of height levels of the gridded output. The levels are given in metres units. The default value is an empty list.
    :type output_levels: float or list[float]


    :param user_species_path: Specifies the location of the user defined species files. Both an absolute and relative path can be given here. If it is left blank (this is the default value) Metview will use the MV_FLEXPART_SPECIES environment variable to locate the species. For more details about the species `click here <https://confluence.ecmwf.int/display/METV/FLEXPART+species>`_.
    :type user_species_path: str


    :param release_species: Specifies the list of the species released for the simulation. At all the release locations the same species are emitted. The species are identified by the NNN number (with leading zeros) appearing in the the name of the SPECIES_NNN files. These files contain the physical and chemical properties of species. For more details about the species `click here <https://confluence.ecmwf.int/display/METV/FLEXPART+species>`_.
    :type release_species: str or list[str]


    :param release_units: Specifies the units of the "mass" of the released species. The possible options are "mass" and mixr. The default value is "mass". See the table below to find out what the actual units mean.  

         for forward simulations :  

         ``release_units``| ``receptor_units`` ---|--- keyword| units| keyword| units in concentration fields "mass"| kg| "mass"| kg m-3 "mass"| kg| mixr| kg kg-1 mixr| 1| "mass"| kg m-3 mixr| 1| mixr| kg kg-1  for backward simulations:_

         ``release_units``| ``receptor_units`` ---|--- keyword| units| keyword| units in residence time fields "mass"| 1| "mass"| s "mass"| 1| mixr| s m3 kg-1 mixr| 1| "mass"| s kg m-3 mixr| 1| mixr| s
    :type release_units: str, default: "mass"


    :param releases: Specifies the ``releases`` as a group of :func:`flexpart_release` icons.
    :type releases: str


    :param receptor_units: Specifies the concentration units at the receptor. The possible options are "mass" ("mass" concentrations) and mixr ("mass" mixing ratio). The default value is "mass". See the table above to find out what the actual units mean.
    :type receptor_units: str, default: "mass"


    :param receptors: Enables the usage of receptor sites ( "on" or "off" ). When it is enabled the list of receptor sites can be defined via ``receptor_names`` , ``receptor_latitudes`` and Receptor Longitude. The default value is "off".  For more details about receptor output `click here <https://confluence.ecmwf.int/display/METV/FLEXPART+species>`_.
    :type receptors: {"on", "off"}, default: "off"


    :param receptor_names: Specifies the list of receptor site names.The default value is an empty list.
    :type receptor_names: str or list[str]


    :param receptor_latitudes: Specifies the list of receptor site latitudes. The default value is an empty list.
    :type receptor_latitudes: str or list[str]


    :param receptor_longitudes: 
    :type receptor_longitudes: str or list[str]


    :param age_classes: Specifies the list of times for the age class calculation. If it is left blank (this is the default value) no age class is defined.
    :type age_classes: str or list[str]


    :param particle_splitting: Specifies the interval for ``particle_splitting`` in HHHH[:MM[:SS]] format. Each particle is split into two after travelling the multiple of this interval. If "0" (default value) is given here ``particle_splitting`` is disabled.
    :type particle_splitting: str, default: "0"


    :param sync_interval: All processes are synchronized with this time interval, therefore, all other time constants must be multiples of this value. ``output_interval`` and ``output_averaging_interval`` must be at least twice of this value. The default value is 900.
    :type sync_interval: str, default: "0:15"


    :param ctl: Specifies the factor by which the time step must be smaller than the Lagrangian time scale (TL). ``ctl`` must be >1 for time steps shorter than the Lagrangian time scale. If ``ctl``<0, a purely random walk simulation is done. The default value -4.
    :type ctl: number, default: -5.0


    :param vertical_timestep_reduction: Specifies the reduction factor (as an integer) for the time step used for vertical wind. The default value is 4.
    :type vertical_timestep_reduction: number, default: 4


    :param subgrid_terrain: 
    :type subgrid_terrain: {"on", "off"}, default: "off"


    :param convection: Enables ``convection`` parametrization ( "on" or "off" ). The default value is "off".
    :type convection: {"on", "off"}, default: "off"


    :param output_for_each_release: 
    :type output_for_each_release: {"on", "off"}, default: "off"


    :param quasi_lagrangian: Specifies whether particles should be numbered individually ( "on" ) or identified by the release location number ( "off" ). The default value is "off".
    :type quasi_lagrangian: {"on", "off"}, default: "off"


    :param domain_fill: Enables the ``domain_fill`` mode. The possible values are as follows:

         *  none : ``domain_fill`` is disabled   

                  *  full : in this mode the the particles are not released at specific locations but the 3D-volume of the first release is taken and the particles are uniformly distributed in the volume proportionally to air density. Each particle will receive the same mass, altogether accounting for the total atmospheric mass. Subsequently, particles can move freely in the atmosphere.
         *  o3_tracer : in this mode domain-filling is to simulate a stratospheric ozone tracer. This option is similar to fill option, but only particles in the stratosphere (defined by PV < 2 pvu) are released.

         The default value is none.
    :type domain_fill: str, default: "no"


    :param sensitivity: Enables computing ``sensitivity`` to initial conditions in backward simulations. The possible values are none , mass (mass concentration units) or mixr (mass mixing ratio units). The default value is none.
    :type sensitivity: str, default: "no"


    :rtype: None
