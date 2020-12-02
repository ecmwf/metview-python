
mobs
=========================

.. container::
    
    .. container:: leftside

        .. image:: /_static/MOBS.png
           :width: 48px

    .. container:: rightside

        This function performs the same task as the `Observation Plotting <https://confluence.ecmwf.int/display/METV/Observation+Plotting>`_ icon in Metview’s user interface. It accepts its parameters as keyword arguments, described below.


.. py:function:: mobs(**kwargs)
  
    Description comes here!


    :param obs_distance_apart: Minimum distance between the centre of any two observations in cm
    :type obs_distance_apart: number, default: 1.0


    :param obs_level: 
    :type obs_level: number, default: 500


    :param obs_colour: Observation Colour
    :type obs_colour: str, default: "black"


    :param obs_size: size of a single onservation in cm
    :type obs_size: number, default: 0.2


    :param obs_ring_size: Size of the station ring  in cm
    :type obs_ring_size: number, default: 0.2


    :param obs_present_weather: Turn "on"/"off" the present weather
    :type obs_present_weather: {"on", "off"}, default: "on"


    :param obs_present_weather_colour: Colour used to display  the present weather
    :type obs_present_weather_colour: str, default: "automatic"


    :param obs_pressure: Turn "on"/"off" the pressure
    :type obs_pressure: {"on", "off"}, default: "on"


    :param obs_pressure_colour: Colour used to display the pressure
    :type obs_pressure_colour: str, default: "automatic"


    :param obs_upper_air_pressure: Turn "on"/"off" the upper air pressure level (satob)
    :type obs_upper_air_pressure: {"on", "off"}, default: "off"


    :param obs_upper_air_pressure_colour: Colour used to display the upper air pressure level
    :type obs_upper_air_pressure_colour: str, default: "automatic"


    :param obs_pressure_tendency: Turn "on"/"off" the pressure tendency
    :type obs_pressure_tendency: {"on", "off"}, default: "on"


    :param obs_pressure_tendency_colour: Colour used to display the pressure tendency
    :type obs_pressure_tendency_colour: str, default: "automatic"


    :param obs_station_ring: Turn "on"/"off" the station ring
    :type obs_station_ring: {"on", "off"}, default: "on"


    :param obs_station_ring_colour: Colour used to display the station ring
    :type obs_station_ring_colour: str, default: "automatic"


    :param obs_temperature: Turn "on"/"off" the Air temperature
    :type obs_temperature: {"on", "off"}, default: "on"


    :param obs_temperature_colour: Colour  used to display the Air temperature
    :type obs_temperature_colour: str, default: "automatic"


    :param obs_thickness: Turn On/off the Thickness
    :type obs_thickness: int, default: on


    :param obs_thickness_colour: Colour  used to display the thickness
    :type obs_thickness_colour: str, default: "automatic"


    :param obs_height: Turn "on"/"off" the height (geopotential)
    :type obs_height: {"on", "off"}, default: "on"


    :param obs_height_colour: Colour  used to display  the height information
    :type obs_height_colour: str, default: "automatic"


    :param obs_identification: Turn "on"/"off" the station identification
    :type obs_identification: {"on", "off"}, default: "off"


    :param obs_identification_colour: Colour  used to display  the station identification
    :type obs_identification_colour: str, default: "automatic"


    :param obs_cloud: Turn "on"/"off" the cloud
    :type obs_cloud: {"on", "off"}, default: "on"


    :param obs_low_cloud: Turn "on"/"off" the low cloud
    :type obs_low_cloud: {"on", "off"}, default: "on"


    :param obs_low_cloud_colour: Colour used to display the low cloud
    :type obs_low_cloud_colour: str, default: "automatic"


    :param obs_medium_cloud: Turn "on"/"off" the medium cloud
    :type obs_medium_cloud: {"on", "off"}, default: "on"


    :param obs_medium_cloud_colour: Colour used to display the  medium cloud
    :type obs_medium_cloud_colour: str, default: "automatic"


    :param obs_high_cloud: Turn "on"/"off" the high cloud
    :type obs_high_cloud: {"on", "off"}, default: "on"


    :param obs_high_cloud_colour: Colour used to display the high cloud
    :type obs_high_cloud_colour: str, default: "red"


    :param obs_dewpoint: Turn "on"/"off" the dewpoint
    :type obs_dewpoint: {"on", "off"}, default: "on"


    :param obs_dewpoint_colour: Colour used to display the dewpoint
    :type obs_dewpoint_colour: str, default: "red"


    :param obs_sea_temperature: Turn "on"/"off" the sea temperature
    :type obs_sea_temperature: {"on", "off"}, default: "on"


    :param obs_sea_temperature_colour: Colour sed to display the sea temperature
    :type obs_sea_temperature_colour: str, default: "black"


    :param obs_waves: Turn "on"/"off" the waves and swell information
    :type obs_waves: {"on", "off"}, default: "on"


    :param obs_waves_colour: Colour used to display  the waves and swell
    :type obs_waves_colour: str, default: "black"


    :param obs_past_weather: Turn "on"/"off" the pas Weather level (satob)
    :type obs_past_weather: {"on", "off"}, default: "on"


    :param obs_past_weather_colour: Colour  used to display  the past weather
    :type obs_past_weather_colour: str, default: "red"


    :param obs_time: Turn "on"/"off" the observation time
    :type obs_time: {"on", "off"}, default: "off"


    :param obs_time_colour: Colour used to display the observation time
    :type obs_time_colour: str, default: "automatic"


    :param obs_visibility: Turn "on"/"off" the visibility
    :type obs_visibility: {"on", "off"}, default: "on"


    :param obs_visibility_colour: Colour  used to display  the visibility
    :type obs_visibility_colour: str, default: "automatic"


    :param obs_wind: Turn "on"/"off" the wind
    :type obs_wind: {"on", "off"}, default: "on"


    :param obs_wind_colour: Colour used to display wind
    :type obs_wind_colour: str, default: "automatic"


    :param obs_wind_projected: if "on" (default), the wind will be reprojected according to the projection used in the map.
    :type obs_wind_projected: {"on", "off"}, default: "on"


    :rtype: None


.. minigallery:: metview.mobs
    :add-heading:

