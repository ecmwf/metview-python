
mcoast
=========================

.. container::
    
    .. container:: leftside

        .. image:: /_static/MCOAST.png
           :width: 48px

    .. container:: rightside

        This icon performs an ODB/SQL query on an ODB database (ODB-1) or file (ODB-2). The result is always an ODB file (in ODB-2 format).


.. py:function:: mcoast(**kwargs)
  
    Description comes here!


    :param map_coastline: 
    :type map_coastline: str


    :param map_coastline_colour: 
    :type map_coastline_colour: str


    :param map_coastline_style: 
    :type map_coastline_style: str


    :param map_coastline_thickness: 
    :type map_coastline_thickness: int


    :param map_coastline_resolution: 
    :type map_coastline_resolution: str


    :param map_coastline_land_shade: 
    :type map_coastline_land_shade: str


    :param map_coastline_land_shade_colour: 
    :type map_coastline_land_shade_colour: str


    :param map_coastline_sea_shade: 
    :type map_coastline_sea_shade: str


    :param map_coastline_sea_shade_colour: 
    :type map_coastline_sea_shade_colour: str


    :param map_boundaries: 
    :type map_boundaries: str


    :param map_rivers: 
    :type map_rivers: str


    :param map_rivers_style: 
    :type map_rivers_style: str


    :param map_rivers_colour: 
    :type map_rivers_colour: str


    :param map_rivers_thickness: 
    :type map_rivers_thickness: int


    :param map_cities: 
    :type map_cities: str


    :param map_cities_font_name: 
    :type map_cities_font_name: str


    :param map_cities_font_style: 
    :type map_cities_font_style: str


    :param map_cities_font_size: 
    :type map_cities_font_size: number


    :param map_cities_unit_system: 
    :type map_cities_unit_system: str


    :param map_cities_font_colour: 
    :type map_cities_font_colour: str


    :param map_cities_text_blanking: 
    :type map_cities_text_blanking: str


    :param map_cities_name_position: 
    :type map_cities_name_position: str


    :param map_cities_marker: 
    :type map_cities_marker: str


    :param map_cities_marker_height: 
    :type map_cities_marker_height: number


    :param map_cities_marker_colour: 
    :type map_cities_marker_colour: str


    :param map_boundaries_style: 
    :type map_boundaries_style: str


    :param map_boundaries_colour: 
    :type map_boundaries_colour: str


    :param map_boundaries_thickness: 
    :type map_boundaries_thickness: int


    :param map_disputed_boundaries: 
    :type map_disputed_boundaries: str


    :param map_disputed_boundaries_style: 
    :type map_disputed_boundaries_style: str


    :param map_disputed_boundaries_colour: 
    :type map_disputed_boundaries_colour: str


    :param map_disputed_boundaries_thickness: 
    :type map_disputed_boundaries_thickness: int


    :param map_administrative_boundaries: 
    :type map_administrative_boundaries: str


    :param map_administrative_boundaries_countries_list: 
    :type map_administrative_boundaries_countries_list: str or list[str]


    :param map_administrative_boundaries_style: 
    :type map_administrative_boundaries_style: str


    :param map_administrative_boundaries_colour: 
    :type map_administrative_boundaries_colour: str


    :param map_administrative_boundaries_thickness: 
    :type map_administrative_boundaries_thickness: int


    :param map_grid: 
    :type map_grid: str


    :param map_grid_line_style: 
    :type map_grid_line_style: str


    :param map_grid_thickness: 
    :type map_grid_thickness: int


    :param map_grid_colour: 
    :type map_grid_colour: str


    :param map_grid_latitude_reference: 
    :type map_grid_latitude_reference: number


    :param map_grid_latitude_increment: 
    :type map_grid_latitude_increment: number


    :param map_grid_longitude_reference: 
    :type map_grid_longitude_reference: number


    :param map_grid_longitude_increment: 
    :type map_grid_longitude_increment: number


    :param map_grid_frame: 
    :type map_grid_frame: str


    :param map_grid_frame_line_style: 
    :type map_grid_frame_line_style: str


    :param map_grid_frame_thickness: 
    :type map_grid_frame_thickness: int


    :param map_grid_frame_colour: 
    :type map_grid_frame_colour: str


    :param map_label: 
    :type map_label: str


    :param map_label_font: 
    :type map_label_font: str


    :param map_label_font_style: 
    :type map_label_font_style: str


    :param map_label_colour: 
    :type map_label_colour: str


    :param map_label_height: 
    :type map_label_height: number


    :param map_label_blanking: 
    :type map_label_blanking: str


    :param map_label_latitude_frequency: 
    :type map_label_latitude_frequency: number


    :param map_label_longitude_frequency: 
    :type map_label_longitude_frequency: number


    :param map_label_left: 
    :type map_label_left: str


    :param map_label_right: 
    :type map_label_right: str


    :param map_label_top: 
    :type map_label_top: str


    :param map_label_bottom: 
    :type map_label_bottom: str


    :param map_user_layer: 
    :type map_user_layer: str


    :param map_user_layer_name: 
    :type map_user_layer_name: str


    :param map_user_layer_colour: 
    :type map_user_layer_colour: str


    :param map_user_layer_style: 
    :type map_user_layer_style: str


    :param map_user_layer_thickness: 
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

