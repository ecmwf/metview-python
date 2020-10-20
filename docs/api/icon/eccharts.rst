
eccharts
=========================

.. container::
    
    .. container:: leftside

        .. image:: /_static/ECCHARTS.png
           :width: 48px

    .. container:: rightside

        This icon represents the `eccharts <https://confluence.ecmwf.int/display/METV/eccharts>`_ icon in Metview's user interface.


.. py:function:: eccharts(**kwargs)
  
    Description comes here!


    :param layer: Specifies the name of the ecCharts ``layer``.
    :type layer: str


    :param style: Specifies the contouring ``style`` for the selected ``layer``. Each ecCharts ``layer`` is associated with a group of predefined ``style``s. When a given ``layer`` is selected in ``layer`` the icon editor only shows the available ``style``s for that ``layer`` and the default ``style`` is automatically selected.
    :type style: str


    :param title: Specifies the type of the ``title`` generated for the plot. The possible values are as follows:

         *  default : the standard Metview automatic ``title`` will be used and the resulting list will not contain a :func:`mtext` icon. This is how it looks:

         ![](/download/attachments/118822740/image2020-2-6_9-36-10.png?version=1&modification``date``=1580981770610&api=v2)

         *  ``style``_1 : the resulting list will contain a :func:`mtext` icon defining a ``title`` of a different ``style``. This is how it looks:

         ![](/download/attachments/118822740/image2020-2-6_9-34-32.png?version=1&modification``date``=1580981672933&api=v2)

         The default option is default.

         When overlaying an EcCharts icon with other EcCharts icons or fields always use the default option (otherwise the contouring setting could be applied incorrectly to some of the fields).

         This option was introduced in Metview 5.8.0.
    :type title: str


    :param expver: 
    :type expver: str


    :param date: Specifies the run ``date`` of the forecast. This is the same ``date`` parameter as in the MARS retrieval icon. The ``date`` is given in YYYYMMDD format. Relative ``date``s are allowed: e.g. -1 means yesterday, 0 means today, etc. The default is -1.
    :type date: str


    :param time: Specifies the run ``time`` of the forecast. This is the same ``time`` parameter as in the MARS retrieval icon. The default is 0.
    :type time: number


    :param step: Specifies the forecast ``step``s in hours. Here a list of values can be given.
    :type step: str or list[str]


    :param interval: 
    :type interval: str


    :param quantile: 
    :type quantile: str or list[str]


    :param grid: Specifies the resolution of the resulting global ``grid`` in dx/dy format, where dx is the ``grid`` increment in West-East direction, while dy is the ``grid`` increment in South-North direction (both in units of degrees). The default value is: 1/1.
    :type grid: float or list[float]


    :param fail_on_data_error: When this parameter is set to yes an error in the data retrieval or the post-processing ``step``s will force the icon to fail and a Macro/Python script running the eccharts()`function will fail as well. While if it is set to no the icon will not fail and the eccharts command in Macro/Python will return nil/None. The default value is yes.
    :type fail_on_data_error: str


    :rtype: None


.. minigallery:: metview.eccharts
    :add-heading:

