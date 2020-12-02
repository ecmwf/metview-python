
mthermo
=========================

.. container::
    
    .. container:: leftside

        .. image:: /_static/MTHERMO.png
           :width: 48px

    .. container:: rightside

        This function performs the same task as the `Thermo Plotting <https://confluence.ecmwf.int/display/METV/Thermo+Plotting>`_ icon in Metview’s user interface. It accepts its parameters as keyword arguments, described below.


.. py:function:: mthermo(**kwargs)
  
    Description comes here!


    :param legend: 
    :type legend: {"on", "off"}, default: "off"


    :param legend_user_text: 
    :type legend_user_text: str


    :param thermo_temperature_line: 
    :type thermo_temperature_line: {"on", "off"}, default: "on"


    :param thermo_temperature_line_style: 
    :type thermo_temperature_line_style: {"solid", "dash", "dot", "chain_dot", "chain_dash"}, default: "solid"


    :param thermo_temperature_line_colour: 
    :type thermo_temperature_line_colour: str, default: "red"


    :param thermo_temperature_line_thickness: 
    :type thermo_temperature_line_thickness: int, default: 8


    :param thermo_temperature_missing_data_mode: 
    :type thermo_temperature_missing_data_mode: {"ignore", "join", "drop"}, default: "join"


    :param thermo_temperature_missing_data_style: 
    :type thermo_temperature_missing_data_style: {"solid", "dash", "dot", "chain_dot", "chain_dash"}, default: "solid"


    :param thermo_temperature_missing_data_colour: 
    :type thermo_temperature_missing_data_colour: str, default: "red"


    :param thermo_temperature_missing_data_thickness: 
    :type thermo_temperature_missing_data_thickness: int, default: 8


    :param thermo_dewpoint_line: 
    :type thermo_dewpoint_line: {"on", "off"}, default: "on"


    :param thermo_dewpoint_line_style: 
    :type thermo_dewpoint_line_style: {"solid", "dash", "dot", "chain_dot", "chain_dash"}, default: "dash"


    :param thermo_dewpoint_line_colour: 
    :type thermo_dewpoint_line_colour: str, default: "red"


    :param thermo_dewpoint_line_thickness: 
    :type thermo_dewpoint_line_thickness: int, default: 8


    :param thermo_dewpoint_missing_data_mode: 
    :type thermo_dewpoint_missing_data_mode: {"ignore", "join", "drop"}, default: "join"


    :param thermo_dewpoint_missing_data_style: 
    :type thermo_dewpoint_missing_data_style: {"solid", "dash", "dot", "chain_dot", "chain_dash"}, default: "dash"


    :param thermo_dewpoint_missing_data_colour: 
    :type thermo_dewpoint_missing_data_colour: str, default: "red"


    :param thermo_dewpoint_missing_data_thickness: 
    :type thermo_dewpoint_missing_data_thickness: int, default: 8


    :rtype: None


.. minigallery:: metview.mthermo
    :add-heading:

