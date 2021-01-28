
geo_to_grib
=========================

.. container::
    
    .. container:: leftside

        .. image:: /_static/GEO_TO_GRIB.png
           :width: 48px

    .. container:: rightside

		Interpolates irregularly spaced point data (:class:`Geopoints`) into a GRIB field (:class:`Fieldset`), which can then be plotted, saved or combined with other GRIB data. The method used to compute the values of the grid points from the input data depends on the ``interpolation_method`` parameter. The resulting GRIB field can be a regular lat/lon grid of defined size, or else based on a template GRIB file supplied by the user. Note that only the first parameter of a double-valued :class:`Geopoints` vector will be used in the calculations. For the reverse computation, see :func:`grib_to_geo`.


		.. note:: This function performs the same task as the `Geopoints To Grib <https://confluence.ecmwf.int/display/METV/Geopoints+To+Grib>`_ icon in Metview’s user interface. It accepts its parameters as keyword arguments, described below.


.. py:function:: geo_to_grib(**kwargs)
  
    Interpolates irregularly spaced point data (:class:`Geopoints`) into a GRIB field (:class:`Fieldset`).


    :param geopoints: Specifies the input :class:`Geopoints` data.
    :type geopoints: Specifies the input :class:`Geopoints`

    :param grid_definition_mode: If set to "user", the output grid will be a regular lat/lon matrix defined by ``area`` and ``grid``; if set to "grib", a sample :class:`Fieldset` should be specified in ``template_grib``.
    :type grid_definition_mode: {"user", "grib"}, default: "user"

    :param area: Specifies the area of the output ``grid`` in south/west/north/east format. Only available if ``grib_definition_mode`` is "user".
    :type area: list[float], default: [-90, -180, 90, 180]

    :param grid: Specifies a resolution in degrees, thus together with ``area``, determining the limits and density of the regular grid for interpolation of the point data values. Only available if ``grib_definition_mode`` is "user".
    :type grid: list[float], default: [1.5, 1.5]

    :param template_grib: 
    :type template_grib: :class:`Fieldset`

    :param tolerance: Specifies a neighbourhood in degrees around each grid point. All :class:`Geopoints` data within this neighbourhood are used to interpolate the value at the central grid point. E.g. if ``tolerance`` is 2 then all geopoints within a +/-2 degrees square around the grid point are used. If your :class:`Geopoints` data has high spatial density then you can afford to specify a narrow neighbourhood, if the density is sparse you should use a wide neighbourhood. Remember that the wider the neighbourhood the smoother the resulting interpolated field (and the slower the computation).
    :type tolerance: float or list[float], default: 3

    :param interpolation_method: Specifies how the values of the geopoints within the window around a resulting grid point will be combined to produce the resulting value. The available algorithms are:
		
				* "reciprocal": the mean of the values, weighted by the inverse of their distance from the target point. If one of the geopoints lies exactly on the target point then its value is used directly and the rest of the values discarded.
				* "exponential_mean": computes the mean of the values weighted (multiplied) by the following:
		
						 * if ``tolerance`` is not zero: :math:`\exp^{-distance/tolerance^2}`     
						 * if ``tolerance`` is zero: 1 if the point is on the target point, 0 otherwise
						.. note:: This method, combined with setting ``tolerance`` to zero computes the proportion of points which lie exactly on the target point.       
				* "exponential_sum": performs the same computation as "exponential_mean", but does not finally divide by the total weight. With a ``tolerance`` of zero, this method will compute the number of input points that lie exactly on each target point.         
				* "nearest_grid_point_mean": for each target grid point, computes the unweighted mean value of the geopoints for whom this is the closest grid point; any grid point which is not the closest to any geopoints will be given a missing value.         
				* "nearest_grid_point_sum": for each target grid point, computes the unweighted sum of the values of the geopoints for whom this is the closest grid point; any grid point which is not the closest to any geopoints will be given a missing value.        
				* "nearest_grid_point_count": for each target grid point, computes the number of geopoints for whom this is the closest grid point. Note that for a regular target ``grid``, this essentially produces a 'heat map', where the value of a grid point will be the number of geopoints within its grid box. This is not necessarily true for quasi-regular grids, e.g. reduced Gaussian, reduced lat/lon or octahedral (which is just a specific type of reduced Gaussian).
    :type interpolation_method: str, default: "reciprocal"

    :param parameter: If it is not set to 255 specifies the **paramId** ecCodes key in the output field. Otherwise the **paramId** in the sample field is kept.
    :type parameter: number, default: 255

    :param grib_table2_version: If ``parameter`` is not set to 255 specifies the **table2Version** ecCodes key in the output field.
    :type grib_table2_version: number, default: 1

    :rtype: :class:`Fieldset`


.. mv-minigallery:: geo_to_grib

