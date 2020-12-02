
mcont
=========================

.. container::
    
    .. container:: leftside

        .. image:: /_static/MCONT.png
           :width: 48px

    .. container:: rightside

        This function performs the same task as the `Contouring <https://confluence.ecmwf.int/display/METV/Contouring>`_ icon in Metview’s user interface. It accepts its parameters as keyword arguments, described below.


.. py:function:: mcont(**kwargs)
  
    Description comes here!


    :param contour_automatic_setting: Turn the automatic setting of contouring attributes
    :type contour_automatic_setting: {"off", "ecmwf", "style_name"}, default: "off"


    :param contour_style_name: Use of a predeined setting
    :type contour_style_name: str


    :param legend: Turn legend "on" or "off"
    :type legend: {"on", "off"}, default: "off"


    :param contour: Turn contouring "on" or "off"
    :type contour: {"on", "off"}, default: "on"


    :param contour_line_style: Style of contour line
    :type contour_line_style: {"solid", "dash", "dot", "chain_dot", "chain_dash"}, default: "solid"


    :param contour_line_thickness: Thickness of contour line
    :type contour_line_thickness: int, default: 1


    :param contour_line_colour_rainbow: if "on", rainbow colouring method will be used.
    :type contour_line_colour_rainbow: {"on", "off"}, default: "off"


    :param contour_line_colour: Colour of contour line
    :type contour_line_colour: str, default: "blue"


    :param contour_line_colour_rainbow_method: Method of generating the colours for isoline
    :type contour_line_colour_rainbow_method: {"calculate", "list"}, default: "calculate"


    :param contour_line_colour_rainbow_max_level_colour: Colour to be used for the max level
    :type contour_line_colour_rainbow_max_level_colour: str, default: "blue"


    :param contour_line_colour_rainbow_min_level_colour: Colour to be used for the mainlevel
    :type contour_line_colour_rainbow_min_level_colour: str, default: "red"


    :param contour_line_colour_rainbow_direction: Direction of colour sequencing for colouring
    :type contour_line_colour_rainbow_direction: {"clockwise", "anti-clockwise"}, default: "anti-clockwise"


    :param contour_line_colour_rainbow_colour_list: List of colours to be used in rainbow isolines
    :type contour_line_colour_rainbow_colour_list: str or list[str]


    :param contour_line_colour_rainbow_colour_list_policy: What to do if the list of colours is smaller that the list of contour: "lastone"/"cycle"
    :type contour_line_colour_rainbow_colour_list_policy: {"lastone", "cycle"}, default: "lastone"


    :param contour_line_thickness_rainbow_list: List of thickness to used when rainbow method is on
    :type contour_line_thickness_rainbow_list: float or list[float]


    :param contour_line_thickness_rainbow_list_policy: What to do if the list of thickness is smaller that the list of contour: "lastone"/"cycle"
    :type contour_line_thickness_rainbow_list_policy: {"lastone", "cycle"}, default: "lastone"


    :param contour_line_style_rainbow_list: List of line style to used when rainbow method is on
    :type contour_line_style_rainbow_list: str or list[str]


    :param contour_line_style_rainbow_list_policy: What to do if the list of line styles is smaller that the list of contour: "lastone"/"cycle"
    :type contour_line_style_rainbow_list_policy: {"lastone", "cycle"}, default: "lastone"


    :param contour_highlight: Plot contour highlights ("on"/"off")
    :type contour_highlight: {"on", "off"}, default: "on"


    :param contour_highlight_style: Style of highlighting ("solid"/ "dash"/ "dot"/ "chain_dash"/ "chain_dot")
    :type contour_highlight_style: {"solid", "dash", "dot", "chain_dot", "chain_dash"}, default: "solid"


    :param contour_reference_level: Contour level referenceContour level from which contour interval is calculatedContour level from which contour interval is calculated
    :type contour_reference_level: number, default: 0.0


    :param contour_highlight_colour: Colour of highlight line
    :type contour_highlight_colour: str, default: "blue"


    :param contour_highlight_thickness: Thickness of highlight line
    :type contour_highlight_thickness: int, default: 3


    :param contour_highlight_frequency: Frequency of highlight line
    :type contour_highlight_frequency: number, default: 4


    :param contour_level_selection_type: "count": calculate a reasonable  contour "interval" taking into account the min/max and the requested number of isolines.        "interval": regularly spaced intervals using the reference_level as base.        "level_list": uses the given list of levels.
    :type contour_level_selection_type: {"count", "interval", "level_list"}, default: "count"


    :param contour_max_level: Highest level for contours to be drawn
    :type contour_max_level: number, default: 1.0e+21


    :param contour_min_level: Lowest level for contours to be drawn
    :type contour_min_level: number, default: -1.0e+21


    :param contour_shade_max_level: Highest level for contours to be shadedMaximum level for which shading is required
    :type contour_shade_max_level: number, default: 1.0e+21


    :param contour_shade_min_level: Lowest level for contours to be shadedMinimum level for which shading is required
    :type contour_shade_min_level: number, default: -1.0e+21


    :param contour_level_list: List of contour levels to be plotted
    :type contour_level_list: float or list[float]


    :param contour_interval: Interval in data units between two contour lines
    :type contour_interval: number, default: 8.0


    :param contour_level_count: Count or number of levels to be plotted. Magics will try to find "nice levels",         this means that the number of levels could be slightly different from the asked number of levels
    :type contour_level_count: number, default: 10


    :param contour_level_tolerance: Tolerance: Do not use nice levels if the number of levels is really to different [count +/- tolerance]
    :type contour_level_tolerance: number, default: 2


    :param contour_label: Plot labels "on" contour lines
    :type contour_label: {"on", "off"}, default: "on"


    :param contour_label_type: Type of label (text/"number"/both
    :type contour_label_type: str, default: "number"


    :param contour_label_text: Text for labels
    :type contour_label_text: str


    :param contour_label_height: Height of contour labels
    :type contour_label_height: number, default: 0.3


    :param contour_label_format: Format of contour labels (MAGICS Format/("(automatic)"))
    :type contour_label_format: str, default: "(automatic)"


    :param contour_label_blanking: Label Blanking
    :type contour_label_blanking: {"on", "off"}, default: "on"


    :param contour_label_font: Name of the font
    :type contour_label_font: {"arial", "courier", "helvetica", "times", "serif", "sansserif", "symbol"}, default: "sansserif"


    :param contour_label_font_style: Style of the font "normal"/"bold"/"italic"
    :type contour_label_font_style: {"normal", "bold", "italic", "bolditalic"}, default: "normal"


    :param contour_label_colour: Colour of contour labels
    :type contour_label_colour: {"background", "contour_line_colour"}, default: "contour_line_colour"


    :param contour_label_frequency: Every Nth contour line is labelled
    :type contour_label_frequency: number, default: 2


    :param contour_shade: Turn shading "on"
    :type contour_shade: {"on", "off"}, default: "off"


    :param contour_shade_technique: Technique used for shading ("polygon_shading"/ "cell_shading"/ "marker")
    :type contour_shade_technique: {"polygon_shading", "grid_shading", "cell_shading", "marker"}, default: "polygon_shading"


    :param contour_shade_colour_method: Method of generating the colours of the bands in contour shading ("list"/"calculate"/advanced)
    :type contour_shade_colour_method: {"calculate", "list", "gradients", "palette"}, default: "calculate"


    :param contour_shade_method: Method used for shading
    :type contour_shade_method: {"area_fill", "dot", "hatch"}, default: "dot"


    :param contour_shade_cell_resolution: Number of cells per cm for CELL shading
    :type contour_shade_cell_resolution: number, default: 10


    :param contour_shade_cell_method: NMethod of determining the colour of a cell
    :type contour_shade_cell_method: {"nearest", "interpolate"}, default: "nearest"


    :param contour_grid_shading_position: "middle" : the point is in the midlle of the cell, "bottom_left" : the point is in the bottom left corner
    :type contour_grid_shading_position: {"middle", "bottom_left"}, default: "middle"


    :param contour_shade_colour_table: Colour table to be used with marker shading technique
    :type contour_shade_colour_table: str or list[str]


    :param contour_shade_height_table: Height table to be used with marker shading technique
    :type contour_shade_height_table: float or list[float]


    :param contour_shade_marker_table_type: "index": using ``contour_shade``_marker_table and  defining  the markers by "index", "name": using ``contour_shade``_marker_name_table and defining the symbols by their names
    :type contour_shade_marker_table_type: {"index", "name"}, default: "index"


    :param contour_shade_marker_table: Marker table to be used with marker shading technique
    :type contour_shade_marker_table: float or list[float]


    :param contour_shade_marker_name_table: Marker name table to be used with mareker shading technique
    :type contour_shade_marker_name_table: str or list[str]


    :param contour_shade_max_level_colour: Highest shading band colour
    :type contour_shade_max_level_colour: str, default: "blue"


    :param contour_shade_min_level_colour: Lowest shading band colour
    :type contour_shade_min_level_colour: str, default: "red"


    :param contour_shade_colour_direction: Direction of colour sequencing for shading
    :type contour_shade_colour_direction: {"clockwise", "anti_clockwise"}, default: "anti_clockwise"


    :param contour_shade_colour_list: List of colours to be used in contour shading.
    :type contour_shade_colour_list: str or list[str]


    :param contour_gradients_colour_list: Colour used at the stops : the gradeint will be calculated between 2 consecutive ones.
    :type contour_gradients_colour_list: str


    :param contour_gradients_waypoint_method: waypoints at the "left", "right", middle of the interval.
    :type contour_gradients_waypoint_method: {"both", "ignore", "left", "right"}, default: "both"


    :param contour_gradients_technique: Technique to apply to compute the gradients "rgb"/"hcl"/"hsl"
    :type contour_gradients_technique: {"rgb", "hcl", "hsl"}, default: "rgb"


    :param contour_gradients_technique_direction: Technique to apply to compute the gradients "clockwise"/anticlockwise
    :type contour_gradients_technique_direction: {"clockwise", "anti_clockwise", "shortest", "longest"}, default: "clockwise"


    :param contour_gradients_step_list: Number of steps to compute for each interval
    :type contour_gradients_step_list: float or list[float], default: 10


    :param contour_shade_palette_name: Colour used at the stops : the gradient will be calculated between 2 consecutive ones.
    :type contour_shade_palette_name: str


    :param contour_shade_palette_policy: What to do if the list of colours is smaller that the list of levels: "lastone"/"cycle"
    :type contour_shade_palette_policy: {"lastone", "cycle"}, default: "lastone"


    :param contour_shade_dot_size: Size of dot in shading pattern
    :type contour_shade_dot_size: number, default: 0.02


    :param contour_shade_max_level_density: Dots/square centimetre in highest shading band
    :type contour_shade_max_level_density: number, default: 50.0


    :param contour_shade_min_level_density: Dots/square centimetre in lowest shading band
    :type contour_shade_min_level_density: number, default: 1.0


    :param contour_shade_hatch_index: The hatching pattern(s) to use. 0 Provides an automatic sequence of patterns, other values set a constant pattern across all contour bands.
    :type contour_shade_hatch_index: number, default: 0


    :param contour_shade_hatch_thickness: Thickness of hatch lines
    :type contour_shade_hatch_thickness: int, default: 1


    :param contour_shade_hatch_density: Number of hatch lines per cm.
    :type contour_shade_hatch_density: number, default: 18.0


    :param contour_legend_text: Text to be used in legend
    :type contour_legend_text: str


    :param contour_method: Contouring method
    :type contour_method: {"automatic", "sample", "linear", "akima760", "akima474"}, default: "automatic"


    :param contour_akima_x_resolution: X resolution of Akima interpolationX resolution of Akima interpolation.
    :type contour_akima_x_resolution: number, default: 1.5


    :param contour_akima_y_resolution: Y resolution of Akima interpolationY resolution of Akima interpolation.
    :type contour_akima_y_resolution: number, default: 1.5


    :param contour_interpolation_floor: Any value below this floor will be forced  to the floor value.avoid the bubbles artificially created by the interpolation method
    :type contour_interpolation_floor: number, default: -1.0e21


    :param contour_interpolation_ceiling: any value above this ceiling will be forced  to the ceiling value.avoid the bubbles artificially created by the interpolation method
    :type contour_interpolation_ceiling: number, default: 1.0e21


    :param contour_internal_reduction_factor: Internal factor for contouring
    :type contour_internal_reduction_factor: number, default: 4.0


    :param contour_threads: NUmber of threads used to optimise the contouring  (possible "1", "4" or "9")
    :type contour_threads: {"1", "4", "9"}, default: "4"


    :param contour_hilo: Plot local maxima/minima
    :type contour_hilo: {"on", "off", "hi", "lo"}, default: "off"


    :param contour_hilo_type: Type of high/low ("text"/"number"/"both")
    :type contour_hilo_type: {"text", "number", "both"}, default: "text"


    :param contour_hi_text: Text to represent local maxima
    :type contour_hi_text: str, default: "h"


    :param contour_lo_text: Text to represent local minima
    :type contour_lo_text: str, default: "l"


    :param contour_hilo_blanking: Blank around highs and lows
    :type contour_hilo_blanking: {"on", "off"}, default: "off"


    :param contour_hilo_format: Format of HILO numbers (MAGICS Format/("(automatic)"))
    :type contour_hilo_format: str, default: "(automatic)"


    :param contour_hilo_window_size: Size of the window used to calculate the Hi/Lo
    :type contour_hilo_window_size: number, default: 3


    :param contour_hilo_suppress_radius: 
    :type contour_hilo_suppress_radius: number, default: 15.0


    :param contour_hilo_max_value: Local HiLo above specified value are not drawn
    :type contour_hilo_max_value: number, default: 1.0e+21


    :param contour_hilo_min_value: Local HiLo below specified value are not drawn
    :type contour_hilo_min_value: number, default: -1.0e+21


    :param contour_hi_max_value: Local HI above specified value are not drawn
    :type contour_hi_max_value: number, default: 1.0e+21


    :param contour_hi_min_value: Local HI below specified value are not drawn
    :type contour_hi_min_value: number, default: -1.0e+21


    :param contour_lo_max_value: Local Lo above specified value are not drawn
    :type contour_lo_max_value: number, default: 1.0e+21


    :param contour_lo_min_value: Local Lo below specified value are not drawn
    :type contour_lo_min_value: number, default: -1.0e+21


    :param contour_hilo_marker: Plot hilo marker ("on"/"off")
    :type contour_hilo_marker: {"on", "off"}, default: "off"


    :param contour_hilo_marker_height: Height of HighLow marker symbol
    :type contour_hilo_marker_height: number, default: 0.1


    :param contour_hilo_marker_index: Index of marker symbol
    :type contour_hilo_marker_index: number, default: 3


    :param contour_hilo_marker_colour: Colour of grid point markers
    :type contour_hilo_marker_colour: str, default: "red"


    :param contour_hilo_position_file_name: 
    :type contour_hilo_position_file_name: str


    :param contour_hilo_height: Height of local maxima/minima text or numbers
    :type contour_hilo_height: number, default: 0.4


    :param contour_hilo_quality: 
    :type contour_hilo_quality: {"high", "medium", "low"}, default: "low"


    :param contour_hi_colour: Colour of local maxima text or number
    :type contour_hi_colour: str, default: "blue"


    :param contour_lo_colour: Colour of local minima text or number
    :type contour_lo_colour: str, default: "blue"


    :param contour_grid_value_plot: Plot Grid point values
    :type contour_grid_value_plot: {"on", "off"}, default: "off"


    :param contour_grid_value_type: For Gaussian fields, plot "normal" (regular) values or "reduced" grid values.  ("normal"/"reduced"/"akima"). If "akima", the "akima" grid values will be plotted
    :type contour_grid_value_type: {"normal", "reduced", "akima"}, default: "normal"


    :param contour_grid_value_plot_type: ("value"/"marker"/"both")
    :type contour_grid_value_plot_type: {"value", "marker", "both"}, default: "value"


    :param contour_grid_value_min: The minimum value for which grid point values are to be plotted
    :type contour_grid_value_min: number, default: -1.0e+21


    :param contour_grid_value_max: The maximum value for which grid point values are to be plotted
    :type contour_grid_value_max: number, default: 1.0e+21


    :param contour_grid_value_lat_frequency: The grid point values in every Nth latitude row are plotted
    :type contour_grid_value_lat_frequency: number, default: 1


    :param contour_grid_value_lon_frequency: The grid point values in every Nth longitude column are plotted
    :type contour_grid_value_lon_frequency: number, default: 1


    :param contour_grid_value_height: Height of grid point values
    :type contour_grid_value_height: number, default: 0.25


    :param contour_grid_value_colour: Colour of grid point values
    :type contour_grid_value_colour: str, default: "blue"


    :param contour_grid_value_format: Format of grid point values
    :type contour_grid_value_format: str, default: "(automatic)"


    :param contour_grid_value_quality: ("low"/"medium"/"high")
    :type contour_grid_value_quality: {"high", "medium", "low"}, default: "low"


    :param contour_grid_value_marker_height: Height of grid point markersHeight of grid point markers
    :type contour_grid_value_marker_height: number, default: 0.25


    :param contour_grid_value_marker_colour: Colour of grid point markersColour of grid point markers
    :type contour_grid_value_marker_colour: str, default: "red"


    :param contour_grid_value_marker_qual: ("low"/MEDIUM/HIGH)Quality of the grid point marker
    :type contour_grid_value_marker_qual: str, default: "low"


    :param contour_grid_value_marker_index: Table number of marker index. See Appendix for Plotting AttributesTable number of marker index. See Appendix for Plotting Attributes
    :type contour_grid_value_marker_index: number, default: 3


    :param grib_scaling_of_retrieved_fields: Toggles the scaling of the retrieved fields "on" / "off". Fields which are retrieved from MARS or derived from other fields are in SI units. If this parameter is "on" , MAGICS will perform a unit conversion (scaling) "on" the retrieved fields that it plots, converting from these SI units to units of customary meteorological usage - e.g. Pressure from Pa to hPa/mb, Temperature from K to °C.Certain parameters will be scaled into more user-friendly units if the data has not been manipulated
    :type grib_scaling_of_retrieved_fields: {"on", "off"}, default: "on"


    :param grib_scaling_of_derived_fields: Toggles the scaling of the derived fields "on" / "off" . Any field you derive is in SI units, so set this parameter to "on" to convert to meteorological style units. E.g. :

         * If you retrieve two temperature fields, they are plotted in °C . If you derive a mean temperature from them, it will be plotted in K if you do not scale the derived field.
         * Precipitation fields are cumulative fields plotted in mm - if you subtract two consecutive ones to obtain the precipitation for the time step between them, you will plot a field in m if you do not scale the derived field.Certain parameters will be scaled into more user-friendly units if the data has been manipulated
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


    :rtype: None


.. minigallery:: metview.mcont
    :add-heading:

