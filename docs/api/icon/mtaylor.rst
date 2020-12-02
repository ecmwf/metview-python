
mtaylor
=========================

.. container::
    
    .. container:: leftside

        .. image:: /_static/MTAYLOR.png
           :width: 48px

    .. container:: rightside

        This function performs the same task as the `Taylor Grid <https://confluence.ecmwf.int/display/METV/Taylor+Grid>`_ icon in Metview’s user interface. It accepts its parameters as keyword arguments, described below.


.. py:function:: mtaylor(**kwargs)
  
    Description comes here!


    :param taylor_label: Label of the grid
    :type taylor_label: str, default: "correlation"


    :param taylor_label_colour: Colour of the label
    :type taylor_label_colour: str, default: "navy"


    :param taylor_label_height: Hieght of the label
    :type taylor_label_height: number, default: 0.35


    :param taylor_primary_grid_increment: Reference used  of the Standard deviation plotting.
    :type taylor_primary_grid_increment: number, default: 0.5


    :param taylor_primary_grid_line_colour: Colour used to plot the primary grid
    :type taylor_primary_grid_line_colour: str, default: "navy"


    :param taylor_primary_grid_line_thickness: Thickness used to plot the primary grid
    :type taylor_primary_grid_line_thickness: int, default: 1


    :param taylor_primary_grid_line_style: Line Style used to plot the primary grid
    :type taylor_primary_grid_line_style: {"solid", "dash", "dot", "chain_dash", "chain_dot"}, default: "solid"


    :param taylor_primary_grid_reference: Reference used  of the Standard deviation plotting.
    :type taylor_primary_grid_reference: number, default: 0.5


    :param taylor_reference_line_colour: Colour used to plot the primary grid
    :type taylor_reference_line_colour: str, default: "navy"


    :param taylor_reference_line_thickness: Thickness used to plot the primary grid
    :type taylor_reference_line_thickness: int, default: 2


    :param taylor_reference_line_style: Line Style used to plot the primary grid
    :type taylor_reference_line_style: {"solid", "dash", "dot", "chain_dash", "chain_dot"}, default: "solid"


    :param taylor_primary_label: Turn the labels ("on"/"off") of the primary grid
    :type taylor_primary_label: {"on", "off"}, default: "on"


    :param taylor_primary_label_colour: Colour of the  labels  of the primary grid
    :type taylor_primary_label_colour: str, default: "navy"


    :param taylor_primary_label_height: Height of the  labels  of the primary grid
    :type taylor_primary_label_height: number, default: 0.35


    :param taylor_secondary_grid: turn "on"/"off" the secondaries lines for the grid.
    :type taylor_secondary_grid: {"on", "off"}, default: "off"


    :param taylor_secondary_grid_reference: Reference used  of the Standard deviation plotting.
    :type taylor_secondary_grid_reference: number, default: 0.5


    :param taylor_secondary_grid_increment: Reference used  of the Standard deviation plotting.
    :type taylor_secondary_grid_increment: number, default: 0.5


    :param taylor_secondary_grid_line_colour: Colour used to plot the primary grid
    :type taylor_secondary_grid_line_colour: str, default: "navy"


    :param taylor_secondary_grid_line_thickness: Thickness used to plot the primary grid
    :type taylor_secondary_grid_line_thickness: int, default: 1


    :param taylor_secondary_grid_line_style: Line Style used to plot the primary grid
    :type taylor_secondary_grid_line_style: {"solid", "dash", "dot", "chain_dash", "chain_dot"}, default: "solid"


    :param taylor_secondary_label: Turn the labels ("on"/"off") of the secondary grid
    :type taylor_secondary_label: {"on", "off"}, default: "on"


    :param taylor_secondary_label_colour: Colour of the  labels  of the secondary grid
    :type taylor_secondary_label_colour: str, default: "navy"


    :param taylor_secondary_label_height: Height of the  labels  of the secondary grid
    :type taylor_secondary_label_height: number, default: 0.35


    :rtype: None


.. minigallery:: metview.mtaylor
    :add-heading:

