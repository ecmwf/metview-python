
percentile
=========================

.. container::
    
    .. container:: leftside

        .. image:: /_static/PERCENTILE.png
           :width: 48px

    .. container:: rightside

		Computes a set of percentiles of a given input :class:`Fieldset`. A percentile is a number such that the given percentage of a distribution is equal to or below it. For instance, the median is the 50th percentile - 50% of the values are equal to or below it. The generated fields can simp


		.. note:: This function performs the same task as the `Percentile <https://confluence.ecmwf.int/display/METV/percentile>`_ icon in Metview’s user interface. It accepts its parameters as keyword arguments, described below.


.. py:function:: percentile(**kwargs)
  
    Computes a set of percentiles of a given input :class:`Fieldset`.


    :param source: Specifies the GRIB file path and name. Alternatively, parameter ``data`` can be used. If both ``source`` and ``data`` are specified ``data`` takes precedence.
    :type source: str, default: "off"

    :param data: Specifies the GRIB data required for the application. Takes precedence over ``source``.
    :type data: :class:`Fieldset`

    :param percentiles: Specifies a list of percentile values from 0 to 100.
    :type percentiles: float or list[float], default: 10.0

    :param interpolation: Specifies the interpolation method used to compute the ``percentiles``. Given a list of numbers V, the algorithm used to compute a percentile is the following. First, the the rank (R) of a P-th percentile is computed. This is done using the following formula: R = P/100 x (N + 1) where P is the desired percentile and N is the number of input fields. Then, the percentile itself is computed:
		
		* If R is an integer, the P-th percentile will be the number with rank R.
		* If R is not an integer, the P-th percentile is computed by interpolation as follows:
		
				* If ``interpolation`` is "nearest_neighbour", the following equation is used: P-th = V[int(R + 0.5)]
				* If ``interpolation`` is "linear", the following steps are used: 
		
						1. Define IR as the integer portion of R
						2. Define FR as the fractional portion of R
						3. Find the scores with Rank IR and with Rank IR + 1, e.g. V[IR] and V[IR+1]
						4. Interpolate by multiplying the difference between the scores by FR and add the result to the lower score, e.g. Pth = FR * (V[IR+1] - V[IR]) + V[IR]
    :type interpolation: {"nearest_neighbour", "linear"}, default: "nearest_neighbour"

    :param compute_if_missing_present: Specifies how to handle the presence of missing values in the input data:
		
		* "on": for each grid point, the percentiles are computed using only the non-missing values
		* "off": for each grid point, if there are any missing values, the result for that point will be a missing value
    :type compute_if_missing_present: {"on", "off"}, default: "on"

    :rtype: :class:`Filedset`


.. mv-minigallery:: percentile

