
obsfilter
=========================

.. container::
    
    .. container:: leftside

        .. image:: /_static/OBSFILTER.png
           :width: 48px

    .. container:: rightside

		Filters data from a BUFR file and produces output either as :class:`BUFR`, :class:`Geopoints` or :class:`CSV`. A tutorial about the use of :func:`obsfilter` can be found `here <https://confluence.ecmwf.int/display/METV/Observation+Filter?preview=/14158627/18482215/mv_bufr_tutorial.pdf>`_. 
		
		**What is BUFR?**
		
		BUFR stands for Binary Universal Form for Data Representation, the format in which observation data (in the broadest sense including ground observations, radiosonde soundings, radar and satellite images and soundings) are stored. Full details can be found in the WMO referencesand the ECMWF Meteorological Bulletin M1.4/4 "BUFR User Guide and Reference Manual" (1994).
		
		Very (very) briefly, a BUFR file is composed of BUFR messages. Each message has header sections containing information (e.g. type, subtype, date and time) and a section containing one or  more observations in a coded format. Each observation contains several values of different observed physical quantities (e.g. SYNOP, TEMP, PILOT, METAR,...). Observations are classified by Type (defined by WMO) and Subtype (which may be particular to each institution).
		
		**What is geopoints?**
		
		Geopoints files are ASCII files containing single or paired parameter (observed physical quantity) values together with space and time coordinates.
		
		If you need observations of a given parameter for combination with other types of data, e.g. to derive differences between forecast fields and observations, they are required to be in geopoints format. You must use this icon to filter out the single parameter values out of the BUFR file or archived observation data and return/save them as a geopoints variable/file.
		
		**Filtering Efficiency**
		
		You may filter observations according to a wide variety of parameters or combinations thereof: you may filter on date and time, on location (meteorological station, WMO block, user defined area, proximity to user defined line) and range of values.vRegarding the structure of the input BUFR file, note that some of the filtering parameters such as observation type, subtype, date and time are located in the header part of the BUFR message, whilst others are located in the data part of the BUFR message itsel. This implies that the filtering of BUFR data according to parameters located in the header does not require decoding of the remaining information and thus is considerably (about 10 times) faster. Internally, filtering is always done first on the header parameters (if specified).


		.. note:: This function performs the same task as the `Observation Filter <https://confluence.ecmwf.int/display/METV/Observation+Filter>`_ icon in Metview’s user interface. It accepts its parameters as keyword arguments, described below.


.. py:function:: obsfilter(**kwargs)
  
    Filters and extracts BUFR data.


    :param data: The input data.
    :type data: :class:`BUFR`

    :param output: Specifies the output format you want. The possible options are as follows:
		  
		* "bufr": the output is a new :class:`BUFR`. Messages containing subsets are split each subset forming an individual message in the output. Not all the filtering options are available in this mode. 
		* "geopoints": the output is a standard 6-column :class:`Geopoints`.
		* "polar_vector": the output is a :class:`Geopoints` with polar vector data.
		* "xy_vector": the output is a :class:`Geopoints` with xy vector data.
		* "ncols": the output is a :class:`Geopoints` with arbitrary number of data columns.
		* "csv": the output is a :class:`Table` containing only the parameters specified in ``parameter`` (no location, data, time and levels is extracted).
    :type output: {"bufr", "geopoints", "polar_vector", "xy_vector", "ncols", "csv"}, default: "bufr"

    :param parameter: Specifies the parameters to be extracted by their ecCodes BUFR keynames. For compatibility the BUFR descriptors can still be given here but their usage is discouraged. Available when ``output`` is not "bufr".
    :type parameter: str or list[str], default: "012004"

    :param missing_data: If set to "ignore", missing data is not included in the ``output`` file. If set to "include", missing data will be written to the output file, its value being set to that specified by ``missing_data_value``. Note that when ``output`` is is one of the two geopoints vector formats, the test for missing data` is only performed on the first ``parameter``. Available when ``output`` is not "bufr".
    :type missing_data: {"ignore", "include"}, default: "ignore"

    :param missing_data_value: Any missing observations will be written as this value. It is wise, therefore, to ensure that this value is outside the range of possible values for the requested parameter(s). Note that when ``output`` is one of the two geopoints vector formats, the test for missing data is only performed on the first ``parameter``. Available when ``output`` is not "bufr" and ``missing_data`` is "include".
    :type missing_data_value: number, default: 3.0e+38

    :param level: The possible values are as follows:
		
		* "surface": use this for surface observations (e.g. SYNOP)
		* "single": defines level filter by a single pressure value (e.g. TEMP)
		* "thickness": defines a pressure layer filter (e.g. TEMP)
		* "occurrence": defines a filter based on the occurrence of ``parameter`` within a BUFR message/subset
		* "descriptor_value": defines a filter based on the value of the ``level_descriptor`` parameter.
		* "descriptor_range": defines a filter based on the value range of the ``level_descriptor`` parameter.
		Available when ``output`` is not "bufr".
    :type level: str, default: "surface"

    :param level_descriptor: Specifies the parameter defining the level when ``level`` is "descriptor_value" or "descriptor_range".
    :type level_descriptor: str, default: "007004"

    :param first_level: Specifies the first value for the ``level`` filter. If ``level`` is "single" or "thickness" this must be a pressure value given in hPa. If ``level`` is "thickness" this defines the bottom of the layer (towards the surface). If ``level`` is "descriptor_range" it sets the minimum of the range.
    :type first_level: str, default: "30"

    :param second_level: Specifies the second value for the ``level`` filter. If ``level`` is "thickness" this must be a pressure value given in hPa at the top of the layer. If ``level`` is "descriptor_range" it sets the maximum of the range.
    :type second_level: str, default: "10"

    :param occurrence_index: Specifies the numerical index of a ``parameter`` that has several values within one observation (e.g. cloud amount on different levels or water temperature at different depths). Available if ``level`` is set to "occurrence".
    :type occurrence_index: number, default: 1

    :param observation_types: Specifies the numerical code or text string for the desired observation type.
    :type observation_types: str or list[str], default: "any"

    :param observation_subtypes: Specifies the numerical code or text string for the desired observation subtype. Note that institutions are free to define their own subtypes hence these are not an international standard.
    :type observation_subtypes: str or list[str], default: "any"

    :param date_and_time_from: Specifies if date and time should be taken from the BUFR header section ("metadata") or from the data section ("data").
    :type date_and_time_from: {"metadata", "data"}, default: "metadata"

    :param date: Specifies the observation(s) date in YYYYMMDD format. Relative dates are allowed: e.g. -1 (yesterday).  Specifying a value for ``date`` requires setting a value for ``time``.
    :type date: str

    :param time: Specifies the time of the observation(s). The required format is HHMM.
    :type time: str

    :param resolution_in_mins: Specifies a time window in minutes around the value chosen for ``time``.
    :type resolution_in_mins: number, default: 0

    :param wmo_blocks: Specifies a WMO block number. These identify a geographical region, e.g. 02 for Sweden and Finland, 16 for Italy and Greece.
    :type wmo_blocks: str or list[str], default: "any"

    :param wmo_stations: Specifies a list of WMO stations, using the five digit station identifier (the first two of which are the WMO block number).
    :type wmo_stations: str or list[str], default: "any"

    :param location_filter: Specifies a location filter.
    :type location_filter: {"none", "area", "line"}, default: "none"

    :param area: Specifies the coordinates of the area of interest in the form of [North, West, South, East]. Enabled when ``location_filter`` is "area".
    :type area: list[float], default: [60, -12, 50, 3]

    :param line: Specifies the coordinates of a transect line in [lat1, lon1, lat2, lon2] format. This will filter all the observations close enough to the line - how close is defined by ``delta_in_km``. Enabled when ``location_filter`` is "line".
    :type line: float or list[float], default: 40

    :param delta_in_km: Specifies the width of the cross section line in km defined in ``line``.
    :type delta_in_km: number, default: 50

    :param custom_filter: Allows to filter observations by the value of a ``custom_parameter``. You can select observations equal to a value (option "value") or within/outside a given range of values (options "range" or "exclude").
    :type custom_filter: {"none", "value", "range", "exclude"}, default: "none"

    :param custom_parameter: Specifies the parameter for ``custom_filter``. Use an ecCodes BUFR keyname here. For compatibility a BUFR descriptors can still be given here but their usage is discouraged.
    :type custom_parameter: str, default: "01007"

    :param custom_values: Specifies the value condition for ``custom_filter``. You may specify a list of values here. If ``custom_filter`` is "range" or "exclude" you need to specify a list with two elements here.
    :type custom_values: float or list[float], default: 200

    :param fail_on_error: 
    :type fail_on_error: {"yes", "no"}, default: "yes"

    :param fail_on_empty_output: Controls the behaviour when the resulting output is empty. If it is set to "no" :func:`obs_filter` will return None, while if the value is "yes" the Python script running :func:`obs_filter` will abort.
    :type fail_on_empty_output: {"yes", "no"}, default: "no"

    :rtype: :class:`BUFR`, :class:`Geopoints` or :class:`CSV`


.. minigallery:: metview.obsfilter
    :add-heading:

