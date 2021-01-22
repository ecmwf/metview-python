
mtaylor
=========================

.. container::
    
    .. container:: leftside

        .. image:: /_static/MTAYLOR.png
           :width: 48px

    .. container:: rightside

		Configures the background of a Taylor diagram.


		.. note:: This function performs the same task as the `Taylor Grid <https://confluence.ecmwf.int/display/METV/Taylor+Grid>`_ icon in Metview’s user interface. It accepts its parameters as keyword arguments, described below.


.. py:function:: mtaylor(**kwargs)
  
    Defines the background of a Taylor diagram.


    :param taylor_label: Text of the main label.
    :type taylor_label: str, default: "correlation"

    :param taylor_label_colour: Colour of the label.
    :type taylor_label_colour: str, default: "navy"

    :param taylor_label_height: Height (cm) of the label.
    :type taylor_label_height: number, default: 0.35

    :param taylor_primary_grid_increment: Grid increment for the primary grid (standard deviation).
    :type taylor_primary_grid_increment: number, default: 0.5

    :param taylor_primary_grid_line_colour: Colour of the primary grid.
    :type taylor_primary_grid_line_colour: str, default: "navy"

    :param taylor_primary_grid_line_thickness: Thickness of the primary grid.
    :type taylor_primary_grid_line_thickness: int, default: 1

    :param taylor_primary_grid_line_style: Line style of the primary grid.
    :type taylor_primary_grid_line_style: {"solid", "dash", "dot", "chain_dash", "chain_dot"}, default: "solid"

    :param taylor_primary_grid_reference: Reference value for the primary grid.
    :type taylor_primary_grid_reference: number, default: 0.5

    :param taylor_reference_line_colour: Colour of the reference line.
    :type taylor_reference_line_colour: str, default: "navy"

    :param taylor_reference_line_thickness: Thickness of the reference line.
    :type taylor_reference_line_thickness: int, default: 2

    :param taylor_reference_line_style: Line style of the reference line.
    :type taylor_reference_line_style: {"solid", "dash", "dot", "chain_dash", "chain_dot"}, default: "solid"

    :param taylor_primary_label: Enables labels of the primary grid.
    :type taylor_primary_label: {"on", "off"}, default: "on"

    :param taylor_primary_label_colour: Colour of the labels of the primary grid.
    :type taylor_primary_label_colour: str, default: "navy"

    :param taylor_primary_label_height: Height (cm) of the labels of the primary grid.
    :type taylor_primary_label_height: number, default: 0.35

    :param taylor_secondary_grid: Enables the plotting of the secondary (standard deviation) grid.
    :type taylor_secondary_grid: {"on", "off"}, default: "off"

    :param taylor_secondary_grid_reference: Reference value used for the secondary grid.
    :type taylor_secondary_grid_reference: number, default: 0.5

    :param taylor_secondary_grid_increment: Increment used for the secondary grid.
    :type taylor_secondary_grid_increment: number, default: 0.5

    :param taylor_secondary_grid_line_colour: Colour of the secondary grid.
    :type taylor_secondary_grid_line_colour: str, default: "navy"

    :param taylor_secondary_grid_line_thickness: Thickness of the secondary grid.
    :type taylor_secondary_grid_line_thickness: int, default: 1

    :param taylor_secondary_grid_line_style: Line style of the secondary grid.
    :type taylor_secondary_grid_line_style: {"solid", "dash", "dot", "chain_dash", "chain_dot"}, default: "solid"

    :param taylor_secondary_label: Enables labels for the secondary grid.
    :type taylor_secondary_label: {"on", "off"}, default: "on"

    :param taylor_secondary_label_colour: Colour of the labels for the secondary grid.
    :type taylor_secondary_label_colour: str, default: "navy"

    :param taylor_secondary_label_height: Height (cm) of the labels for the secondary grid.
    :type taylor_secondary_label_height: number, default: 0.35

    :rtype: :class:`Request`
.. include:: /gallery/backref/mtaylor.rst