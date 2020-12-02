
mthermogrid
=========================

.. container::
    
    .. container:: leftside

        .. image:: /_static/MTHERMOGRID.png
           :width: 48px

    .. container:: rightside

        This function performs the same task as the `Thermo Grid <https://confluence.ecmwf.int/display/METV/Thermo+Grid>`_ icon in Metview’s user interface. It accepts its parameters as keyword arguments, described below.


.. py:function:: mthermogrid(**kwargs)
  
    Description comes here!


    :param thermo_isotherm_grid: Plot the isotherms
    :type thermo_isotherm_grid: {"on", "off"}, default: "on"


    :param thermo_isotherm_colour: Colou of the isotherms
    :type thermo_isotherm_colour: str, default: "charcoal"


    :param thermo_isotherm_thickness: Thickness  of the isotherms
    :type thermo_isotherm_thickness: int, default: 1


    :param thermo_isotherm_style: Line Style  of the isotherms
    :type thermo_isotherm_style: {"solid", "dash", "dot", "chain_dot", "chain_dash"}, default: "solid"


    :param thermo_isotherm_interval: interval for isotherms grid
    :type thermo_isotherm_interval: number, default: 10


    :param thermo_isotherm_reference: Reference   of the isotherms
    :type thermo_isotherm_reference: number, default: 0


    :param thermo_isotherm_reference_colour: Reference   of the isotherms
    :type thermo_isotherm_reference_colour: str, default: "red"


    :param thermo_isotherm_reference_style: Reference   of the isotherms
    :type thermo_isotherm_reference_style: {"solid", "dash", "dot", "chain_dot", "chain_dash"}, default: "solid"


    :param thermo_isotherm_reference_thickness: Reference   of the isotherms
    :type thermo_isotherm_reference_thickness: int, default: 2


    :param thermo_isotherm_label_colour: Label Colour for the isotherms
    :type thermo_isotherm_label_colour: str, default: "charcoal"


    :param thermo_isotherm_label_font_name: 
    :type thermo_isotherm_label_font_name: str, default: "sanserif"


    :param thermo_isotherm_label_font_style: Font Style used for the isotherms labels
    :type thermo_isotherm_label_font_style: {"normal", "bold", "italic", "bolditalic"}, default: "normal"


    :param thermo_isotherm_label_font_size: Font Size used for the isotherms labels
    :type thermo_isotherm_label_font_size: number, default: 0.3


    :param thermo_isotherm_label_frequency: Isotherm frequency for labelling
    :type thermo_isotherm_label_frequency: number, default: 1


    :param thermo_isobar_grid: Plot the isobars
    :type thermo_isobar_grid: {"on", "off"}, default: "on"


    :param thermo_isobar_colour: Colou of the isobars
    :type thermo_isobar_colour: str, default: "evergreen"


    :param thermo_isobar_thickness: Thickness  of the isobars
    :type thermo_isobar_thickness: int, default: 2


    :param thermo_isobar_style: Line Style  of the isobars
    :type thermo_isobar_style: {"solid", "dash", "dot", "chain_dot", "chain_dash"}, default: "solid"


    :param thermo_isobar_interval: Interval between isobars
    :type thermo_isobar_interval: number, default: 100


    :param thermo_isobar_reference: Line Style  of the isobars
    :type thermo_isobar_reference: number, default: 1000


    :param thermo_isobar_label_colour: Label Colour for the isotherms
    :type thermo_isobar_label_colour: str, default: "evergreen"


    :param thermo_isobar_label_font_name: 
    :type thermo_isobar_label_font_name: str, default: "sanserif"


    :param thermo_isobar_label_font_style: Font Style used for the isobars labels
    :type thermo_isobar_label_font_style: {"normal", "bold", "italic", "bolditalic"}, default: "normal"


    :param thermo_isobar_label_font_size: Font Size used for the isobars labels
    :type thermo_isobar_label_font_size: number, default: 0.3


    :param thermo_isobar_label_frequency: isobar frequency for labelling
    :type thermo_isobar_label_frequency: number, default: 1


    :param thermo_dry_adiabatic_grid: Plot the dry_adiabatics
    :type thermo_dry_adiabatic_grid: {"on", "off"}, default: "on"


    :param thermo_dry_adiabatic_colour: Colou of the dry_adiabatics
    :type thermo_dry_adiabatic_colour: str, default: "charcoal"


    :param thermo_dry_adiabatic_thickness: Thickness  of the dry_adiabatics
    :type thermo_dry_adiabatic_thickness: int, default: 1


    :param thermo_dry_adiabatic_style: Line Style  of the dry_adiabatics
    :type thermo_dry_adiabatic_style: {"solid", "dash", "dot", "chain_dot", "chain_dash"}, default: "solid"


    :param thermo_dry_adiabatic_interval: Interval between 2 dry_adiabatics.
    :type thermo_dry_adiabatic_interval: number, default: 10


    :param thermo_dry_adiabatic_reference: Reference   of the dry_adiabatics
    :type thermo_dry_adiabatic_reference: number, default: 0


    :param thermo_dry_adiabatic_label_colour: Label Colour for the isotherms
    :type thermo_dry_adiabatic_label_colour: str, default: "charcoal"


    :param thermo_dry_adiabatic_label_font_name: 
    :type thermo_dry_adiabatic_label_font_name: str, default: "sanserif"


    :param thermo_dry_adiabatic_label_font_style: Font Style used for the dry_adiabatics labels
    :type thermo_dry_adiabatic_label_font_style: {"normal", "bold", "italic", "bolditalic"}, default: "normal"


    :param thermo_dry_adiabatic_label_font_size: Font Size used for the dry_adiabatics labels
    :type thermo_dry_adiabatic_label_font_size: number, default: 0.3


    :param thermo_dry_adiabatic_label_frequency: frequency for dry_adiabatic labelling
    :type thermo_dry_adiabatic_label_frequency: number, default: 1


    :param thermo_saturated_adiabatic_grid: Plot the saturated_adiabatics
    :type thermo_saturated_adiabatic_grid: {"on", "off"}, default: "on"


    :param thermo_saturated_adiabatic_colour: Colou of the saturated_adiabatics
    :type thermo_saturated_adiabatic_colour: str, default: "charcoal"


    :param thermo_saturated_adiabatic_thickness: Thickness  of the dry_adiabatics
    :type thermo_saturated_adiabatic_thickness: int, default: 2


    :param thermo_saturated_adiabatic_style: Line Style  of the saturated_adiabatics
    :type thermo_saturated_adiabatic_style: {"solid", "dash", "dot", "chain_dot", "chain_dash"}, default: "solid"


    :param thermo_saturated_adiabatic_interval: interval for saturated_adiabatics grid
    :type thermo_saturated_adiabatic_interval: number, default: 5


    :param thermo_saturated_adiabatic_reference: Reference   of the saturated_adiabatics
    :type thermo_saturated_adiabatic_reference: number, default: 0


    :param thermo_saturated_adiabatic_label_colour: Label Colour for the isotherms
    :type thermo_saturated_adiabatic_label_colour: str, default: "charcoal"


    :param thermo_saturated_adiabatic_label_font_name: 
    :type thermo_saturated_adiabatic_label_font_name: str, default: "sanserif"


    :param thermo_saturated_adiabatic_label_font_style: Font Style used for the saturated_adiabatics labels
    :type thermo_saturated_adiabatic_label_font_style: {"normal", "bold", "italic", "bolditalic"}, default: "normal"


    :param thermo_saturated_adiabatic_label_font_size: Font Size used for the saturated_adiabatics labels
    :type thermo_saturated_adiabatic_label_font_size: number, default: 0.3


    :param thermo_saturated_adiabatic_label_frequency: saturated_adiabatic frequency for labelling
    :type thermo_saturated_adiabatic_label_frequency: number, default: 1


    :param thermo_mixing_ratio_grid: Plot the mixing_ratios
    :type thermo_mixing_ratio_grid: {"on", "off"}, default: "on"


    :param thermo_mixing_ratio_colour: Colou of the mixing_ratios
    :type thermo_mixing_ratio_colour: str, default: "purple"


    :param thermo_mixing_ratio_thickness: Thickness  of the mixing_ratios
    :type thermo_mixing_ratio_thickness: int, default: 1


    :param thermo_mixing_ratio_style: Line Style  of the mixing_ratios
    :type thermo_mixing_ratio_style: {"solid", "dash", "dot", "chain_dot", "chain_dash"}, default: "dash"


    :param thermo_mixing_ratio_frequency: mixing_ratio frequency for grid
    :type thermo_mixing_ratio_frequency: number, default: 1


    :param thermo_mixing_ratio_label_colour: Label Colour for the isotherms
    :type thermo_mixing_ratio_label_colour: str, default: "purple"


    :param thermo_mixing_ratio_label_font_name: 
    :type thermo_mixing_ratio_label_font_name: str, default: "sanserif"


    :param thermo_mixing_ratio_label_font_style: Font Style used for the mixing_ratios labels
    :type thermo_mixing_ratio_label_font_style: {"normal", "bold", "italic", "bolditalic"}, default: "normal"


    :param thermo_mixing_ratio_label_font_size: Font Size used for the mixing_ratios labels
    :type thermo_mixing_ratio_label_font_size: number, default: 0.3


    :param thermo_mixing_ratio_label_frequency: mixing_ratio frequency for labelling
    :type thermo_mixing_ratio_label_frequency: number, default: 1


    :rtype: None


.. minigallery:: metview.mthermogrid
    :add-heading:

