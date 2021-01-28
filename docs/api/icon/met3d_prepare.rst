
met3d_prepare
=========================

.. container::
    
    .. container:: leftside

        .. image:: /_static/MET3D_PREPARE.png
           :width: 48px

    .. container:: rightside

		Retrieves and post-processes GRIB data from ECMWF's MARS archive so that it could be used in the Met.3D visualisation system.


		.. note:: This function performs the same task as the `Met3d Prepare <https://confluence.ecmwf.int/display/METV/met3d+prepare>`_ icon in Metview’s user interface. It accepts its parameters as keyword arguments, described below.


.. py:function:: met3d_prepare(**kwargs)
  
    Retrieves and post-processes GRIB data from ECMWF's MAR archive to be used in Met.3D.


    :param mode: Specifies the main retrieval mode. In "fc" mode the selected steps of a given forecast can be used for data generation. If ``mode`` is set to "an" a period with a start and end date and constant time-step can be defined.
    :type mode: {"fc", "an"}, default: "fc"

    :param product: Specifies the type of data to be retrieved from MARS. In "hires\" mode the operational deterministic forecast is retrieved. While in "ens" mode the operational ENS forecast (both "pf" and "cf" members) is used. If ``mode`` is "an" this option is disabled and automatically set to "hires".
    :type product: {"hires", "ens"}, default: "hires"

    :param number: Specifies the perturbed ensemble members to be retrieved as a list. Enabled when ``product`` is set to "ens".
    :type number: str or list[str], default: ["1, TO, 50"]

    :param levtype: Specifies the type of vertical levels. The possible values are: "pl" (pressure levels) and "ml" (ECMWF model levels).
    :type levtype: {"pl", "ml"}, default: "pl"

    :param pl_levelist: Specifies the list of pressure levels in hPa when ``levtype`` is "pl"
    :type pl_levelist: str or list[str], default: ["1000, 925, 850, 700, 500, 400, 300"]

    :param ml_levelist: Specifies the list of model levels when ``levtype`` is "ml". If the list of model levels is a sole negative number (-N) it means that all the model levels will be retrieved from the surface up to level N. Please note that model level numbering starts at the topmost atmospheric level (click `here <https://www.ecmwf.int/en/forecasts/documentation-and-support/137-model-levels>`_ for details).
    :type ml_levelist: str or list[str], default: "-10"

    :param params_2d: Specifies the list of surface parameters. Please note that when the following precipitation rate parameters are specified their sum is computed and added as a "tprate" field to the results:
		
		* Convective rain rate: crr
		* Large scale rain rate: lsrr
		* Convective snowfall rate water equivalent: csfr
		* Large scale snowfall rate water equivalent: lssfr
    :type params_2d: str or list[str], default: ["2t, 10u, 10v"]

    :param params_3d: Specifies the list of upper level parameters. Please note that on model levels "z" (geopotential) is not archived in MARS. However, when "z" is specified in ``param_3d`` it will be automatically computed (the fields needed for the computations will also be automatically retrieved). To be able to plot "jet cores" in 3D "z" is needed.
    :type params_3d: str or list[str], default: ["t, q, u, v"]

    :param date: Specifies the run date of the forecast. Available when ``mode`` is "fc". The default value is -1 (i.e. yesterday).
    :type date: str, default: "-1"

    :param time: Specifies the run time of the forecast in hours. Available when ``mode`` is "fc".
    :type time: str, default: "0"

    :param step: Specifies the forecast steps in hours. Available when ``mode`` is "fc".
    :type step: int or list[int], default: 0

    :param analysis_start_date: Specifies the start date of the analysis period. Available when ``mode`` is "an". The default value is -1 (i.e. yesterday).
    :type analysis_start_date: str, default: "-1"

    :param analysis_start_time: Specifies the start time of the period. Available when ``mode`` is "an".
    :type analysis_start_time: str, default: "0"

    :param analysis_end_date: Specifies the end date of the period. Available when ``mode`` is "an". The default value is -1 (i.e. yesterday).
    :type analysis_end_date: str, default: "-1"

    :param analysis_end_time: Specifies the end time of the period. Available when ``mode`` is "an".
    :type analysis_end_time: str, default: "0"

    :param analysis_step: Specifies the timestep of the analysis period in hours. Available when ``mode`` is "an".
    :type analysis_step: int, default: 6

    :param area: Specifies the area of the output ``grid`` in [South, West, North, East] format.
    :type area: list[float], default: [-90, -180, 90, 180]

    :param grid: Specifies the resolution of the output grid in [dx, dy] format, where dx is the grid increment in East-West direction, while dy is the grid increment in North-South direction (both in units of degrees).
    :type grid: list[float], default: [1, 1]

    :param retrieve_group_by_time: Specifies how the MARS retrievals should be executed. When it is set to "on" the following happens:
		
		* forecasts: all steps are retrieved together
		* analyses: times within the same day are retrieved together
		When it is set to "off" each step/time is retrieved separately (in a loop). 
    :type retrieve_group_by_time: {"on", "off"}, default: "on"

    :rtype: :class:`Fieldset`


.. mv-minigallery:: met3d_prepare

