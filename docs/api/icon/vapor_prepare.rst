
vapor_prepare
=========================

.. container::
    
    .. container:: leftside

        .. image:: /_static/VAPOR_PREPARE.png
           :width: 48px

    .. container:: rightside

		Converts GRIB data into the format required by the `VAPOR <https://confluence.ecmwf.int/display/METV/3D+visualisation+with+VAPOR>`_  3D visualisation system.
		
		.. tip:: A tutorial for :func:`vapor_prepare` can be found `here <https://confluence.ecmwf.int/display/METV/VAPOR+Tutorial>`_.  Details about setting up the Metview VAPOR interface outside ECMWF can be accessed `here <https://confluence.ecmwf.int/display/METV/VAPOR+Setup>`_.
		
		**VAPOR input files**
		
		VAPOR input data is described by **.vdf** (VAPOR Data Format) files. These are XML files containing the name and dimension of all the variables and the path of the actual data files storing the data values.  VAPOR stores its data values in **.vdc** (VAPOR Data Collection) files. These are NetCDF files containing wavelet compressed 3D data. There is a separate file for each variable and timestep organized into a folder hierarchy.
		
		**VAPOR grids**
		
		VAPOR input data must be defined on a 3D grid,  which has to be regular horizontally (on a map projection). The vertical grid structures supported by the Metview VAPOR interface are as follows: 
		
		* For **layered** grids VAPOR expects a parameter specifying the elevation of each 3D level in the input data. This is typically the case for pressure or ECMWF model level (:math:`\eta` levels) data with height or geopotential available (or it can be computed).
		* For **regular** grids the 3D levels are supposed to be equidistant (in the user coordinate space). This type can be used when the data is available on equidistant height levels.
		
		The situation when pressure or model level data is present without height information is somewhat special. The grid in this case is not layered but can be regarded as regular in its own coordinate space (pressure or model levels) letting z axis simply represent pressure or model levels in the 3D scene rendered in VAPOR.
		
		VAPOR uses a right-handed coordinate system which means that:
		
		* the horizontal grid has to start at the SW corner
		* the vertical coordinates have to increase along the z axis (upwards)
		
		**How does vaport_prepare work?**
		
		First :func:`vapor_prepare` parses the GRIB data then generates the vdf and vdc files out of it. Internally it dumps GRIB data into a raw binary format then converts it into VAPOR format by using the **raw2vdf** VAPOR command line tool. :func:`vapor_prepare` implicitly rearranges the grid to make it VAPOR compliant.
		
		**Which GRIBs are supported for the conversion?**
		
		Only GRIB fields on a regular lat-lon grid are supported at the moment. However, please note that  GRIBs can be internally interpolated to a regular lat-lon grid by using the ``vapor_area_selection`` parameter. The parameters to be converted are supposed to have the same validity date and time and the same vertical levels. They also have to be valid on the same grid.


		.. note:: This function performs the same task as the `Vapor Prepare <https://confluence.ecmwf.int/display/METV/vapor+prepare>`_ icon in Metview’s user interface. It accepts its parameters as keyword arguments, described below.


.. py:function:: vapor_prepare(**kwargs)
  
    Converts GRIB data into the format required by the VAPOR 3D visualisation system.


    :param vapor_input_mode: Specifies the data input mode. The only available mode is "icon". In this case a set of :class:`Fieldset` objects has to be specified in ``vapor_input_data``.
    :type vapor_input_mode: {"icon"}, default: "icon"

    :param vapor_input_data: Specifies the input data as a set of :class:`Fieldset` objects. It is available when ``vapor_input_mode`` is "icon".
    :type vapor_input_data: :class:`Fieldset` or list[:class:`Fieldset`]

    :param vapor_2d_params: Specifies the list of 2D parameters from the input data to be converted into VAPOR format. The parameters are identified by their ecCodes shortNames or paramIds.
    :type vapor_2d_params: str or list[str], default: "2t"

    :param vapor_3d_params: Specifies the list of 3D parameters from the input data to be converted into VAPOR format. The parameters are identified by their ecCodes shortNames or paramIds.
    :type vapor_3d_params: str or list[str], default: "t"

    :param vapor_vertical_grid_type: Specifies the type of the 3D data to be used in VAPOR. The possible values are as follows:
		
		* "layered": VAPOR expects a parameter specifying the elevation of each 3D level in the input data. This parameter is then called ELEVATION in VAPOR. The "layered" type is typically used when we have pressure or ECMWF model level (hybrid/eta levels) input data with height or geopotential available.
		* "regular": the vertical grid is supposed to be equidistant (in the user coordinate space). This type can be used when we have data on equidistant height levels. The "regular" type can also be used for pressure or model level data when no height information is available. In this case the 3D scene is rendered in a pressure or model level "space". Besides, because VAPOR requires vertical coordinate values increasing along the z axis the vertical coordinate values (pressure or model level number) are multiplied by -1 for VAPOR.
    :type vapor_vertical_grid_type: {"layered", "regular"}, default: "layered"

    :param vapor_elevation_param: Specifies the short name or parameter id of of the 3D parameter interpreted as the elevation of the 3D levels. Available when ``vapor_vertical_grid_type`` is "layered". This parameter has to be either the height or the geopotential ("z") of the levels. If geopotential is specified it is converted into metres by Metview for VAPOR.         
		
		.. note:: Neither the height nor the geopotential of model levels are archived in MARS. It means that for model level data either of these fields has to be computed for "layered" mode. These computations can be done with :func:`vapor_prepare`` by simply specifying "z" for ``vapor_elevation_param``. The computations can only be carried out if the input data contains temperature (t) and specific humidity (q) on model levels and geopotential ("z") and logarithm of surface pressure (lnsp) on the bottommost model level.
    :type vapor_elevation_param: str, default: "z"

    :param vapor_bottom_coordinate: The bottom elevation level. Available when ``vapor_vertical_grid_type`` is "layered".
    :type vapor_bottom_coordinate: number, default: 0

    :param vapor_top_coordinate: The top elevation level. Available when ``vapor_vertical_grid_type`` is "layered".
    :type vapor_top_coordinate: number, default: 16000

    :param vapor_area_selection: Specifies the area selection mode.  If it is set to "native" the whole area of the input data is converted into VAPOR format. While if it is set to "interpolate" the input data is interpolated to a specific (lat-lon) grid and area.
    :type vapor_area_selection: {"native", "interpolate"}, default: "native"

    :param vapor_area: Specifies the area of the output grid in [south, west, north, east] format. Available when ``vapor_area_selection`` is "interpolate".
    :type vapor_area: list[float], default: [-90, -180, 90, 180]

    :param vapor_grid: Specifies the resolution of the output grid in [dx, dy] format, where dx is the grid increment in east-west direction, while dy is the grid increment in north-south direction (both in degrees units). Available when ``vapor_area_selection`` is "interpolate".
    :type vapor_grid: list[float], default: [1, 1]

    :param vapor_step_number: Specifies the number of steps from the input dataset that will be converted into the VAPOR format. The default value is -1 meaning that all the available steps will be converted.
    :type vapor_step_number: number, default: -1

    :param vapor_refinement_level: This option specifies the number of refinement levels in a VAPOR data approximation hierarchy where the resolution of each successive level is a factor of two finer along each dimension. If it is set to 0 no hierarchy will be created (all data will be stored at their native resolution). If it is 1 a single approximation will be created, thus the hierarchy will have two levels: the first approximation (indexed as 0 in VAPOR) and the native grid resolution (indexed as 1 in VAPOR). And so on.
    :type vapor_refinement_level: str, default: "2"

    :param vapor_vdf_name: Specifies the name of the resulting VDF file (the .vdf suffix is automatically appended to the filename).
    :type vapor_vdf_name: str

    :param vapor_output_path: Specifies the output directory (can be a relative path) where the VDF file and VDC directory hierarchy will be generated. If this directory does not exist Metview will create it. VAPOR data files can be huge (gigabytes) so the output path to store the results of the GRIB to VAPOR conversion should always be carefully selected.
    :type vapor_output_path: str, default: [", tmp"]

    :rtype: :class:`Request`
