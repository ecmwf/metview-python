Filters data from a BUFR file and produces output either as :class:`Bufr`, :class:`Geopoints` or :class:`Table`. A tutorial about the use of :func:`obsfilter` can be found `here <https://confluence.ecmwf.int/display/METV/Observation+Filter?preview=/14158627/18482215/mv_bufr_tutorial.pdf>`_. 

**What is BUFR?**

BUFR stands for Binary Universal Form for Data Representation, the format in which observation data (in the broadest sense including ground observations, radiosonde soundings, radar and satellite images and soundings) are stored. Full details can be found in the WMO referencesand the ECMWF Meteorological Bulletin M1.4/4 "BUFR User Guide and Reference Manual" (1994).

Very (very) briefly, a BUFR file is composed of BUFR messages. Each message has header sections containing information (e.g. type, subtype, date and time) and a section containing one or  more observations in a coded format. Each observation contains several values of different observed physical quantities (e.g. SYNOP, TEMP, PILOT, METAR,...). Observations are classified by Type (defined by WMO) and Subtype (which may be particular to each institution).

**What is geopoints?**

Geopoints files are ASCII files containing single or paired parameter (observed physical quantity) values together with space and time coordinates.

If you need observations of a given parameter for combination with other types of data, e.g. to derive differences between forecast fields and observations, they are required to be in geopoints format. You must use this icon to filter out the single parameter values out of the BUFR file or archived observation data and return/save them as a geopoints variable/file.

**Filtering Efficiency**

You may filter observations according to a wide variety of parameters or combinations thereof: you may filter on date and time, on location (meteorological station, WMO block, user defined area, proximity to user defined line) and range of values.vRegarding the structure of the input BUFR file, note that some of the filtering parameters such as observation type, subtype, date and time are located in the header part of the BUFR message, whilst others are located in the data part of the BUFR message itsel. This implies that the filtering of BUFR data according to parameters located in the header does not require decoding of the remaining information and thus is considerably (about 10 times) faster. Internally, filtering is always done first on the header parameters (if specified).