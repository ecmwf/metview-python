
mthermogrid
=========================

.. container::
    
    .. container:: leftside

        .. image:: /_static/MTHERMOGRID.png
           :width: 48px

    .. container:: rightside

        This icon represents the `Thermo Grid <https://confluence.ecmwf.int/display/METV/Thermo+Grid>`_ icon in Metview's user interface.


.. py:function:: mthermogrid(**kwargs)
  
    Description comes here!


    :param thermo_isotherm_grid: Plot the isotherms. The possible values:

        * on
        * off
        The default is: on.
    :type thermo_isotherm_grid: str


    :param thermo_isotherm_colour: Colou of the isotherms. The possible values:

        * background
        The default is: charcoal.
    :type thermo_isotherm_colour: str


    :param thermo_isotherm_thickness: Thickness  of the isotherms. The default is: 1.
    :type thermo_isotherm_thickness: int


    :param thermo_isotherm_style: Line Style  of the isotherms. The possible values:

        * solid
        * dash
        * dot
        * chain_dot
        * chain_dash
        The default is: solid.
    :type thermo_isotherm_style: str


    :param thermo_isotherm_interval: interval for isotherms grid. The default is: 10.
    :type thermo_isotherm_interval: number


    :param thermo_isotherm_reference: Reference   of the isotherms. The default is: 0.
    :type thermo_isotherm_reference: number


    :param thermo_isotherm_reference_colour: Reference   of the isotherms. The possible values:

        * background
        The default is: red.
    :type thermo_isotherm_reference_colour: str


    :param thermo_isotherm_reference_style: Reference   of the isotherms. The possible values:

        * solid
        * dash
        * dot
        * chain_dot
        * chain_dash
        The default is: solid.
    :type thermo_isotherm_reference_style: str


    :param thermo_isotherm_reference_thickness: Reference   of the isotherms. The default is: 2.
    :type thermo_isotherm_reference_thickness: int


    :param thermo_isotherm_label_colour: Label Colour for the isotherms. The possible values:

        * background
        The default is: charcoal.
    :type thermo_isotherm_label_colour: str


    :param thermo_isotherm_label_font_name: 
    :type thermo_isotherm_label_font_name: str


    :param thermo_isotherm_label_font_style: Font Style used for the isotherms labels. The possible values:

        * normal
        * bold
        * italic
        * bolditalic
        The default is: normal.
    :type thermo_isotherm_label_font_style: str


    :param thermo_isotherm_label_font_size: Font Size used for the isotherms labels. The default is: 0.3.
    :type thermo_isotherm_label_font_size: number


    :param thermo_isotherm_label_frequency: Isotherm frequency for labelling. The default is: 1.
    :type thermo_isotherm_label_frequency: number


    :param thermo_isobar_grid: Plot the isobars. The possible values:

        * on
        * off
        The default is: on.
    :type thermo_isobar_grid: str


    :param thermo_isobar_colour: Colou of the isobars. The possible values:

        * background
        The default is: evergreen.
    :type thermo_isobar_colour: str


    :param thermo_isobar_thickness: Thickness  of the isobars. The default is: 2.
    :type thermo_isobar_thickness: int


    :param thermo_isobar_style: Line Style  of the isobars. The possible values:

        * solid
        * dash
        * dot
        * chain_dot
        * chain_dash
        The default is: solid.
    :type thermo_isobar_style: str


    :param thermo_isobar_interval: Interval between isobars. The default is: 100.
    :type thermo_isobar_interval: number


    :param thermo_isobar_reference: Line Style  of the isobars. The default is: 1000.
    :type thermo_isobar_reference: number


    :param thermo_isobar_label_colour: Label Colour for the isotherms. The possible values:

        * background
        The default is: evergreen.
    :type thermo_isobar_label_colour: str


    :param thermo_isobar_label_font_name: 
    :type thermo_isobar_label_font_name: str


    :param thermo_isobar_label_font_style: Font Style used for the isobars labels. The possible values:

        * normal
        * bold
        * italic
        * bolditalic
        The default is: normal.
    :type thermo_isobar_label_font_style: str


    :param thermo_isobar_label_font_size: Font Size used for the isobars labels. The default is: 0.3.
    :type thermo_isobar_label_font_size: number


    :param thermo_isobar_label_frequency: isobar frequency for labelling. The default is: 1.
    :type thermo_isobar_label_frequency: number


    :param thermo_dry_adiabatic_grid: Plot the dry_adiabatics. The possible values:

        * on
        * off
        The default is: on.
    :type thermo_dry_adiabatic_grid: str


    :param thermo_dry_adiabatic_colour: Colou of the dry_adiabatics. The possible values:

        * background
        The default is: charcoal.
    :type thermo_dry_adiabatic_colour: str


    :param thermo_dry_adiabatic_thickness: Thickness  of the dry_adiabatics. The default is: 1.
    :type thermo_dry_adiabatic_thickness: int


    :param thermo_dry_adiabatic_style: Line Style  of the dry_adiabatics. The possible values:

        * solid
        * dash
        * dot
        * chain_dot
        * chain_dash
        The default is: solid.
    :type thermo_dry_adiabatic_style: str


    :param thermo_dry_adiabatic_interval: Interval between 2 dry_adiabatics. The default is: 10.
    :type thermo_dry_adiabatic_interval: number


    :param thermo_dry_adiabatic_reference: Reference   of the dry_adiabatics. The default is: 0.
    :type thermo_dry_adiabatic_reference: number


    :param thermo_dry_adiabatic_label_colour: Label Colour for the isotherms. The possible values:

        * background
        The default is: charcoal.
    :type thermo_dry_adiabatic_label_colour: str


    :param thermo_dry_adiabatic_label_font_name: 
    :type thermo_dry_adiabatic_label_font_name: str


    :param thermo_dry_adiabatic_label_font_style: Font Style used for the dry_adiabatics labels. The possible values:

        * normal
        * bold
        * italic
        * bolditalic
        The default is: normal.
    :type thermo_dry_adiabatic_label_font_style: str


    :param thermo_dry_adiabatic_label_font_size: Font Size used for the dry_adiabatics labels. The default is: 0.3.
    :type thermo_dry_adiabatic_label_font_size: number


    :param thermo_dry_adiabatic_label_frequency: frequency for dry_adiabatic labelling. The default is: 1.
    :type thermo_dry_adiabatic_label_frequency: number


    :param thermo_saturated_adiabatic_grid: Plot the saturated_adiabatics. The possible values:

        * on
        * off
        The default is: on.
    :type thermo_saturated_adiabatic_grid: str


    :param thermo_saturated_adiabatic_colour: Colou of the saturated_adiabatics. The possible values:

        * background
        The default is: charcoal.
    :type thermo_saturated_adiabatic_colour: str


    :param thermo_saturated_adiabatic_thickness: Thickness  of the dry_adiabatics. The default is: 2.
    :type thermo_saturated_adiabatic_thickness: int


    :param thermo_saturated_adiabatic_style: Line Style  of the saturated_adiabatics. The possible values:

        * solid
        * dash
        * dot
        * chain_dot
        * chain_dash
        The default is: solid.
    :type thermo_saturated_adiabatic_style: str


    :param thermo_saturated_adiabatic_interval: interval for saturated_adiabatics grid. The default is: 5.
    :type thermo_saturated_adiabatic_interval: number


    :param thermo_saturated_adiabatic_reference: Reference   of the saturated_adiabatics. The default is: 0.
    :type thermo_saturated_adiabatic_reference: number


    :param thermo_saturated_adiabatic_label_colour: Label Colour for the isotherms. The possible values:

        * background
        The default is: charcoal.
    :type thermo_saturated_adiabatic_label_colour: str


    :param thermo_saturated_adiabatic_label_font_name: 
    :type thermo_saturated_adiabatic_label_font_name: str


    :param thermo_saturated_adiabatic_label_font_style: Font Style used for the saturated_adiabatics labels. The possible values:

        * normal
        * bold
        * italic
        * bolditalic
        The default is: normal.
    :type thermo_saturated_adiabatic_label_font_style: str


    :param thermo_saturated_adiabatic_label_font_size: Font Size used for the saturated_adiabatics labels. The default is: 0.3.
    :type thermo_saturated_adiabatic_label_font_size: number


    :param thermo_saturated_adiabatic_label_frequency: saturated_adiabatic frequency for labelling. The default is: 1.
    :type thermo_saturated_adiabatic_label_frequency: number


    :param thermo_mixing_ratio_grid: Plot the mixing_ratios. The possible values:

        * on
        * off
        The default is: on.
    :type thermo_mixing_ratio_grid: str


    :param thermo_mixing_ratio_colour: Colou of the mixing_ratios. The possible values:

        * background
        The default is: purple.
    :type thermo_mixing_ratio_colour: str


    :param thermo_mixing_ratio_thickness: Thickness  of the mixing_ratios. The default is: 1.
    :type thermo_mixing_ratio_thickness: int


    :param thermo_mixing_ratio_style: Line Style  of the mixing_ratios. The possible values:

        * solid
        * dash
        * dot
        * chain_dot
        * chain_dash
        The default is: dash.
    :type thermo_mixing_ratio_style: str


    :param thermo_mixing_ratio_frequency: mixing_ratio frequency for grid. The default is: 1.
    :type thermo_mixing_ratio_frequency: number


    :param thermo_mixing_ratio_label_colour: Label Colour for the isotherms. The possible values:

        * background
        The default is: purple.
    :type thermo_mixing_ratio_label_colour: str


    :param thermo_mixing_ratio_label_font_name: 
    :type thermo_mixing_ratio_label_font_name: str


    :param thermo_mixing_ratio_label_font_style: Font Style used for the mixing_ratios labels. The possible values:

        * normal
        * bold
        * italic
        * bolditalic
        The default is: normal.
    :type thermo_mixing_ratio_label_font_style: str


    :param thermo_mixing_ratio_label_font_size: Font Size used for the mixing_ratios labels. The default is: 0.3.
    :type thermo_mixing_ratio_label_font_size: number


    :param thermo_mixing_ratio_label_frequency: mixing_ratio frequency for labelling. The default is: 1.
    :type thermo_mixing_ratio_label_frequency: number


    :rtype: None


.. minigallery:: metview.mthermogrid
    :add-heading:

