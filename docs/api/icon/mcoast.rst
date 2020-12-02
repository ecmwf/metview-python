
mcoast
=========================

.. container::
    
    .. container:: leftside

        .. image:: /_static/MCOAST.png
           :width: 48px

    .. container:: rightside

        This function performs the same task as the `Coastlines <https://confluence.ecmwf.int/display/METV/Coastlines>`_ icon in Metview’s user interface. It accepts its parameters as keyword arguments, described below.


.. py:function:: mcoast(**kwargs)
  
    Description comes here!


    :param map_coastline: Plot coastlines "on" map ("on"/"off")
    :type map_coastline: {"on", "off"}, default: "on"


    :param map_coastline_colour: Colour of coastlines
    :type map_coastline_colour: str, default: "black"


    :param map_coastline_style: Line style of coastlines
    :type map_coastline_style: {"solid", "dash", "dot", "chain_dot", "chain_dash"}, default: "solid"


    :param map_coastline_thickness: Line thickness of coastlines
    :type map_coastline_thickness: int, default: 1


    :param map_coastline_resolution: Select one of the pre-defined resolutions: "automatic", "low", "medium", and "high".  When set to "automatic", a resolution appropriate to the scale of the map is chosen in order to balance quality with speed.
    :type map_coastline_resolution: {"automatic", "low", "medium", "high", "full"}, default: "automatic"


    :param map_coastline_land_shade: Sets if land areas are shaded
    :type map_coastline_land_shade: {"on", "off"}, default: "off"


    :param map_coastline_land_shade_colour: Colour of Shading of land areas
    :type map_coastline_land_shade_colour: str, default: "green"


    :param map_coastline_sea_shade: Shade the sea areas
    :type map_coastline_sea_shade: {"on", "off"}, default: "off"


    :param map_coastline_sea_shade_colour: Colour of Shading of sea areas
    :type map_coastline_sea_shade_colour: str, default: "blue"


    :param map_boundaries: Add the political boundaries
    :type map_boundaries: {"on", "off"}, default: "off"


    :param map_rivers: Display rivers ("on"/"off")
    :type map_rivers: {"on", "off"}, default: "off"


    :param map_rivers_style: Line style for rivers
    :type map_rivers_style: {"solid", "dash", "dot", "chain_dot", "chain_dash"}, default: "solid"


    :param map_rivers_colour: Colour of the rivers
    :type map_rivers_colour: str, default: "blue"


    :param map_rivers_thickness: Line thickness of rivers
    :type map_rivers_thickness: int, default: 1


    :param map_cities: Add the cities (capitals)
    :type map_cities: {"on", "off"}, default: "off"


    :param map_cities_font_name: 
    :type map_cities_font_name: {"arial", "courier", "helvetica", "times", "serif", "sansserif", "symbol"}, default: "sansserif"


    :param map_cities_font_style: Font style used for city names.
    :type map_cities_font_style: {"normal", "bold", "italic", "bolditalic"}, default: "normal"


    :param map_cities_font_size: Font size of city names.
    :type map_cities_font_size: number, default: 2.5


    :param map_cities_unit_system: Unit for city name sizes.
    :type map_cities_unit_system: {"percent", "cm"}, default: "percent"


    :param map_cities_font_colour: Colour used for city names.
    :type map_cities_font_colour: str, default: "navy"


    :param map_cities_text_blanking: Use Blanking when plotting the cityes names .
    :type map_cities_text_blanking: {"on", "off"}, default: "on"


    :param map_cities_name_position: Position where to display the city names.
    :type map_cities_name_position: {"above", "below", "left", "right"}, default: "above"


    :param map_cities_marker: Marker for cities.
    :type map_cities_marker: {"circle", "box", "snowflake", "plus"}, default: "plus"


    :param map_cities_marker_height: Height of city markers.
    :type map_cities_marker_height: number, default: 0.7


    :param map_cities_marker_colour: Colour for city markers.
    :type map_cities_marker_colour: str, default: "evergreen"


    :param map_boundaries_style: Line style of boundaries.
    :type map_boundaries_style: {"solid", "dash", "dot", "chain_dot", "chain_dash"}, default: "solid"


    :param map_boundaries_colour: Colour of boundaries.
    :type map_boundaries_colour: str, default: "grey"


    :param map_boundaries_thickness: Line thickness of boundaries.
    :type map_boundaries_thickness: int, default: 1


    :param map_disputed_boundaries: Display the disputed boundaries.
    :type map_disputed_boundaries: {"on", "off"}, default: "on"


    :param map_disputed_boundaries_style: Line style of disputed boundaries.
    :type map_disputed_boundaries_style: {"solid", "dash", "dot", "chain_dot", "chain_dash"}, default: "dash"


    :param map_disputed_boundaries_colour: Colour of disputed boundaries.
    :type map_disputed_boundaries_colour: str, default: "automatic"


    :param map_disputed_boundaries_thickness: Line thickness of disputed boundaries.
    :type map_disputed_boundaries_thickness: int, default: 1


    :param map_administrative_boundaries: Display administrative boundaries.
    :type map_administrative_boundaries: {"on", "off"}, default: "off"


    :param map_administrative_boundaries_countries_list: 
    :type map_administrative_boundaries_countries_list: str or list[str]


    :param map_administrative_boundaries_style: 
    :type map_administrative_boundaries_style: {"solid", "dash", "dot", "chain_dot", "chain_dash"}, default: "dash"


    :param map_administrative_boundaries_colour: 
    :type map_administrative_boundaries_colour: str, default: "automatic"


    :param map_administrative_boundaries_thickness: 
    :type map_administrative_boundaries_thickness: int, default: 1


    :param map_grid: Plot grid lines "on" map ("on"/"off")
    :type map_grid: {"on", "off"}, default: "on"


    :param map_grid_line_style: Line style of map grid lines
    :type map_grid_line_style: {"solid", "dash", "dot", "chain_dot", "chain_dash"}, default: "solid"


    :param map_grid_thickness: Thickness of map grid lines
    :type map_grid_thickness: int, default: 1


    :param map_grid_colour: Colour of map grid lines
    :type map_grid_colour: str, default: "black"


    :param map_grid_latitude_reference: Reference Latitude from which all latitude lines are drawn
    :type map_grid_latitude_reference: number, default: 0


    :param map_grid_latitude_increment: Interval between latitude grid lines
    :type map_grid_latitude_increment: number, default: 10


    :param map_grid_longitude_reference: Reference Longitude from which all longitude lines are drawn
    :type map_grid_longitude_reference: number, default: 0


    :param map_grid_longitude_increment: Interval between longitude grid lines
    :type map_grid_longitude_increment: number, default: 20


    :param map_grid_frame: Add a frame around the projection
    :type map_grid_frame: {"on", "off"}, default: "off"


    :param map_grid_frame_line_style: Line style of map grid lines
    :type map_grid_frame_line_style: {"solid", "dash", "dot", "chain_dot", "chain_dash"}, default: "solid"


    :param map_grid_frame_thickness: Thickness of map grid lines
    :type map_grid_frame_thickness: int, default: 1


    :param map_grid_frame_colour: Colour of map grid lines
    :type map_grid_frame_colour: str, default: "black"


    :param map_label: Plot label  "on" map grid lines ("on"/"off")
    :type map_label: {"on", "off"}, default: "on"


    :param map_label_font: Font of grid labels
    :type map_label_font: {"arial", "courier", "helvetica", "times", "serif", "sansserif", "symbol"}, default: "sansserif"


    :param map_label_font_style: Font of grid labels
    :type map_label_font_style: {"normal", "bold", "italic", "bolditalic"}, default: "normal"


    :param map_label_colour: Colour of map labels
    :type map_label_colour: str, default: "black"


    :param map_label_height: Height og grid labels
    :type map_label_height: number, default: 0.25


    :param map_label_blanking: Blanking of the grid labels
    :type map_label_blanking: {"on", "off"}, default: "on"


    :param map_label_latitude_frequency: Evry Nth latitue grid is labelled
    :type map_label_latitude_frequency: number, default: 1


    :param map_label_longitude_frequency: Evry Nth longitude grid is labelled
    :type map_label_longitude_frequency: number, default: 1


    :param map_label_left: Enable the labels "on" the left of the map
    :type map_label_left: {"on", "off"}, default: "on"


    :param map_label_right: Enable the labels "on" the right of the map
    :type map_label_right: {"on", "off"}, default: "on"


    :param map_label_top: Enable the labels "on" the top of the map
    :type map_label_top: {"on", "off"}, default: "on"


    :param map_label_bottom: Enable the labels "on" the bottom of the map
    :type map_label_bottom: {"on", "off"}, default: "on"


    :param map_user_layer: Display user shape file layer
    :type map_user_layer: {"on", "off"}, default: "off"


    :param map_user_layer_name: Path + name of the shape file to use
    :type map_user_layer_name: str


    :param map_user_layer_colour: Colour of the User Layer
    :type map_user_layer_colour: str, default: "blue"


    :param map_user_layer_style: Line style for User Layer
    :type map_user_layer_style: {"solid", "dash", "dot", "chain_dot", "chain_dash"}, default: "solid"


    :param map_user_layer_thickness: Line thickness of User Layer
    :type map_user_layer_thickness: int, default: 1


    :param map_layer_mode: Specifies how the "background" (land-sea shading) and "foreground" (grid, coastlines, rivers, borders and cities) map layers are rendered into the plot with respect to the data layers. The possible values are as follows:

         *  "split" : the coastlines icon is "split" into "background" and "foreground" map layers. The "background" map layer is rendered first, followed by the data layers with the "foreground" map layers appearing atop
         *  "foreground" : all the map layers are rendered on top of the data layers
         *  "background" : all the map layers are rendered below the data layers

         The default value is "split".

         Script (Macro/Python) usage

         If ``map_layer_mode`` is set to "split" and the Coastlines icon appears after the data objects in the plot(...) command, the coastlines are put on top of the data. This behaviour is required in order to maintain backward compatibility.

         

         ## Adding a user-supplied shapefile as a layer

         If you have a shapefile with geographical polygons, this can be added to a plot via the Coastlines icon. The relevant parameters are ``map_user_layer`` , ``map_user_layer`` Name , ``map_user_layer`` Style , ``map_user_layer`` Colour and ``map_user_layer`` Thickness . To use an own shapefile, set ``map_user_layer`` to On , then set ``map_user_layer`` Name to the path to the shapefile, with the base file name of the file as the last element. For example if the path to the shapefile is /home/me/files and there is a shapefile called MyShape.shp in that directory, then we would set this parameter to /home/me/files/MyShape`.

         The following screenshot shows the result of loading a shapefile of UK roads into Metview:

         ![](/download/attachments/31920784/uk-roads- shapefile.png?version=1&modificationDate=1563196586094&api=v2)
    :type map_layer_mode: {"split", "foreground", "background"}, default: "split"


    :rtype: None


.. minigallery:: metview.mcoast
    :add-heading:

