
flextra_prepare
=========================

.. container::
    
    .. container:: leftside

        .. image:: /_static/FLEXTRA_PREPARE.png
           :width: 48px

    .. container:: rightside

        This icon represents the `flextra prepare <https://confluence.ecmwf.int/display/METV/flextra+prepare>`_ icon in Metview's user interface.


.. py:function:: flextra_prepare(**kwargs)
  
    Description comes here!


    :param flextra_prepare_mode: Specifies the data preparation mode. The possible values are: Forecast and Period.

         In Forecast mode the selected steps of a given forecast can be used for data generation. If the mode is set to Period a period with a start and end date and constant time-step can be defined. In this case FLEXTRA Prepare_ tries to retrieve analysis fields from MARS whenever it is possible (for dates in the past) and uses forecast fields otherwise (for dates in the future).
    :type flextra_prepare_mode: str


    :param flextra_input_source: Specifies the source of the input GRIB data. The possible values are: mars and file.The default value is mars.

         If the input source is mars the input GRIB data is retrieved from the MARS archive. When Prepare Mode is forecast the input source can also be set to file. In this case the GRIB file specified in Input File will be used as input data.
    :type flextra_input_source: str


    :param flextra_input_file: Specifies the full path to the file containing the input GRIB data. Available when Prepare Mode is forecast and  Input Source is file. The input file must contain the following fields for all the steps specified in ``flextra_step`` :  

         Filed type| Parameters ---|--- surface fields|

         ["sp", "z"]  model level fields| ["u","v","t","etadot"]
    :type flextra_input_file: str


    :param flextra_fc_mars_expver: The MARS experiment identifier of the forecast fields. The default value is 1 (operational forecast).
    :type flextra_fc_mars_expver: str


    :param flextra_an_mars_expver: The MARS experiment identifier of the analysis fields. The default value is 1 (operational analysis).
    :type flextra_an_mars_expver: str


    :param flextra_date: Specifies the run date of the forecast. Available when ``flextra_prepare_mode`` is Forecast.
    :type flextra_date: str


    :param flextra_time: Specifies the run time of the forecast . Available when ``flextra_prepare_mode`` is Forecast.
    :type flextra_time: str


    :param flextra_step: Specifies the forecast steps in hours. Here a list of values is given. Available when ``flextra_prepare_mode`` is Forecast.
    :type flextra_step: str or list[str]


    :param flextra_period_start_date: Specifies the start date of the period. Available when ``flextra_prepare_mode`` is Period.
    :type flextra_period_start_date: str


    :param flextra_period_start_time: Specifies the start time of the period. Available when ``flextra_prepare_mode`` is Period.
    :type flextra_period_start_time: str


    :param flextra_period_end_date: Specifies the end date of the period. Available when ``flextra_prepare_mode`` is Period.
    :type flextra_period_end_date: str


    :param flextra_period_end_time: Specifies the end time of the period. Available when ``flextra_prepare_mode`` is Period.
    :type flextra_period_end_time: str


    :param flextra_period_step: Specifies the time step of the period in hours. The allowed values are as follows: 3 or 6. Available when ``flextra_prepare_mode`` is Period.
    :type flextra_period_step: str


    :param flextra_grid_interpolation: Specifies if the input GRIB fields need to be interpolated onto a target grid specified by ``flextra_area`` and ``flextra_grid``. The possible values are on / off. Available when Input source is file. The default value is: on.
    :type flextra_grid_interpolation: str


    :param flextra_area: Specifies the area of the output grid in south/west/north/east format. The default value is -90/-179/90/180.

         In versions before 5.0.0 the default value is -90/-180/90/180.

         Please note that to make global domains work with FLEXTRA the western border must be set to one gridcell east of 180. E.g. if the east-west grid resolution is 1 degree ``flextra_area`` should be set to -90/-179/90/180 etc.
    :type flextra_area: float or list[float]


    :param flextra_grid: Specifies the resolution of the output grid in dx/dy format, where dx is the grid increment in east-west direction, while dy is the grid increment in north-south direction (both in units of degrees). The default value is: 1/1.
    :type flextra_grid: float or list[float]


    :param flextra_top_level: Only data on and below this model level will be used to generate the FLEXTRA input fields. This level can be specified either as a model level or as a pressure value. In the latter case FLEXTRA Prepare will use the data retrieved for the first date to determine the topmost model level. The default value of this parameter is 1 , which means that all the model levels will be used if ``flextra_top_level`` Units is set to Model Levels.
    :type flextra_top_level: number


    :param flextra_top_level_units: Specifies the units of the value of ``flextra_top_level``. The allowed values are Model Levels or hPa. The default value is Model Levels.
    :type flextra_top_level_units: str


    :param flextra_reuse_input: 
    :type flextra_reuse_input: str


    :param flextra_output_path: Specifies the output directory (it has to be an absolute path) where the GRIB files and the AVAILABLE file will be generated. If this directory does not exist Metview will create it. The output GRIB files have the following naming convention: EN yymmddhh._
    :type flextra_output_path: str


    :rtype: None


.. minigallery:: metview.flextra_prepare
    :add-heading:

