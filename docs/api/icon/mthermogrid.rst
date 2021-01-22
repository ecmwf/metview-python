
mthermogrid
=========================

.. container::
    
    .. container:: leftside

        .. image:: /_static/MTHERMOGRID.png
           :width: 48px

    .. container:: rightside

		This is the visual definition for specifying how a thermodynamic diagram background is displayed. It controls features related to isotherms, isobars, mixing ratio lines, dry and moist adiabats.


		.. note:: This function performs the same task as the `Thermo Grid <https://confluence.ecmwf.int/display/METV/Thermo+Grid>`_ icon in Metview’s user interface. It accepts its parameters as keyword arguments, described below.


.. py:function:: mthermogrid(**kwargs)
  
    Defines the background of a thermodynamic diagram.


    :param thermo_isotherm_grid: Plots the isotherms.
    :type thermo_isotherm_grid: {"on", "off"}, default: "on"

    :param thermo_isotherm_colour: Colour of the isotherms.
    :type thermo_isotherm_colour: str, default: "charcoal"

    :param thermo_isotherm_thickness: Thickness of the isotherms.
    :type thermo_isotherm_thickness: int, default: 1

    :param thermo_isotherm_style: Line style of the isotherms.
    :type thermo_isotherm_style: {"solid", "dash", "dot", "chain_dot", "chain_dash"}, default: "solid"

    :param thermo_isotherm_interval: Interval for the isotherms.
    :type thermo_isotherm_interval: number, default: 10

    :param thermo_isotherm_reference: Reference value of the isotherms.
    :type thermo_isotherm_reference: number, default: 0

    :param thermo_isotherm_reference_colour: Colour of the reference isotherm.
    :type thermo_isotherm_reference_colour: str, default: "red"

    :param thermo_isotherm_reference_style: Line style of the reference isotherm.
    :type thermo_isotherm_reference_style: {"solid", "dash", "dot", "chain_dot", "chain_dash"}, default: "solid"

    :param thermo_isotherm_reference_thickness: Thickness of the reference isotherm.
    :type thermo_isotherm_reference_thickness: int, default: 2

    :param thermo_isotherm_label_colour: Colour of the isotherm labels.
    :type thermo_isotherm_label_colour: str, default: "charcoal"

    :param thermo_isotherm_label_font_name: Font name of the isotherm labels.
    :type thermo_isotherm_label_font_name: str, default: "sanserif"

    :param thermo_isotherm_label_font_style: Font style of the isotherm labels.
    :type thermo_isotherm_label_font_style: {"normal", "bold", "italic", "bolditalic"}, default: "normal"

    :param thermo_isotherm_label_font_size: Font size of the isotherm labels.
    :type thermo_isotherm_label_font_size: number, default: 0.3

    :param thermo_isotherm_label_frequency: Frequency for isotherm labelling.
    :type thermo_isotherm_label_frequency: number, default: 1

    :param thermo_isobar_grid: Plots the isobars.
    :type thermo_isobar_grid: {"on", "off"}, default: "on"

    :param thermo_isobar_colour: Colour of the isobars.
    :type thermo_isobar_colour: str, default: "evergreen"

    :param thermo_isobar_thickness: Thickness of the isobars.
    :type thermo_isobar_thickness: int, default: 2

    :param thermo_isobar_style: Line style of the isobars.
    :type thermo_isobar_style: {"solid", "dash", "dot", "chain_dot", "chain_dash"}, default: "solid"

    :param thermo_isobar_interval: Interval between isobars (hPa).
    :type thermo_isobar_interval: number, default: 100

    :param thermo_isobar_reference: Reference value of the isobars (hPa).
    :type thermo_isobar_reference: number, default: 1000

    :param thermo_isobar_label_colour: Colour of the isobar labels.
    :type thermo_isobar_label_colour: str, default: "evergreen"

    :param thermo_isobar_label_font_name: Font name of the isobar labels.
    :type thermo_isobar_label_font_name: str, default: "sanserif"

    :param thermo_isobar_label_font_style: Font style of the isobar labels.
    :type thermo_isobar_label_font_style: {"normal", "bold", "italic", "bolditalic"}, default: "normal"

    :param thermo_isobar_label_font_size: Font size of the isobar labels.
    :type thermo_isobar_label_font_size: number, default: 0.3

    :param thermo_isobar_label_frequency: Frequency of the isobar labels.
    :type thermo_isobar_label_frequency: number, default: 1

    :param thermo_dry_adiabatic_grid: Plots the dry adiabats.
    :type thermo_dry_adiabatic_grid: {"on", "off"}, default: "on"

    :param thermo_dry_adiabatic_colour: Colour of the dry adiabats.
    :type thermo_dry_adiabatic_colour: str, default: "charcoal"

    :param thermo_dry_adiabatic_thickness: Thickness of the dry adiabats.
    :type thermo_dry_adiabatic_thickness: int, default: 1

    :param thermo_dry_adiabatic_style: Line style of the dry adiabats.
    :type thermo_dry_adiabatic_style: {"solid", "dash", "dot", "chain_dot", "chain_dash"}, default: "solid"

    :param thermo_dry_adiabatic_interval: Interval between the dry adiabats (C).
    :type thermo_dry_adiabatic_interval: number, default: 10

    :param thermo_dry_adiabatic_reference: Reference value of the dry adiabats (C).
    :type thermo_dry_adiabatic_reference: number, default: 0

    :param thermo_dry_adiabatic_label_colour: Colour of the dry adiabat labels.
    :type thermo_dry_adiabatic_label_colour: str, default: "charcoal"

    :param thermo_dry_adiabatic_label_font_name: Font name of the dry adiabat labels.
    :type thermo_dry_adiabatic_label_font_name: str, default: "sanserif"

    :param thermo_dry_adiabatic_label_font_style: Font style of the dry adiabat labels.
    :type thermo_dry_adiabatic_label_font_style: {"normal", "bold", "italic", "bolditalic"}, default: "normal"

    :param thermo_dry_adiabatic_label_font_size: Font size of the dry adiabat labels.
    :type thermo_dry_adiabatic_label_font_size: number, default: 0.3

    :param thermo_dry_adiabatic_label_frequency: Frequency of the dry adiabat labels.
    :type thermo_dry_adiabatic_label_frequency: number, default: 1

    :param thermo_saturated_adiabatic_grid: Plots the saturated adiabats.
    :type thermo_saturated_adiabatic_grid: {"on", "off"}, default: "on"

    :param thermo_saturated_adiabatic_colour: Colour of the saturated adiabats.
    :type thermo_saturated_adiabatic_colour: str, default: "charcoal"

    :param thermo_saturated_adiabatic_thickness: Thickness of the saturated adiabats.
    :type thermo_saturated_adiabatic_thickness: int, default: 2

    :param thermo_saturated_adiabatic_style: Line style of the saturated adiabats.
    :type thermo_saturated_adiabatic_style: {"solid", "dash", "dot", "chain_dot", "chain_dash"}, default: "solid"

    :param thermo_saturated_adiabatic_interval: Interval between the saturated adiabats (C).
    :type thermo_saturated_adiabatic_interval: number, default: 5

    :param thermo_saturated_adiabatic_reference: Reference value of the saturated adiabats (C).
    :type thermo_saturated_adiabatic_reference: number, default: 0

    :param thermo_saturated_adiabatic_label_colour: Colour of the saturated adiabat labels.
    :type thermo_saturated_adiabatic_label_colour: str, default: "charcoal"

    :param thermo_saturated_adiabatic_label_font_name: Font name of the saturated adiabat labels.
    :type thermo_saturated_adiabatic_label_font_name: str, default: "sanserif"

    :param thermo_saturated_adiabatic_label_font_style: Font style of the saturated adiabat labels.
    :type thermo_saturated_adiabatic_label_font_style: {"normal", "bold", "italic", "bolditalic"}, default: "normal"

    :param thermo_saturated_adiabatic_label_font_size: Font Size used for the saturated_adiabatics labels
    :type thermo_saturated_adiabatic_label_font_size: number, default: 0.3

    :param thermo_saturated_adiabatic_label_frequency: Frequency of the saturated adiabat labels.
    :type thermo_saturated_adiabatic_label_frequency: number, default: 1

    :param thermo_mixing_ratio_grid: Plots the mixing ratio lines.
    :type thermo_mixing_ratio_grid: {"on", "off"}, default: "on"

    :param thermo_mixing_ratio_colour: Colour of the mixing ratio lines.
    :type thermo_mixing_ratio_colour: str, default: "purple"

    :param thermo_mixing_ratio_thickness: Thickness of the mixing ratio lines.
    :type thermo_mixing_ratio_thickness: int, default: 1

    :param thermo_mixing_ratio_style: Line style of the mixing ratio lines.
    :type thermo_mixing_ratio_style: {"solid", "dash", "dot", "chain_dot", "chain_dash"}, default: "dash"

    :param thermo_mixing_ratio_frequency: Frequency of the mixing ratio lines.
    :type thermo_mixing_ratio_frequency: number, default: 1

    :param thermo_mixing_ratio_label_colour: Colour of the mixing ratio labels.
    :type thermo_mixing_ratio_label_colour: str, default: "purple"

    :param thermo_mixing_ratio_label_font_name: Font name of the mixing ratio labels.
    :type thermo_mixing_ratio_label_font_name: str, default: "sanserif"

    :param thermo_mixing_ratio_label_font_style: Font style of the mixing ratio labels.
    :type thermo_mixing_ratio_label_font_style: {"normal", "bold", "italic", "bolditalic"}, default: "normal"

    :param thermo_mixing_ratio_label_font_size: Font size of the mixing ratio labels.
    :type thermo_mixing_ratio_label_font_size: number, default: 0.3

    :param thermo_mixing_ratio_label_frequency: Frequency of the mixing ratio labels.
    :type thermo_mixing_ratio_label_frequency: number, default: 1

    :rtype: :class:`Request`
.. include:: /gallery/backref/mthermogrid.rst