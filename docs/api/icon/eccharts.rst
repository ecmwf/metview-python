
eccharts
=========================

.. container::
    
    .. container:: leftside

        .. image:: /_static/ECCHARTS.png
           :width: 48px

    .. container:: rightside

		Generates data to recreate the plot layers of the ecCharts web-based visualisation system in the Metview environment performing the following steps:
		
		1. retrieves global forecast fields for a given ecCharts layer from the MARS archive
		2. applies the required post-processing steps on the data
		3. defines the visualisation using one of the pre-defined ecCharts styles available for the layer. 
		
		:func:`eccharts` returns a list that can be directly passed onto :func:`plot` to generate a plot. This list contains the following items:
		
		1. the GRIB fields (:class:`Fieldset`) retrieved from MARS then post-processed
		2. a plot title definition (:func:`mtext`)
		3. a contouring definition (:func:`mcont`) using the specified pre-defined style associated with the layer
		4. a legend definition (:func:`mlegend`)
		
		The second item in this list is optional and only included if ``title`` is set to "style_1".


		.. note:: This function performs the same task as the `Eccharts <https://confluence.ecmwf.int/display/METV/eccharts>`_ icon in Metview’s user interface. It accepts its parameters as keyword arguments, described below.


.. py:function:: eccharts(**kwargs)
  
    Generates data to recreate the plot layers of the ecCharts web-based visualisation system in the Metview environment.


    :param layer: Specifies the name of the ecCharts layer.
    :type layer: str

    :param style: Specifies a named contouring style for the selected ``layer``. Each ecCharts layer is associated with a group of predefined styles and if this parameter is left empty the default style will be assigned to ``layer``. 
		
		.. note:: In the user interface the ecCharts icon editor contains a style browser. When a given ``layer`` is selected the style browser only shows the available styles for that layer with the default style automatically selected.
    :type style: str

    :param title: Specifies the type of the title generated for the plot. The possible values are as follows:
		
		* "default": the automatic Metview title will be used and the returned list will not contain an :func:`mtext` object
		* "style_1": the returned list will contain an :func:`mtext` object defining a title with a different style. 
		
		When overlaying an :func:`eccharts` object with other objects always use the "default" option, otherwise the contouring setting will be applied incorrectly to some of the fields.    
    :type title: {"default", "style_1"}, default: "default"

    :param expver: 
    :type expver: str, default: "1"

    :param date: Specifies the run date of the forecast in YYYYMMDD format. This is the same ``date`` parameter as in the MARS retrieval icon. Relative dates are allowed: e.g. -1 means yesterday, 0 means today, etc.
    :type date: str, default: "-1"

    :param time: Specifies the run time of the forecast. This is the same ``time`` parameter as in the MARS retrieval icon.
    :type time: number, default: 0

    :param step: Specifies the forecast steps in hours. Here a list of values can be given.
    :type step: str or list[str], default: "0"

    :param interval: 
    :type interval: {"3", "6", "9", "12", "24", "48", "72"}, default: "3"

    :param quantile: 
    :type quantile: str or list[str]

    :param grid: Specifies the resolution of the resulting global grid in [dx, dy] format, where dx is the grid increment in West-East direction, while dy is the grid increment in South-North direction (both in units of degrees).
    :type grid: list[float], default: [1, 1]

    :param fail_on_data_error: When this parameter is set to "yes" an error in the data retrieval or the post-processing steps will force the icon to fail and a Python script running :func:`eccharts` will fail as well. When if it is set to "no" the icon will not fail and :func:`eccharts` will return None.
    :type fail_on_data_error: {"yes", "no"}, default: "yes"

    :rtype: list


.. mv-minigallery:: eccharts

