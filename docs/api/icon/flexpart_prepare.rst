
flexpart_prepare
=========================

.. container::
    
    .. container:: leftside

        .. image:: /_static/FLEXPART_PREPARE.png
           :width: 48px

    .. container:: rightside

        This function performs the same task as the `Flexpart Prepare <https://confluence.ecmwf.int/display/METV/flexpart+prepare>`_ icon in Metview’s user interface. It accepts its parameters as keyword arguments, described below.


.. py:function:: flexpart_prepare(**kwargs)
  
    Description comes here!


    :param prepare_mode: Specifies the data preparation mode. The possible values are: 

		* "forecast": the selected steps of a given forecast can be used for data generation. 
		* "period": a period with a start and end date and constant time-step can be defined. In this case :func:`flextra_prepare` tries to retrieve analysis fields from MARS whenever it is possible (for dates in the past) and uses forecast fields otherwise (for dates in the future).
    :type prepare_mode: {"forecast", "period"}, default: "forecast"


    :param input_source: Specifies the source of the input GRIB data. If the ``input_source`` is "mars" the input GRIB data is retrieved from the MARS archive. When ``prepare_mode`` is forecast ``input_source`` can also be set to "file".  In this case the GRIB file specified in ``input_file`` will be used as input data.
    :type input_source: {"mars", "file"}, default: "mars"


    :param input_file: Specifies the full path to the file containing the input GRIB data. Available when ``prepare_mode`` is "forecast" and ``input_source`` is "file". The input_file must contain the following fields:  

		.. note:: The surface fluxes are accumulated fields and for the de-accumulation process they also require the step preceding the first step. We have a special case when the first step is 0 because in this case we need two additional steps but from the previous model run! E.g. for a 0 UTC model run when we use 3 hourly steps we need the fluxes from step=6 and step=3 of the 18 UTC run on the previous day.
    :type input_file: str


    :param date: Specifies the run date of the forecast. Available when ``prepare_mode`` is "forecast".
    :type date: number, default: -1


    :param time: Specifies the run time of the forecast in hours. Available when ``prepare_mode`` is "forecast".
    :type time: number, default: 0


    :param step: Specifies the forecast steps in hours. Available when ``prepare_mode`` is "forecast".
    :type step: str or list[str], default: "0"


    :param period_start_date: Specifies the start date of the period. Available when ``prepare_mode`` is "period".
    :type period_start_date: number, default: -1


    :param period_start_time: Specifies the start time of the period. Available when ``prepare_mode`` is "period".
    :type period_start_time: number, default: 0


    :param period_end_date: Specifies the end date of the period. Available when ``prepare_mode`` is "period".
    :type period_end_date: number, default: -1


    :param period_end_time: Specifies the end time of the period. Available when ``prepare_mode`` is "period".
    :type period_end_time: number, default: 0


    :param period_step: Specifies the timestep of the period in hours. Available when ``prepare_mode`` is "period".
    :type period_step: {"3", "6"}, default: "3"


    :param grid_interpolation: Specifies if the input GRIB fields need to be interpolated onto a target grid specified by ``area`` and ``grid``. Available when ``input_source`` is "file".
    :type grid_interpolation: {"on", "off"}, default: "on"


    :param area: Specifies the area of the output ``grid`` in south/west/north/east format. 

		.. note:: To make global domains work with FLEXPART the western border must be set to one grid cell east of 180. E.g. if the east-west grid resolution is 1 degree ``area`` should be set to [-90, -179, 90, 180] etc.
    :type area: list[float], default: [-90, -179, 90, 180]


    :param grid: Specifies the resolution of the output grid in [dx/dy] format, where dx is the grid increment in east-west direction, while dy is the grid increment in north-south direction (both in units of degrees).
    :type grid: list[float], default: [1, 1]


    :param top_level: Only data on and below this model level will be used to generate the FLEXPART input fields. This level can be specified either as a model level or as a pressure value. In the latter case :func:`flexpart_prepare` will use the data retrieved for the first date to determine the topmost model level. The default value of this parameter is 1, which means that all the model levels will be used if ``top_level_units`` is set to "ml".
    :type top_level: number, default: 1


    :param top_level_units: Specifies the units of the value of ``top_level``.
    :type top_level_units: {"ml", "hpa"}, default: "ml"


    :param reuse_input: 
    :type reuse_input: {"on", "off"}, default: "on"


    :param output_path: Specifies the output directory (can be a relative or absolute path) where the GRIB files and the AVAILABLE file will be generated. If this directory does not exist Metview will create it. The output GRIB files have the following naming convention: ENyymmddhh
    :type output_path: str


    :rtype: None
