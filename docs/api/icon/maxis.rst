
maxis
=========================

.. container::
    
    .. container:: leftside

        .. image:: /_static/MAXIS.png
           :width: 48px

    .. container:: rightside

        This function performs the same task as the `Axis Plotting <https://confluence.ecmwf.int/display/METV/Axis+Plotting>`_ icon in Metview’s user interface. It accepts its parameters as keyword arguments, described below.


.. py:function:: maxis(**kwargs)
  
    Description comes here!


    :param axis_orientation: Orientation of axis
    :type axis_orientation: {"horizontal", "vertical"}, default: "horizontal"


    :param axis_position: Position of the axes
    :type axis_position: {"bottom", "top", "left", "right", "automatic"}, default: "automatic"


    :param axis_type: Method to position ticks on an axis
    :type axis_type: {"regular", "position_list", "logarithmic", "date", "geoline"}, default: "regular"


    :param axis_line: Plot the axis line
    :type axis_line: {"on", "off"}, default: "on"


    :param axis_line_colour: Colour of axis line
    :type axis_line_colour: str, default: "automatic"


    :param axis_line_style: Line Style of axis line
    :type axis_line_style: {"solid", "dash", "dot", "chain_dot", "chain_dash"}, default: "solid"


    :param axis_line_thickness: Thickness of axis line
    :type axis_line_thickness: int, default: 2


    :param axis_grid: Plot axis grid lines
    :type axis_grid: {"on", "off"}, default: "off"


    :param axis_grid_colour: Colour of grid lines
    :type axis_grid_colour: str, default: "black"


    :param axis_grid_line_style: Line style of grid
    :type axis_grid_line_style: {"solid", "dash", "dot", "chain_dot", "chain_dash"}, default: "solid"


    :param axis_grid_thickness: Thickness of grid lines
    :type axis_grid_thickness: int, default: 1


    :param axis_grid_reference_level: value to be used as reference for the grid
    :type axis_grid_reference_level: number, default: 1.0e21


    :param axis_grid_reference_colour: Colour of the reference  grid line
    :type axis_grid_reference_colour: str, default: "automatic"


    :param axis_grid_reference_line_style: Line style of the reference  grid line
    :type axis_grid_reference_line_style: {"solid", "dash", "dot", "chain_dot", "chain_dash"}, default: "solid"


    :param axis_grid_reference_thickness: Thickness of the reference grid line
    :type axis_grid_reference_thickness: int, default: 2


    :param axis_title: Plot axis title
    :type axis_title: {"on", "off"}, default: "on"


    :param axis_title_text: The axis title text
    :type axis_title_text: str


    :param axis_title_orientation: Orientation of the axis title
    :type axis_title_orientation: {"horizontal", "vertical", "parallel"}, default: "parallel"


    :param axis_title_colour: Colour of axis title
    :type axis_title_colour: str, default: "automatic"


    :param axis_title_height: Height of axis title
    :type axis_title_height: number, default: 0.4


    :param axis_title_font: Font of axis title
    :type axis_title_font: {"arial", "courier", "helvetica", "times", "serif", "sansserif", "symbol"}, default: "sansserif"


    :param axis_title_font_style: Font style of axis title
    :type axis_title_font_style: {"normal", "bold", "italic", "bolditalic"}, default: "normal"


    :param axis_tick: Plot ticks
    :type axis_tick: {"on", "off"}, default: "on"


    :param axis_tick_interval: Interval between ticks in user units
    :type axis_tick_interval: number, default: 1.0e21


    :param axis_tick_position_list: Array specifying the positions of ticks (in user coordinates!)
    :type axis_tick_position_list: float or list[float]


    :param axis_tick_position: Tick position, if "in" the ticks will positioned inside the frame.
    :type axis_tick_position: {"out", "in"}, default: "out"


    :param axis_tick_colour: Colour of ticks
    :type axis_tick_colour: str, default: "automatic"


    :param axis_tick_size: Size of ticks
    :type axis_tick_size: number, default: 0.175


    :param axis_tick_thickness: Thickness of tick marks
    :type axis_tick_thickness: int, default: 2


    :param axis_tick_label: Plot tick labels ("on"/"off")
    :type axis_tick_label: {"on", "off"}, default: "on"


    :param axis_tick_label_type: Type of tick labels required
    :type axis_tick_label_type: {"number", "label_list", "latitude", "longitude"}, default: "number"


    :param axis_tick_label_frequency: Label every nth tick mark
    :type axis_tick_label_frequency: number, default: 1


    :param axis_tick_label_first: Turn "off" first (left or bottom) tick label
    :type axis_tick_label_first: {"on", "off"}, default: "on"


    :param axis_tick_label_last: Turn "off" last (right or top) tick label
    :type axis_tick_label_last: {"on", "off"}, default: "on"


    :param axis_tick_label_position: Position labels on or between ticks
    :type axis_tick_label_position: {"on_tick", "inter_tick"}, default: "on_tick"


    :param axis_tick_label_orientation: Orientation of the tick labels
    :type axis_tick_label_orientation: {"horizontal", "vertical", "parallel"}, default: "horizontal"


    :param axis_tick_label_font: Font name - please make sure this font is installed!
    :type axis_tick_label_font: {"arial", "courier", "helvetica", "times", "serif", "sansserif", "symbol"}, default: "sansserif"


    :param axis_tick_label_font_style: Font style. Set this to an empty string in order to remove all styling.
    :type axis_tick_label_font_style: {"normal", "bold", "italic", "bolditalic"}, default: "normal"


    :param axis_tick_label_colour: Colour of tick labels
    :type axis_tick_label_colour: str, default: "automatic"


    :param axis_tick_label_height: Height of tick labels
    :type axis_tick_label_height: number, default: 0.3


    :param axis_tick_label_list: Array for passing user defined tick labels
    :type axis_tick_label_list: str or list[str]


    :param axis_tick_label_format: Format of tick label values
    :type axis_tick_label_format: str, default: "(automatic)"


    :param axis_minor_tick: Plot minor ticks ("on"/"off")
    :type axis_minor_tick: {"on", "off"}, default: "off"


    :param axis_minor_tick_count: Number of minor tick marks between two ticks
    :type axis_minor_tick_count: number, default: 2


    :param axis_minor_tick_colour: Colour of minor ticks
    :type axis_minor_tick_colour: str, default: "automatic"


    :param axis_minor_tick_thickness: Thickness of minor ticks
    :type axis_minor_tick_thickness: int, default: 1


    :param axis_minor_grid: 
    :type axis_minor_grid: {"on", "off"}, default: "off"


    :param axis_minor_grid_colour: Colour of grid lines
    :type axis_minor_grid_colour: str, default: "black"


    :param axis_minor_grid_line_style: Line style of grid
    :type axis_minor_grid_line_style: {"solid", "dash", "dot", "chain_dot", "chain_dash"}, default: "solid"


    :param axis_minor_grid_thickness: Thickness of grid lines
    :type axis_minor_grid_thickness: int, default: 1


    :param axis_tip_title: Plot ticks ("on"/"off")
    :type axis_tip_title: {"on", "off"}, default: "off"


    :param axis_tip_title_text: Text to show in the tip
    :type axis_tip_title_text: str


    :param axis_tip_title_colour: Coloour of the tip
    :type axis_tip_title_colour: str, default: "automatic"


    :param axis_tip_title_height: font size of the tip
    :type axis_tip_title_height: number, default: 0.4


    :param axis_tip_title_quality: Quality of the font
    :type axis_tip_title_quality: {"high", "medium", "low"}, default: "medium"


    :param axis_date_type: Select the type of date axis.
    :type axis_date_type: {"automatic", "years", "months", "days", "hours", "monthly", "climate"}, default: "days"


    :param axis_years_label: controls the labeling of the years
    :type axis_years_label: {"on", "off"}, default: "on"


    :param axis_years_label_colour: Label colour for 'YEARS
    :type axis_years_label_colour: str, default: "automatic"


    :param axis_years_label_quality: 
    :type axis_years_label_quality: {"high", "medium", "low"}, default: "medium"


    :param axis_years_label_height: Label height for 'YEARS
    :type axis_years_label_height: number, default: 0.2


    :param axis_months_label: controls the labeling of the months
    :type axis_months_label: {"on", "off"}, default: "on"


    :param axis_months_label_composition: Number of letters per month to plot
    :type axis_months_label_composition: {"one", "two", "three"}, default: "three"


    :param axis_months_label_colour: Label colour for months
    :type axis_months_label_colour: str, default: "automatic"


    :param axis_months_label_quality: 
    :type axis_months_label_quality: {"high", "medium", "low"}, default: "medium"


    :param axis_months_label_height: Label height for months
    :type axis_months_label_height: number, default: 0.2


    :param axis_days_label: controls the labeling of the hours
    :type axis_days_label: {"day", "number", "both", "off"}, default: "both"


    :param axis_days_label_composition: Number of letters per days to plot
    :type axis_days_label_composition: {"one", "three", "full"}, default: "three"


    :param axis_days_label_position: for short time series : if 12 the label will be at 12h .
    :type axis_days_label_position: number, default: 12


    :param axis_days_label_colour: Label colour for days
    :type axis_days_label_colour: str, default: "black"


    :param axis_days_sunday_label_colour: Label colour for sundays
    :type axis_days_sunday_label_colour: str, default: "red"


    :param axis_days_label_quality: 
    :type axis_days_label_quality: {"high", "medium", "low"}, default: "medium"


    :param axis_days_label_height: Label height for  days
    :type axis_days_label_height: number, default: 0.2


    :param axis_hours_label: controls the labeling of the hours
    :type axis_hours_label: {"on", "off"}, default: "off"


    :param axis_hours_label_colour: Label quality for hours
    :type axis_hours_label_colour: str, default: "black"


    :param axis_hours_label_quality: 
    :type axis_hours_label_quality: {"high", "medium", "low"}, default: "medium"


    :param axis_hours_label_height: Label height for  hours
    :type axis_hours_label_height: number, default: 0.2


    :rtype: None


.. minigallery:: metview.maxis
    :add-heading:

