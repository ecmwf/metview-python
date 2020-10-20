
percentile
=========================

.. container::
    
    .. container:: leftside

        .. image:: /_static/PERCENTILE.png
           :width: 48px

    .. container:: rightside

        This icon represents the `percentile <https://confluence.ecmwf.int/display/METV/percentile>`_ icon in Metview's user interface.


.. py:function:: percentile(**kwargs)
  
    Description comes here!


    :param source: Specifies the GRIB file path and name. Alternatively, parameter ``data`` can be used.
    :type source: str


    :param data: Specifies the ``data`` required for the application. This can be any icon returning GRIB ``data`` (e.g. MARS Retrieval, GRIB Filter, Formula, Simple Formula). The icon field assist button provides a tailor made MARS request in case you need some guidance in the ``data`` specification. Alternatively, parameter ``source`` can be used.
    :type data: str


    :param percentiles: Specifies a list of values from 0 to 100.
    :type percentiles: float or list[float]


    :param interpolation: Specifies the ``interpolation`` method used to compute the ``percentiles``: nearest_neighbour or linear. The default value is: nearest_neighbour.

         Given a list of numbers V , the algorithm used to compute a percentile is the following:

         1. Compute the rank (R) of a P-th percentile. This is done using the following formula: R = P/100 x (N + 1) where P is the desired percentile and N is the number of input fields.

         2. Compute the percentile:

         1. If R is an integer, the P-th percentile will be the number with rank R.

         2. If R is not an integer, the P-th percentile is computed by ``interpolation`` as follows:

         1. If the ``interpolation`` method is Nearest Neighbour , the following equation is used: P-th = V[int(R + 0.5)]

         2. If the ``interpolation`` method is Linear , the following steps are used:

         1. Define IR as the integer portion of R

         2. Define FR as the fractional portion or R

         3. Find the scores with Rank IR and with Rank IR + 1, e.g. V[IR] and V[IR+1]

         4. Interpolate by multiplying the difference between the scores by FR and add the result to the lower score, e.g. Pth = FR * (V[IR+1] - V[IR]) + V[IR]
    :type interpolation: str


    :param compute_if_missing_present: 
    :type compute_if_missing_present: str


    :rtype: None


.. minigallery:: metview.percentile
    :add-heading:

