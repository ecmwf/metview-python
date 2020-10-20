
maxis
=========================

.. container::
    
    .. container:: leftside

        .. image:: /_static/MAXIS.png
           :width: 48px

    .. container:: rightside

        This icon represents the `Axis Plotting <https://confluence.ecmwf.int/display/METV/Axis+Plotting>`_ icon in Metview's user interface.


.. py:function:: maxis(**kwargs)
  
    Description comes here!


    :param axis_orientation: Orientation of axis. The possible values:

        * horizontal
        * vertical
        The default is: horizontal.
    :type axis_orientation: str


    :param axis_position: Position of the axes. The possible values:

        * bottom
        * top
        * left
        * right
        * automatic
        The default is: automatic.
    :type axis_position: str


    :param axis_type: Method to position ticks on an axis. The possible values:

        * regular
        * position_list
        * logarithmic
        * date
        * geoline
        The default is: regular.
    :type axis_type: str


    :param axis_line: Plot the axis line. The possible values:

        * on
        * off
        The default is: on.
    :type axis_line: str


    :param axis_line_colour: Colour of axis line. The possible values:

        * background
        The default is: automatic.
    :type axis_line_colour: str


    :param axis_line_style: Line Style of axis line. The possible values:

        * solid
        * dash
        * dot
        * chain_dot
        * chain_dash
        The default is: solid.
    :type axis_line_style: str


    :param axis_line_thickness: Thickness of axis line. The default is: 2.
    :type axis_line_thickness: int


    :param axis_grid: Plot axis grid lines. The possible values:

        * on
        * off
        The default is: off.
    :type axis_grid: str


    :param axis_grid_colour: Colour of grid lines. The possible values:

        * background
        The default is: black.
    :type axis_grid_colour: str


    :param axis_grid_line_style: Line style of grid. The possible values:

        * solid
        * dash
        * dot
        * chain_dot
        * chain_dash
        The default is: solid.
    :type axis_grid_line_style: str


    :param axis_grid_thickness: Thickness of grid lines. The default is: 1.
    :type axis_grid_thickness: int


    :param axis_grid_reference_level: value to be used as reference for the grid. The default is: 1.0e21.
    :type axis_grid_reference_level: number


    :param axis_grid_reference_colour: Colour of the reference  grid line. The possible values:

        * background
        The default is: automatic.
    :type axis_grid_reference_colour: str


    :param axis_grid_reference_line_style: Line style of the reference  grid line. The possible values:

        * solid
        * dash
        * dot
        * chain_dot
        * chain_dash
        The default is: solid.
    :type axis_grid_reference_line_style: str


    :param axis_grid_reference_thickness: Thickness of the reference grid line. The default is: 2.
    :type axis_grid_reference_thickness: int


    :param axis_title: Plot axis title. The possible values:

        * on
        * off
        The default is: on.
    :type axis_title: str


    :param axis_title_text: The axis title text
    :type axis_title_text: str


    :param axis_title_orientation: Orientation of the axis title. The possible values:

        * horizontal
        * vertical
        * parallel
        The default is: parallel.
    :type axis_title_orientation: str


    :param axis_title_colour: Colour of axis title. The possible values:

        * background
        The default is: automatic.
    :type axis_title_colour: str


    :param axis_title_height: Height of axis title. The default is: 0.4.
    :type axis_title_height: number


    :param axis_title_font: Font of axis title. The possible values:

        * arial
        * courier
        * helvetica
        * times
        * serif
        * sansserif
        * symbol
        The default is: sansserif.
    :type axis_title_font: str


    :param axis_title_font_style: Font style of axis title. The possible values:

        * normal
        * bold
        * italic
        * bolditalic
        The default is: normal.
    :type axis_title_font_style: str


    :param axis_tick: Plot ticks. The possible values:

        * on
        * off
        The default is: on.
    :type axis_tick: str


    :param axis_tick_interval: Interval between ticks in user units. The default is: 1.0e21.
    :type axis_tick_interval: number


    :param axis_tick_position_list: Array specifying the positions of ticks (in user coordinates!)
    :type axis_tick_position_list: float or list[float]


    :param axis_tick_position: Tick position, if in the ticks will positioned inside the frame. The possible values:

        * out
        * in
        The default is: out.
    :type axis_tick_position: str


    :param axis_tick_colour: Colour of ticks. The possible values:

        * background
        The default is: automatic.
    :type axis_tick_colour: str


    :param axis_tick_size: Size of ticks. The default is: 0.175.
    :type axis_tick_size: number


    :param axis_tick_thickness: Thickness of tick marks. The default is: 2.
    :type axis_tick_thickness: int


    :param axis_tick_label: Plot tick labels (ON/OFF). The possible values:

        * on
        * off
        The default is: on.
    :type axis_tick_label: str


    :param axis_tick_label_type: Type of tick labels required. The possible values:

        * number
        * label_list
        * latitude
        * longitude
        The default is: number.
    :type axis_tick_label_type: str


    :param axis_tick_label_frequency: Label every nth tick mark. The default is: 1.
    :type axis_tick_label_frequency: number


    :param axis_tick_label_first: Turn off first (left or bottom) tick label. The possible values:

        * on
        * off
        The default is: on.
    :type axis_tick_label_first: str


    :param axis_tick_label_last: Turn off last (right or top) tick label. The possible values:

        * on
        * off
        The default is: on.
    :type axis_tick_label_last: str


    :param axis_tick_label_position: Position labels on or between ticks. The possible values:

        * on_tick
        * inter_tick
        The default is: on_tick.
    :type axis_tick_label_position: str


    :param axis_tick_label_orientation: Orientation of the tick labels. The possible values:

        * horizontal
        * vertical
        * parallel
        The default is: horizontal.
    :type axis_tick_label_orientation: str


    :param axis_tick_label_font: Font name - please make sure this font is installed!. The possible values:

        * arial
        * courier
        * helvetica
        * times
        * serif
        * sansserif
        * symbol
        The default is: sansserif.
    :type axis_tick_label_font: str


    :param axis_tick_label_font_style: Font style. Set this to an empty string in order to remove all styling. The possible values:

        * normal
        * bold
        * italic
        * bolditalic
        The default is: normal.
    :type axis_tick_label_font_style: str


    :param axis_tick_label_colour: Colour of tick labels. The possible values:

        * background
        The default is: automatic.
    :type axis_tick_label_colour: str


    :param axis_tick_label_height: Height of tick labels. The default is: 0.3.
    :type axis_tick_label_height: number


    :param axis_tick_label_list: Array for passing user defined tick labels
    :type axis_tick_label_list: str or list[str]


    :param axis_tick_label_format: Format of tick label values. The default is: (automatic).
    :type axis_tick_label_format: str


    :param axis_minor_tick: Plot minor ticks (ON/OFF). The possible values:

        * on
        * off
        The default is: off.
    :type axis_minor_tick: str


    :param axis_minor_tick_count: Number of minor tick marks between two ticks. The default is: 2.
    :type axis_minor_tick_count: number


    :param axis_minor_tick_colour: Colour of minor ticks. The possible values:

        * background
        The default is: automatic.
    :type axis_minor_tick_colour: str


    :param axis_minor_tick_thickness: Thickness of minor ticks. The default is: 1.
    :type axis_minor_tick_thickness: int


    :param axis_minor_grid: 
    :type axis_minor_grid: str


    :param axis_minor_grid_colour: Colour of grid lines. The possible values:

        * background
        The default is: black.
    :type axis_minor_grid_colour: str


    :param axis_minor_grid_line_style: Line style of grid. The possible values:

        * solid
        * dash
        * dot
        * chain_dot
        * chain_dash
        The default is: solid.
    :type axis_minor_grid_line_style: str


    :param axis_minor_grid_thickness: Thickness of grid lines. The default is: 1.
    :type axis_minor_grid_thickness: int


    :param axis_tip_title: Plot ticks (ON/OFF). The possible values:

        * on
        * off
        The default is: off.
    :type axis_tip_title: str


    :param axis_tip_title_text: Text to show in the tip
    :type axis_tip_title_text: str


    :param axis_tip_title_colour: Coloour of the tip. The possible values:

        * background
        The default is: automatic.
    :type axis_tip_title_colour: str


    :param axis_tip_title_height: font size of the tip. The default is: 0.4.
    :type axis_tip_title_height: number


    :param axis_tip_title_quality: Quality of the font. The possible values:

        * high
        * medium
        * low
        The default is: medium.
    :type axis_tip_title_quality: str


    :param axis_date_type: Select the type of date axis. The possible values:

        * automatic
        * years
        * months
        * days
        * hours
        * monthly
        * climate
        The default is: days.
    :type axis_date_type: str


    :param axis_years_label: controls the labeling of the years. The possible values:

        * on
        * off
        The default is: on.
    :type axis_years_label: str


    :param axis_years_label_colour: Label colour for 'YEARS. The possible values:

        * background
        The default is: automatic.
    :type axis_years_label_colour: str


    :param axis_years_label_quality: 
    :type axis_years_label_quality: str


    :param axis_years_label_height: Label height for 'YEARS. The default is: 0.2.
    :type axis_years_label_height: number


    :param axis_months_label: controls the labeling of the months. The possible values:

        * on
        * off
        The default is: on.
    :type axis_months_label: str


    :param axis_months_label_composition: Number of letters per month to plot. The possible values:

        * one
        * two
        * three
        The default is: three.
    :type axis_months_label_composition: str


    :param axis_months_label_colour: Label colour for months. The possible values:

        * background
        The default is: automatic.
    :type axis_months_label_colour: str


    :param axis_months_label_quality: 
    :type axis_months_label_quality: str


    :param axis_months_label_height: Label height for months. The default is: 0.2.
    :type axis_months_label_height: number


    :param axis_days_label: controls the labeling of the hours. The possible values:

        * day
        * number
        * both
        * off
        The default is: both.
    :type axis_days_label: str


    :param axis_days_label_composition: Number of letters per days to plot. The possible values:

        * one
        * three
        * full
        The default is: three.
    :type axis_days_label_composition: str


    :param axis_days_label_position: for short time series : if 12 the label will be at 12h . The default is: 12.
    :type axis_days_label_position: number


    :param axis_days_label_colour: Label colour for days. The possible values:

        * background
        The default is: black.
    :type axis_days_label_colour: str


    :param axis_days_sunday_label_colour: Label colour for sundays. The possible values:

        * background
        The default is: red.
    :type axis_days_sunday_label_colour: str


    :param axis_days_label_quality: 
    :type axis_days_label_quality: str


    :param axis_days_label_height: Label height for  days. The default is: 0.2.
    :type axis_days_label_height: number


    :param axis_hours_label: controls the labeling of the hours. The possible values:

        * on
        * off
        The default is: off.
    :type axis_hours_label: str


    :param axis_hours_label_colour: Label quality for hours. The possible values:

        * background
        The default is: black.
    :type axis_hours_label_colour: str


    :param axis_hours_label_quality: 
    :type axis_hours_label_quality: str


    :param axis_hours_label_height: Label height for  hours. The default is: 0.2.
    :type axis_hours_label_height: number


    :rtype: None


.. minigallery:: metview.maxis
    :add-heading:

