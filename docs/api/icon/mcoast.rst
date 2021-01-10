
mcoast
=========================

.. container::
    
    .. container:: leftside

        .. image:: /_static/MCOAST.png
           :width: 48px

    .. container:: rightside

		This is the visual definition for specifying how a map is displayed in a :func:`geoview`. It controls features such as coastlines, land and sea shading and grid lines.


		.. note:: This function performs the same task as the `Coastlines <https://confluence.ecmwf.int/display/METV/Coastlines>`_ icon in Metview’s user interface. It accepts its parameters as keyword arguments, described below.


.. py:function:: mcoast(**kwargs)
  
    Specifies the map style for a :func:`geoview`.


    :param map_coastline: Plot coastlines onto the map.
    :type map_coastline: {"on", "off"}, default: "on"

    :param map_coastline_colour: Colour of coastlines.
    :type map_coastline_colour: str, default: "black"

    :param map_coastline_style: Line style of coastlines.
    :type map_coastline_style: {"solid", "dash", "dot", "chain_dot", "chain_dash"}, default: "solid"

    :param map_coastline_thickness: Line thickness of coastlines.
    :type map_coastline_thickness: int, default: 1

    :param map_coastline_resolution: Select one of the pre-defined resolutions. When set to "automatic", a resolution appropriate to the scale of the map is chosen in order to balance quality with speed.
    :type map_coastline_resolution: {"automatic", "low", "medium", "high", "full"}, default: "automatic"

    :param map_coastline_land_shade: Sets if land areas are shaded.
    :type map_coastline_land_shade: {"on", "off"}, default: "off"

    :param map_coastline_land_shade_colour: Colour of shading of land areas.
    :type map_coastline_land_shade_colour: str, default: "green"

    :param map_coastline_sea_shade: Sets if sea areas are shaded.
    :type map_coastline_sea_shade: {"on", "off"}, default: "off"

    :param map_coastline_sea_shade_colour: Colour of shading of sea areas.
    :type map_coastline_sea_shade_colour: str, default: "blue"

    :param map_boundaries: Plots political boundaries.
    :type map_boundaries: {"on", "off"}, default: "off"

    :param map_rivers: Plots rivers.
    :type map_rivers: {"on", "off"}, default: "off"

    :param map_rivers_style: Line style for rivers.
    :type map_rivers_style: {"solid", "dash", "dot", "chain_dot", "chain_dash"}, default: "solid"

    :param map_rivers_colour: Colour of the rivers.
    :type map_rivers_colour: str, default: "blue"

    :param map_rivers_thickness: Line thickness of the rivers.
    :type map_rivers_thickness: int, default: 1

    :param map_cities: Plots cities (capitals only).
    :type map_cities: {"on", "off"}, default: "off"

    :param map_cities_font_name: Defines the font type for cities.
    :type map_cities_font_name: {"arial", "courier", "helvetica", "times", "serif", "sansserif", "symbol"}, default: "sansserif"

    :param map_cities_font_style: Defines the font style for cities.
    :type map_cities_font_style: {"normal", "bold", "italic", "bolditalic"}, default: "normal"

    :param map_cities_font_size: Font size of city names.
    :type map_cities_font_size: number, default: 2.5

    :param map_cities_unit_system: Units for ``map_cities_font_size``.
    :type map_cities_unit_system: {"percent", "cm"}, default: "percent"

    :param map_cities_font_colour: Colour used for city names.
    :type map_cities_font_colour: str, default: "navy"

    :param map_cities_text_blanking: Use blanking when plotting the city names.
    :type map_cities_text_blanking: {"on", "off"}, default: "on"

    :param map_cities_name_position: Position where to display the city names around their locations.
    :type map_cities_name_position: {"above", "below", "left", "right"}, default: "above"

    :param map_cities_marker: Defines marker for cities.
    :type map_cities_marker: {"circle", "box", "snowflake", "plus"}, default: "plus"

    :param map_cities_marker_height: Height of ``map_cities_marker``.
    :type map_cities_marker_height: number, default: 0.7

    :param map_cities_marker_colour: Colour for ``map_cities_marker``.
    :type map_cities_marker_colour: str, default: "evergreen"

    :param map_boundaries_style: Line style of map boundaries.
    :type map_boundaries_style: {"solid", "dash", "dot", "chain_dot", "chain_dash"}, default: "solid"

    :param map_boundaries_colour: Colour of map boundaries.
    :type map_boundaries_colour: str, default: "grey"

    :param map_boundaries_thickness: Line thickness of map boundaries.
    :type map_boundaries_thickness: int, default: 1

    :param map_disputed_boundaries: Plot disputed boundaries onto the map.
    :type map_disputed_boundaries: {"on", "off"}, default: "on"

    :param map_disputed_boundaries_style: Line style of disputed boundaries.
    :type map_disputed_boundaries_style: {"solid", "dash", "dot", "chain_dot", "chain_dash"}, default: "dash"

    :param map_disputed_boundaries_colour: Colour of disputed boundaries.
    :type map_disputed_boundaries_colour: str, default: "automatic"

    :param map_disputed_boundaries_thickness: Line thickness of disputed boundaries.
    :type map_disputed_boundaries_thickness: int, default: 1

    :param map_administrative_boundaries: Plots administrative boundaries into the map.
    :type map_administrative_boundaries: {"on", "off"}, default: "off"

    :param map_administrative_boundaries_countries_list: List of countries whose administrative boundaries will be plotted.
    :type map_administrative_boundaries_countries_list: str or list[str]

    :param map_administrative_boundaries_style: Line style for administrative boundaries.
    :type map_administrative_boundaries_style: {"solid", "dash", "dot", "chain_dot", "chain_dash"}, default: "dash"

    :param map_administrative_boundaries_colour: Colour of administrative boundaries.
    :type map_administrative_boundaries_colour: str, default: "automatic"

    :param map_administrative_boundaries_thickness: Line thickness of administrative boundaries.
    :type map_administrative_boundaries_thickness: int, default: 1

    :param map_grid: Plots grid lines onto the map.
    :type map_grid: {"on", "off"}, default: "on"

    :param map_grid_line_style: Line style of map grid lines.
    :type map_grid_line_style: {"solid", "dash", "dot", "chain_dot", "chain_dash"}, default: "solid"

    :param map_grid_thickness: Thickness of map grid lines.
    :type map_grid_thickness: int, default: 1

    :param map_grid_colour: Colour of map grid lines.
    :type map_grid_colour: str, default: "black"

    :param map_grid_latitude_reference: Reference latitude from which all latitude grid lines are drawn.
    :type map_grid_latitude_reference: number, default: 0

    :param map_grid_latitude_increment: Interval (in degrees) between latitude grid lines.
    :type map_grid_latitude_increment: number, default: 10

    :param map_grid_longitude_reference: Reference longitude from which all longitude lines are drawn.
    :type map_grid_longitude_reference: number, default: 0

    :param map_grid_longitude_increment: Interval (in degrees) between longitude grid lines.
    :type map_grid_longitude_increment: number, default: 20

    :param map_grid_frame: Add a frame around the map.
    :type map_grid_frame: {"on", "off"}, default: "off"

    :param map_grid_frame_line_style: Line style of map grid lines.
    :type map_grid_frame_line_style: {"solid", "dash", "dot", "chain_dot", "chain_dash"}, default: "solid"

    :param map_grid_frame_thickness: Thickness of map grid lines.
    :type map_grid_frame_thickness: int, default: 1

    :param map_grid_frame_colour: Colour of map grid lines.
    :type map_grid_frame_colour: str, default: "black"

    :param map_label: Plots labels for map grid lines.
    :type map_label: {"on", "off"}, default: "on"

    :param map_label_font: Font of map grid labels.
    :type map_label_font: {"arial", "courier", "helvetica", "times", "serif", "sansserif", "symbol"}, default: "sansserif"

    :param map_label_font_style: Font of map grid labels.
    :type map_label_font_style: {"normal", "bold", "italic", "bolditalic"}, default: "normal"

    :param map_label_colour: Colour of map grid labels.
    :type map_label_colour: str, default: "black"

    :param map_label_height: Height of map grid labels.
    :type map_label_height: number, default: 0.25

    :param map_label_blanking: Blanking of the grid labels.
    :type map_label_blanking: {"on", "off"}, default: "on"

    :param map_label_latitude_frequency: Every n-th latitude grid line is labelled.
    :type map_label_latitude_frequency: number, default: 1

    :param map_label_longitude_frequency: Every n-th longitude grid line is labelled.
    :type map_label_longitude_frequency: number, default: 1

    :param map_label_left: Enable the labels on the left of the map.
    :type map_label_left: {"on", "off"}, default: "on"

    :param map_label_right: Enable the labels on the right of the map.
    :type map_label_right: {"on", "off"}, default: "on"

    :param map_label_top: Enable the labels on the top of the map.
    :type map_label_top: {"on", "off"}, default: "on"

    :param map_label_bottom: Enable the labels on the bottom of the map.
    :type map_label_bottom: {"on", "off"}, default: "on"

    :param map_user_layer: Display user shape file layer.
    :type map_user_layer: {"on", "off"}, default: "off"

    :param map_user_layer_name: Path to the shape file to use.
    :type map_user_layer_name: str

    :param map_user_layer_colour: Colour of the user layer.
    :type map_user_layer_colour: str, default: "blue"

    :param map_user_layer_style: Line style of the user layer.
    :type map_user_layer_style: {"solid", "dash", "dot", "chain_dot", "chain_dash"}, default: "solid"

    :param map_user_layer_thickness: Line thickness of the user layer.
    :type map_user_layer_thickness: int, default: 1

    :param map_layer_mode: Specifies how the background (land-sea shading) and foreground (grid, coastlines, rivers, borders and cities) map layers are rendered into the plot with respect to the data layers. The possible values are as follows:
		
		* "split": the coastlines definition is split into background and foreground map layers. The background map layer is rendered first, followed by the data layers with the foreground map layers appearing atop
		* "foreground": all the map layers are rendered on top of the data layers
		* "background": all the map layers are rendered below the data layers
		If ``map_layer_mode`` is set to "split" and the :func:`mcoast` appears after the data objects in :func:`plot`, the coastlines are put on top of the data. This behaviour is required in order to maintain backward compatibility.
    :type map_layer_mode: {"split", "foreground", "background"}, default: "split"

    :rtype: :class:`Request`


.. minigallery:: metview.mcoast
    :add-heading:

