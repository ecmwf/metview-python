
geo_to_grib
=========================

.. container::
    
    .. container:: leftside

        .. image:: /_static/GEO_TO_GRIB.png
           :width: 48px

    .. container:: rightside

        This icon represents the `Geopoints To Grib <https://confluence.ecmwf.int/display/METV/Geopoints+To+Grib>`_ icon in Metview's user interface.


.. py:function:: geo_to_grib(**kwargs)
  
    Description comes here!


    :param geopoints: Specifies the input data, which must be in ```geopoints`` <https://confluence.ecmwf.int/display/METV/``geopoints``>`_ format (e.g. a ``geopoints`` data icon or an _Observation Filter icon returning ``geopoints``)
    :type geopoints: str


    :param grid_definition_mode: If set to User , the output ``grid`` will be a regular lat/lon matrix defined by the ``parameter``s ``area`` and ``grid`` ; if set to Grib , an example GRIB file should be specified by the ``parameter`` ``template_grib``.
    :type grid_definition_mode: str


    :param area: Specifies a geographical ``area`` over which to carry out the interpolation, the default being for the whole globe. Enter coordinates (lat/lon) of an ``area`` separated by a "/" (top left lat and lon, bottom right lat and lon); alternatively, use the assist button to define the ``area`` graphically. Only available if Grib Definition Mode is User.
    :type area: float or list[float]


    :param grid: Specifies a resolution in degrees, thus together with ``area`` , determining the limits and density of the regular ``grid`` for interpolation of the point data values. Enter the longitude and latitude resolution as numbers separated by a "/". Only available if Grib Definition Mode is User.
    :type grid: float or list[float]


    :param template_grib: 
    :type template_grib: str


    :param tolerance: Specifies a neighbourhood in degrees around each ``grid`` point. All ``geopoints`` data within this neighbourhood are used to interpolate the value at the central ``grid`` point. E.g. if ``tolerance`` is 2 then all ``geopoints`` within a +/-2 degrees square around the ``grid`` point are used.

         If your ``geopoints`` data has high spatial density then you can afford to specify a short neighbourhood, if the density is sparse you should use a wide neighbourhood. Remember that the wider the neighbourhood the smoother the resulting interpolated field (and the slower the computation).
    :type tolerance: float or list[float]


    :param interpolation_method: Specifies how the values of the ``geopoints`` within the window around a resulting ``grid`` point will be combined to produce the resulting value. The available algorithms are:

         *  Reciprocal : the mean of the values, weighted by the inverse of their distance from the target point. If one of the ``geopoints`` lies exactly on the target point then its value is used directly and the rest of the values discarded.
         *  Exponential Mean : computes the mean of the values weighted (multiplied) by the following:

         * if ``tolerance`` is not zero: \\( e^{-distance/``tolerance``^2} \\) 

         * if ``tolerance`` is zero: 1 if the point is on the target point, 0 otherwise
         * note that this method, combined with setting ``tolerance`` to zero computes the proportion of points which lie exactly on the target point
         *  Exponential Sum : performs the same computation as Exponential Mean , but does not finally divide by the total weight. With a ``tolerance`` of zero, this method will compute the number of input points that lie exactly on each target point.
         *  Nearest ``grid``point Mean : for each target ``grid`` point, computes the unweighted mean value of the ``geopoints`` for whom this is the closest ``grid`` point; any ``grid`` point which is not the closest to any ``geopoints`` will be given a missing value
         *  Nearest ``grid``point Sum : for each target ``grid`` point, computes the unweighted sum of the values of the ``geopoints`` for whom this is the closest ``grid`` point; any ``grid`` point which is not the closest to any ``geopoints`` will be given a missing value
         *  Nearest ``grid``point Count : for each target ``grid`` point, computes the number of ``geopoints`` for whom this is the closest ``grid`` point. Note that for a regular target ``grid``, this essentially produces a 'heat map', where the value of a ``grid`` point will be the number of ``geopoints`` within its ``grid`` box. This is not necessarily true for quasi-regular ``grid``s, e.g. reduced Gaussian, reduced lat/lon or octahedral (which is just a specific type of reduced Gaussian).
    :type interpolation_method: str


    :param parameter: If not set to 255, then the paramId GRIB_API key on the output field will be set to this value.

         ## ``grib_table2_version``

         If ``parameter`` is not set to 255, then the table2Version GRIB_API key on the output field will be set to this value.
    :type parameter: number


    :param grib_table2_version: 
    :type grib_table2_version: number


    :rtype: None


.. minigallery:: metview.geo_to_grib
    :add-heading:

