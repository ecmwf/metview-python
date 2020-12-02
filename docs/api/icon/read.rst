
read
=========================

.. container::
    
    .. container:: leftside

        .. image:: /_static/READ.png
           :width: 48px

    .. container:: rightside

        This function performs the same task as the `Read <https://confluence.ecmwf.int/display/METV/read>`_ icon in Metview’s user interface. It accepts its parameters as keyword arguments, described below.


.. py:function:: read(**kwargs)
  
    Description comes here!


    :param source: 
    :type source: str, default: "off"


    :param logstats: 
    :type logstats: str


    :param data: 
    :type data: str


    :param cfspath: 
    :type cfspath: str, default: "off"


    :param order: 
    :type order: {"0", "1"}, default: "0"


    :param class: 
    :type class: {"od", "rd", "er", "cs", "e4", "ei", "dm", "pv", "el", "to", "co", "en", "me", "sr", "dt", "laef", "yt", "yp", "mc", "pe", "em", "e2", "era5", "cera-20c", "rm", "ncep 20cr", "j5", "cera-sat", "c3", "l5", "ce", "cr", "at", "be", "hr", "dk", "fi", "fr", "de", "gr", "hu", "is", "ie", "it", "nl", "no", "pt", "si", "es", "se", "ch", "tr", "uk", "uzzz", "ma", "te", "any"}, default: "any"


    :param stream: 
    :type stream: str, default: "any"


    :param type: 
    :type type: str, default: "any"


    :param model: 
    :type model: str, default: "any"


    :param levtype: 
    :type levtype: {"any", "pv", "pt", "sfc", "pl", "ml", "dp", "wv", "layer", "cat", "o2d", "o3d", "sol", "off", "all"}, default: "any"


    :param levelist: 
    :type levelist: str or list[str], default: "any"


    :param param: 
    :type param: str or list[str], default: "any"


    :param date: 
    :type date: str or list[str], default: "any"


    :param verify: 
    :type verify: str or list[str], default: "off"


    :param refdate: 
    :type refdate: str or list[str], default: "off"


    :param hdate: 
    :type hdate: str or list[str], default: "off"


    :param fcmonth: 
    :type fcmonth: str or list[str], default: "off"


    :param fcperiod: 
    :type fcperiod: str or list[str], default: "off"


    :param time: 
    :type time: str or list[str], default: "any"


    :param leadtime: 
    :type leadtime: str or list[str], default: "any"


    :param opttime: 
    :type opttime: str or list[str], default: "any"


    :param reference: 
    :type reference: str or list[str], default: "any"


    :param step: 
    :type step: str or list[str], default: "any"


    :param anoffset: 
    :type anoffset: str or list[str], default: "any"


    :param range: 
    :type range: str, default: "any"


    :param accuracy: 
    :type accuracy: str, default: "n"


    :param style: 
    :type style: {"dissemination", "off", "any"}, default: "any"


    :param interpolation: 
    :type interpolation: str, default: "any"


    :param area: 
    :type area: str or list[str], default: "any"


    :param frame: 
    :type frame: str, default: "off"


    :param bitmap: 
    :type bitmap: str, default: "off"


    :param resol: 
    :type resol: str, default: "auto"


    :param rotation: 
    :type rotation: str or list[str], default: "any"


    :param grid: 
    :type grid: str or list[str], default: "any"


    :param gaussian: 
    :type gaussian: {"reduced", "regular", "off"}, default: "off"


    :param specification: 
    :type specification: str, default: "off"


    :param packing: 
    :type packing: {"simple", "complex", "second order", "archived value", "off"}, default: "off"


    :param ensemble: 
    :type ensemble: str or list[str], default: "off"


    :param cluster: 
    :type cluster: str or list[str], default: "off"


    :param probability: 
    :type probability: str or list[str], default: "off"


    :param number: 
    :type number: str or list[str], default: "any"


    :param quantile: 
    :type quantile: str or list[str], default: "any"


    :param frequency: 
    :type frequency: str or list[str], default: "any"


    :param direction: 
    :type direction: str or list[str], default: "any"


    :param diagnostic: 
    :type diagnostic: str or list[str], default: "any"


    :param iteration: 
    :type iteration: str or list[str], default: "any"


    :param channel: 
    :type channel: str or list[str], default: "any"


    :param ident: 
    :type ident: str or list[str], default: "any"


    :param instrument: 
    :type instrument: str or list[str], default: "any"


    :param filter: 
    :type filter: str, default: "any"


    :param repres: 
    :type repres: {"bu", "sh", "ll", "gg", "sv", "og", "all", "any"}, default: "any"


    :param origin: 
    :type origin: str or list[str], default: "any"


    :param padding: 
    :type padding: str, default: "any"


    :param domain: 
    :type domain: {"g", "g", "m", "n", "s", "b", "e", "a", "b", "c", "d", "w", "f", "t", "u", "x", "all", "v", "h", "i", "j", "k", "l", "o", "p", "q", "r", "y", "z", "any"}, default: "any"


    :param system: 
    :type system: str, default: "any"


    :param method: 
    :type method: str or list[str], default: "any"


    :param product: 
    :type product: {"inst", "tims", "tavg", "tacc", "all", "any"}, default: "any"


    :param section: 
    :type section: {"h", "v", "z", "m", "all", "any"}, default: "any"


    :param latitude: 
    :type latitude: str, default: "any"


    :param longitude: 
    :type longitude: str, default: "any"


    :param expver: 
    :type expver: str, default: "any"


    :param lsm: 
    :type lsm: {"on", "off"}, default: "off"


    :param truncation: 
    :type truncation: str, default: "off"


    :param intgrid: 
    :type intgrid: str or list[str], default: "off"


    :rtype: None


.. minigallery:: metview.read
    :add-heading:

