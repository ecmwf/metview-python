
mcont
=========================

.. container::
    
    .. container:: leftside

        .. image:: /_static/MCONT.png
           :width: 48px

    .. container:: rightside

		This is the visual definition for specifying how gridded data is displayed. It controls features such as isolines, shading, highs & lows, and grid value plotting.


		.. note:: This function performs the same task as the `Contouring <https://confluence.ecmwf.int/display/METV/Contouring>`_ icon in Metview’s user interface. It accepts its parameters as keyword arguments, described below.


.. py:function:: mcont(**kwargs)
  
    Specifies the style for gridded data plotting.


    :param contour_automatic_setting: Specifies the automatic contour settings mode. When it is set to "ecmwf" the default ecCharts style will be assigned to each GRIB field.
    :type contour_automatic_setting: {"off", "ecmwf", "style_name"}, default: "off"

    :param contour_style_name: Specifies the predefined contour style name. Enabled when ``contour_automatic_setting`` is "style_name".
    :type contour_style_name: str

    :param legend: Turns legend "on" or "off".
    :type legend: {"on", "off"}, default: "off"

    :param contour: Turns contour lines "on" or "off".
    :type contour: {"on", "off"}, default: "on"

    :param contour_line_style: Style of contour lines.
    :type contour_line_style: {"solid", "dash", "dot", "chain_dot", "chain_dash"}, default: "solid"

    :param contour_line_thickness: Thickness of contour lines.
    :type contour_line_thickness: int, default: 1

    :param contour_line_colour_rainbow: If it is set to "on", rainbow colouring method will be used for contour lines.
    :type contour_line_colour_rainbow: {"on", "off"}, default: "off"

    :param contour_line_colour: Colour of contour lines.
    :type contour_line_colour: str, default: "blue"

    :param contour_line_colour_rainbow_method: Method of generating the colours for individual isolines when ``contour_line_colour_rainbow`` is "on".
    :type contour_line_colour_rainbow_method: {"calculate", "list"}, default: "calculate"

    :param contour_line_colour_rainbow_max_level_colour: Colour to be used for the maximum isoline level when ``contour_line_colour_rainbow_method`` is "calculate".
    :type contour_line_colour_rainbow_max_level_colour: str, default: "blue"

    :param contour_line_colour_rainbow_min_level_colour: Colour to be used for the minimum isoline level when ``contour_line_colour_rainbow_method`` is "calculate".
    :type contour_line_colour_rainbow_min_level_colour: str, default: "red"

    :param contour_line_colour_rainbow_direction: Direction of colour sampling along the colour wheel when ``contour_line_colour_rainbow_method`` is "calculate".
    :type contour_line_colour_rainbow_direction: {"clockwise", "anti-clockwise"}, default: "anti-clockwise"

    :param contour_line_colour_rainbow_colour_list: List of colours to be used for rainbow isolines when ``contour_line_colour_rainbow_method`` is "list".
    :type contour_line_colour_rainbow_colour_list: str or list[str]

    :param contour_line_colour_rainbow_colour_list_policy: Specifies what to do if there are fewer colour items in ``contour_line_colour_rainbow_colour_list`` than the number of contour values.
    :type contour_line_colour_rainbow_colour_list_policy: {"lastone", "cycle"}, default: "lastone"

    :param contour_line_thickness_rainbow_list: List of thickness values to be used for rainbow isolines when ``contour_line_colour_rainbow_method`` is "list".
    :type contour_line_thickness_rainbow_list: float or list[float]

    :param contour_line_thickness_rainbow_list_policy: Specifies what to do if there are fewer thickness items in ``contour_line_thickness_rainbow_list`` than the number of contour values.
    :type contour_line_thickness_rainbow_list_policy: {"lastone", "cycle"}, default: "lastone"

    :param contour_line_style_rainbow_list: List of line style items to be used for rainbow isolines when ``contour_line_colour_rainbow_method`` is "list".
    :type contour_line_style_rainbow_list: str or list[str]

    :param contour_line_style_rainbow_list_policy: Specifies what to do if there are fewer line style items in ``contour_line_style_rainbow_list`` than the number of contour values.
    :type contour_line_style_rainbow_list_policy: {"lastone", "cycle"}, default: "lastone"

    :param contour_highlight: Plot contour highlights.
    :type contour_highlight: {"on", "off"}, default: "on"

    :param contour_highlight_style: Style of contour highlighting.
    :type contour_highlight_style: {"solid", "dash", "dot", "chain_dot", "chain_dash"}, default: "solid"

    :param contour_reference_level: Specifies contour level from which the contour interval is calculated.
    :type contour_reference_level: number, default: 0.0

    :param contour_highlight_colour: Colour of the highlighted contour lines.
    :type contour_highlight_colour: str, default: "blue"

    :param contour_highlight_thickness: Thickness of the highlighted contour lines.
    :type contour_highlight_thickness: int, default: 3

    :param contour_highlight_frequency: Frequency of highlighted contour lines.
    :type contour_highlight_frequency: number, default: 4

    :param contour_level_selection_type: Specifies how the contour values are defined:
		
		* "count": calculate a reasonable  contour interval taking into account the min/max and the requested number of isolines. 
		* "interval": regularly spaced intervals using the ``contour_reference_level`` as base.
		* "level_list": uses the given ``contour_level_list``.
    :type contour_level_selection_type: {"count", "interval", "level_list"}, default: "count"

    :param contour_max_level: Highest level for contours to be drawn.
    :type contour_max_level: number, default: 1.0e+21

    :param contour_min_level: Lowest level for contours to be drawn.
    :type contour_min_level: number, default: -1.0e+21

    :param contour_shade_max_level: Highest level for contours to be shaded.
    :type contour_shade_max_level: number, default: 1.0e+21

    :param contour_shade_min_level: Lowest level for contours to be shaded.
    :type contour_shade_min_level: number, default: -1.0e+21

    :param contour_level_list: List of contour levels to be plotted.
    :type contour_level_list: float or list[float]

    :param contour_interval: Interval in data units between two contour lines when ``contour_level_selection_type`` is "interval".
    :type contour_interval: number, default: 8.0

    :param contour_level_count: Number of levels to be plotted when ``contour_level_selection_type`` is "count". The plotting library will try to find a "nice" set of levels, which means that the number of levels could be slightly different than specified here.
    :type contour_level_count: number, default: 10

    :param contour_level_tolerance: Do not use nice levels if the number of levels differs from ``contour_level_count`` by more than ``contour_level_tolerance``.
    :type contour_level_tolerance: number, default: 2

    :param contour_label: Plots labels on contour lines.
    :type contour_label: {"on", "off"}, default: "on"

    :param contour_label_type: Type of contour labels.
    :type contour_label_type: str, default: "number"

    :param contour_label_text: Text for contour labels.
    :type contour_label_text: str

    :param contour_label_height: Height (cm) of contour labels.
    :type contour_label_height: number, default: 0.3

    :param contour_label_format: Format of contour labels.
    :type contour_label_format: str, default: "(automatic)"

    :param contour_label_blanking: Enables contour label blanking.
    :type contour_label_blanking: {"on", "off"}, default: "on"

    :param contour_label_font: The font type used for contour labels.
    :type contour_label_font: {"arial", "courier", "helvetica", "times", "serif", "sansserif", "symbol"}, default: "sansserif"

    :param contour_label_font_style: Style of the font used for contour labels.
    :type contour_label_font_style: {"normal", "bold", "italic", "bolditalic"}, default: "normal"

    :param contour_label_colour: Colour of contour labels.
    :type contour_label_colour: {"background", "contour_line_colour"}, default: "contour_line_colour"

    :param contour_label_frequency: Specifies the contour line frequency for contour labels. The labels will appear on every ``contour_label_frequency`` lines.
    :type contour_label_frequency: number, default: 2

    :param contour_shade: Enables contour shading.
    :type contour_shade: {"on", "off"}, default: "off"

    :param contour_shade_technique: Specifies the technique used for shading.
    :type contour_shade_technique: {"polygon_shading", "grid_shading", "cell_shading", "marker"}, default: "polygon_shading"

    :param contour_shade_colour_method: Method of generating the colours of the bands in contour shading.
    :type contour_shade_colour_method: {"calculate", "list", "gradients", "palette"}, default: "calculate"

    :param contour_shade_method: Rendering method used for contour shading.
    :type contour_shade_method: {"area_fill", "dot", "hatch"}, default: "dot"

    :param contour_shade_cell_resolution: Number of cells per cm when ``contour_shade_technique`` is "cell_shading".
    :type contour_shade_cell_resolution: number, default: 10

    :param contour_shade_cell_method: Method of determining the colour of a cell when ``contour_shade_technique`` is "cell_shading".
    :type contour_shade_cell_method: {"nearest", "interpolate"}, default: "nearest"

    :param contour_grid_shading_position: When it is "middle" the point is in the middle of the cell, when it is  "bottom_left": the point is in the bottom left corner. Available when ``contour_shade_technique`` is "grid_shading".
    :type contour_grid_shading_position: {"middle", "bottom_left"}, default: "middle"

    :param contour_shade_colour_table: Colour table to be used with marker shading technique. Available when ``contour_shade_technique`` is "marker".
    :type contour_shade_colour_table: str or list[str]

    :param contour_shade_height_table: Height table to be used with marker shading technique. Available when ``contour_shade_technique`` is "marker".
    :type contour_shade_height_table: float or list[float]

    :param contour_shade_marker_table_type: Specifies how the markers are specified when ``contour_shade_technique`` is "marker".
    :type contour_shade_marker_table_type: {"index", "name"}, default: "index"

    :param contour_shade_marker_table: Marker table defined by a a set of numerical symbol identifiers when ``contour_shade_marker_table_type`` is "index".
    :type contour_shade_marker_table: float or list[float]

    :param contour_shade_marker_name_table: Marker table defined by a a set of symbol names when ``contour_shade_marker_table_type`` is "index".
    :type contour_shade_marker_name_table: str or list[str]

    :param contour_shade_max_level_colour: Highest shading band colour.
    :type contour_shade_max_level_colour: str, default: "blue"

    :param contour_shade_min_level_colour: Lowest shading band colour.
    :type contour_shade_min_level_colour: str, default: "red"

    :param contour_shade_colour_direction: Direction of colour sampling along the colour wheel for isoline shading when ``contour_shade_colour_method`` is "calculate".
    :type contour_shade_colour_direction: {"clockwise", "anti_clockwise"}, default: "anti_clockwise"

    :param contour_shade_colour_list: List of colours to be used in contour shading when ``contour_shade_colour_method`` is "list".
    :type contour_shade_colour_list: str or list[str]

    :param contour_gradients_colour_list: Colour used at the stops, the gradient will be calculated between 2 consecutive ones.
    :type contour_gradients_colour_list: str

    :param contour_gradients_waypoint_method: Waypoints at the "left", "right", middle of the interval.
    :type contour_gradients_waypoint_method: {"both", "ignore", "left", "right"}, default: "both"

    :param contour_gradients_technique: Technique to apply to compute the gradients.
    :type contour_gradients_technique: {"rgb", "hcl", "hsl"}, default: "rgb"

    :param contour_gradients_technique_direction: Technique to apply to compute the gradients.
    :type contour_gradients_technique_direction: {"clockwise", "anti_clockwise", "shortest", "longest"}, default: "clockwise"

    :param contour_gradients_step_list: Number of steps to compute for each interval.
    :type contour_gradients_step_list: float or list[float], default: 10

    :param contour_shade_palette_name: The name of the colour palette to use when ``contour_shade_colour_method`` is "palette".
    :type contour_shade_palette_name: str

    :param contour_shade_palette_policy: What to do if the list of colours is smaller than the list of levels.
    :type contour_shade_palette_policy: {"lastone", "cycle"}, default: "lastone"

    :param contour_shade_dot_size: Size of dot in shading pattern when ``contour_shade_method`` is "dot".
    :type contour_shade_dot_size: number, default: 0.02

    :param contour_shade_max_level_density: Dots per square centimetre in highest shading band when ``contour_shade_method`` is "dot".
    :type contour_shade_max_level_density: number, default: 50.0

    :param contour_shade_min_level_density: Dots per square centimetre in lowest shading band when ``contour_shade_method`` is "dot".
    :type contour_shade_min_level_density: number, default: 1.0

    :param contour_shade_hatch_index: The hatching pattern(s) to use. 0 Provides an automatic sequence of patterns, other values set a constant pattern across all contour bands.
    :type contour_shade_hatch_index: number, default: 0

    :param contour_shade_hatch_thickness: Thickness of hatch lines.
    :type contour_shade_hatch_thickness: int, default: 1

    :param contour_shade_hatch_density: Number of hatch lines per cm.
    :type contour_shade_hatch_density: number, default: 18.0

    :param contour_legend_text: Text to be used in legend.
    :type contour_legend_text: str

    :param contour_method: Contouring method.
    :type contour_method: {"automatic", "sample", "linear", "akima760", "akima474"}, default: "automatic"

    :param contour_akima_x_resolution: X resolution of Akima interpolation. Available when ``contour_method`` is "akima760" or "akima474".
    :type contour_akima_x_resolution: number, default: 1.5

    :param contour_akima_y_resolution: Y resolution of Akima interpolation. Available when ``contour_method`` is "akima760" or "akima474".
    :type contour_akima_y_resolution: number, default: 1.5

    :param contour_interpolation_floor: Any value below this floor will be forced to the floor value. Avoid the bubbles artificially created by the interpolation method.
    :type contour_interpolation_floor: number, default: -1.0e21

    :param contour_interpolation_ceiling: Any value above this ceiling will be forced to the ceiling value. Avoid the bubbles artificially created by the interpolation method.
    :type contour_interpolation_ceiling: number, default: 1.0e21

    :param contour_internal_reduction_factor: Internal factor for contouring.
    :type contour_internal_reduction_factor: number, default: 4.0

    :param contour_threads: Number of threads used to optimise the contouring.
    :type contour_threads: {"1", "4", "9"}, default: "4"

    :param contour_hilo: Plots local maxima/minima (highs/lows).
    :type contour_hilo: {"on", "off", "hi", "lo"}, default: "off"

    :param contour_hilo_type: Type of high/low value plotting.
    :type contour_hilo_type: {"text", "number", "both"}, default: "text"

    :param contour_hi_text: Text to represent local maxima.
    :type contour_hi_text: str, default: "h"

    :param contour_lo_text: Text to represent local minima.
    :type contour_lo_text: str, default: "l"

    :param contour_hilo_blanking: Blanking around high/low text.
    :type contour_hilo_blanking: {"on", "off"}, default: "off"

    :param contour_hilo_format: Format of high/low numbers.
    :type contour_hilo_format: str, default: "(automatic)"

    :param contour_hilo_window_size: Size of the window used to calculate the high/low values.
    :type contour_hilo_window_size: number, default: 3

    :param contour_hilo_suppress_radius: 
    :type contour_hilo_suppress_radius: number, default: 15.0

    :param contour_hilo_max_value: Local high/low values above the specified value are not drawn.
    :type contour_hilo_max_value: number, default: 1.0e+21

    :param contour_hilo_min_value: Local high/low values below the specified value are not drawn.
    :type contour_hilo_min_value: number, default: -1.0e+21

    :param contour_hi_max_value: Local high values above the specified value are not drawn.
    :type contour_hi_max_value: number, default: 1.0e+21

    :param contour_hi_min_value: Local high values below the specified value are not drawn.
    :type contour_hi_min_value: number, default: -1.0e+21

    :param contour_lo_max_value: Local low values above the specified value are not drawn.
    :type contour_lo_max_value: number, default: 1.0e+21

    :param contour_lo_min_value: Local low values below the specified value are not drawn.
    :type contour_lo_min_value: number, default: -1.0e+21

    :param contour_hilo_marker: Plot high/low markers.
    :type contour_hilo_marker: {"on", "off"}, default: "off"

    :param contour_hilo_marker_height: Height (cm) of high/low marker symbols.
    :type contour_hilo_marker_height: number, default: 0.1

    :param contour_hilo_marker_index: Index of high/low marker symbols.
    :type contour_hilo_marker_index: number, default: 3

    :param contour_hilo_marker_colour: Colour of high/low marker symbols.
    :type contour_hilo_marker_colour: str, default: "red"

    :param contour_hilo_position_file_name: 
    :type contour_hilo_position_file_name: str

    :param contour_hilo_height: Height of high/low text or numbers.
    :type contour_hilo_height: number, default: 0.4

    :param contour_hilo_quality: 
    :type contour_hilo_quality: {"high", "medium", "low"}, default: "low"

    :param contour_hi_colour: Colour of high values text or number.
    :type contour_hi_colour: str, default: "blue"

    :param contour_lo_colour: Colour of low values text or number.
    :type contour_lo_colour: str, default: "blue"

    :param contour_grid_value_plot: Plots grid point values.
    :type contour_grid_value_plot: {"on", "off"}, default: "off"

    :param contour_grid_value_type: None
    :type contour_grid_value_type: {"normal", "reduced", "akima"}, default: "normal"

    :param contour_grid_value_plot_type: None
    :type contour_grid_value_plot_type: {"value", "marker", "both"}, default: "value"

    :param contour_grid_value_min: The minimum value for which grid point values are to be plotted.
    :type contour_grid_value_min: number, default: -1.0e+21

    :param contour_grid_value_max: The maximum value for which grid point values are to be plotted.
    :type contour_grid_value_max: number, default: 1.0e+21

    :param contour_grid_value_lat_frequency: The frequency of latitude rows for grid point value plotting.
    :type contour_grid_value_lat_frequency: number, default: 1

    :param contour_grid_value_lon_frequency: The frequency of latitude rows for grid point value plotting.
    :type contour_grid_value_lon_frequency: number, default: 1

    :param contour_grid_value_height: Height of the grid point values.
    :type contour_grid_value_height: number, default: 0.25

    :param contour_grid_value_colour: Colour of the grid point values.
    :type contour_grid_value_colour: str, default: "blue"

    :param contour_grid_value_format: Format of the grid point values.
    :type contour_grid_value_format: str, default: "(automatic)"

    :param contour_grid_value_quality: None
    :type contour_grid_value_quality: {"high", "medium", "low"}, default: "low"

    :param contour_grid_value_marker_height: Height of the grid point markers.
    :type contour_grid_value_marker_height: number, default: 0.25

    :param contour_grid_value_marker_colour: Colour of the grid point markers.
    :type contour_grid_value_marker_colour: str, default: "red"

    :param contour_grid_value_marker_qual: Quality of the grid point marker.
    :type contour_grid_value_marker_qual: {"high", "medium", "low"}, default: "low"

    :param contour_grid_value_marker_index: Index of marker symbol for grid point plotting.
    :type contour_grid_value_marker_index: number, default: 3

    :param grib_scaling_of_retrieved_fields: Toggles the contour scaling of the retrieved fields. Fields which are retrieved from MARS or derived from other fields are in SI units. If this parameter is "on", the plotting library will perform a unit conversion (scaling) on the retrieved fields that it plots, converting from these SI units to units of customary meteorological usage - e.g. Pressure from Pa to hPa, Temperature from K to Celsius. Certain parameters will be scaled into more user-friendly units if the data has not been manipulated.
    :type grib_scaling_of_retrieved_fields: {"on", "off"}, default: "on"

    :param grib_scaling_of_derived_fields: Toggles the contour scaling of the derived fields. Any field you derive are supposed to be in SI units, so set this parameter to "on" to convert to meteorological style units. E.g.: 
		
		* If you retrieve two temperature fields, they are plotted in Celsius . If you derive a mean temperature from them, it will be plotted in K if you do not scale the derived field.
		* Precipitation fields are cumulative fields plotted in mm - if you subtract two consecutive ones to obtain the precipitation for the time step between them, you will plot a field in m if you do not scale the derived field. 
		* Certain parameters will be scaled into more user-friendly units if the data has been manipulated.
    :type grib_scaling_of_derived_fields: {"on", "off"}, default: "off"

    :param grib_interpolation_method: 
    :type grib_interpolation_method: {"interpolate", "nearest", "nearest_valid"}, default: "interpolate"

    :param grib_interpolation_method_missing_fill_count: 
    :type grib_interpolation_method_missing_fill_count: number, default: 1

    :param grib_interpolation_regular_resolution: Sets the plotting resolution, in degrees, of GRIB fields encoded in space_view projection. The default is 0.1.
    :type grib_interpolation_regular_resolution: number, default: 0.1

    :param contour_sample_x_interval: 
    :type contour_sample_x_interval: number, default: 2

    :param contour_sample_y_interval: 
    :type contour_sample_y_interval: number, default: 2

    :rtype: :class:`Request`


.. minigallery:: metview.mcont
    :add-heading:

