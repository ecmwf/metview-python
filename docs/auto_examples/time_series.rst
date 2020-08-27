.. only:: html

    .. note::
        :class: sphx-glr-download-link-note

        Click :ref:`here <sphx_glr_download_auto_examples_time_series.py>`     to download the full example code
    .. rst-class:: sphx-glr-example-title

    .. _sphx_glr_auto_examples_time_series.py:


Time Series from GRIB
==============================================



.. image:: /auto_examples/images/sphx_glr_time_series_001.png
    :alt: time series
    :class: sphx-glr-single-img


.. rst-class:: sphx-glr-script-out

 Out:

 .. code-block:: none

    t2m integrals:  [15.389773866854247, 15.024168029715582, 13.23835544389342, 11.819085469697036, 10.979054516585, 10.5406890547408, 12.199208273398275, 14.139508392262172, 14.91943545255036, 14.656285465631584, 12.970959265055969, 11.406201790424861, 10.523838525228541, 10.15017142531118, 11.885731504369978, 13.922712360367228, 14.905755567033012, 14.683973639844876, 12.933330096025069, 11.381208274253492, 10.524247404668511, 10.140708819447717, 11.971525823069701, 13.997205123785891, 14.866102786660065, 14.545488709862855, 12.698307853318642, 11.184003257854869, 10.329501856510616, 10.052014920350265, 11.830756456102982, 13.825386961329835, 14.681783974516934]
    t2d integrals:  [8.045567313323902, 8.141261696776455, 8.372396936163454, 7.947697002055662, 7.599740858687876, 7.388100340906873, 7.6949520694423015, 7.70269400726059, 7.520419032001221, 7.621937488465386, 7.807176335709978, 7.512234903922544, 7.206257636597145, 7.1240429092743405, 7.549312879275531, 7.600638347236417, 7.523081708572062, 7.651132464306844, 7.97945670560245, 7.6167563634104525, 7.286927545039737, 7.125411381389421, 7.5805728895054365, 7.469299587426887, 7.3440654594245, 7.436541810300462, 7.86764590287515, 7.473750516579054, 7.126501492882331, 7.058177809209227, 7.571318667870358, 7.3603325925186605, 7.266669032439275]






|


.. code-block:: default


    # (C) Copyright 2017- ECMWF.
    #
    # This software is licensed under the terms of the Apache Licence Version 2.0
    # which can be obtained at http://www.apache.org/licenses/LICENSE-2.0.
    #
    # In applying this licence, ECMWF does not waive the privileges and immunities
    # granted to it by virtue of its status as an intergovernmental organisation
    # nor does it submit to any jurisdiction.
    #

    import metview as mv

    # read a set of t2m and t2d forecast steps from a GRIB file
    both_t = mv.read("t2m_td.grib")

    # filter the t2m and dewpoint t into separate fieldsets (and K->C)
    t2m = mv.read(data=both_t, param="2t") - 273.15
    t2d = mv.read(data=both_t, param="2d") - 273.15

    # for each temperature type, get the integral over an area
    # - returns a list of numbers, one for each field
    area = [75, -12.5, 35, 42.5]  # N,W,S,E
    t2m_int = mv.integrate(t2m, area)
    t2d_int = mv.integrate(t2d, area)
    print("t2m integrals: ", t2m_int)
    print("t2d integrals: ", t2d_int)

    # get the valid times for each field
    times_t2m = mv.valid_date(t2m)
    times_t2d = mv.valid_date(t2d)

    # set up the Cartesian view to plot into
    # including customised axes so that we can change the size
    # of the labels and add titles
    haxis = mv.maxis(
        axis_type="date",
        axis_years_label_height=0.45,
        axis_months_label_height=0.45,
        axis_days_label_height=0.45,
    )

    vaxis = mv.maxis(axis_title_text="Temperature, K", axis_title_height=0.5)

    ts_view = mv.cartesianview(
        x_automatic="on",
        x_axis_type="date",
        y_automatic="on",
        horizontal_axis=haxis,
        vertical_axis=vaxis,
    )

    # create the curves for both parameters
    curve_2t = mv.input_visualiser(
        input_x_type="date", input_date_x_values=times_t2m, input_y_values=t2m_int
    )

    curve_2d = mv.input_visualiser(
        input_x_type="date", input_date_x_values=times_t2d, input_y_values=t2d_int
    )

    # set up visual styling for each curve
    common_graph = {"graph_line_thickness": 2, "legend": "on"}
    graph_2t = mv.mgraph(common_graph, graph_line_colour="black", legend_user_text="t2m")
    graph_2d = mv.mgraph(common_graph, graph_line_colour="red", legend_user_text="t2d")

    # customise the legend
    legend = mv.mlegend(legend_display_type="disjoint", legend_text_font_size=0.5)

    # define the output plot file
    mv.setoutput(mv.pdf_output(output_name="time_series"))

    # plot everything into the Cartesian view
    mv.plot(ts_view, curve_2t, graph_2t, curve_2d, graph_2d, legend)


.. rst-class:: sphx-glr-timing

   **Total running time of the script:** ( 0 minutes  0.430 seconds)


.. _sphx_glr_download_auto_examples_time_series.py:


.. only :: html

 .. container:: sphx-glr-footer
    :class: sphx-glr-footer-example



  .. container:: sphx-glr-download sphx-glr-download-python

     :download:`Download Python source code: time_series.py <time_series.py>`



  .. container:: sphx-glr-download sphx-glr-download-jupyter

     :download:`Download Jupyter notebook: time_series.ipynb <time_series.ipynb>`


.. only:: html

 .. rst-class:: sphx-glr-signature

    `Gallery generated by Sphinx-Gallery <https://sphinx-gallery.github.io>`_
