
meteogram
=========================

.. container::
    
    .. container:: leftside

        .. image:: /_static/METPLUS.png
           :width: 48px

    .. container:: rightside

        This function performs the same task as the `Meteogram <https://confluence.ecmwf.int/display/METV/meteogram>`_ icon in Metview’s user interface. It accepts its parameters as keyword arguments, described below.


.. py:function:: meteogram(**kwargs)
  
    Description comes here!


    :param type: Specifies the ``type`` of meteogram to be generated. The Epsgrams are derived from the Ensemble Prediction System, whereas the Metgrams are derived from the deterministic forecast model. The available ``type``s are 10 Days Epsgram , 15 Days Epsgram , 15 Days Epsgram With Climate, 10 Days Metgram and 10 Days Wave Epsgram.
    :type type: {"10_days_epsgram", "15_days_epsgram", "15_days_epsgram_with_climate", "10_days_wave_epsgram", "10_days_plumes"}, default: "15_days_epsgram"


    :param station: Specifies the location at which to derive the meteogram. Provide a ``station``_ icon with the location details.
    :type station: str


    :param data_selection_type: Determines how the meteogram data source is selected: "latest" (default) will retrieve the "latest" meteogram available; ``"date"`` will allow the further selection of a specific ``"date"`` and time; "local" allows the specification of a path to a "local" SPOT ``database`` (details of the ``database`` ``format`` are not provided here).
    :type data_selection_type: {"latest", "date", "local"}, default: "latest"


    :param date: Specifies the day on which the forecast is based (first day on the plot). The default value is -1 (yesterday), but you can use other ``format``s, such as YYMMDD or YYYY-MM-DD . Only available if Data Selection ``type`` is set to ``date``.
    :type date: number, default: -1


    :param forecast_run_time: Specify the forecast time (hours of the day) from either 00h or 12h. Only available if Data Selection ``type`` is set to ``date``.
    :type forecast_run_time: {"00", "12"}, default: "12"


    :param experiment: Specifies the MARS ``experiment`` number from which the meteograms are to be plotted. You will only need to modify this parameter if you want to display data from a source other than the ECMWF model. Note that this parameter is a string, so for example '0001' is different from '1'.
    :type experiment: number, default: 0001


    :param format: Specifies the output ``format`` (the default is PostScript).
    :type format: {"pdf", "png", "ps"}, default: "pdf"


    :param database: If not "latest" , then this parameter is taken to be the entire path to the ``database`` directory. Only available if Data Selection ``type`` is set to Local.

         ##  Macro Example Using the Meteogram Icon

         The Meteogram icon returns a graphics file as its output, so there is no need to render it through the plot() command; instead, it can be simply written to disk with the write() command, as shown below.   

            london = ``station``s (name : "London, St James Park")  metgram_london = meteogram ( ``type`` : "10_days_epsgram", ``format`` : "pdf", ``station`` : london )  write ('metgram_london.pdf', metgram_london)
    :type database: str, default: "latest"


    :rtype: None
