
retrieve
=========================

.. container::
    
    .. container:: leftside

        .. image:: /_static/RETRIEVE.png
           :width: 48px

    .. container:: rightside

        This function performs the same task as the `Retrieve <https://confluence.ecmwf.int/display/METV/retrieve>`_ icon in Metview’s user interface. It accepts its parameters as keyword arguments, described below.


.. py:function:: retrieve(**kwargs)
  
    Description comes here!


    :param dataset: 
    :type dataset: str


    :param class: 
    :type class: {"od", "rd", "er", "cs", "e4", "ei", "dm", "pv", "el", "to", "co", "en", "me", "sr", "dt", "laef", "yt", "yp", "mc", "pe", "em", "e2", "era5", "cera-20c", "rm", "ncep 20cr", "j5", "cera-sat", "c3", "l5", "ce", "cr", "at", "be", "hr", "dk", "fi", "fr", "de", "gr", "hu", "is", "ie", "it", "nl", "no", "pt", "si", "es", "se", "ch", "tr", "uk", "uzzz", "ma", "te"}, default: "od"


    :param type: 
    :type type: str, default: "an"


    :param stream: 
    :type stream: str, default: "da"


    :param expver: 
    :type expver: str or list[str], default: "1"


    :param model: 
    :type model: str, default: "off"


    :param repres: 
    :type repres: {"bu", "sh", "ll", "gg", "sv", "og", "all"}, default: "sh"


    :param obsgroup: 
    :type obsgroup: {"satellite", "ers1", "trmm", "qscat", "reo3", "hirs", "amsua", "amsub", "mhs", "geos", "resat", "meris", "gpsro", "satob", "scatt", "ssmi all-sky", "iasi", "airs", "ssmis all-sky", "tmi all-sky", "amsre all-sky", "conv", "smos", "windsat all-sky", "ssmi", "amsua all-sky", "amsre", "tmi", "ssmis", "gbrad", "mwhs", "mwts", "mwri all-sky", "iras", "msu", "ssu", "vtpr1", "vtpr2", "atms", "resat averaging kernels", "cris", "wave integrated parameters", "wave spectra", "raingg", "surface multisensor", "amsr-2 all-sky", "saphir all-sky", "amsub all-sky", "mhs all-sky", "doppler wind lidar", "iris", "aatsr", "atms all-sky", "gmi all-sky", "godae sea surface temperatures", "atovs multisensor", "atmospheric composition", "non-surface multisensor", "mwts2", "ssmi 1dvar tcwv cloudy-sky", "mwhs2 all-sky", "ssmt2", "smap", "tovs multisensor", "cloud reflectivity", "cloud lidar", "test", "off"}, default: "off"


    :param reportype: 
    :type reportype: str or list[str], default: "off"


    :param obstype: 
    :type obstype: str or list[str], default: "s"


    :param levtype: 
    :type levtype: {"pv", "pt", "sfc", "pl", "ml", "dp", "wv", "layer", "cat", "o2d", "o3d", "sol", "off", "all"}, default: "pl"


    :param levelist: 
    :type levelist: str or list[str], default: "1000"


    :param param: 
    :type param: str or list[str], default: "z"


    :param date: 
    :type date: str or list[str], default: "-1"


    :param verify: 
    :type verify: str, default: "off"


    :param refdate: 
    :type refdate: str or list[str], default: "off"


    :param hdate: 
    :type hdate: str or list[str], default: "off"


    :param fcmonth: 
    :type fcmonth: str or list[str], default: "off"


    :param fcperiod: 
    :type fcperiod: str or list[str], default: "off"


    :param time: 
    :type time: str or list[str], default: "12"


    :param leadtime: 
    :type leadtime: str or list[str], default: "off"


    :param opttime: 
    :type opttime: str or list[str], default: "off"


    :param range: 
    :type range: str, default: "off"


    :param step: 
    :type step: str or list[str], default: "00"


    :param anoffset: 
    :type anoffset: str or list[str]


    :param reference: 
    :type reference: str or list[str], default: "off"


    :param number: 
    :type number: str or list[str], default: "off"


    :param quantile: 
    :type quantile: str or list[str], default: "off"


    :param domain: 
    :type domain: {"g", "g", "m", "n", "s", "b", "e", "a", "b", "c", "d", "w", "f", "t", "u", "x", "all", "v", "h", "i", "j", "k", "l", "o", "p", "q", "r", "y", "z"}, default: "g"


    :param frequency: 
    :type frequency: str or list[str], default: "off"


    :param direction: 
    :type direction: str or list[str], default: "off"


    :param diagnostic: 
    :type diagnostic: str or list[str], default: "off"


    :param iteration: 
    :type iteration: str or list[str], default: "off"


    :param channel: 
    :type channel: str or list[str], default: "off"


    :param ident: 
    :type ident: str or list[str], default: "off"


    :param origin: 
    :type origin: str or list[str], default: "off"


    :param system: 
    :type system: str, default: "off"


    :param method: 
    :type method: str or list[str], default: "off"


    :param product: 
    :type product: {"inst", "tims", "tavg", "tacc", "all", "off"}, default: "off"


    :param section: 
    :type section: {"h", "v", "z", "m", "all", "off"}, default: "off"


    :param latitude: 
    :type latitude: str, default: "off"


    :param longitude: 
    :type longitude: str, default: "off"


    :param source: 
    :type source: str, default: ""


    :param target: 
    :type target: str, default: ""


    :param logstats: 
    :type logstats: str


    :param transfer: 
    :type transfer: str


    :param fieldset: 
    :type fieldset: str


    :param cfspath: 
    :type cfspath: str, default: ""


    :param format: 
    :type format: str, default: "p"


    :param disp: 
    :type disp: str, default: "off"


    :param resol: 
    :type resol: str, default: "auto"


    :param accuracy: 
    :type accuracy: str, default: "n"


    :param style: 
    :type style: {"dissemination", "off"}, default: "off"


    :param interpolation: 
    :type interpolation: str, default: "off"


    :param area: 
    :type area: str or list[str], default: "g"


    :param block: 
    :type block: str or list[str], default: "off"


    :param instrument: 
    :type instrument: str or list[str], default: "off"


    :param filter: 
    :type filter: str, default: "off"


    :param rotation: 
    :type rotation: str or list[str], default: "off"


    :param frame: 
    :type frame: str, default: "off"


    :param bitmap: 
    :type bitmap: str, default: "off"


    :param grid: 
    :type grid: str or list[str], default: "off"


    :param gaussian: 
    :type gaussian: {"reduced", "regular", "off"}, default: "off"


    :param specification: 
    :type specification: str, default: "off"


    :param packing: 
    :type packing: str, default: "off"


    :param padding: 
    :type padding: str, default: "off"


    :param duplicates: 
    :type duplicates: {"keep", "remove"}, default: "keep"


    :param launch: 
    :type launch: str, default: ""


    :param job: 
    :type job: str, default: "off"


    :param use: 
    :type use: str, default: "normal"


    :param password: 
    :type password: str, default: "off"


    :param costonly: 
    :type costonly: str, default: "n"


    :param optimise: 
    :type optimise: str, default: "off"


    :param process: 
    :type process: str, default: "off"


    :param branch: 
    :type branch: str, default: "off"


    :param database: 
    :type database: str or list[str]


    :param expect: 
    :type expect: str, default: "off"


    :param _version: 
    :type _version: str, default: "2.0"


    :param lsm: 
    :type lsm: {"on", "off"}, default: "off"


    :param truncation: 
    :type truncation: str, default: "off"


    :param intgrid: 
    :type intgrid: str or list[str], default: "off"


    :param ppengine: 
    :type ppengine: {"emos", "mir", "off"}, default: "off"


    :rtype: None


.. minigallery:: metview.retrieve
    :add-heading:

