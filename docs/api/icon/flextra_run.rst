
flextra_run
=========================

.. container::
    
    .. container:: leftside

        .. image:: /_static/FLEXTRA_RUN.png
           :width: 48px

    .. container:: rightside

        This icon represents the `flextra run <https://confluence.ecmwf.int/display/METV/flextra+run>`_ icon in Metview's user interface.


.. py:function:: flextra_run(**kwargs)
  
    Description comes here!


    :param flextra_exe_path: Specifies a user defined FLEXTRA executable. Both absolute and relative path can be given here. If it is left blank (this is the default) Metview will use the MV_FLEXTRA_EXE environment variable to locate the executable.
    :type flextra_exe_path: str


    :param flextra_input_mode: Specifies how the input data path is specified. The possible values are path and icon. When it is set to path we will specify the input data files and the AVAILABLE file by their paths. While in icon mode the input data is specified by a  :func:`flextra_prepare` icon in ``flextra_input_data``. The default value is path.
    :type flextra_input_mode: str


    :param flextra_input_data: Specifies the location of the input data files using a :func:`flextra_prepare` icon.
    :type flextra_input_data: str


    :param flextra_input_path: Specifies the location of the input data files. Both an absolute and relative path can be given here. Enabled when ``flextra_input_mode`` is path.
    :type flextra_input_path: str


    :param flextra_available_file_path: Specifies the location of the AVAILABLE file. The default is SAME_AS_INPUT_PATH , which means that the AVAILABLE file is located in the same directory as the input data. Enabled when ``flextra_input_mode`` is path.
    :type flextra_available_file_path: str


    :param flextra_run_label: Specifies the ``flextra_run_label``. The default value is: " FLEXTRA RUN ".
    :type flextra_run_label: str


    :param flextra_run_mode: Specifies the run mode for the FLEXTRA simulation. The possible values are as follows:

         * In normal mode, a group of trajectories is specified starting from the same point but at different times. Several starting points (thus several groups of trajectories) can be defined for a single FLEXTRA run.
         * In cet mode, trajectories are generated starting from the points of a user-defined uniform grid in a three-dimensional domain.
         * In filight mode, both the starting location and starting time for each trajectory can be set individually. This mode is useful to calculate e.g. trajectories released along the flight track of an aircraft.

         The default value is normal.
    :type flextra_run_mode: str


    :param flextra_trajectory_direction: Specifies the FLEXTRA simulation direction in time. The possible values are: forward and backward. The default value is forward.
    :type flextra_trajectory_direction: str


    :param flextra_trajectory_length: 
    :type flextra_trajectory_length: str


    :param flextra_first_starting_date: 
    :type flextra_first_starting_date: str


    :param flextra_first_starting_time: 
    :type flextra_first_starting_time: str


    :param flextra_last_starting_date: 
    :type flextra_last_starting_date: str


    :param flextra_last_starting_time: 
    :type flextra_last_starting_time: str


    :param flextra_starting_time_interval: Specifies the starting interval of trajectories within the starting period. Enabled when ``flextra_run_mode`` is set to normal or cet. The format is HHH[:MM[:SS]`_. The default value is: 6 (i.e. 6 hours).
    :type flextra_starting_time_interval: str


    :param flextra_output_interval_mode: Specifies how the output data (i.e. trajectory waypoints) will be written out into the output file. It can have three values:

         *  original : The trajectory points are written out into the output file exactly at the computational time steps. In the FLEXTRA terminology these are called flexible time steps.
         *  interval : The trajectory points are written out into the output file at regular intervals specified by parameter ``flextra_output_interval_value``. In the FLEXTRA terminology these are called constant time steps.
         *  both : Two output files will be generated: one for the flexible time steps and one for the constant time steps.

         The default value is interval.
    :type flextra_output_interval_mode: str


    :param flextra_output_interval_value: Specifies the output frequency when ``flextra_output_interval_mode`` is set to interval or both. The format is HHH[:MM[:SS]`_. The default value is 3 , which means 3 hourly output.
    :type flextra_output_interval_value: str


    :param flextra_normal_types: Specifies the list of trajectory types as numerical IDs when ``flextra_run_mode`` is set to normal. The possible values are as follows:

         Numerical ID| Description ---|--- 1| 3 dimensional 2| model level 3| mixing layer 4| isobaric 5| isentropi c  The default value is 1 (three-dimensional trajectories).
    :type flextra_normal_types: float or list[float]


    :param flextra_normal_names: Specifies the trajectory names when ``flextra_run_mode`` is set to normal.
    :type flextra_normal_names: str or list[str]


    :param flextra_normal_latitudes: Specifies the latitudes of the trajectory start points when ``flextra_run_mode`` is set to normal.
    :type flextra_normal_latitudes: float or list[float]


    :param flextra_normal_longitudes: Specifies the longitudes of the trajectory start points when ``flextra_run_mode`` is set to normal.
    :type flextra_normal_longitudes: float or list[float]


    :param flextra_normal_levels: Specifies the levels of the trajectory start points when ``flextra_run_mode`` is set to normal.
    :type flextra_normal_levels: float or list[float]


    :param flextra_normal_level_units: Specifies the level types (as numerical IDs) of the trajectory start points when ``flextra_run_mode`` is set to normal. The possible values are as follows:

         Numerical ID| Description ---|--- 1| Metres above sea level 2| Metres above ground level 3| hPa  The default value is 1 (metres above sea level).
    :type flextra_normal_level_units: float or list[float]


    :param flextra_cet_type: 
    :type flextra_cet_type: str


    :param flextra_cet_name: Specifies the trajectory name when ``flextra_run_mode`` is set to cet.
    :type flextra_cet_name: str


    :param flextra_cet_area: Specify the geographical area of the start grid by a S/W/N/E list.
    :type flextra_cet_area: float or list[float]


    :param flextra_cet_dx: Specifies the start grid resolution in West-East direction in degrees when ``flextra_run_mode`` is set to cet. The default value is 1.
    :type flextra_cet_dx: number


    :param flextra_cet_dy: Specifies the start grid resolution in South-North direction in degrees when ``flextra_run_mode`` is set to cet. The default value is 1.
    :type flextra_cet_dy: number


    :param flextra_cet_top_level: Specifies the top level of the start grid volume when ``flextra_run_mode`` is set to cet. The default value is 1.
    :type flextra_cet_top_level: number


    :param flextra_cet_bottom_level: Specifies the bottom level of the start grid when ``flextra_run_mode`` is set to cet. The default value is 1.
    :type flextra_cet_bottom_level: number


    :param flextra_cet_dz: Specifies the start grid vertical resolution when ``flextra_run_mode`` is set to cet. The default value is 1
    :type flextra_cet_dz: number


    :param flextra_cet_level_units: Specifies the level types (as numerical IDs or strings) of the start grid when ``flextra_run_mode`` is set to cet. The possible values are as follows:

         Numerical ID| String (case insensitive)| Description ---|---|--- 1| metres asl| Metres above sea level 2| metres agl| Metres above ground level 3| hPa|   The default value is 1 (metres above sea level).
    :type flextra_cet_level_units: str


    :param flextra_flight_type: 
    :type flextra_flight_type: str


    :param flextra_flight_name: 
    :type flextra_flight_name: str


    :param flextra_flight_latitudes: Specifies the latitudes of the trajectory start points when ``flextra_run_mode`` is set to flight.
    :type flextra_flight_latitudes: float or list[float]


    :param flextra_flight_longitudes: Specifies the longitudes of the trajectory start points when ``flextra_run_mode`` is set to flight.
    :type flextra_flight_longitudes: float or list[float]


    :param flextra_flight_levels: Specifies the levels of the trajectory start points when ``flextra_run_mode`` is set to flight.
    :type flextra_flight_levels: float or list[float]


    :param flextra_flight_level_units: Specifies the level types (as numerical IDs or strings) of the trajectory start points when ``flextra_run_mode`` is set to flight. The possible values are as follows

         Numerical ID| String (case insensitive)| Description ---|---|--- 1| metres asl| Metres above sea level 2| metres agl| Metres above ground level 3| hPa|   The default value is 1 (metres above sea level).
    :type flextra_flight_level_units: str


    :param flextra_flight_starting_dates: 
    :type flextra_flight_starting_dates: str or list[str]


    :param flextra_flight_starting_times: 
    :type flextra_flight_starting_times: str or list[str]


    :param flextra_interpolation_type: Specifies the interpolation type. The possible values are as follows:

         Value| Description ---|--- 1|

         * horizontal interpolation bicubic
         * vertical interpolation polynomial
         * temporal interpolation linear

          >1|

         * horizontal interpolation bilinear
         * vertical interpolation linear
         * temporal interpolation linear

           The default value is 1.
    :type flextra_interpolation_type: str


    :param flextra_cfl_spatial: Specifies the factor by which the time step must be smaller than that determined from the CFL criterion.  This factor must be >1_! The default value is . 2.0.
    :type flextra_cfl_spatial: number


    :param flextra_cfl_temporal: Specifies the factor by which the time step must be smaller than the time interval of the wind fields. This factor must be >1_! The default value is 2.0.
    :type flextra_cfl_temporal: number


    :param flextra_uncertainty_trajectories: 
    :type flextra_uncertainty_trajectories: str


    :param flextra_uncertainty_trajectory_number: 
    :type flextra_uncertainty_trajectory_number: number


    :param flextra_uncertainty_trajectory_distance: 
    :type flextra_uncertainty_trajectory_distance: number


    :param flextra_uncertainty_trajectory_time_constant: 
    :type flextra_uncertainty_trajectory_time_constant: number


    :param flextra_u_random_error: 
    :type flextra_u_random_error: number


    :param flextra_v_random_error: 
    :type flextra_v_random_error: number


    :param flextra_w_random_error: 
    :type flextra_w_random_error: number


    :rtype: None


.. minigallery:: metview.flextra_run
    :add-heading:

