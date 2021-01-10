
flextra_run
=========================

.. container::
    
    .. container:: leftside

        .. image:: /_static/FLEXTRA_RUN.png
           :width: 48px

    .. container:: rightside

		
		Runs the `FLEXTRA <https://confluence.ecmwf.int/display/METV/The+FLEXTRA+interface>`_ trajectory model
		
		.. tip:: A tutorial on using FLEXTRA from within Metview is available `here <https://confluence.ecmwf.int/display/METV/FLEXTRA+tutorial>`_.


		.. note:: This function performs the same task as the `Flextra Run <https://confluence.ecmwf.int/display/METV/flextra+run>`_ icon in Metview’s user interface. It accepts its parameters as keyword arguments, described below.


.. py:function:: flextra_run(**kwargs)
  
    Runs the `FLEXTRA <https://confluence.ecmwf.int/display/METV/The+FLEXTRA+interface>`_ trajectory model.


    :param flextra_exe_path: Specifies a user defined FLEXTRA executable. Both absolute and relative path can be given here. If it is left blank (this is the default) Metview will use the MV_FLEXTRA_EXE environment variable to locate the executable.
    :type flextra_exe_path: str

    :param flextra_input_mode: Specifies how the input data path is defined. When it is set to "path" you need to specify the input data file and the AVAILABLE file by their paths in ``flextra_input_path``. In "icon" mode the input data is specified by a :func:`flextra_prepare` object in ``flextra_input_data``.
    :type flextra_input_mode: {"path", "icon"}, default: "icon"

    :param flextra_input_data: Specifies the location of the input data files using :func:`flextra_prepare`.
    :type flextra_input_data: :func:`flextra_prepare`

    :param flextra_input_path: Specifies the location of the input data files. Both an absolute and relative path can be given here. Enabled when ``flextra_input_mode`` is "path".
    :type flextra_input_path: str

    :param flextra_available_file_path: Specifies the location of the AVAILABLE file. The default is "same_as_input_path" , which means that the AVAILABLE file is located in the same directory as the input data. Enabled when ``flextra_input_mode`` is "path".
    :type flextra_available_file_path: str, default: "same_as_input_path"

    :param flextra_run_label: Specifies the FLEXTRA run label.
    :type flextra_run_label: str, default: "flextra run"

    :param flextra_run_mode: Specifies the run mode for the FLEXTRA simulation. The possible values are as follows:
		
		* "normal": a group of trajectories is specified starting from the same point but at different times. Several starting points (thus several groups of trajectories) can be defined for a single FLEXTRA run.
		* "cet": trajectories are generated starting from the points of a user-defined uniform grid in a three-dimensional domain.
		* "flight": both the starting location and starting time for each trajectory can be set individually. This mode is useful to calculate e.g. trajectories released along the flight track of an aircraft.
    :type flextra_run_mode: {"normal", "cet", "flight"}, default: "normal"

    :param flextra_trajectory_direction: Specifies the FLEXTRA simulation direction in time.
    :type flextra_trajectory_direction: {"forward", "backward"}, default: "forward"

    :param flextra_trajectory_length: Specifies the length of the FLEXTRA simulation. The format is HHH[:MM[:SS].
    :type flextra_trajectory_length: str, default: "48"

    :param flextra_first_starting_date: Specifies the start date of the period within which the trajectories will be released. Enabled when ``flextra_run_mode`` is "normal" or  "cet". The format is YYYYMMDD.  Relative dates are allowed: e.g. -1 means yesterday, 0 means today, etc.
    :type flextra_first_starting_date: str

    :param flextra_first_starting_time: Specifies the start time of the period within which the trajectories will be released. Enabled when ``flextra_run_mode`` is "normal" or "cet". The format is HH[:MM[:SS].
    :type flextra_first_starting_time: str

    :param flextra_last_starting_date: Specifies the end date of the period within which the trajectories will be released. Enabled when ``flextra_run_mode`` is "normal" or  "cet". The format is YYYYMMDD. Relative dates are allowed: e.g. -1 means yesterday, 0 means today, etc.
    :type flextra_last_starting_date: str

    :param flextra_last_starting_time: Specifies the end time of the period within which the trajectories will be released. Enabled when ``flextra_run_mode`` is "normal" or "cet". The format is HH[:MM[:SS].'
    :type flextra_last_starting_time: str

    :param flextra_starting_time_interval: Specifies the starting interval of trajectories within the starting period. Enabled when ``flextra_run_mode`` is set to "normal" or "cet". The format is HHH[:MM[:SS].
    :type flextra_starting_time_interval: str, default: "6"

    :param flextra_output_interval_mode: Specifies how the output data (i.e. trajectory waypoints) will be written out into the output file. It can have three values:
		
		* "original": the trajectory points are written out into the output file exactly at the computational time steps. In the FLEXTRA terminology these are called flexible time steps.
		* "interval": the trajectory points are written out into the output file at regular intervals specified by parameter ``flextra_output_interval_value``. In the FLEXTRA terminology these are called constant time steps.
		* "both": two output files will be generated: one for the flexible time steps and one for the constant time steps.
    :type flextra_output_interval_mode: {"original", "interval", "both"}, default: "interval"

    :param flextra_output_interval_value: Specifies the output frequency when ``flextra_output_interval_mode`` is set to "interval" or "both". The format is HHH[:MM[:SS]. The default value is "3", which means "3" hourly output.
    :type flextra_output_interval_value: str, default: "3"

    :param flextra_normal_types: Specifies the list of trajectory types as numerical IDs when ``flextra_run_mode`` is "normal". The possible values are as follows:
		
		* 1: 3 dimensional
		* 2: model level
		* 3: mixing layer
		* 4: isobaric
		* 5: isentropic
    :type flextra_normal_types: int or list[int]

    :param flextra_normal_names: Specifies the trajectory names when ``flextra_run_mode`` is set to "normal".
    :type flextra_normal_names: str or list[str]

    :param flextra_normal_latitudes: Specifies the latitudes of the trajectory start points when ``flextra_run_mode`` is set to "normal".
    :type flextra_normal_latitudes: float or list[float]

    :param flextra_normal_longitudes: Specifies the longitudes of the trajectory start points when ``flextra_run_mode`` is set to "normal".
    :type flextra_normal_longitudes: float or list[float]

    :param flextra_normal_levels: Specifies the levels of the trajectory start points when ``flextra_run_mode`` is set to "normal".
    :type flextra_normal_levels: float or list[float]

    :param flextra_normal_level_units: Specifies the level types (as numerical IDs) of the trajectory start points when ``flextra_run_mode`` is set to "normal". The possible values are as follows:
		
		* 1: metres above sea level 
		* 2: metres above ground level
		* 3: hPa  
    :type flextra_normal_level_units: int or list[int], default: 1

    :param flextra_cet_type: Specifies the list of trajectory types (numerical IDs or strings) when ``flextra_run_mode`` is set to "cet". The possible values are as follows:
		
		* 1 or "3d"
		* 2 or "model_level"
		* 3 or "isobaric"
		* 4 or "isentropic"
    :type flextra_cet_type: list[int] or list[str], default: "3d"

    :param flextra_cet_name: Specifies the trajectory name when ``flextra_run_mode`` is set to "cet".
    :type flextra_cet_name: str

    :param flextra_cet_area: Specify the geographical area of the start grid by a [South, West, North, East] list.
    :type flextra_cet_area: list[float], default: [-90, -180, 90, 180]

    :param flextra_cet_dx: Specifies the start grid resolution in West-East direction in degrees when ``flextra_run_mode`` is set to "cet".
    :type flextra_cet_dx: number, default: 1

    :param flextra_cet_dy: Specifies the start grid resolution in South-North direction in degrees when ``flextra_run_mode`` is set to "cet".
    :type flextra_cet_dy: number, default: 1

    :param flextra_cet_top_level: Specifies the top level of the start grid volume when ``flextra_run_mode`` is set to "cet".
    :type flextra_cet_top_level: number, default: 1

    :param flextra_cet_bottom_level: Specifies the bottom level of the start grid when ``flextra_run_mode`` is set to "cet".
    :type flextra_cet_bottom_level: number, default: 1

    :param flextra_cet_dz: Specifies the start grid vertical resolution when ``flextra_run_mode`` is set to "cet".
    :type flextra_cet_dz: number, default: 1

    :param flextra_cet_level_units: Specifies the level types (as numerical IDs or strings) of the start grid when ``flextra_run_mode`` is set to "cet". The possible values are as follows:
		
		* 1 or "metres_asl": metres above sea level 
		* 2 or "metres agl": metres above ground level
		* 3 or "hpa"  
    :type flextra_cet_level_units: {"metres_asl", "metres_agl", "hpa"}, default: "hpa"

    :param flextra_flight_type: 
    :type flextra_flight_type: str, default: "3d"

    :param flextra_flight_name: Specifies the trajectory names when ``flextra_run_mode`` is set to "flight".
    :type flextra_flight_name: {"list[str]"}

    :param flextra_flight_latitudes: Specifies the latitudes of the trajectory start points when ``flextra_run_mode`` is set to "flight".
    :type flextra_flight_latitudes: float or list[float]

    :param flextra_flight_longitudes: Specifies the longitudes of the trajectory start points when ``flextra_run_mode`` is set to "flight".
    :type flextra_flight_longitudes: float or list[float]

    :param flextra_flight_levels: Specifies the levels of the trajectory start points when ``flextra_run_mode`` is set to "flight".
    :type flextra_flight_levels: float or list[float]

    :param flextra_flight_level_units: Specifies the level types (as numerical IDs or strings) of the trajectory start points when ``flextra_run_mode`` is set to "flight". The possible values are as follows:
		
		* 1 or "metres_asl": metres above sea level 
		* 2 or "metres agl": metres above ground level
		* 3 or "hpa"  
    :type flextra_flight_level_units: {"metres_asl", "metres_agl", "hpa"}, default: "hpa"

    :param flextra_flight_starting_dates: Specifies the starting dates of the trajectories when ``flextra_run_mode`` is set to "flight". The format is HHH[:MM[:SS].
    :type flextra_flight_starting_dates: str or list[str], default: "6"

    :param flextra_flight_starting_times: Specifies the starting times of the trajectories when ``flextra_run_mode`` is set to "flight". The format is HH[:MM[:SS].
    :type flextra_flight_starting_times: str or list[str]

    :param flextra_interpolation_type: Specifies the interpolation type. The possible values are as follows:
		
		* 1: horizontal interpolation: bicubic, vertical interpolation: polynomial, temporal interpolation: linear
		* >1: horizontal interpolation: bilinear, vertical interpolation: linear, temporal interpolation: linear
    :type flextra_interpolation_type: interpolation, default: 1

    :param flextra_cfl_spatial: Specifies the factor by which the time step must be smaller than that determined from the CFL criterion. This factor must be >1!
    :type flextra_cfl_spatial: number, default: 2.0

    :param flextra_cfl_temporal: Specifies the factor by which the time step must be smaller than the time interval of the wind fields. This factor must be >1!
    :type flextra_cfl_temporal: number, default: 2.0

    :param flextra_uncertainty_trajectories: 
    :type flextra_uncertainty_trajectories: str, default: "off"

    :param flextra_uncertainty_trajectory_number: 
    :type flextra_uncertainty_trajectory_number: number, default: 0

    :param flextra_uncertainty_trajectory_distance: 
    :type flextra_uncertainty_trajectory_distance: number, default: 0.5

    :param flextra_uncertainty_trajectory_time_constant: 
    :type flextra_uncertainty_trajectory_time_constant: number, default: 2.0

    :param flextra_u_random_error: 
    :type flextra_u_random_error: number, default: 0.08

    :param flextra_v_random_error: 
    :type flextra_v_random_error: number, default: 0.08

    :param flextra_w_random_error: 
    :type flextra_w_random_error: number, default: 0.08

    :rtype: :class:`Request`
