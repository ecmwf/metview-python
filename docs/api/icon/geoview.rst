
geoview
=========================

.. container::
    
    .. container:: leftside

        .. image:: /_static/GEOVIEW.png
           :width: 48px

    .. container:: rightside

        This function performs the same task as the `Geographical View <https://confluence.ecmwf.int/display/METV/Geographical+View>`_ icon in Metview’s user interface. It accepts its parameters as keyword arguments, described below.


.. py:function:: geoview(**kwargs)
  
    Description comes here!


    :param coastlines: 
    :type coastlines: str


    :param area_mode: 
    :type area_mode: {"name", "user"}, default: "user"


    :param area_name: 
    :type area_name: {"antarctic", "arctic", "australasia", "central_america", "central_europe", "east_tropic", "eastern_asia", "equatorial_pacific", "eurasia", "europe", "global", "middle_east_and_india", "north_america", "north_atlantic", "north_east_europe", "north_pole", "north_west_europe", "northern_africa", "pacific", "south_america", "south_atlantic_and_indian_ocean", "south_east_asia_and_indonesia", "south_east_europe", "south_pole", "south_west_europe", "southern_africa", "southern_asia", "west_tropic", "western_asia"}, default: "europe"


    :param map_projection: 
    :type map_projection: {"cylindrical", "bonne", "collignon", "epsg:4326", "epsg:3857", "geos", "goode", "lambert", "lambert_north_atlantic", "mercator", "mollweide", "polar_north", "polar_south", "polar_stereographic", "robinson", "tpers"}, default: "cylindrical"


    :param map_area_definition: 
    :type map_area_definition: {"corners", "centre", "full"}, default: "full"


    :param area: 
    :type area: float or list[float], default: -90


    :param map_hemisphere: 
    :type map_hemisphere: {"north", "south"}, default: "north"


    :param map_vertical_longitude: 
    :type map_vertical_longitude: number, default: 0


    :param map_centre_latitude: 
    :type map_centre_latitude: str, default: "45.0"


    :param map_centre_longitude: 
    :type map_centre_longitude: str, default: "0.0"


    :param map_scale: 
    :type map_scale: str, default: "130.0e4"


    :param map_projection_height: 
    :type map_projection_height: str, default: "42164000"


    :param map_projection_tilt: 
    :type map_projection_tilt: str, default: "0.0"


    :param map_projection_azimuth: 
    :type map_projection_azimuth: str, default: "20.0"


    :param map_projection_view_latitude: 
    :type map_projection_view_latitude: str, default: "20.0"


    :param map_projection_view_longitude: 
    :type map_projection_view_longitude: str, default: "-60.0"


    :param map_overlay_control: 
    :type map_overlay_control: {"always", "by_date", "by_level", "never"}, default: "always"


    :param subpage_clipping: 
    :type subpage_clipping: {"on", "off"}, default: "off"


    :param subpage_x_position: 
    :type subpage_x_position: str, default: "7.5"


    :param subpage_y_position: 
    :type subpage_y_position: str, default: "5"


    :param subpage_x_length: 
    :type subpage_x_length: str, default: "85"


    :param subpage_y_length: 
    :type subpage_y_length: str, default: "85"


    :param subpage_metadata_info: 
    :type subpage_metadata_info: {"on", "off"}, default: "off"


    :param subpage_metadata_javascript_path: 
    :type subpage_metadata_javascript_path: str, default: "map.js"


    :param page_frame: 
    :type page_frame: {"on", "off"}, default: "off"


    :param page_frame_colour: 
    :type page_frame_colour: str, default: "charcoal"


    :param page_frame_line_style: 
    :type page_frame_line_style: {"solid", "dot", "dash", "chain_dot", "chain_dash"}, default: "solid"


    :param page_frame_thickness: 
    :type page_frame_thickness: int, default: 2


    :param page_id_line: 
    :type page_id_line: {"on", "off"}, default: "off"


    :param page_id_line_user_text: 
    :type page_id_line_user_text: str


    :param subpage_frame: 
    :type subpage_frame: {"on", "off"}, default: "on"


    :param subpage_frame_colour: 
    :type subpage_frame_colour: str, default: "black"


    :param subpage_frame_line_style: 
    :type subpage_frame_line_style: {"solid", "dot", "dash", "chain_dot", "chain_dash"}, default: "solid"


    :param subpage_frame_thickness: 
    :type subpage_frame_thickness: int, default: 2


    :param subpage_background_colour: 
    :type subpage_background_colour: str, default: "none"


    :rtype: None


.. minigallery:: metview.geoview
    :add-heading:

