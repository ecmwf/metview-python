
thermoview
=========================

.. container::
    
    .. container:: leftside

        .. image:: /_static/THERMOVIEW.png
           :width: 48px

    .. container:: rightside

		
		
		Specifies the view for thermodynamic diagram plots from a suitable :class:`Fieldset` (GRIB), :class:`Bufr` and :func:`input_visualiser` data source. It can also take the output from :func:`thermo_data` as an input. In this case, a consistency check is performed between the parameters that are common to both functions.
		
		In addition to the parameters required for the thermodynamic computation, :func:`thermoview` specifies the axis details as well as the plot positioning in the plot frame of the display window/paper sheet and the overlay of different data units in the same plot. 
		
		When using :func:`thermoview` the generated profile data cannot be accessed. If you need to access this data use :func:`thermo_data` instead.
		
		For further details on the role and usage of views in the visualisation process, please see `Anaylis Views <https://confluence.ecmwf.int/display/METV/Analysis+Views>`_.
		


		.. note:: This function performs the same task as the `Thermo View <https://confluence.ecmwf.int/display/METV/Thermo+View>`_ icon in Metview’s user interface. It accepts its parameters as keyword arguments, described below.


.. py:function:: thermoview(**kwargs)
  
    Specifies the view for thermodynamic diagram plots.


    :param type: Specifies the type of the thermodynamic diagram to be produced.
    :type type: {"tephigram", "skewt", "emagram"}, default: "tephigram"

    :param bottom_pressure: Specifies the value (hPa) at the bottom of the pressure axis of the thermodynamic diagram.
    :type bottom_pressure: number, default: 1015.0

    :param top_pressure: Specifies the value (hPa) at the top of the pressure axis of the thermodynamic diagram.
    :type top_pressure: number, default: 100

    :param minimum_temperature: Specifies the minimum value (Celsius) on the temperature axis of the thermodynamic diagram.
    :type minimum_temperature: number, default: -90

    :param maximum_temperature: Specifies the maximum value (Celsius) on the temperature axis of the thermodynamic diagram.
    :type maximum_temperature: number, default: 50

    :param thermo_grid: Configures the background attributes of the thermodynamic diagram, please see :func:`mthermogrid` for details.
    :type thermo_grid: :func:`mthermogrid`

    :param point_selection: Specifies how the geographical location, for which the diagram is to be plotted, will be selected.
    :type point_selection: {"coordinates", "area_average", "station"}, default: "coordinates"

    :param coordinates: Specifies the geographical location (as [lat, lon]) for which the diagram is to be plotted. Available when ``point_selection`` is "coordinates".
    :type coordinates: list[float], default: [0, 0]

    :param area_average: Specifies a geographical area over which an area average value will be used, instead of a point value, to produce the diagram.  The area is defined as [north, west, south, east]. Available when ``point_selection`` is "area_average".
    :type area_average: list[float], default: [30, -30, -30, 30]

    :param station: Specifies the location as a :func:`stations`` object for which the diagram is to be plotted. Available if ``point_selection` is "station".
    :type station: :func:`stations``

    :param point_extraction: Specifies the way to calculate values at the point location for GRIB thermodynamic diagrams. The possible options are:
		
		* "interpolate": interpolate values from the four surrounding grid points.
		* "nearest_gridpoint": use the data from the nearest grid point.
    :type point_extraction: {"interpolate", "nearest_gridpoint"}, default: "interpolate"

    :param dew_point_formulation: Specifies the equation to compute the dew point.
    :type dew_point_formulation: {"saturation_over_water", "mixed_phase_0_to\_\-23"}, default: "saturation_over_water"

    :param temperature_param: Specifies the ecCodes paramId used to identify the temperature in the input data.
    :type temperature_param: number, default: 130

    :param specific_humidity_param: Specifies the ecCodes paramId used to identify the specific humidity in the input data.
    :type specific_humidity_param: number, default: 133

    :param lnsp_param: Specifies the ecCodes paramId used to identify the Logarithm of Surface Pressure (LNSP) in the input data.
    :type lnsp_param: number, default: 152

    :param u_wind_param: Specifies the ecCodes paramId used to identify the U wind component in the input data.
    :type u_wind_param: number, default: 131

    :param v_wind_param: Specifies the ecCodes paramId used to identify the V wind component in the input data.
    :type v_wind_param: number, default: 132

    :param subpage_clipping: Clips plot to subpage borders.
    :type subpage_clipping: {"on", "off"}, default: "off"

    :param subpage_x_position: Specifies the X offset of the plot from the left side of the plot frame (any subdivision of the display area). This is expressed as a percentage of the X-dimension of the plot frame.
    :type subpage_x_position: number, default: 12

    :param subpage_y_position: Specifies the Y offset of the plot from the bottom side of the plot frame (any subdivision of the display area). This is expressed as a percentage of the Y-dimension of the plot frame.
    :type subpage_y_position: number, default: 10

    :param subpage_x_length: Specifies the X length of the plot. This is expressed as a percentage of the X-dimension of the plot frame. Hence the sum of this X length plus the X offset cannot exceed 100 (it is advised that it does not exceed 95 since you need some margin on the right for things like axis or map grid labels).
    :type subpage_x_length: number, default: 75

    :param subpage_y_length: Same as ``subpage_x_length`` but for the Y length of the plot.
    :type subpage_y_length: number, default: 80

    :param page_frame: Toggles the plotting of a border line around the plot frame.
    :type page_frame: {"on", "off"}, default: "off"

    :param page_frame_colour: Colour of the page frame.
    :type page_frame_colour: str, default: "charcoal"

    :param page_frame_line_style: Line style of the page frame.
    :type page_frame_line_style: {"solid", "dot", "dash", "chain_dot", "chain_dash"}, default: "solid"

    :param page_frame_thickness: Line thickness of the page frame.
    :type page_frame_thickness: int, default: 2

    :param page_id_line: Toggles the plotting of plot identification line.
    :type page_id_line: {"on", "off"}, default: "off"

    :param page_id_line_user_text: Specifies user text to be added to the plot identification line. Only available when ``page_id_line`` is "on".
    :type page_id_line_user_text: str

    :param subpage_frame: Toggles the plotting of a border line around the plot itself. In most cases you will want this to be left "on". When "off" the sides of the plot not equipped with axis will not be plotted.
    :type subpage_frame: {"on", "off"}, default: "off"

    :param subpage_frame_colour: Colour of the subpage frame.
    :type subpage_frame_colour: str, default: "black"

    :param subpage_frame_line_style: Line style of the subpage frame.
    :type subpage_frame_line_style: {"solid", "dot", "dash", "chain_dot", "chain_dash"}, default: "solid"

    :param subpage_frame_thickness: Line thickness of the subpage frame.
    :type subpage_frame_thickness: int, default: 2

    :param subpage_background_colour: Specifies the colour of the background of the plot (i.e. not affected by visual definitions like contour shadings or lines).
    :type subpage_background_colour: str, default: "white"

    :rtype: :class:`Request`
.. include:: /gallery/backref/thermoview.rst