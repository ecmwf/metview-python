
mobs
=========================

.. container::
    
    .. container:: leftside

        .. image:: /_static/MOBS.png
           :width: 48px

    .. container:: rightside

		This is the visual definition used for plotting conventional BUFR observations (i.e. SYNOP, SHIP, BUOY, TEMP) onto a map using the standard WMO graphical representation for station data.


		.. note:: This function performs the same task as the `Observation Plotting <https://confluence.ecmwf.int/display/METV/Observation+Plotting>`_ icon in Metview’s user interface. It accepts its parameters as keyword arguments, described below.


.. py:function:: mobs(**kwargs)
  
    Defines the style for plotting conventional observations in BUFR using the standard WMO graphical representation for station data.


    :param obs_distance_apart: Minimum distance between the centre of any two observations in cm. When it is set to 0 all the observations are plotted.
    :type obs_distance_apart: number, default: 1.0

    :param obs_level: Specifies the pressure level (in hPa) for upper air observations.
    :type obs_level: number, default: 500

    :param obs_colour: The observation colour.
    :type obs_colour: str, default: "black"

    :param obs_size: Size of a single observation in cm.
    :type obs_size: number, default: 0.2

    :param obs_ring_size: Size of the station ring in cm.
    :type obs_ring_size: number, default: 0.2

    :param obs_present_weather: Plots the present weather.
    :type obs_present_weather: {"on", "off"}, default: "on"

    :param obs_present_weather_colour: Colour of the present weather.
    :type obs_present_weather_colour: str, default: "automatic"

    :param obs_pressure: Plots the pressure.
    :type obs_pressure: {"on", "off"}, default: "on"

    :param obs_pressure_colour: Colour of the pressure.
    :type obs_pressure_colour: str, default: "automatic"

    :param obs_upper_air_pressure: Plots the upper air pressure level (satob).
    :type obs_upper_air_pressure: {"on", "off"}, default: "off"

    :param obs_upper_air_pressure_colour: Colour of the upper air pressure level.
    :type obs_upper_air_pressure_colour: str, default: "automatic"

    :param obs_pressure_tendency: Plots the pressure tendency.
    :type obs_pressure_tendency: {"on", "off"}, default: "on"

    :param obs_pressure_tendency_colour: Colour of the pressure tendency.
    :type obs_pressure_tendency_colour: str, default: "automatic"

    :param obs_station_ring: Plots the station ring.
    :type obs_station_ring: {"on", "off"}, default: "on"

    :param obs_station_ring_colour: Colour of the station ring.
    :type obs_station_ring_colour: str, default: "automatic"

    :param obs_temperature: Plots the air temperature.
    :type obs_temperature: {"on", "off"}, default: "on"

    :param obs_temperature_colour: Colour of the air temperature.
    :type obs_temperature_colour: str, default: "automatic"

    :param obs_thickness: Plots the thickness.
    :type obs_thickness: int, default: on

    :param obs_thickness_colour: Colour of the thickness.
    :type obs_thickness_colour: str, default: "automatic"

    :param obs_height: Plots the height (geopotential).
    :type obs_height: {"on", "off"}, default: "on"

    :param obs_height_colour: Colour of the height.
    :type obs_height_colour: str, default: "automatic"

    :param obs_identification: Plots the station identification.
    :type obs_identification: {"on", "off"}, default: "off"

    :param obs_identification_colour: Colour of the station identification.
    :type obs_identification_colour: str, default: "automatic"

    :param obs_cloud: Plots the cloud data.
    :type obs_cloud: {"on", "off"}, default: "on"

    :param obs_low_cloud: Plots the low cloud.
    :type obs_low_cloud: {"on", "off"}, default: "on"

    :param obs_low_cloud_colour: Colour of the low cloud.
    :type obs_low_cloud_colour: str, default: "automatic"

    :param obs_medium_cloud: Plots the medium cloud.
    :type obs_medium_cloud: {"on", "off"}, default: "on"

    :param obs_medium_cloud_colour: Colour of the medium cloud.
    :type obs_medium_cloud_colour: str, default: "automatic"

    :param obs_high_cloud: Plots the high cloud.
    :type obs_high_cloud: {"on", "off"}, default: "on"

    :param obs_high_cloud_colour: Colour of the high cloud.
    :type obs_high_cloud_colour: str, default: "red"

    :param obs_dewpoint: Plots the dewpoint.
    :type obs_dewpoint: {"on", "off"}, default: "on"

    :param obs_dewpoint_colour: Colour of the dewpoint.
    :type obs_dewpoint_colour: str, default: "red"

    :param obs_sea_temperature: Plots the sea temperature.
    :type obs_sea_temperature: {"on", "off"}, default: "on"

    :param obs_sea_temperature_colour: Colour of the sea temperature.
    :type obs_sea_temperature_colour: str, default: "black"

    :param obs_waves: Plots the waves and swell information.
    :type obs_waves: {"on", "off"}, default: "on"

    :param obs_waves_colour: Colour of the waves and swell.
    :type obs_waves_colour: str, default: "black"

    :param obs_past_weather: Plots the past weather.
    :type obs_past_weather: {"on", "off"}, default: "on"

    :param obs_past_weather_colour: Colour of the past weather.
    :type obs_past_weather_colour: str, default: "red"

    :param obs_time: Plots the observation time.
    :type obs_time: {"on", "off"}, default: "off"

    :param obs_time_colour: Colour of the observation time.
    :type obs_time_colour: str, default: "automatic"

    :param obs_visibility: Plots the visibility.
    :type obs_visibility: {"on", "off"}, default: "on"

    :param obs_visibility_colour: Colour of the visibility.
    :type obs_visibility_colour: str, default: "automatic"

    :param obs_wind: Plots the wind.
    :type obs_wind: {"on", "off"}, default: "on"

    :param obs_wind_colour: Colour of the wind.
    :type obs_wind_colour: str, default: "automatic"

    :param obs_wind_projected: If it is "on", the wind will be reprojected according to the projection used in the map.
    :type obs_wind_projected: {"on", "off"}, default: "on"

    :rtype: :class:`Request`


.. mv-minigallery:: mobs

