
mcont
=========================

.. container::
    
    .. container:: leftside

        .. image:: /_static/MCONT.png
           :width: 48px

    .. container:: rightside

        This icon represents the `Contouring <https://confluence.ecmwf.int/display/METV/Contouring>`_ icon in Metview's user interface.


.. py:function:: mcont(**kwargs)
  
    Description comes here!


    :param contour_automatic_setting: Turn the automatic setting of contouring attributes. The possible values:

        * off
        * ecmwf
        * style_name
        The default is: off.
    :type contour_automatic_setting: str


    :param contour_style_name: Use of a predeined setting
    :type contour_style_name: str


    :param legend: Turn legend on or off. The possible values:

        * on
        * off
        The default is: off.
    :type legend: str


    :param contour: Turn contouring on or off. The possible values:

        * on
        * off
        The default is: on.
    :type contour: str


    :param contour_line_style: Style of contour line. The possible values:

        * solid
        * dash
        * dot
        * chain_dot
        * chain_dash
        The default is: solid.
    :type contour_line_style: str


    :param contour_line_thickness: Thickness of contour line. The default is: 1.
    :type contour_line_thickness: int


    :param contour_line_colour_rainbow: if On, rainbow colouring method will be used. The possible values:

        * on
        * off
        The default is: off.
    :type contour_line_colour_rainbow: str


    :param contour_line_colour: Colour of contour line. The possible values:

        * background
        The default is: blue.
    :type contour_line_colour: str


    :param contour_line_colour_rainbow_method: Method of generating the colours for isoline. The possible values:

        * calculate
        * list
        The default is: calculate.
    :type contour_line_colour_rainbow_method: str


    :param contour_line_colour_rainbow_max_level_colour: Colour to be used for the max level. The possible values:

        * background
        The default is: blue.
    :type contour_line_colour_rainbow_max_level_colour: str


    :param contour_line_colour_rainbow_min_level_colour: Colour to be used for the mainlevel. The possible values:

        * background
        The default is: red.
    :type contour_line_colour_rainbow_min_level_colour: str


    :param contour_line_colour_rainbow_direction: Direction of colour sequencing for colouring. The possible values:

        * clockwise
        * anti-clockwise
        The default is: anti-clockwise.
    :type contour_line_colour_rainbow_direction: str


    :param contour_line_colour_rainbow_colour_list: List of colours to be used in rainbow isolines
    :type contour_line_colour_rainbow_colour_list: str or list[str]


    :param contour_line_colour_rainbow_colour_list_policy: What to do if the list of colours is smaller that the list of contour: lastone/cycle. The possible values:

        * lastone
        * cycle
        The default is: lastone.
    :type contour_line_colour_rainbow_colour_list_policy: str


    :param contour_line_thickness_rainbow_list: List of thickness to used when rainbow method is on
    :type contour_line_thickness_rainbow_list: float or list[float]


    :param contour_line_thickness_rainbow_list_policy: What to do if the list of thickness is smaller that the list of contour: lastone/cycle. The possible values:

        * lastone
        * cycle
        The default is: lastone.
    :type contour_line_thickness_rainbow_list_policy: str


    :param contour_line_style_rainbow_list: List of line style to used when rainbow method is on
    :type contour_line_style_rainbow_list: str or list[str]


    :param contour_line_style_rainbow_list_policy: What to do if the list of line styles is smaller that the list of contour: lastone/cycle. The possible values:

        * lastone
        * cycle
        The default is: lastone.
    :type contour_line_style_rainbow_list_policy: str


    :param contour_highlight: Plot contour highlights (ON/OFF). The possible values:

        * on
        * off
        The default is: on.
    :type contour_highlight: str


    :param contour_highlight_style: Style of highlighting (SOLID/ DASH/ DOT/ CHAIN_DASH/ CHAIN_DOT). The possible values:

        * solid
        * dash
        * dot
        * chain_dot
        * chain_dash
        The default is: solid.
    :type contour_highlight_style: str


    :param contour_reference_level: Contour level referenceContour level from which contour interval is calculatedContour level from which contour interval is calculated. The default is: 0.0.
    :type contour_reference_level: number


    :param contour_highlight_colour: Colour of highlight line. The possible values:

        * background
        The default is: blue.
    :type contour_highlight_colour: str


    :param contour_highlight_thickness: Thickness of highlight line. The default is: 3.
    :type contour_highlight_thickness: int


    :param contour_highlight_frequency: Frequency of highlight line. The default is: 4.
    :type contour_highlight_frequency: number


    :param contour_level_selection_type: count: calculate a reasonable  contour interval taking into account the min/max and the requested number of isolines.        interval: regularly spaced intervals using the reference_level as base.        level_list: uses the given list of levels. The possible values:

        * count
        * interval
        * level_list
        The default is: count.
    :type contour_level_selection_type: str


    :param contour_max_level: Highest level for contours to be drawn. The default is: 1.0e+21.
    :type contour_max_level: number


    :param contour_min_level: Lowest level for contours to be drawn. The default is: -1.0e+21.
    :type contour_min_level: number


    :param contour_shade_max_level: Highest level for contours to be shadedMaximum level for which shading is required. The default is: 1.0e+21.
    :type contour_shade_max_level: number


    :param contour_shade_min_level: Lowest level for contours to be shadedMinimum level for which shading is required. The default is: -1.0e+21.
    :type contour_shade_min_level: number


    :param contour_level_list: List of contour levels to be plotted
    :type contour_level_list: float or list[float]


    :param contour_interval: Interval in data units between two contour lines. The default is: 8.0.
    :type contour_interval: number


    :param contour_level_count: Count or number of levels to be plotted. Magics will try to find "nice levels",         this means that the number of levels could be slightly different from the asked number of levels. The default is: 10.
    :type contour_level_count: number


    :param contour_level_tolerance: Tolerance: Do not use nice levels if the number of levels is really to different [count +/- tolerance]. The default is: 2.
    :type contour_level_tolerance: number


    :param contour_label: Plot labels on contour lines. The possible values:

        * on
        * off
        The default is: on.
    :type contour_label: str


    :param contour_label_type: Type of label (text/number/both. The default is: number.
    :type contour_label_type: str


    :param contour_label_text: Text for labels
    :type contour_label_text: str


    :param contour_label_height: Height of contour labels. The default is: 0.3.
    :type contour_label_height: number


    :param contour_label_format: Format of contour labels (MAGICS Format/(AUTOMATIC)). The default is: (automatic).
    :type contour_label_format: str


    :param contour_label_blanking: Label Blanking. The possible values:

        * on
        * off
        The default is: on.
    :type contour_label_blanking: str


    :param contour_label_font: Name of the font. The possible values:

        * arial
        * courier
        * helvetica
        * times
        * serif
        * sansserif
        * symbol
        The default is: sansserif.
    :type contour_label_font: str


    :param contour_label_font_style: Style of the font normal/bold/italic. The possible values:

        * normal
        * bold
        * italic
        * bolditalic
        The default is: normal.
    :type contour_label_font_style: str


    :param contour_label_colour: Colour of contour labels. The possible values:

        * background
        * contour_line_colour
        The default is: contour_line_colour.
    :type contour_label_colour: str


    :param contour_label_frequency: Every Nth contour line is labelled. The default is: 2.
    :type contour_label_frequency: number


    :param contour_shade: Turn shading on. The possible values:

        * on
        * off
        The default is: off.
    :type contour_shade: str


    :param contour_shade_technique: Technique used for shading (POLYGON_SHADING/ CELL_SHADING/ MARKER). The possible values:

        * polygon_shading
        * grid_shading
        * cell_shading
        * marker
        The default is: polygon_shading.
    :type contour_shade_technique: str


    :param contour_shade_colour_method: Method of generating the colours of the bands in contour shading (list/calculate/advanced). The possible values:

        * calculate
        * list
        * gradients
        * palette
        The default is: calculate.
    :type contour_shade_colour_method: str


    :param contour_shade_method: Method used for shading. The possible values:

        * area_fill
        * dot
        * hatch
        The default is: dot.
    :type contour_shade_method: str


    :param contour_shade_cell_resolution: Number of cells per cm for CELL shading. The default is: 10.
    :type contour_shade_cell_resolution: number


    :param contour_shade_cell_method: NMethod of determining the colour of a cell. The possible values:

        * nearest
        * interpolate
        The default is: nearest.
    :type contour_shade_cell_method: str


    :param contour_grid_shading_position: Middle : the point is in the midlle of the cell, bottom_left : the point is in the bottom left corner. The possible values:

        * middle
        * bottom_left
        The default is: middle.
    :type contour_grid_shading_position: str


    :param contour_shade_colour_table: Colour table to be used with marker shading technique
    :type contour_shade_colour_table: str or list[str]


    :param contour_shade_height_table: Height table to be used with marker shading technique
    :type contour_shade_height_table: float or list[float]


    :param contour_shade_marker_table_type: index: using ``contour_shade``_marker_table and  defining  the markers by index, name: using ``contour_shade``_marker_name_table and defining the symbols by their names. The possible values:

        * index
        * name
        The default is: index.
    :type contour_shade_marker_table_type: str


    :param contour_shade_marker_table: Marker table to be used with marker shading technique
    :type contour_shade_marker_table: float or list[float]


    :param contour_shade_marker_name_table: Marker name table to be used with mareker shading technique
    :type contour_shade_marker_name_table: str or list[str]


    :param contour_shade_max_level_colour: Highest shading band colour. The possible values:

        * background
        The default is: blue.
    :type contour_shade_max_level_colour: str


    :param contour_shade_min_level_colour: Lowest shading band colour. The possible values:

        * background
        The default is: red.
    :type contour_shade_min_level_colour: str


    :param contour_shade_colour_direction: Direction of colour sequencing for shading. The possible values:

        * clockwise
        * anti_clockwise
        The default is: anti_clockwise.
    :type contour_shade_colour_direction: str


    :param contour_shade_colour_list: List of colours to be used in contour shading.
    :type contour_shade_colour_list: str or list[str]


    :param contour_gradients_colour_list: Colour used at the stops : the gradeint will be calculated between 2 consecutive ones.
    :type contour_gradients_colour_list: str


    :param contour_gradients_waypoint_method: waypoints at the left, right, middle of the interval. The possible values:

        * both
        * ignore
        * left
        * right
        The default is: both.
    :type contour_gradients_waypoint_method: str


    :param contour_gradients_technique: Technique to apply to compute the gradients rgb/hcl/hsl. The possible values:

        * rgb
        * hcl
        * hsl
        The default is: rgb.
    :type contour_gradients_technique: str


    :param contour_gradients_technique_direction: Technique to apply to compute the gradients clockwise/anticlockwise. The possible values:

        * clockwise
        * anti_clockwise
        * shortest
        * longest
        The default is: clockwise.
    :type contour_gradients_technique_direction: str


    :param contour_gradients_step_list: Number of steps to compute for each interval. The default is: 10.
    :type contour_gradients_step_list: float or list[float]


    :param contour_shade_palette_name: Colour used at the stops : the gradient will be calculated between 2 consecutive ones.
    :type contour_shade_palette_name: str


    :param contour_shade_palette_policy: What to do if the list of colours is smaller that the list of levels: lastone/cycle. The possible values:

        * lastone
        * cycle
        The default is: lastone.
    :type contour_shade_palette_policy: str


    :param contour_shade_dot_size: Size of dot in shading pattern. The default is: 0.02.
    :type contour_shade_dot_size: number


    :param contour_shade_max_level_density: Dots/square centimetre in highest shading band. The default is: 50.0.
    :type contour_shade_max_level_density: number


    :param contour_shade_min_level_density: Dots/square centimetre in lowest shading band. The default is: 1.0.
    :type contour_shade_min_level_density: number


    :param contour_shade_hatch_index: The hatching pattern(s) to use. 0 Provides an automatic sequence of patterns, other values set a constant pattern across all contour bands. The default is: 0.
    :type contour_shade_hatch_index: number


    :param contour_shade_hatch_thickness: Thickness of hatch lines. The default is: 1.
    :type contour_shade_hatch_thickness: int


    :param contour_shade_hatch_density: Number of hatch lines per cm. The default is: 18.0.
    :type contour_shade_hatch_density: number


    :param contour_legend_text: Text to be used in legend
    :type contour_legend_text: str


    :param contour_method: Contouring method. The possible values:

        * automatic
        * sample
        * linear
        * akima760
        * akima474
        The default is: automatic.
    :type contour_method: str


    :param contour_akima_x_resolution: X resolution of Akima interpolationX resolution of Akima interpolation. The default is: 1.5.
    :type contour_akima_x_resolution: number


    :param contour_akima_y_resolution: Y resolution of Akima interpolationY resolution of Akima interpolation. The default is: 1.5.
    :type contour_akima_y_resolution: number


    :param contour_interpolation_floor: Any value below this floor will be forced  to the floor value.avoid the bubbles artificially created by the interpolation method. The default is: -1.0e21.
    :type contour_interpolation_floor: number


    :param contour_interpolation_ceiling: any value above this ceiling will be forced  to the ceiling value.avoid the bubbles artificially created by the interpolation method. The default is: 1.0e21.
    :type contour_interpolation_ceiling: number


    :param contour_internal_reduction_factor: Internal factor for contouring. The default is: 4.0.
    :type contour_internal_reduction_factor: number


    :param contour_threads: NUmber of threads used to optimise the contouring  (possible 1, 4 or 9). The possible values:

        * 1
        * 4
        * 9
        The default is: 4.
    :type contour_threads: str


    :param contour_hilo: Plot local maxima/minima. The possible values:

        * on
        * off
        * hi
        * lo
        The default is: off.
    :type contour_hilo: str


    :param contour_hilo_type: Type of high/low (TEXT/NUMBER/BOTH). The possible values:

        * text
        * number
        * both
        The default is: text.
    :type contour_hilo_type: str


    :param contour_hi_text: Text to represent local maxima. The default is: h.
    :type contour_hi_text: str


    :param contour_lo_text: Text to represent local minima. The default is: l.
    :type contour_lo_text: str


    :param contour_hilo_blanking: Blank around highs and lows. The possible values:

        * on
        * off
        The default is: off.
    :type contour_hilo_blanking: str


    :param contour_hilo_format: Format of HILO numbers (MAGICS Format/(AUTOMATIC)). The default is: (automatic).
    :type contour_hilo_format: str


    :param contour_hilo_window_size: Size of the window used to calculate the Hi/Lo. The default is: 3.
    :type contour_hilo_window_size: number


    :param contour_hilo_suppress_radius: 
    :type contour_hilo_suppress_radius: number


    :param contour_hilo_max_value: Local HiLo above specified value are not drawn. The default is: 1.0e+21.
    :type contour_hilo_max_value: number


    :param contour_hilo_min_value: Local HiLo below specified value are not drawn. The default is: -1.0e+21.
    :type contour_hilo_min_value: number


    :param contour_hi_max_value: Local HI above specified value are not drawn. The default is: 1.0e+21.
    :type contour_hi_max_value: number


    :param contour_hi_min_value: Local HI below specified value are not drawn. The default is: -1.0e+21.
    :type contour_hi_min_value: number


    :param contour_lo_max_value: Local Lo above specified value are not drawn. The default is: 1.0e+21.
    :type contour_lo_max_value: number


    :param contour_lo_min_value: Local Lo below specified value are not drawn. The default is: -1.0e+21.
    :type contour_lo_min_value: number


    :param contour_hilo_marker: Plot hilo marker (ON/OFF). The possible values:

        * on
        * off
        The default is: off.
    :type contour_hilo_marker: str


    :param contour_hilo_marker_height: Height of HighLow marker symbol. The default is: 0.1.
    :type contour_hilo_marker_height: number


    :param contour_hilo_marker_index: Index of marker symbol. The default is: 3.
    :type contour_hilo_marker_index: number


    :param contour_hilo_marker_colour: Colour of grid point markers. The possible values:

        * background
        The default is: red.
    :type contour_hilo_marker_colour: str


    :param contour_hilo_position_file_name: 
    :type contour_hilo_position_file_name: str


    :param contour_hilo_height: Height of local maxima/minima text or numbers. The default is: 0.4.
    :type contour_hilo_height: number


    :param contour_hilo_quality: 
    :type contour_hilo_quality: str


    :param contour_hi_colour: Colour of local maxima text or number. The possible values:

        * background
        The default is: blue.
    :type contour_hi_colour: str


    :param contour_lo_colour: Colour of local minima text or number. The possible values:

        * background
        The default is: blue.
    :type contour_lo_colour: str


    :param contour_grid_value_plot: Plot Grid point values. The possible values:

        * on
        * off
        The default is: off.
    :type contour_grid_value_plot: str


    :param contour_grid_value_type: For Gaussian fields, plot normal (regular) values or reduced grid values.  (NORMAL/REDUCED/akima). If akima, the akima grid values will be plotted. The possible values:

        * normal
        * reduced
        * akima
        The default is: normal.
    :type contour_grid_value_type: str


    :param contour_grid_value_plot_type: (VALUE/MARKER/BOTH). The possible values:

        * value
        * marker
        * both
        The default is: value.
    :type contour_grid_value_plot_type: str


    :param contour_grid_value_min: The minimum value for which grid point values are to be plotted. The default is: -1.0e+21.
    :type contour_grid_value_min: number


    :param contour_grid_value_max: The maximum value for which grid point values are to be plotted. The default is: 1.0e+21.
    :type contour_grid_value_max: number


    :param contour_grid_value_lat_frequency: The grid point values in every Nth latitude row are plotted. The default is: 1.
    :type contour_grid_value_lat_frequency: number


    :param contour_grid_value_lon_frequency: The grid point values in every Nth longitude column are plotted. The default is: 1.
    :type contour_grid_value_lon_frequency: number


    :param contour_grid_value_height: Height of grid point values. The default is: 0.25.
    :type contour_grid_value_height: number


    :param contour_grid_value_colour: Colour of grid point values. The possible values:

        * background
        The default is: blue.
    :type contour_grid_value_colour: str


    :param contour_grid_value_format: Format of grid point values. The default is: (automatic).
    :type contour_grid_value_format: str


    :param contour_grid_value_quality: (LOW/MEDIUM/HIGH). The possible values:

        * high
        * medium
        * low
        The default is: low.
    :type contour_grid_value_quality: str


    :param contour_grid_value_marker_height: Height of grid point markersHeight of grid point markers. The default is: 0.25.
    :type contour_grid_value_marker_height: number


    :param contour_grid_value_marker_colour: Colour of grid point markersColour of grid point markers. The possible values:

        * background
        The default is: red.
    :type contour_grid_value_marker_colour: str


    :param contour_grid_value_marker_qual: (LOW/MEDIUM/HIGH)Quality of the grid point marker. The default is: low.
    :type contour_grid_value_marker_qual: str


    :param contour_grid_value_marker_index: Table number of marker index. See Appendix for Plotting AttributesTable number of marker index. See Appendix for Plotting Attributes. The default is: 3.
    :type contour_grid_value_marker_index: number


    :param grib_scaling_of_retrieved_fields: Toggles the scaling of the retrieved fields On / Off. Fields which are retrieved from MARS or derived from other fields are in SI units. If this parameter is On , MAGICS will perform a unit conversion (scaling) on the retrieved fields that it plots, converting from these SI units to units of customary meteorological usage - e.g. Pressure from Pa to hPa/mb, Temperature from K to °C.Certain parameters will be scaled into more user-friendly units if the data has not been manipulated. The possible values:

        * on
        * off
        The default is: on.
    :type grib_scaling_of_retrieved_fields: str


    :param grib_scaling_of_derived_fields: Toggles the scaling of the derived fields On / Off . Any field you derive is in SI units, so set this parameter to On to convert to meteorological style units. E.g. :

         * If you retrieve two temperature fields, they are plotted in °C . If you derive a mean temperature from them, it will be plotted in K if you do not scale the derived field.
         * Precipitation fields are cumulative fields plotted in mm - if you subtract two consecutive ones to obtain the precipitation for the time step between them, you will plot a field in m if you do not scale the derived field.Certain parameters will be scaled into more user-friendly units if the data has been manipulated. The possible values:

        * on
        * off
        The default is: off.
    :type grib_scaling_of_derived_fields: str


    :param grib_interpolation_method: 
    :type grib_interpolation_method: str


    :param grib_interpolation_method_missing_fill_count: 
    :type grib_interpolation_method_missing_fill_count: number


    :param grib_interpolation_regular_resolution: Sets the plotting resolution, in degrees, of GRIB fields encoded in space_view projection. The default is 0.1.
    :type grib_interpolation_regular_resolution: number


    :param contour_sample_x_interval: 
    :type contour_sample_x_interval: number


    :param contour_sample_y_interval: 
    :type contour_sample_y_interval: number


    :rtype: None


.. minigallery:: metview.mcont
    :add-heading:

