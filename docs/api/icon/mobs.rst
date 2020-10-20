
mobs
=========================

.. container::
    
    .. container:: leftside

        .. image:: /_static/MOBS.png
           :width: 48px

    .. container:: rightside

        This icon represents the `Observation Plotting <https://confluence.ecmwf.int/display/METV/Observation+Plotting>`_ icon in Metview's user interface.


.. py:function:: mobs(**kwargs)
  
    Description comes here!


    :param obs_distance_apart: Minimum distance between the centre of any two observations in cm. The default is: 1.0.
    :type obs_distance_apart: number


    :param obs_level: 
    :type obs_level: number


    :param obs_colour: Observation Colour. The possible values:

        * background
        The default is: black.
    :type obs_colour: str


    :param obs_size: size of a single onservation in cm. The default is: 0.2.
    :type obs_size: number


    :param obs_ring_size: Size of the station ring  in cm. The default is: 0.2.
    :type obs_ring_size: number


    :param obs_present_weather: Turn On/off the present weather. The possible values:

        * on
        * off
        The default is: on.
    :type obs_present_weather: str


    :param obs_present_weather_colour: Colour used to display  the present weather. The possible values:

        * background
        The default is: automatic.
    :type obs_present_weather_colour: str


    :param obs_pressure: Turn On/off the pressure. The possible values:

        * on
        * off
        The default is: on.
    :type obs_pressure: str


    :param obs_pressure_colour: Colour used to display the pressure. The possible values:

        * background
        The default is: automatic.
    :type obs_pressure_colour: str


    :param obs_upper_air_pressure: Turn On/off the upper air pressure level (satob). The possible values:

        * on
        * off
        The default is: off.
    :type obs_upper_air_pressure: str


    :param obs_upper_air_pressure_colour: Colour used to display the upper air pressure level. The possible values:

        * background
        The default is: automatic.
    :type obs_upper_air_pressure_colour: str


    :param obs_pressure_tendency: Turn On/off the pressure tendency. The possible values:

        * on
        * off
        The default is: on.
    :type obs_pressure_tendency: str


    :param obs_pressure_tendency_colour: Colour used to display the pressure tendency. The possible values:

        * background
        The default is: automatic.
    :type obs_pressure_tendency_colour: str


    :param obs_station_ring: Turn On/off the station ring. The possible values:

        * on
        * off
        The default is: on.
    :type obs_station_ring: str


    :param obs_station_ring_colour: Colour used to display the station ring. The possible values:

        * background
        The default is: automatic.
    :type obs_station_ring_colour: str


    :param obs_temperature: Turn On/off the Air temperature. The possible values:

        * on
        * off
        The default is: on.
    :type obs_temperature: str


    :param obs_temperature_colour: Colour  used to display the Air temperature. The possible values:

        * background
        The default is: automatic.
    :type obs_temperature_colour: str


    :param obs_thickness: Turn On/off the Thickness. The possible values:

        * on
        * off
        The default is: on.
    :type obs_thickness: str


    :param obs_thickness_colour: Colour  used to display the thickness. The possible values:

        * background
        The default is: automatic.
    :type obs_thickness_colour: str


    :param obs_height: Turn On/off the height (geopotential). The possible values:

        * on
        * off
        The default is: on.
    :type obs_height: str


    :param obs_height_colour: Colour  used to display  the height information. The possible values:

        * background
        The default is: automatic.
    :type obs_height_colour: str


    :param obs_identification: Turn On/off the station identification. The possible values:

        * on
        * off
        The default is: off.
    :type obs_identification: str


    :param obs_identification_colour: Colour  used to display  the station identification. The possible values:

        * background
        The default is: automatic.
    :type obs_identification_colour: str


    :param obs_cloud: Turn On/off the cloud. The possible values:

        * on
        * off
        The default is: on.
    :type obs_cloud: str


    :param obs_low_cloud: Turn On/off the low cloud. The possible values:

        * on
        * off
        The default is: on.
    :type obs_low_cloud: str


    :param obs_low_cloud_colour: Colour used to display the low cloud. The possible values:

        * background
        The default is: automatic.
    :type obs_low_cloud_colour: str


    :param obs_medium_cloud: Turn On/off the medium cloud. The possible values:

        * on
        * off
        The default is: on.
    :type obs_medium_cloud: str


    :param obs_medium_cloud_colour: Colour used to display the  medium cloud. The possible values:

        * background
        The default is: automatic.
    :type obs_medium_cloud_colour: str


    :param obs_high_cloud: Turn On/off the high cloud. The possible values:

        * on
        * off
        The default is: on.
    :type obs_high_cloud: str


    :param obs_high_cloud_colour: Colour used to display the high cloud. The possible values:

        * background
        The default is: red.
    :type obs_high_cloud_colour: str


    :param obs_dewpoint: Turn On/off the dewpoint. The possible values:

        * on
        * off
        The default is: on.
    :type obs_dewpoint: str


    :param obs_dewpoint_colour: Colour used to display the dewpoint. The possible values:

        * background
        The default is: red.
    :type obs_dewpoint_colour: str


    :param obs_sea_temperature: Turn On/off the sea temperature. The possible values:

        * on
        * off
        The default is: on.
    :type obs_sea_temperature: str


    :param obs_sea_temperature_colour: Colour sed to display the sea temperature. The possible values:

        * background
        The default is: black.
    :type obs_sea_temperature_colour: str


    :param obs_waves: Turn On/off the waves and swell information. The possible values:

        * on
        * off
        The default is: on.
    :type obs_waves: str


    :param obs_waves_colour: Colour used to display  the waves and swell. The possible values:

        * background
        The default is: black.
    :type obs_waves_colour: str


    :param obs_past_weather: Turn On/off the pas Weather level (satob). The possible values:

        * on
        * off
        The default is: on.
    :type obs_past_weather: str


    :param obs_past_weather_colour: Colour  used to display  the past weather. The possible values:

        * background
        The default is: red.
    :type obs_past_weather_colour: str


    :param obs_time: Turn On/off the observation time. The possible values:

        * on
        * off
        The default is: off.
    :type obs_time: str


    :param obs_time_colour: Colour used to display the observation time. The possible values:

        * background
        The default is: automatic.
    :type obs_time_colour: str


    :param obs_visibility: Turn On/off the visibility. The possible values:

        * on
        * off
        The default is: on.
    :type obs_visibility: str


    :param obs_visibility_colour: Colour  used to display  the visibility. The possible values:

        * background
        The default is: automatic.
    :type obs_visibility_colour: str


    :param obs_wind: Turn On/off the wind. The possible values:

        * on
        * off
        The default is: on.
    :type obs_wind: str


    :param obs_wind_colour: Colour used to display wind. The possible values:

        * background
        The default is: automatic.
    :type obs_wind_colour: str


    :param obs_wind_projected: if on (default), the wind will be reprojected according to the projection used in the map. The possible values:

        * on
        * off
        The default is: on.
    :type obs_wind_projected: str


    :rtype: None


.. minigallery:: metview.mobs
    :add-heading:

