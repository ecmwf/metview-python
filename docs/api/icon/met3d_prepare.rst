
met3d_prepare
=========================

.. container::
    
    .. container:: leftside

        .. image:: /_static/MET3D_PREPARE.png
           :width: 48px

    .. container:: rightside

        This function performs the same task as the `Met3d Prepare <https://confluence.ecmwf.int/display/METV/met3d+prepare>`_ icon in Metview’s user interface. It accepts its parameters as keyword arguments, described below.


.. py:function:: met3d_prepare(**kwargs)
  
    Description comes here!


    :param mode: Specifies the main retrieval ``mode``. The possible values are: forecast and analysis.

         In forecast ``mode`` the selected ``step``s of a given forecast can be used for data generation. If the ``mode`` is set to analysis a period with a start and end ``date`` and constant ``time``-``step`` can be defined.
    :type mode: str, default: "fc"


    :param product: Specifies the type of data to be retrieved from MARS. The possible values are: "hires" and "ens". The default is "hires".  

         In "hires" ``mode`` the operational deterministic forecast is retrieved. While in "ens" ``mode`` the operational "ens" forecast (both "pf" and "cf" members) is used. If ``mode`` is set to analysis this option is disabled and automatically set to "hires".
    :type product: {"hires", "ens"}, default: "hires"


    :param number: Specifies the perturbed ensemble members to be retrieved as a list. The default value is: "1"/TO/50. Only enabled when ``product`` is set to ens.
    :type number: str or list[str], default: "1"


    :param levtype: Specifies the type of vertical levels. The possible values are: "pl" (pressure levels) and "ml" (``mode``l levels). The default value is: "pl".
    :type levtype: {"pl", "ml"}, default: "pl"


    :param pl_levelist: 
    :type pl_levelist: str or list[str], default: ["1000, 925, 850, 700, 500, 400, 300"]


    :param ml_levelist: 
    :type ml_levelist: str or list[str], default: "-10"


    :param params_2d: 
    :type params_2d: str or list[str], default: "2t"


    :param params_3d: 
    :type params_3d: str or list[str], default: "t"


    :param date: Specifies the run ``date`` of the forecast. Available when ``mode`` is forecast. The default value is -1 (i.e. yesterday).
    :type date: str, default: "-1"


    :param time: Specifies the run ``time`` of the forecast in hours. Available when ``mode`` is forecast. The default value is "0".
    :type time: str, default: "0"


    :param step: Specifies the forecast ``step``s in hours. Here a list of values can be given. Available when ``mode`` is forecast. The default value is "0".
    :type step: str or list[str], default: "0"


    :param analysis_start_date: Specifies the start ``date`` of the analysis period. Available when ``mode`` is analysis. The default value is -1 (i.e. yesterday).
    :type analysis_start_date: str, default: "-1"


    :param analysis_start_time: Specifies the start ``time`` of the period. Available when ``mode`` is period. The default value is "0".
    :type analysis_start_time: str, default: "0"


    :param analysis_end_date: Specifies the end ``date`` of the period. Available when ``mode`` is period. The default value is -1 (i.e. yesterday).
    :type analysis_end_date: str, default: "-1"


    :param analysis_end_time: Specifies the end ``time`` of the period. Available when ``mode`` is period. The default value is "0".
    :type analysis_end_time: str, default: "0"


    :param analysis_step: Specifies the ``time`` ``step`` of the analysis period in hours. The allowed values are as follows: "6" or 12. Available when ``mode`` is period. The default value is "6".
    :type analysis_step: str, default: "6"


    :param area: Specifies the ``area`` of the output ``grid`` in south/west/north/east format. The default value is -90/-180/90/180.
    :type area: float or list[float], default: -90


    :param grid: Specifies the resolution of the output ``grid`` in dx/dy format, where dx is the ``grid`` increment in east-west direction, while dy is the ``grid`` increment in north-south direction (both in units of degrees). The default value is: 1/1.
    :type grid: float or list[float], default: 1


    :param retrieve_group_by_time: 
    :type retrieve_group_by_time: {"on", "off"}, default: "on"


    :rtype: None
