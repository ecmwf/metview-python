
flexpart_run
=========================

.. container::
    
    .. container:: leftside

        .. image:: /_static/FLEXPART_RUN.png
           :width: 48px

    .. container:: rightside

		Runs the `FLEXPART <https://confluence.ecmwf.int/display/METV/The+FLEXPART+interface>`_ Lagrangian particle dispersion model and converts its outputs to formats that Metview can work with.
		
		.. tip:: A tutorial on using FLEXPART from within Metview is available `here <https://confluence.ecmwf.int/display/METV/Using+FLEXPART+with+Metview>`_.


		.. note:: This function performs the same task as the `Flexpart Run <https://confluence.ecmwf.int/display/METV/flexpart+run>`_ icon in Metview’s user interface. It accepts its parameters as keyword arguments, described below.


.. py:function:: flexpart_run(**kwargs)
  
    Runs the `FLEXPART <https://confluence.ecmwf.int/display/METV/The+FLEXPART+interface>`_ Lagrangian particle dispersion model.


    :param output_path: Specifies the location of the output data files. Both an absolute and relative path can be given here. Please note that Metview converts FLEXPART output into other formats and only these converted results are copied from the work directory into ``output_path``. For further details about the output formats click `here <https://confluence.ecmwf.int/display/METV/FLEXPART+output>`_.
    :type output_path: str

    :param input_data: Specifies the location of the input data files and the AVAILABLE file using a :func:`flexpart_prepare` object. Please note that ``input_data`` takes precedence over ``input_path``.
    :type input_data: :func:`flexpart_prepare`

    :param input_path: Specifies the path of the directory containing the input data files and the AVAILABLE file. Both an absolute and relative path can be given here. Please note that when ``input_data`` is set this path is ignored.
    :type input_path: str

    :param user_exe_path: Specifies a user defined FLEXPART executable. Both absolute and relative path can be given here. If it is left blank (this is the default) Metview will use the MV_FLEXPART_EXE environment variable to locate the executable.
    :type user_exe_path: str

    :param user_resources_path: Specifies the location of the user defined parameter files (IGBP_int1.dat, OH_7lev_agl.dat, surfdata.t, surfdepo.t ) needed to run FLEXPART. Both an absolute and relative path can be given here. If it is left blank (this is the default) Metview will use the MV_FLEXPART_RESOURCES environment variable to locate the resources. For further details about the resources `click here <https://confluence.ecmwf.int/display/METV/FLEXPART+setup>`_.
    :type user_resources_path: str

    :param simulation_direction: Specifies the FLEXPART simulation direction in time.
    :type simulation_direction: {"forward", "backward"}, default: "forward"

    :param starting_date: Specifies the beginning date of the simulation in YYYYMMDD format. Relative dates are allowed, e.g. -1 means yesterday, 0 means today, etc.
    :type starting_date: str

    :param starting_time: Specifies the beginning time of the simulation in HH[:MM[:SS]] format.
    :type starting_time: str

    :param ending_date: Specifies the ending date of the simulation in YYYYMMDD format. Relative dates are allowed, e.g. -1 means yesterday, 0 means today, etc.
    :type ending_date: str

    :param ending_time: Specifies the ending time of the simulation in HH[:MM[:SS]] format.
    :type ending_time: str

    :param output_interval: Specifies the frequency for the output generation. The output is averaged over the period given in ``output_averaging_interval``. The format is HHHH[:MM[:SS]].
    :type output_interval: str, default: "3"

    :param output_averaging_interval: Specifies the averaging interval for the output generation in HHHH[:MM[:SS]] format. If 0 is given here instantaneous values are written into the output files.
    :type output_averaging_interval: str, default: "3"

    :param output_sampling_rate: Specifies the sampling rate used for the averaging of the output. This period must be shorter than the ``output_averaging_interval``. The format is HHHH[:MM[:SS]]
    :type output_sampling_rate: str, default: "0:15"

    :param output_field_type: Specifies the type of the gridded output fields. The possible values are:
		
		for forward simulations:
		
		* "none": no gridded output
		* "conc": concentration
		* "mixr": mass mixing ratio
		* "both": concentration and mass mixing ratio
		
		for backward simulations:
		
		* "none": no gridded output
		* "rtime": residence time/response function
		
		For more details about gridded output `click here. <https://confluence.ecmwf.int/display/METV/FLEXPART+output>`_
    :type output_field_type: {"none", "conc", "mixr", "both", "rtime"}, default: "conc"

    :param output_flux: Specifies if the fluxes should be computed and written out as a gridded output. Fluxes corresponding to northward, southward, eastward, westward, upward and downward directions are calculated for each grid cell of the output grid.The control surfaces are placed in the middle of each output grid cell. For more details about flux output `click here. <https://confluence.ecmwf.int/display/METV/FLEXPART+output>`_
    :type output_flux: {"on", "off"}, default: "off"

    :param output_trajectory: Specifies if the plume trajectories should be computed. For more details about trajectory output `click here. <https://confluence.ecmwf.int/display/METV/FLEXPART+output>`_
    :type output_trajectory: {"on", "off"}, default: "off"

    :param output_area: Specifies the area for the gridded output in degrees in S/W/N/E format.
    :type output_area: list[float], default: [-90, -180, 90, 180]

    :param output_grid: Specifies the grid resolution for the gridded output in degrees as [east_west_resolution, north_south_resolution].
    :type output_grid: list[float], default: [1, 1]

    :param output_levels: Specifies the list of height levels of the gridded output. The levels are given in metres units.
    :type output_levels: list[float], default: []

    :param user_species_path: Specifies the location of the user defined species files. Both an absolute and relative path can be given here. If it is left blank (this is the default value) Metview will use the MV_FLEXPART_SPECIES environment variable to locate the species. For more details about the species `click here <https://confluence.ecmwf.int/display/METV/FLEXPART+species>`_.
    :type user_species_path: str

    :param release_species: Specifies the list of the species released for the simulation. At all the release locations the same species are emitted. The species are identified by the NNN number (with leading zeros) appearing in the the name of the SPECIES_NNN files. These files contain the physical and chemical properties of species. For more details about the species `click here <https://confluence.ecmwf.int/display/METV/FLEXPART+species>`_.
    :type release_species: str or list[str]

    :param release_units: Specifies the units of the mass of the released species.
    :type release_units: {"mass", "mixr"}, default: "mass"

    :param releases: Specifies the releases as a list of :func:`flexpart_release` objects.
    :type releases: list

    :param receptor_units: Specifies the concentration units at the receptor. The possible options are "mass" (mass concentrations) and "mixr" (mass mixing ratio). See the table above to find out what the actual units mean.
    :type receptor_units: {"mass", "mixr"}, default: "mass"

    :param receptors: Enables the usage of receptor sites. When it is enabled the list of receptor sites can be defined via ``receptor_names``, ``receptor_latitudes`` and ``receptor_longitudes``. For more details about receptor output `click here <https://confluence.ecmwf.int/display/METV/FLEXPART+species>`_.
    :type receptors: {"on", "off"}, default: "off"

    :param receptor_names: Specifies the list of receptor site names.
    :type receptor_names: str or list[str]

    :param receptor_latitudes: Specifies the list of receptor site latitudes.
    :type receptor_latitudes: float or list[float]

    :param receptor_longitudes: Specifies the list of receptor site longitudes.
    :type receptor_longitudes: float or list[float]

    :param age_classes: Specifies the list of times for the age class calculation. If it is left blank (this is the default value) no age class is defined.
    :type age_classes: str or list[str]

    :param particle_splitting: Specifies the interval for particle splitting in HHHH[:MM[:SS]] format. Each particle is split into two after travelling the multiple of this interval. If "0" (default value) is given here particle splitting is disabled.
    :type particle_splitting: str, default: "0"

    :param sync_interval: All processes are synchronized with this time interval, therefore, all other time constants must be multiples of this value. ``output_interval`` and ``output_averaging_interval`` must be at least twice of this value. The format is HHHH[:MM[:SS]]
    :type sync_interval: str, default: "0:15"

    :param ctl: Specifies the factor by which the time step must be smaller than the Lagrangian time scale (TL). ``ctl`` must be > 1 for time steps shorter than the Lagrangian time scale. If ``ctl`` < 0, a purely random walk simulation is done.
    :type ctl: number, default: -5.0

    :param vertical_timestep_reduction: Specifies the reduction factor (as an integer) for the time step used for vertical wind.
    :type vertical_timestep_reduction: number, default: 4

    :param subgrid_terrain: Enables subgridscale terrain parametrization (increase of mixing heights due to subgridscale orographic variations).
    :type subgrid_terrain: {"on", "off"}, default: "off"

    :param convection: Enables convection parametrization.
    :type convection: {"on", "off"}, default: "off"

    :param output_for_each_release: Specifies whether a separate output fields should be generated for each release. When this option is set to "off" for forward simulations the output fields for a given species contain the sum of all the releases. For backward simulations it must be set to "on".
    :type output_for_each_release: {"on", "off"}, default: "off"

    :param quasi_lagrangian: Specifies whether particles should be numbered individually ("on") or identified by the release location number ("off").
    :type quasi_lagrangian: {"on", "off"}, default: "off"

    :param domain_fill: "Enables the domain fill mode. The possible values are as follows:
		
		* "no": domain fill is disabled
		* "full": the the particles are not released at specific locations but the 3D-volume of the first release is taken and the particles are uniformly distributed in the volume proportionally to air density. Each particle will receive the same mass, altogether accounting for the total atmospheric mass. Subsequently, particles can move freely in the atmosphere.
		* "o3_tracer": simulates a stratospheric ozone tracer. This option is similar to fill option, but only particles in the stratosphere (defined by PV < 2 pvu) are released.
    :type domain_fill: {"none", "full", "o3_tracer"}, default: "no"

    :param sensitivity: Enables computing sensitivity to initial conditions in backward simulations. The possible values are "no", "mass" (mass concentration units) or "mixr" (mass mixing ratio units).
    :type sensitivity: {"no", "mass", "mixr"}, default: "no"

    :rtype: :class:`Request`


.. mv-minigallery:: flexpart_run

