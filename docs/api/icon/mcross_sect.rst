
mcross_sect
=========================

.. container::
    
    .. container:: leftside

        .. image:: /_static/MXSECTION.png
           :width: 48px

    .. container:: rightside

        This function performs the same task as the `Cross Section Data <https://confluence.ecmwf.int/display/METV/Cross+Section+Data>`_ icon in Metview’s user interface. It accepts its parameters as keyword arguments, described below.


.. py:function:: mcross_sect(**kwargs)
  
    Description comes here!


    :param data: 
    :type data: str


    :param line: 
    :type line: float or list[float], default: 0


    :param wind_parallel: When this option is "on" , the wind components are projected onto the cross section plane. For 2D wind the result is a signed scalar ``data`` (a contour plot). When 3D wind ``data`` are available a vector plot is produced with the vertical component scaled/computed as specified in parameter ``w_wind_scaling_factor_mode``. Valid values are "on" / "off".
    :type wind_parallel: {"on", "off"}, default: "on"


    :param wind_perpendicular: When this option is "on" , the wind components are projected onto the normal vector of the cross section plane. The result is a signed scalar ``data`` (a contour plot). Valid values are "on" / "off". This cannot be set to "on" if ``wind_parallel`` is also "on".
    :type wind_perpendicular: {"on", "off"}, default: "off"


    :param wind_intensity: When this option is "on" the result depends "on" other settings:

         * When both ``wind_parallel`` and ``wind_perpendicular`` are "off" , the result is the length of the 2D/3D wind vector at the cross section plane
         * When Wind Parralel is "on" , the result is the absolute value of the projected wind onto the cross section plane
         * When ``wind_perpendicular`` is "on" , the result is the absolute value of the wind projected onto the normal vector of the cross section plane

         Valid values are "on" / "off".
    :type wind_intensity: {"on", "off"}, default: "off"


    :param lnsp_param: Specifies the ecCodes paramId of the LNSP ``data``. The default value is 152 (as used by ECMWF).
    :type lnsp_param: number, default: 152


    :param u_wind_param: Specifies the ecCodes paramId of the U wind component ``data``. The default value is 131 (as used by ECMWF).
    :type u_wind_param: number, default: 131


    :param v_wind_param: Specifies the ecCodes paramId of the V wind component ``data``. The default value is 132 (as used by ECMWF).
    :type v_wind_param: number, default: 132


    :param w_wind_param: Specifies the ecCodes paramId of the vertical wind component ``data``. The default value is 135 i.e. pressure velocity (as used by ECMWF).
    :type w_wind_param: number, default: 135


    :param t_param: Specifies the ecCodes paramId of the temperature ``data`` used in the vertical wind computations when ``w_wind_scaling_factor_mode`` is set to Compute. The default value is 130 (as used by ECMWF).
    :type t_param: number, default: 130


    :param horizontal_point_mode: Specifies how the geographical points along the input transect ``line`` will be computed. Valid values are "interpolate" and Nearest Gridpoint. Setting this option to "interpolate" will create a regular set of interpolated geographical points along the transect ``line``. Setting this option to Nearest Gridpoint will instead select the nearest points from the ``data``.
    :type horizontal_point_mode: {"interpolate", "nearest_gridpoint"}, default: "interpolate"


    :param vertical_coordinates: Setting this option to "user" will enable the use of general height-based coordinates. In this mode, additional GRIB fields should be supplied (one per level) where the values of the grid points represent the heights of their locations. Valid values are "default" and _User.The "default" value is "default".
    :type vertical_coordinates: {"default", "user"}, default: "default"


    :param vertical_coordinate_param: Specifies the ecCodes paramId of the general height-based coordinates if ``vertical_coordinates`` is set to User.
    :type vertical_coordinate_param: str


    :param w_wind_scaling_factor_mode: Specifies the representation of the vertical wind component (defined as ``w_wind_param`` ). The valid values are as follows:

         *  "automatic" : the values are scaled by a factor based on the geographical area, the top/bottom pressure levels and the size of the plot window.
         *  "user" : the values are scaled by the factor defined via parameter ``w_wind_scaling_factor``.
         *  "compute" : in this mode, supposing that ``w_wind_param`` defines the the pressure velocity , the vertical wind component in m/s is computed using the following hydrostatic formula:

         \\[ w = - \frac{\omega R T}{p g} \\]

         where:

         * ω: pressure velocity (Pa/s)
         * p : pressure on (Pa)
         * T: temperature (K)
         * R: gas constant, 287.058 J kg-1 K-1
         * g: gravitational acceleration, 9.81 m/s2

         To make this formula work, the input ``data`` have to be specified either on pressure levels or on model levels together with LNSP. The temperature's paramId is defined by ``t_param``. When temperature is not available, the computations still work but T is replaced by a constant 273.16 K value in the formula. Having computed the vertical wind component, a scaling with the factor defined by ``w_wind_scaling_factor`` is still applied to the resulting values.

         The default value is "automatic".
    :type w_wind_scaling_factor_mode: {"automatic", "user", "compute"}, default: "automatic"


    :param w_wind_scaling_factor: Specifies the vertical wind scaling factor if ``w_wind_scaling_factor_mode`` is set to User or Compute. The default values is -100.
    :type w_wind_scaling_factor: number, default: -100


    :param level_selection_type: Specifies the method to define the output pressure levels when converting model level ``data`` to pressure levels. Options are:

         *  From ``data`` (default)
         * compute the absolute bottom pressure level from the ``data``
         * for each model level, compute the average pressure along the cross section ``line`` and then use this mean pressure as the vertical pressure co-ordinate for that level
         * compute extra levels at the bottom by adding an offset (10 hPa) until it reaches the bottom pressure level, computed previously. This will avoid blank areas in the plot near the orography ``line``.
         *  "count"
         * calculate the output pressure levels by taking into account the bottom and top pressure levels ( ``bottom_level`` and ``top_level`` ) and the given number of levels ( ``level_count`` ) . The computed levels will be evenly spaced on either a ``line``ar or a logarithmic scale depending on the value of ``vertical_scaling``.
         *  ``"level_list"``
         * use the given list of pressure levels ( ``"level_list"`` )
    :type level_selection_type: {"from_data", "count", "level_list"}, default: "from_data"


    :param level_list: Specifies a list of output pressure levels separated by a “/”. Only available if ``level_selection_type`` is set to ``level_list``.
    :type level_list: float or list[float], default: 0.01


    :param level_count: Specifies the number of output pressure levels if ``level_selection_type`` is set to Count.
    :type level_count: number, default: 100


    :param vertical_scaling: Specifies the type of vertical axis - ``line``ar or "log". Only available if ``level_selection_type`` is set to Count.
    :type vertical_scaling: {"linear", "log"}, default: "linear"


    :param bottom_level: Specifies the lower limit of the cross section, i.e. the bottom pressure level (hPa). Only available if ``level_selection_type`` is set to Count.
    :type bottom_level: number, default: 1100.0


    :param top_level: Specifies the upper limit of the cross section, i.e. the top pressure level (hPa). Only available if ``level_selection_type`` is set to Count.
    :type top_level: number, default: 0.01


    :rtype: None


.. minigallery:: metview.mcross_sect
    :add-heading:

