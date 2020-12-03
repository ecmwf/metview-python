
vapor_prepare
=========================

.. container::
    
    .. container:: leftside

        .. image:: /_static/VAPOR_PREPARE.png
           :width: 48px

    .. container:: rightside

        This function performs the same task as the `Vapor Prepare <https://confluence.ecmwf.int/display/METV/vapor+prepare>`_ icon in Metview’s user interface. It accepts its parameters as keyword arguments, described below.


.. py:function:: vapor_prepare(**kwargs)
  
    Description comes here!


    :param vapor_input_mode: Specifies the data input mode. The possible values are: "icon" and Path. The default value is "icon".  

         In "icon" mode a set of GRIB icons has to be specified in ``vapor_input_data``. If the mode is set to Path the input data is read from a specified path on the filesystem (yet to be implemented).
    :type vapor_input_mode: str, default: "icon"


    :param vapor_input_data: Specifies the input data as a set of GRIB icons. It is available when ``vapor_input_mode`` is Icon.
    :type vapor_input_data: str


    :param vapor_2d_params: Specifies the list of 2D parameters from the input data to be converted into VAPOR format. The parameters are identified by their short names or _parameter ids_. The default value is an empty string.
    :type vapor_2d_params: str or list[str], default: "2t"


    :param vapor_3d_params: Specifies the list of 3D parameters from the input data to be converted into VAPOR format. The parameters are identified by their short names  or _parameter ids_. The default value is an empty string.
    :type vapor_3d_params: str or list[str], default: "t"


    :param vapor_vertical_grid_type: Specifies the type of the 3D data to be used in VAPOR. The possible values are: "layered" and Regular. The default value is "layered".

         If the type is set to "layered" VAPOR expects a parameter specifying the elevation of each 3D level in the input data. This parameter is then called ELEVATION in VAPOR. The "layered" type is typically used when we have pressure or model level (η levels) input data with height or geopotential available.  

         For the Regular type the vertical grid is supposed to be equidistant (in the user coordinate space). This type can be used when we have data on equidistant height levels.

         The Regular type can also be used for pressure or model level data when _no height information is available_. In this case the 3D scene is rendered in a pressure or model level "space". Besides, because VAPOR requires vertical coordinate values increasing along the z axis the vertical coordinate values (pressure or model level number) are multiplied by -1 for VAPOR.
    :type vapor_vertical_grid_type: str, default: "layered"


    :param vapor_elevation_param: Specifies the short name or parameter id of of the 3D parameter interpreted as the elevation of the 3D levels. Available when ``vapor_vertical_grid_type`` is Layered.

         This parameter has to be either the height or the geopotential ("z") of the levels. If geopotential is specified it is converted into metres by Metview for Vapor. The default value is "z".

         Derive elevation for model levels

         Please note that neither the height nor the geopotential of model levels are archived in MARS. It means that for model level data either of these fields has to be computed for Layered mode. These computations can be done with _VAPOR Prepare by simply specifying "z" for ``vapor_elevation_param``. The computations can only be carried out if the input data contains temperature (t) and specific humidity (q) on model levels and geopotential ("z") and logarithm of surface pressure (lnsp) on the bottommost model level.
    :type vapor_elevation_param: str, default: "z"


    :param vapor_bottom_coordinate: The name of the upper level GRIB parameter interpreted as the elevation of the upper levels. Available when ``vapor_vertical_grid_type`` is Layered. The default value is 0.
    :type vapor_bottom_coordinate: number, default: 0


    :param vapor_top_coordinate: The name of the upper level GRIB parameter interpreted as the elevation of the upper levels. Available when ``vapor_vertical_grid_type`` is Layered. The default value is 16000.
    :type vapor_top_coordinate: number, default: 16000


    :param vapor_area_selection: Specifies the area selection mode. The possible values are: "native" and Interpolate. The default value is "native".

         If it is set to "native" the whole area of the input data is converted into VAPOR format. While if it is set to Interpolate the input data is interpolated to a specific (lat-lon) grid and area.
    :type vapor_area_selection: str, default: "native"


    :param vapor_area: Specifies the area of the output grid in south/west/north/east format. The default value is -90/-180/90/180. Available when ``vapor_area_selection`` is Interpolate.
    :type vapor_area: float or list[float], default: -90


    :param vapor_grid: Specifies the resolution of the output grid in dx/dy format, where dx is the grid increment in east-west direction, while dy is the grid increment in north-south direction (both in degrees units). The default value is: 1/1. Available when ``vapor_area_selection`` is Interpolate.
    :type vapor_grid: float or list[float], default: 1


    :param vapor_step_number: Specifies the number of steps from the input dataset that will be converted into the VAPOR format. The default value is -1 meaning that all the available steps will be converted.
    :type vapor_step_number: number, default: -1


    :param vapor_refinement_level: This option specifies the number of refinement levels in a VAPOR data approximation hierarchy where the resolution of each successive level is a factor of two finer along each dimension. If level is 0 no hierarchy will be created (all data will be stored at their native resolution). If level is 1 a single approximation will be created, thus the hierarchy will have two levels: the first approximation (indexed as 0 in VAPOR) and the native grid resolution (indexed as 1 in VAPOR). And so on.

         The default value is: "2".
    :type vapor_refinement_level: str, default: "2"


    :param vapor_vdf_name: Specifies the name of the resulting VDF file (the .vdf suffix is automatically appended to the filename). The default value is an empty string.
    :type vapor_vdf_name: str


    :param vapor_output_path: Specifies the output directory (can be a relative path) where the VDF file and VDC directory hierarchy will be generated. If this directory does not exist Metview will create it. The default value is /tmp.

         VAPOR data files can be huge (gigabytes) so the output path to store the results of the GRIB to VAPOR conversion should always be carefully selected.
    :type vapor_output_path: str, default: [", tmp"]


    :rtype: None
