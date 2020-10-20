
mcoast
=========================

.. container::
    
    .. container:: leftside

        .. image:: /_static/MCOAST.png
           :width: 48px

    .. container:: rightside

        This icon represents the `Coastlines <https://confluence.ecmwf.int/display/METV/Coastlines>`_ icon in Metview's user interface.


.. py:function:: mcoast(**kwargs)
  
    Description comes here!


    :param map_coastline: Plot coastlines on map (ON/OFF). The possible values:

        * on
        * off
        The default is: on.
    :type map_coastline: str


    :param map_coastline_colour: Colour of coastlines. The possible values:

        * background
        The default is: black.
    :type map_coastline_colour: str


    :param map_coastline_style: Line style of coastlines. The possible values:

        * solid
        * dash
        * dot
        * chain_dot
        * chain_dash
        The default is: solid.
    :type map_coastline_style: str


    :param map_coastline_thickness: Line thickness of coastlines. The default is: 1.
    :type map_coastline_thickness: int


    :param map_coastline_resolution: Select one of the pre-defined resolutions: automatic, low, medium, and high.  When set to AUTOMATIC, a resolution appropriate to the scale of the map is chosen in order to balance quality with speed. The possible values:

        * automatic
        * low
        * medium
        * high
        * full
        The default is: automatic.
    :type map_coastline_resolution: str


    :param map_coastline_land_shade: Sets if land areas are shaded. The possible values:

        * on
        * off
        The default is: off.
    :type map_coastline_land_shade: str


    :param map_coastline_land_shade_colour: Colour of Shading of land areas. The possible values:

        * background
        The default is: green.
    :type map_coastline_land_shade_colour: str


    :param map_coastline_sea_shade: Shade the sea areas. The possible values:

        * on
        * off
        The default is: off.
    :type map_coastline_sea_shade: str


    :param map_coastline_sea_shade_colour: Colour of Shading of sea areas. The possible values:

        * background
        The default is: blue.
    :type map_coastline_sea_shade_colour: str


    :param map_boundaries: Add the political boundaries. The possible values:

        * on
        * off
        The default is: off.
    :type map_boundaries: str


    :param map_rivers: Display rivers (on/off). The possible values:

        * on
        * off
        The default is: off.
    :type map_rivers: str


    :param map_rivers_style: Line style for rivers. The possible values:

        * solid
        * dash
        * dot
        * chain_dot
        * chain_dash
        The default is: solid.
    :type map_rivers_style: str


    :param map_rivers_colour: Colour of the rivers. The possible values:

        * background
        The default is: blue.
    :type map_rivers_colour: str


    :param map_rivers_thickness: Line thickness of rivers. The default is: 1.
    :type map_rivers_thickness: int


    :param map_cities: Add the cities (capitals). The possible values:

        * on
        * off
        The default is: off.
    :type map_cities: str


    :param map_cities_font_name: 
    :type map_cities_font_name: str


    :param map_cities_font_style: Font style used for city names. The possible values:

        * normal
        * bold
        * italic
        * bolditalic
        The default is: normal.
    :type map_cities_font_style: str


    :param map_cities_font_size: Font size of city names. The default is: 2.5.
    :type map_cities_font_size: number


    :param map_cities_unit_system: Unit for city name sizes. The possible values:

        * percent
        * cm
        The default is: percent.
    :type map_cities_unit_system: str


    :param map_cities_font_colour: Colour used for city names. The possible values:

        * background
        The default is: navy.
    :type map_cities_font_colour: str


    :param map_cities_text_blanking: Use Blanking when plotting the cityes names . The possible values:

        * on
        * off
        The default is: on.
    :type map_cities_text_blanking: str


    :param map_cities_name_position: Position where to display the city names. The possible values:

        * above
        * below
        * left
        * right
        The default is: above.
    :type map_cities_name_position: str


    :param map_cities_marker: Marker for cities. The possible values:

        * circle
        * box
        * snowflake
        * plus
        The default is: plus.
    :type map_cities_marker: str


    :param map_cities_marker_height: Height of city markers. The default is: 0.7.
    :type map_cities_marker_height: number


    :param map_cities_marker_colour: Colour for city markers. The possible values:

        * background
        The default is: evergreen.
    :type map_cities_marker_colour: str


    :param map_boundaries_style: Line style of boundaries. The possible values:

        * solid
        * dash
        * dot
        * chain_dot
        * chain_dash
        The default is: solid.
    :type map_boundaries_style: str


    :param map_boundaries_colour: Colour of boundaries. The possible values:

        * background
        The default is: grey.
    :type map_boundaries_colour: str


    :param map_boundaries_thickness: Line thickness of boundaries. The default is: 1.
    :type map_boundaries_thickness: int


    :param map_disputed_boundaries: Display the disputed boundaries. The possible values:

        * on
        * off
        The default is: on.
    :type map_disputed_boundaries: str


    :param map_disputed_boundaries_style: Line style of disputed boundaries. The possible values:

        * solid
        * dash
        * dot
        * chain_dot
        * chain_dash
        The default is: dash.
    :type map_disputed_boundaries_style: str


    :param map_disputed_boundaries_colour: Colour of disputed boundaries. The possible values:

        * background
        The default is: automatic.
    :type map_disputed_boundaries_colour: str


    :param map_disputed_boundaries_thickness: Line thickness of disputed boundaries. The default is: 1.
    :type map_disputed_boundaries_thickness: int


    :param map_administrative_boundaries: Display administrative boundaries. The possible values:

        * on
        * off
        The default is: off.
    :type map_administrative_boundaries: str


    :param map_administrative_boundaries_countries_list: 
    :type map_administrative_boundaries_countries_list: str or list[str]


    :param map_administrative_boundaries_style: 
    :type map_administrative_boundaries_style: str


    :param map_administrative_boundaries_colour: 
    :type map_administrative_boundaries_colour: str


    :param map_administrative_boundaries_thickness: 
    :type map_administrative_boundaries_thickness: int


    :param map_grid: Plot grid lines on map (On/OFF). The possible values:

        * on
        * off
        The default is: on.
    :type map_grid: str


    :param map_grid_line_style: Line style of map grid lines. The possible values:

        * solid
        * dash
        * dot
        * chain_dot
        * chain_dash
        The default is: solid.
    :type map_grid_line_style: str


    :param map_grid_thickness: Thickness of map grid lines. The default is: 1.
    :type map_grid_thickness: int


    :param map_grid_colour: Colour of map grid lines. The possible values:

        * background
        The default is: black.
    :type map_grid_colour: str


    :param map_grid_latitude_reference: Reference Latitude from which all latitude lines are drawn. The default is: 0.
    :type map_grid_latitude_reference: number


    :param map_grid_latitude_increment: Interval between latitude grid lines. The default is: 10.
    :type map_grid_latitude_increment: number


    :param map_grid_longitude_reference: Reference Longitude from which all longitude lines are drawn. The default is: 0.
    :type map_grid_longitude_reference: number


    :param map_grid_longitude_increment: Interval between longitude grid lines. The default is: 20.
    :type map_grid_longitude_increment: number


    :param map_grid_frame: Add a frame around the projection. The possible values:

        * on
        * off
        The default is: off.
    :type map_grid_frame: str


    :param map_grid_frame_line_style: Line style of map grid lines. The possible values:

        * solid
        * dash
        * dot
        * chain_dot
        * chain_dash
        The default is: solid.
    :type map_grid_frame_line_style: str


    :param map_grid_frame_thickness: Thickness of map grid lines. The default is: 1.
    :type map_grid_frame_thickness: int


    :param map_grid_frame_colour: Colour of map grid lines. The possible values:

        * background
        The default is: black.
    :type map_grid_frame_colour: str


    :param map_label: Plot label  on map grid lines (On/OFF). The possible values:

        * on
        * off
        The default is: on.
    :type map_label: str


    :param map_label_font: Font of grid labels. The possible values:

        * arial
        * courier
        * helvetica
        * times
        * serif
        * sansserif
        * symbol
        The default is: sansserif.
    :type map_label_font: str


    :param map_label_font_style: Font of grid labels. The possible values:

        * normal
        * bold
        * italic
        * bolditalic
        The default is: normal.
    :type map_label_font_style: str


    :param map_label_colour: Colour of map labels. The possible values:

        * background
        The default is: black.
    :type map_label_colour: str


    :param map_label_height: Height og grid labels. The default is: 0.25.
    :type map_label_height: number


    :param map_label_blanking: Blanking of the grid labels. The possible values:

        * on
        * off
        The default is: on.
    :type map_label_blanking: str


    :param map_label_latitude_frequency: Evry Nth latitue grid is labelled. The default is: 1.
    :type map_label_latitude_frequency: number


    :param map_label_longitude_frequency: Evry Nth longitude grid is labelled. The default is: 1.
    :type map_label_longitude_frequency: number


    :param map_label_left: Enable the labels on the left of the map. The possible values:

        * on
        * off
        The default is: on.
    :type map_label_left: str


    :param map_label_right: Enable the labels on the right of the map. The possible values:

        * on
        * off
        The default is: on.
    :type map_label_right: str


    :param map_label_top: Enable the labels on the top of the map. The possible values:

        * on
        * off
        The default is: on.
    :type map_label_top: str


    :param map_label_bottom: Enable the labels on the bottom of the map. The possible values:

        * on
        * off
        The default is: on.
    :type map_label_bottom: str


    :param map_user_layer: Display user shape file layer. The possible values:

        * on
        * off
        The default is: off.
    :type map_user_layer: str


    :param map_user_layer_name: Path + name of the shape file to use
    :type map_user_layer_name: str


    :param map_user_layer_colour: Colour of the User Layer. The possible values:

        * background
        The default is: blue.
    :type map_user_layer_colour: str


    :param map_user_layer_style: Line style for User Layer. The possible values:

        * solid
        * dash
        * dot
        * chain_dot
        * chain_dash
        The default is: solid.
    :type map_user_layer_style: str


    :param map_user_layer_thickness: Line thickness of User Layer. The default is: 1.
    :type map_user_layer_thickness: int


    :param map_layer_mode: Specifies how the background (land-sea shading) and foreground (grid, coastlines, rivers, borders and cities) map layers are rendered into the plot with respect to the data layers. The possible values are as follows:

         *  split : the coastlines icon is split into background and foreground map layers. The background map layer is rendered first, followed by the data layers with the foreground map layers appearing atop
         *  foreground : all the map layers are rendered on top of the data layers
         *  background : all the map layers are rendered below the data layers

         The default value is split.

         Script (Macro/Python) usage

         If ``map_layer_mode`` is set to split and the Coastlines icon appears after the data objects in the plot(...) command, the coastlines are put on top of the data. This behaviour is required in order to maintain backward compatibility.

         

         ## Adding a user-supplied shapefile as a layer

         If you have a shapefile with geographical polygons, this can be added to a plot via the Coastlines icon. The relevant parameters are ``map_user_layer`` , ``map_user_layer`` Name , ``map_user_layer`` Style , ``map_user_layer`` Colour and ``map_user_layer`` Thickness . To use an own shapefile, set ``map_user_layer`` to On , then set ``map_user_layer`` Name to the path to the shapefile, with the base file name of the file as the last element. For example if the path to the shapefile is /home/me/files and there is a shapefile called MyShape.shp in that directory, then we would set this parameter to /home/me/files/MyShape`.

         The following screenshot shows the result of loading a shapefile of UK roads into Metview:

         ![](/download/attachments/31920784/uk-roads- shapefile.png?version=1&modificationDate=1563196586094&api=v2)
    :type map_layer_mode: str


    :rtype: None


.. minigallery:: metview.mcoast
    :add-heading:

