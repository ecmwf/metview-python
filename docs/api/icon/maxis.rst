
maxis
=========================

.. container::
    
    .. container:: leftside

        .. image:: /_static/MAXIS.png
           :width: 48px

    .. container:: rightside

		This is the visual definition responsible for specifying how the axes in non-geographic views (e.g. :func:`cartesianview`), are displayed. Note that :func:`maxis` does not define the projection or the coordinate range - this is done in the view.


		.. note:: This function performs the same task as the `Axis Plotting <https://confluence.ecmwf.int/display/METV/Axis+Plotting>`_ icon in Metview’s user interface. It accepts its parameters as keyword arguments, described below.


.. py:function:: maxis(**kwargs)
  
    Specifies the axis properties for non-geographic views.


    :param axis_orientation: Orientation of the axis.
    :type axis_orientation: {"horizontal", "vertical"}, default: "horizontal"

    :param axis_position: Position of the axis.
    :type axis_position: {"bottom", "top", "left", "right", "automatic"}, default: "automatic"

    :param axis_type: Method to position ticks on the axis.
    :type axis_type: {"regular", "position_list", "logarithmic", "date", "geoline"}, default: "regular"

    :param axis_line: Plots the axis line.
    :type axis_line: {"on", "off"}, default: "on"

    :param axis_line_colour: Colour of the axis line.
    :type axis_line_colour: str, default: "automatic"

    :param axis_line_style: Line style of the axis line.
    :type axis_line_style: {"solid", "dash", "dot", "chain_dot", "chain_dash"}, default: "solid"

    :param axis_line_thickness: Thickness of the axis line.
    :type axis_line_thickness: int, default: 2

    :param axis_grid: Plots the axis grid lines.
    :type axis_grid: {"on", "off"}, default: "off"

    :param axis_grid_colour: Colour of the grid lines.
    :type axis_grid_colour: str, default: "black"

    :param axis_grid_line_style: Line style of the grid lines.
    :type axis_grid_line_style: {"solid", "dash", "dot", "chain_dot", "chain_dash"}, default: "solid"

    :param axis_grid_thickness: Thickness of the grid lines.
    :type axis_grid_thickness: int, default: 1

    :param axis_grid_reference_level: Reference value for the grid.
    :type axis_grid_reference_level: number, default: 1.0e21

    :param axis_grid_reference_colour: Colour of the reference grid line.
    :type axis_grid_reference_colour: str, default: "automatic"

    :param axis_grid_reference_line_style: Line style of the reference grid line.
    :type axis_grid_reference_line_style: {"solid", "dash", "dot", "chain_dot", "chain_dash"}, default: "solid"

    :param axis_grid_reference_thickness: Thickness of the reference grid line.
    :type axis_grid_reference_thickness: int, default: 2

    :param axis_title: Plots the axis title.
    :type axis_title: {"on", "off"}, default: "on"

    :param axis_title_text: The axis title text.
    :type axis_title_text: str

    :param axis_title_orientation: Orientation of the axis title.
    :type axis_title_orientation: {"horizontal", "vertical", "parallel"}, default: "parallel"

    :param axis_title_colour: Colour of the axis title.
    :type axis_title_colour: str, default: "automatic"

    :param axis_title_height: Height of the axis title.
    :type axis_title_height: number, default: 0.4

    :param axis_title_font: Font name of the axis title.
    :type axis_title_font: {"arial", "courier", "helvetica", "times", "serif", "sansserif", "symbol"}, default: "sansserif"

    :param axis_title_font_style: Font style of the axis title.
    :type axis_title_font_style: {"normal", "bold", "italic", "bolditalic"}, default: "normal"

    :param axis_tick: Plots ticks.
    :type axis_tick: {"on", "off"}, default: "on"

    :param axis_tick_interval: Interval between ticks in user units.
    :type axis_tick_interval: number, default: 1.0e21

    :param axis_tick_position_list: List specifying the positions of ticks (in user coordinates!).
    :type axis_tick_position_list: float or list[float]

    :param axis_tick_position: Tick position, if it is "in" the ticks will positioned inside the frame.
    :type axis_tick_position: {"out", "in"}, default: "out"

    :param axis_tick_colour: Colour of the ticks.
    :type axis_tick_colour: str, default: "automatic"

    :param axis_tick_size: Size of the ticks.
    :type axis_tick_size: number, default: 0.175

    :param axis_tick_thickness: Thickness of the ticks.
    :type axis_tick_thickness: int, default: 2

    :param axis_tick_label: Plots tick labels.
    :type axis_tick_label: {"on", "off"}, default: "on"

    :param axis_tick_label_type: Type of the tick labels required.
    :type axis_tick_label_type: {"number", "label_list", "latitude", "longitude"}, default: "number"

    :param axis_tick_label_frequency: Tick label frequency.
    :type axis_tick_label_frequency: number, default: 1

    :param axis_tick_label_first: Turn off the first (left or bottom) tick label.
    :type axis_tick_label_first: {"on", "off"}, default: "on"

    :param axis_tick_label_last: Turn off the last (right or top) tick label.
    :type axis_tick_label_last: {"on", "off"}, default: "on"

    :param axis_tick_label_position: Positions labels on or between ticks.
    :type axis_tick_label_position: {"on_tick", "inter_tick"}, default: "on_tick"

    :param axis_tick_label_orientation: Orientation of the tick labels.
    :type axis_tick_label_orientation: {"horizontal", "vertical", "parallel"}, default: "horizontal"

    :param axis_tick_label_font: Font name of the tick labels.
    :type axis_tick_label_font: {"arial", "courier", "helvetica", "times", "serif", "sansserif", "symbol"}, default: "sansserif"

    :param axis_tick_label_font_style: Font style of the tick labels.
    :type axis_tick_label_font_style: {"normal", "bold", "italic", "bolditalic"}, default: "normal"

    :param axis_tick_label_colour: Colour of the tick labels.
    :type axis_tick_label_colour: str, default: "automatic"

    :param axis_tick_label_height: Height of the tick labels.
    :type axis_tick_label_height: number, default: 0.3

    :param axis_tick_label_list: List of user defined tick labels.
    :type axis_tick_label_list: str or list[str]

    :param axis_tick_label_format: Format of tick label values.
    :type axis_tick_label_format: str, default: "(automatic)"

    :param axis_minor_tick: Plots minor ticks.
    :type axis_minor_tick: {"on", "off"}, default: "off"

    :param axis_minor_tick_count: Number of minor tick marks between two ticks.
    :type axis_minor_tick_count: number, default: 2

    :param axis_minor_tick_colour: Colour of the minor ticks.
    :type axis_minor_tick_colour: str, default: "automatic"

    :param axis_minor_tick_thickness: Thickness of the minor ticks.
    :type axis_minor_tick_thickness: int, default: 1

    :param axis_minor_grid: 
    :type axis_minor_grid: {"on", "off"}, default: "off"

    :param axis_minor_grid_colour: Colour of the minor grid lines.
    :type axis_minor_grid_colour: str, default: "black"

    :param axis_minor_grid_line_style: Line style of the minor grid lines.
    :type axis_minor_grid_line_style: {"solid", "dash", "dot", "chain_dot", "chain_dash"}, default: "solid"

    :param axis_minor_grid_thickness: Thickness of the minor grid lines.
    :type axis_minor_grid_thickness: int, default: 1

    :param axis_tip_title: Plots title ta axis tip.
    :type axis_tip_title: {"on", "off"}, default: "off"

    :param axis_tip_title_text: Text to show in the axis tip title.
    :type axis_tip_title_text: str

    :param axis_tip_title_colour: Colour of the axis tip title.
    :type axis_tip_title_colour: str, default: "automatic"

    :param axis_tip_title_height: Font size of the axis tip title.
    :type axis_tip_title_height: number, default: 0.4

    :param axis_tip_title_quality: Quality of the font of the axi tip title.
    :type axis_tip_title_quality: {"high", "medium", "low"}, default: "medium"

    :param axis_date_type: Select the type of date axis.
    :type axis_date_type: {"automatic", "years", "months", "days", "hours", "monthly", "climate"}, default: "days"

    :param axis_years_label: Plots year labels.
    :type axis_years_label: {"on", "off"}, default: "on"

    :param axis_years_label_colour: Colour of year labels.
    :type axis_years_label_colour: str, default: "automatic"

    :param axis_years_label_quality: Text quality of year labels.
    :type axis_years_label_quality: {"high", "medium", "low"}, default: "medium"

    :param axis_years_label_height: Height of year labels.
    :type axis_years_label_height: number, default: 0.2

    :param axis_months_label: Plots month labels.
    :type axis_months_label: {"on", "off"}, default: "on"

    :param axis_months_label_composition: Number of characters per month to plot.
    :type axis_months_label_composition: {"one", "two", "three"}, default: "three"

    :param axis_months_label_colour: Colour of month labels.
    :type axis_months_label_colour: str, default: "automatic"

    :param axis_months_label_quality: Text quality of month labels.
    :type axis_months_label_quality: {"high", "medium", "low"}, default: "medium"

    :param axis_months_label_height: Height of month labels.
    :type axis_months_label_height: number, default: 0.2

    :param axis_days_label: Controls the day label plotting.
    :type axis_days_label: {"day", "number", "both", "off"}, default: "both"

    :param axis_days_label_composition: Number of characters per days to plot.
    :type axis_days_label_composition: {"one", "three", "full"}, default: "three"

    :param axis_days_label_position: Used for short time series. If it is "12" the day labels will appear at 12h.
    :type axis_days_label_position: number, default: 12

    :param axis_days_label_colour: Colour of the day labels.
    :type axis_days_label_colour: str, default: "black"

    :param axis_days_sunday_label_colour: Colour of the day labels on Sundays.
    :type axis_days_sunday_label_colour: str, default: "red"

    :param axis_days_label_quality: Text quality of the day labels.
    :type axis_days_label_quality: {"high", "medium", "low"}, default: "medium"

    :param axis_days_label_height: Height of the day labels.
    :type axis_days_label_height: number, default: 0.2

    :param axis_hours_label: Plots the hour labels.
    :type axis_hours_label: {"on", "off"}, default: "off"

    :param axis_hours_label_colour: Colour of the hour labels.
    :type axis_hours_label_colour: str, default: "black"

    :param axis_hours_label_quality: Text quality of the hour labels.
    :type axis_hours_label_quality: {"high", "medium", "low"}, default: "medium"

    :param axis_hours_label_height: Height of the hour labels.
    :type axis_hours_label_height: number, default: 0.2

    :rtype: :class:`Request`


.. minigallery:: metview.maxis
    :add-heading:

