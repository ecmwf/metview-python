Fieldset functions
******************

.. .. minigallery:: metview.gradient
..     :add-heading:

.. py:function:: abs(fs)
   
   Returns the fieldset of the absolute value of ``fs`` at each grid point or spectral coefficient. 

   :param fs: input fieldset
   :type fs: :class:`Fieldset`
   :rtype: :class:`Fieldset`

   Missing values are retained, unaltered by the calculation.

.. py:function:: accumulate(fs)

   For each field in ``fs`` this function calculates the sum of all the values of the field. If there is only one field in ``fs`` it returns a number, otherwise a numpy array is returned. Only non-missing values are considered in the calculation. For fields with no valid values NaN is returned.

   :param fs: input fieldset
   :type fs: :class:`Fieldset`
   :rtype: float or ndarray or None

.. py:function:: acos(fs)
   
   Return the fieldset of the arc cosine function of ``fs`` at each grid point. Results are in radians. Missing values are retained, unaltered by the calculation.
   
   :param fs: input fieldset
   :type fs: :class:`Fieldset`
   :rtype: :class:`Fieldset`

.. py:function:: asin(fs)
   
   Return the fieldset of the arc sine function of ``fs`` at each grid point. Results are in radians. Missing values are retained, unaltered by the calculation.
   
   :param fs: input fieldset
   :type fs: :class:`Fieldset`
   :rtype: :class:`Fieldset`   

.. py:function:: atan(fs)
   
   Return the fieldset of the arc tangent function of ``fs`` at each grid point. Results are in radians. Missing values are retained, unaltered by the calculation.
   
   :param fs: input fieldset
   :type fs: :class:`Fieldset`
   :rtype: :class:`Fieldset`

.. py:function:: average(fs)

   For each field in ``fs`` calculates the average of all the field values. 
   
   :param fs: input fieldset
   :type fs: :class:`Fieldset`
   :rtype: float or ndarray or None

   If there is only one field in ``fs`` a float is returned, otherwise a numpy array is returned. Only non-missing values are considered in the calculation. If there are no valid values, the function returns NaN for that field.

   .. note::
      :func:`average` simply returns the mathematical average of all the field values using the following formula:

      .. math:: 
      
         average = \frac {1}{N} \sum_{i}^{N}f_{i}
        
      To get the physically correct average based on the grid cell areas use :func:`integrate`.

.. py:function:: average_ew(fs, area, increment)
   
   Computes the zonal average for each field in ``fs`` for a set of latitude belts.

   :param fs: input fieldset
   :type fs: :class:`Fieldset`
   :param list area: area as [N,W,S,E] to perform the averaging 
   :param int increment: increment in degrees defining the size of the latitude belts
   :rtype: 1d-ndarray or 2d-ndarray

   If ``fs`` only contains one field a 1d-ndarray is returned otherwise the result is a 2d-ndarray. 
   
   The averaging is performed for each field individually within the latitude belts defined by ``area`` and ``increment``. Each grid point value is weighted by the cosine of its latitude. Missing values are ignored. If a latitude belt contains no grid point values Nan is returned for that belt. 

   :Example:
      
      .. code-block:: python

         ave = average_ew(fs, [60,-180,-60,180], 2.5)

      Here we compute the averages over full latitude circles starting from 60N, stepping by 2.5 degrees until 60S. If ``fs`` contains only one field the output will be a 1d-ndarray of 49 E-W average values, from North to South. If ``fs`` contains n fields then the output will be an array of n 1d-arrays each containing 49 values. Each value in the result represents the average at latitude Lat based on those grid points whose latitude coordinate is between Lat-1.25 and Lat+1.25 (1.25 is 2.5/2), i.e. within a latitude belt with width of 2.5 degrees, centered around Lat.

.. py:function:: average_ns(fs, area, increment)
   
   Computes the meridional average for each field in ``fs`` for a set of longitude strips.

   :param fs: input fieldset
   :type fs: :class:`Fieldset`
   :param list area: area as [N,W,S,E] to perform the averaging 
   :param int increment: increment in degrees defining the size of the longitude strips
   :rtype: 1d-ndarray or 2d-ndarray
   
   The averaging is performed for each field individually within the longitude strips defined by ``area`` and ``increment``. Each grid point value is weighted by the cosine of its latitude. Missing values are ignored. If a longitude strip contains no grid point values Nan is returned for that strip. 

   :Example:
      
      .. code-block:: python

         ave = average_ns(fs, [30,0,-30,360], 5)

      Here we compute the averages over longitude strips bounded by 30N and 30S, in 5 degree intervals around the globe. The result for each field in ``fs`` is vector of 73 values (in this case values for 0 and 360 are duplicated values). Each value returned (representing the average at longitude Lon) is the average of non-missing values in those grid points whose longitude coordinate is between Lon-2.5 and Lon+2.5 (2.5 is 5/2), in the strip between 30N and 30S.


.. py:function:: bearing (fs, ref_lat_or_coords, [ref_lon])

   Computes the bearing for each grid point with reference to the given location. 
   
   :param fs: input fieldset
   :type fs: :class:`Fieldset`
   :param ref_lat_or_coords: latitude of the reference point or coordinates of the reference point as [lat, lon]
   :type ref_lat_or_coords: float or list
   :param float ref_lon: longitude of the reference point
   :rtype: :class:`Fieldset`
   
   The bearing is the angle between the Northward meridian going through the reference point and the great circle connecting the reference point and the given gridpoint. It is measured in degrees clockwise from North. If a gridpoint is located on the same latitude as the reference point the bearing is regarded constant: it is either 90° (East) or 270° (West). If the gridpoint is co-located with the reference point the bearing is set to a missing value. The reference location should be specified in degrees.

.. py:function:: base_date(fs)

   Returns the base dates (including the time components) of the given fields. If ``fs`` has only one field, a date is returned; otherwise a list of dates is returned.

   :param fs: input fieldset
   :type fs: :class:`Fieldset`
   :rtype: datetime.datetime or list of datetime.datetime objects

.. py:function:: bitmap(fs, value_or_field)

   Returns a copy of ``fs`` with zero or more of its values replaced with the GRIB missing value indicator. 
   
   :param fs: input fieldset
   :type fs: :class:`Fieldset`
   :param value_or_field: bitmap value or bitmap fieldset
   :type value_or_field: float or :class:`Fieldset`
   :rtype: :class:`Fieldset`
   
   The behaviour of :func:`bitmap` depends on the arguments:

   * if ``value_or_field`` is a number any value being equal to it is replaced with the missing value indicator in ``fs``. 
   * if ``value_or_field`` is a :class:`Fieldset` with the same number of fields as ``fs`` the result takes the arrangement of missing values from ``value_or_field``. 
   * if ``value_or_field`` contains only one field the arrangement of missing values from that field are copied into all fields of the output fieldset. See also :func:`nobitmap`.


.. py:function:: cos(fs)

   Returns the fieldset of the cosine of ``fs`` at each grid point. Input values must be in radians. Missing values are retained, unaltered by the calculation.

   :param fs: input fieldset
   :type fs: :class:`Fieldset`
   :rtype: :class:`Fieldset`  

.. py:function:: coslat(fs)

   Returns the fieldset of the cosine of the latitude of ``fs`` at each grid point. 

   :param fs: input fieldset
   :type fs: :class:`Fieldset`
   :rtype: :class:`Fieldset` 

   Missing values are retained, unaltered by the calculation. 

.. py:function:: count(fs)

   Returns the number of fields in ``fs``.

   :param fs: input fieldset
   :type fs: :class:`Fieldset`
   :rtype: number 

.. py:function:: corr_a(fs1, fs2, [area])    
   
   Computes the correlation between ``fs1`` and ``fs2`` over a weighted area. 
   
   :param fs1: first input fieldset
   :type fs: :class:`Fieldset`
   :param fs2: second input fieldset
   :type fs: :class:`Fieldset`
   :param list area: area as [N,W,S,E] to perform the computations
   :rtype: float or list 
   
   If the ``area`` is not specified the whole field will be used in the calculation. The result is a number for a single field or a list for a multi-field :class:`Fieldset`.

   .. note::
      The following lines are equivalent although the first one is more efficient:
      
      .. code-block:: python

         z = corr_a (x, y)
         z = covar_a (x, y) / (sqrt(var_a(x)) * sqrt(var_a(y)))


.. py:function:: covar(fs1, fs2)   

   Computes the covariance of ``fs1`` and ``fs2``. 
   
   :param fs1: first input fieldset
   :type fs: :class:`Fieldset`
   :param fs2: second input fieldset
   :type fs: :class:`Fieldset`
   :rtype: :class:`Fieldset`
   
   With N fields in ``fs1`` and ``fs2`` by denoting the i-th value in the k-th field by :math:`x_{i}^{k}` and :math:`y_{i}^{k}` respectively, the output values can be written as:

   .. math:: 
      
         z_{i} = \frac {1}{N} \sum_{k}^{N}x_{i}^{k}y_{i}^{k} - \frac {1}{N} \sum_{k}^{N}x_{i}^{k} \frac {1}{N} \sum_{k}^{N}y_{i}^{k}

   A missing value in either ``fs1`` or ``fs2`` will result in a missing value in the corresponding place in the output.

   .. note::
      The following lines are equivalent although the first one is more efficient:
      
      .. code-block:: python

         z = covar(x,y)
         z = mean(x*y)-mean(x)*mean(y)


.. py:function:: covar_a(fs1, fs2, [area])   

   Computes the covariance of ``fs1`` and ``fs2`` over a weighted area. 
   
   :param fs1: first input fieldset
   :type fs: :class:`Fieldset`
   :param fs2: second input fieldset
   :type fs: :class:`Fieldset`
   :param list area: area as [N,W,S,E] to perform the computations
   :rtype: float or list 
   
   If the ``area`` is not specified the whole field will be used in the calculation. The result is a number for a single field or a list for a multi-field :class:`Fieldset`.

.. py:function:: datainfo(fs)   

   Returns a list of dictionaries containing some metadata for each field in ``fs``. 
   
   :param fs: input fieldset
   :type fs: :class:`Fieldset`
   :rtype: list of dictionary
   
   The dictionary contains the following members: 
   
   * index: the index of the field in the fieldset (indexing starts at 1)
   * number_present: the number of values
   * number_missing: the number of missing values
   * proportion_present: the proportion of the 
   * proportion_missing: the proportion
   
.. py:function:: direction(u, v)

   Computes the meteorological wind direction in each grid point of ``u`` and ``v``.

   :param u: u wind component
   :type u: :class:`Fieldset`
   :param v: v wind component
   :type v: :class:`Fieldset`
   :rtype: :class:`Fieldset`

   The resulting values are directions, in degrees clockwise from North, where a value of 0 represents a wind from the North and a value of 90 represents a wind from the East. A missing value in either ``u`` or ``v``  will result in a missing value in the corresponding place in the output fieldset.

.. py:function:: distance(fs, ref_lat_or_coords, [ref_lon])

   Returns a fieldset with the value in each grid point being the distance in **metres** from a given geographical location (the reference). 
   
   :param fs: input fieldset
   :type fs: :class:`Fieldset`
   :param ref_lat_or_coords: latitude of the reference point or coordinates of the reference point as [lat, lon]
   :type ref_lat_or_coords: float or list
   :param float ref_lon: longitude of the reference point
   :rtype: :class:`Fieldset`
   
   The reference location should be specified in degrees.

.. py:function:: div(fs1, fs2):

   Returns a fieldset where values in each grid point are the integer part of the division of ``fs1`` by ``fs2`` (the function is operating field by field).

   :param fs1: first input fieldset
   :type fs1: :class:`Fieldset`
   :param fs2: second input fieldset
   :type fs2: :class:`Fieldset`
   :rtype: :class:`Fieldset` 

   A missing value in either ``fs1`` or ``fs2`` will result in a missing value in the corresponding place in the output fieldset.

.. py:function:: divergence(fx, fy)

   Computes the horizontal divergence of 2-dimensional vector fields. 
   
   :param fx: zonal (west-east) vector component fieldset
   :type fs: :class:`Fieldset`
   :param fx: meridional (south-north) vector component fieldset
   :type fs: :class:`Fieldset`
   :rtype: :class:`Fieldset`  
   
   The computations for a vector field f=(fx , fy) are based on the following formula:

   .. math:: 
      
      div(f) = \frac{1}{R \ cos\phi}\frac{\partial f_x}{\partial \lambda} + \frac{1}{R}\frac{\partial f_y}{\partial \phi} - \frac{f_y}{R}tan\phi

   where:
   
   * R is the radius of the Earth (in m)
   * :math:`\phi` is the latitude
   * :math:`\lambda` is the longitude.

   The derivatives are computed with a second order finite-difference approximation. The resulting fields contain missing values on the poles. If ``fx`` and ``fy`` are horizontal wind components the GRIB **paramId** of the resulting field is set to 155 (=divergence). 
   
   .. warning::
      :func:`divergence` is only implemented for regular latitude-longitude grids.


.. py:function:: duplicate(fs, number_of_copies)

   Returns a fieldset with the specified ``number_of_copies`` of the field in ``fs``. 

   :param fs: input fieldset with **one field** only
   :type fs: :class:`Fieldset`
   :param int number_of_copies: the number of copies required
   :rtype: :class:`Fieldset` 

.. py:function:: exp(fs)

   Returns the fieldset of the exponential of ``fs`` at each grid point. Missing values are retained, unaltered by the calculation.

   :param fs: input fieldset
   :type fs: :class:`Fieldset`
   :rtype: :class:`Fieldset`  


.. py:function:: find(fs, value_or_range, [area_or_mask])

   Returns a list of locations (lat/lon pairs) where the values of ``fs`` equal to or within the range of ``value_or_range``. 
   
   :param fs: input fieldset 
   :type fs: :class:`Fieldset`
   :param value_or_range: the value or range defining the search condition
   :type value_or_range: int or list 
   :param area_or_mask: area or mask field restricting the search
   :type area_or_mask: list or :class:`Fieldset`
   :rtype: list of lists

   The primary search condition is defined by ``value_or_range``:

   * if ``value_or_range`` is a number the locations where ``fs`` equals to this number are returned
   * if ``value_or_range`` is a list of [v1, v2] the locations where ``fs`` values are within the closed range of [v1, v2] are returned

   The optional ``area_or_mask`` argument can pose an additional search condition:

   * if ``area_or_mask`` is a list of four numbers it defines the area as [North,West,South,East] for the search
   * if ``area_or_mask`` is a :class:`Fieldset` with one field it defines a mask for the search, e.i. only those gridpoints are checked where the mask value is non-zero.
   
   Missing values in ``fs`` are not returned.

.. py:function:: float(fs, [number_of_bits])

   Returns a fieldset with integer data converted into floating point data for more accurate computations.
   
   :param fs: input fieldset
   :type fs: :class:`Fieldset`
   :param number number_of_bits: defines the number of bits used for packing the float values. If not given, the default value of 24 is used (unless :func:`gribsetbits` has been called to set it).  
   :rtype: :class:`Fieldset` 

.. py:function:: first_derivative_x(fs)
   
   Computes the zonal (from West to East) partial derivative of each field in ``fs``. 
   
   :param fs: input fieldset
   :type fs: :class:`Fieldset` 
   :rtype: :class:`Fieldset`
   
   The computations for a field f are based on the following formula:

   .. math::

      \frac {\partial f}{\partial x} = \frac{1}{R \ cos\phi}\frac{\partial f}{\partial \lambda} 

   where:
   
   * R is the radius of the Earth
   * :math:`\phi` is the latitude
   * :math:`\lambda` is the longitude.

   The derivatives are computed with a second order finite-difference approximation. The resulting fields contain missing values on the poles. 
   
   .. warning::
      :func:`first_derivative_x` is only implemented for regular latitude-longitude grids.


.. py:function:: first_derivative_y(fs)

   Computes the meridional (from South to North) partial derivative of each field in the fieldset. 
   
   :param fs: input fieldset
   :type fs: :class:`Fieldset` 
   :rtype: :class:`Fieldset`
   
   The computations for a field f are based on the following formula:

   .. math::

      \frac {\partial f}{\partial y} = \frac{1}{R}\frac{\partial f}{\partial \phi} 
   
   where:
   
   * R is the radius of the Earth
   * :math:`\phi` is the latitude
   * :math:`\lambda` is the longitude.

   The derivatives are computed with a second order finite-difference approximation. The resulting fields contain missing values on the poles. 

   .. warning::
      :func:`first_derivative_y` is only implemented for regular latitude-longitude grids.

.. py:function:: frequencies(fs, bins, [area]) 

   Counts the number of grid points whose values fall within a set of specified ``bins``. 
   
   :param fs: input fieldset
   :type fs: :class:`Fieldset` 
   :param list bins: bins used for the computations
   :param list area: area as [North,West,South,East] used for the computations
   :rtype: list or list of lists

   ``bins`` is a list with numbers in ascending order defining the bins. The first and last bins are unbounded. E.g. if ``bins`` = [0, 10, 20] the following bins are defined:
   
   * first bin: (, 0)
   * second bin: [0, 10),
   * third bin: [10, 20),
   * fourth bin: [20, ),
   
   Missing values in ``fs`` are not included in the results.

   If ``fs`` has just one field the result is a list of n+1 elements where n is the number of elements in ``bins``. If ``fs`` has more than one field the result is a list of lists, one for each field. 
   
   .. warning::
      Note that this function accumulates its results between fields in ``fs``!


.. py:function::  geostrophic_wind_pl(z)

   Computes the geostrophic wind from geopotential fields defined on pressure levels. 
   
   :param z: input fieldset (geopotential on pressure levels)
   :type fs: :class:`Fieldset` 
   :rtype: :class:`Fieldset`
   
   For a given z geopotential field the computation of the geostrophic wind components is based on the following formulas:
   
   .. math::
   
      u_g = -\frac{1}{f} \frac{1}{R}\frac{\partial z}{\partial \phi}

      v_g = \frac{1}{f} \frac{1}{R \ cos\phi}\frac{\partial z}{\partial \lambda}

   where:
   
   * R is the radius of the Earth
   * :math:`\phi` is the latitude
   * :math:`\lambda` is the longitude.
   * :math:`f=2\Omega sin\phi` is the Coriolis parameter, where :math:`\Omega` is the Earth's angular velocity.

   The derivatives are computed with a second order finite-difference approximation. The resulting fieldset contains two fields for each input field: the u and v geostrophic wind components. In each output field the points close to the poles and the Equator are bitmapped (they contain missing values). 
   
   .. warning::
      :func:`geostrophic_wind_pl` is only implemented for regular latitude-longitude grids.

.. py:function:: gfind(fs, value, [eps])

   Returns a :class:`Geopoints` holding the grid points whose value is equal to ``value``. 
   
   :param fs: input fieldset
   :type fs: :class:`Fieldset`
   :param float value: the value to match
   :param float eps: when specified data values are selected when :math:`abs(data - value) < eps`
   :rtype: :class:`Fieldset`  
  
   Missing values in ``fs`` are not returned.

.. py:function:: gradient(fs)

   Computes the horizontal gradient of each field in a fieldset. 
   
   :param fs: input fieldset
   :type fs: :class:`Fieldset`
   :rtype: :class:`Fieldset`  
   
   The derivatives are computed with a second order finite-difference approximation. The resulting fieldset contains two fields for each input field: the zonal derivative followed by the meridional derivative. The output fields contain missing values at the poles.

   The computations for a field f are based on the following formula:

      .. math::

         \nabla f = (\frac {\partial f}{\partial x}, \frac {\partial f}{\partial y}) = (\frac{1}{R \ cos\phi}\frac{\partial f}{\partial \lambda}, \frac{1}{R}\frac{\partial f}{\partial \phi} )
   
   where:

   * R is the radius of the Earth (in m)
   * :math:`\phi` is the latitude
   * :math:`\lambda` is the longitude.

   .. warning::
      :func:`gradient` is only implemented for regular latitude-longitude grids.

.. py:function:: grib_get(fs, keys, [grouping])

   Extracts the values of ecCodes keys from the GRIB headers of ``fs`` in an efficient way. 
   
   :param fs: input fieldset
   :type fs: :class:`Fieldset`
   :param list keys: the ecCodes keys
   :param str grouping: grouping mode ("field" or "key")
   :rtype: list of lists
 
   A single call to :func:`grib_get` can replace multiple calls to the other grib_get_* functions and is hence more efficient. 

   By default the keys will be retrieved as str, but their type can be specified by adding a modifier to their names, following the convention used by the ecCodes command line tool *grib_ls* where the key name is followed by a colon and then one or two characters which specify the type:
   
   * s=string
   * l=long
   * d=double
   * la=long array
   * da=double array. 
   
   For example, the key 'centre' can be retrieved as a str with 'centre' or 'centre:s', or as a number with 'centre:l'. 
   
   The result is always a list of lists:
   
   * if ``grouping`` is not specified or set to 'field', the result will be grouped by field, containing one list per field, each of these lists containing one element per key
   * if ``grouping`` is 'key', the result will be grouped by key, containing one list per key, each of these lists containing one element per field. 
   
   :Example:
   
      The following lines of code on a particular 6-field fieldset:
      
      .. code-block:: python

         print(mv.grib_get(f, 
               ['editionNumber', 'centre', 'level', 'step'], 'field'))
         print(mv.grib_get(f, 
               ['editionNumber', 'centre:l', 'level', 'step'], 'key'))

      produces this output:
      
      .. code-block:: python

         [[1,ecmf,1000,0],[1,ecmf,500,0],[1,ecmf,100,0],[1,ecmf,1000,48]]
         [[1,1,1,1],[98,98,98,98],[1000,500,100,1000],[0,0,0,48]]

.. py:function:: grib_get_long(fs, key)
.. py:function:: grib_get_double(fs, key)
.. py:function:: grib_get_string(fs, key)
.. py:function:: grib_get_long_array(fs, key)
.. py:function:: grib_get_double_array(fs, key)
.. py:function:: grib_get_string_array(fs, key)

   Extracts the value of an ecCode key from the GRIB headers of ``fs``. 
   
   :param fs: input fieldset
   :type fs: :class:`Fieldset`
   :param string key: the ecCodes key
   :rtype: float, str or list

   This group of functions is based on the similarly named ecCodes C API functions. The available ecCodes keys can be inspected in various ways:

   * in an interactive Metview session with the GRIB Examiner (right-click Examine or double-click on a GRIB icon)
   * with the ecCodes command line tool *grib_dump* 
   
   Fot further details about keys read `GRIB Keys - ecCodes GRIB FAQ 
   <https://confluence.ecmwf.int/display/UDOC/GRIB+Keys+-+ecCodes+GRIB+FAQ>`_.
   
   :func:`grib_get_long`, :func:`grib_get_double` and :func:`grib_get_string` return a value if ``fs`` has a single field, otherwise they return a list. 
   
   :func:`grib_get_long_array` and :func:`grib_get_double_array` return a 1d-ndarray if ``fs`` has a single field, otherwise they return a list 1d-ndarrays.
   
   :func:`grib_get_string` returns a list of strings if ``fs`` has a single field, otherwise it Returns a list lists.

   .. note::
      :func:`grib_get_long` and :func:`grib_get_long_array` extract a C long value internally but it is cast into float on return.

   :Example:

      This code:

      .. code-block:: python

         print(mv.grib_get_long(data, "editionNumber"))
         print(mv.grib_get_long(data, "max"))
         print(mv.grib_get_double(data, "max"))
         print(mv.grib_get_string(data, "max"))
         print(mv.grib_get_string(data, "typeOfGrid"))

      can result in the following output for single-field GRIB file:

      .. code-block:: python

         1
         317
         317.278808594
         317.279
         regular_ll

   :Example:

      This code shows how to obtain the list of latitudes from a reduced Gaussian grid fieldset:

      .. code-block:: python
         
         import metview as mv

         g = mv.read('your_data_in_gg.grb')
         pl = mv.grib_get_long_array (g, 'pl')
         print(len(pl))
         print(pl)


.. py:function:: grib_set(fs, keys_and_values)

   Sets information in the GRIB header of ``fs`` and returns a new :class:`Fieldset`.
   
   :param fs: input fieldset
   :type fs: :class:`Fieldset`
   :param list keys_and_values: the ecCodes keys and values
   :rtype: :class:`Fieldset`
   
   ``keys_and_values`` has to be a list of the ecCodes keys and their values following each other. The actual data types are deduced the value passed (and not from the key name!). 

   :Example:

      .. code-block:: python
         
         import metview as mv
         f = mv.grib_set(f, 
            ["date", 20150601,       # int
             "time", 0600,           # int
             "stepType", "avg",      # str
             "startStep", 0 ,        # int
             "endStep", 31,          # int
             "unitOfTimeRange", "D", # str
             "longitudeOfLastGridPointInDegrees", 100.5])  #  float

.. py:function:: grib_set_long(fs, keys_and_values)
.. py:function:: grib_set_double(fs, keys_and_values)
.. py:function:: grib_set_string(fs, keys_and_values)

   Sets information in the GRIB header of ``fs`` and returns a new :class:`Fieldset`.
   
   :param fs: input fieldset
   :type fs: :class:`Fieldset`
   :param list keys_and_values: the ecCodes keys and values
   :rtype: :class:`Fieldset`
   
   ``keys_and_values`` has to be a list of the ecCodes keys and their values following each other. The actual values have to match the type of the function.  If applied to a multi-field fieldset, then all fields are modified.

   :Example:

      .. code-block:: python

         f = mv.grib_set_long(f,
            ["centre", 99,
             "level", 200])

.. py:function:: gribsetbits(number_of_bits)

   Sets the number of GRIB packing bits to ``number_of_bits`` (eg 8, 10, 16), and returns the previously used internal value. 

   :param int number_of_bits: number of bits
   :rtype: float 

   This function is particularly useful when dealing with 10-bit satellite images as these require GRIB packing to be set to 10 bits.

.. py:function:: grid_cell_area(fs)

   Computes the area of each grid cell in ``fs`` with the grid points supposed to be at the centre of the grid cells. 
   
   :param fs: input fieldset
   :type fs: :class:`Fieldset`
   :rtype: :class:`Fieldset` 

   The grid cell area is returned in m2 units. This function only works for regular latitude-longitude grids and Gaussian grids.

.. py:function:: indexes(fs, values)

   Finds the index of the values at each gridpoint of ``fs`` in the ``values`` array. 

   :param fs: input fieldset
   :type fs: :class:`Fieldset`
   :type ndarray values: the values to find the index for
   :rtype: :class:`Fieldset`

   Indexes are zero-based and will always have a minimum value of zero and a maximum value equal to the index of the last element of ``values``. A value lying between two values in ``values`` will use the index of the nearest value; if equidistant, then the higher value is used. ``values`` must be sorted in ascending order. 
 
   :Example: 
      
      Let us suppose that our input fieldset contains these values:

      .. code-block:: python

             10 10 30 40
         f = 15 25 35 45
             8  4 20 11

      then the following call:

      .. code-block:: python

         import metview as mv
         import numpy as np
         g = mv.indexes(f, np.array([5, 10, 15, 20, 25, 30]) 

      produces this GRIB, with values equal to the input values' positions in the input array:

      .. code-block:: python

             1 3 5 5
         g = 2 4 5 5
             1 0 3 1

.. py:function:: int(fs)

   Returns the fieldset of the integer part of ``fs`` at each grid point or spectral coefficient.

   :param fs: input fieldset
   :type fs: :class:`Fieldset`
   :rtype: :class:`Fieldset` 

   Missing values are retained, unaltered by the calculation.

.. py:function:: integer(fs)

   Returns the fieldset of the integer part of ``fs`` at each grid point or spectral coefficient.

   :param fs: input fieldset
   :type fs: :class:`Fieldset`
   :rtype: :class:`Fieldset` 

   This function modifies the resulting GRIB header to be of integer data type. Missing values are replaced with LONG_MAX. 
   
   .. note::
      :func:`integer` was used in Metview 3 to enable the plotting of certain types of satellite imagery.

.. py:function:: integral(fs)

   Computes the surface integral of each field in ``fs``. 
   
   :param fs: input fieldset
   :type fs: :class:`Fieldset`
   :rtype: float or ndarray

   The result is either a number (for one input field) or a 1D-ndarray (for multiple input fields). The computations are based on the cell area (in m2 units) returned by :func:`grid_cell_area`.

.. py:function:: integrate(fs, [area_or_mask])

   Computes the average of each field in ``fs`` over an area. 
   
   :param fs: input fieldset
   :type fs: :class:`Fieldset`
   :param area_or_mask: list defining an area or fieldset defining a mask
   :type area_or_mask: list or :class:`Fieldset`
   :rtype: float or ndarray or None
   
   .. note::
      The computations are based on the following approximation of the grid cell areas:

      .. math::

         A_{i} = 2 R^{2} cos\phi_{i} sin(\frac{\Delta\phi_{i}}{2}) \Delta\lambda_{i}
   
      where:

      * R is the radius of the Earth
      * :math:`\phi_{i}` is the latitude of the i-th grid cell
      * :math:`\Delta\phi_{i}` is the size of the grid cells in latitude
      * :math:`\Delta\lambda_{i}` is the size of the i-th grid cell in longitude.
   
      The function then supposes that Δφi is constant and the weighted average over the area is computed as:
   
      .. math::

         \frac {\sum_{i}f_{i} A_{i}}{\sum_{i}A_{i}} = \frac {\sum_{i}f_{i}cos\phi_{i}\Delta\lambda_{i}}{\sum_{i}cos\phi_{i}\Delta\lambda_{i}}

   The formula above is only used for regular **latitude-longitude and Gaussian grids**. For all other grid types :func:`integrate` simply returns the mathematical average of the values (just like :func:`average` does).

   .. warning:: 
   
      Please note that for **Gaussian grids** the formula can only be only regarded as an approximation since :math:`\Delta\phi_{i}` is not constant!

   If ``fs`` contains only one field a number is returned. If there is more than one field a numpy array is returned. Missing values in the input fieldset are bypassed in this calculation. For each field for which there are no valid values None is returned.

   * If ``fs`` is the only argument the integration is done on all grid points.
   * If ``area_or_mask`` is a list it must contain four numbers which are respectively the **north**, **west**, **south** and **east** boundaries of an area. The integration is done on the grid points contained inside this area:

      .. code-block:: python
   
         europe = [75,-12.5,35,42.5]
         x = integrate(field, europe) 

   * If ``area_or_mask`` is a fieldset it is used as a mask. It should contain either one or as many fields as the first fieldset. If it has a single field then this mask is applied to all fields of the input fieldset. If it has the same number of fields as ``fs``, then a different mask is applied to each input field. The integration is performed only on the grid points where the mask values are non zero. The following code shows a simple example:
      
      .. code-block:: python

         # Retrieve land-sea mask and interpolate to LL grid
         lsm = retrieve(
            type : "an",
            date : -1,
            param : "lsm",
            grid : [1.5,1.5],
            levtype : "sfc"
         )

         # The following line forces the values to 0 or 1.
         lsm = lsm > 0.5

         # Now compute the average value on land and on sea
         land = integrate(field, lsm)
         sea = integrate(field, not lsm) 

.. py:function:: interpolate(fs, lat_or_locations, [lon])

   Interpolate the values of ``fs`` to a given location(s) using **bilinear** interpolation. 
     
   :param fs: input fieldset
   :type fs: :class:`Fieldset`
   :param lat_or_locations: 
   :type lat_or_locations: float or list or :class:`Geopoints`
   :param lon: 
   :type lon: float
   :rtype: float or ndarray or :class:`Geopoints` or None

   A **single target location** can be defined with ``lat`` and ``lon`` or by specifying a list of [lat, lon] as ``lat_locations``. If ``fs`` has only one field, a float is returned; otherwise a 1D-ndarray is returned. Where it is not possible to generate a sensible value due to lack of valid data in ``fs``, None is returned.

   For multiple target locations ``lat_or_locations`` must be a :class:`Geopoints` and in this case the first field in ``fs`` is interpolated for each position of the :class:`Geopoints`. The output is then another :class:`Geopoints` taking the date, time and level from ``fs``. Where it is not possible to generate a sensible value due to lack of valid data in the fieldset NaN is used (this can be removed from the output with :func:`remove_missing_values`). 
   
   .. note::
      A similar function, :func:`nearest_gridpoint`, also exists.

.. py:function:: laplacian(fs)

   Computes the Laplacian of each field in ``fs``. 
   
   :param fs: input fieldset
   :type fs: :class:`Fieldset`
   :rtype: :class:`Fieldset`
   
   The computations for a field f are based on the following formula:

   .. math::
 
      \triangle f =\frac{1}{R^2 \ cos^2\phi}\frac{\partial^2 f}{\partial \lambda^2} + \frac{1}{R^2}\frac{\partial^2 f}{\partial \phi^2} - \frac{1}{R^2}tan\phi\frac{\partial f}{\partial \phi}

   where:

      * R: radius of the Earth
      * :math:`\phi`: latitude
      * :math:`\lambda`: longitude.

   The derivatives are computed with a second order finite-difference approximation. The resulting fields contain missing values on the poles. 

   .. warning::
      :func:`laplacian` is only implemented for regular latitude-longitude grids.

.. py:function:: latitudes(fs)

   Returns the latitudes of the grid points in ``fs`` as an ndarray. 
   
   :param fs: input fieldset
   :type fs: :class:`Fieldset`
   :rtype: 1D-ndarray or list of 1D-ndarrays

   If ``fs`` contains more than one field a list of ndarrays is returned. Each of these ndarrays contains one value per gridpoint in each field.

.. py:function:: log(fs)

   Returns the fieldset of the natural logarithm of ``fs`` at each grid point. Missing values are retained, unaltered by the calculation.

   :param fs: input fieldset
   :type fs: :class:`Fieldset`
   :rtype: :class:`Fieldset` 

.. py:function:: log10(fs)

   Returns the fieldset of the log base 10 of ``fs`` at each grid point. Missing values are retained, unaltered by the calculation.

   :param fs: input fieldset
   :type fs: :class:`Fieldset`
   :rtype: :class:`Fieldset`

.. py:function:: longitudes(fs)

   Returns the longitudes of the grid points on ``fs`` as an ndarray. 
   
   :param fs: input fieldset
   :type fs: :class:`Fieldset`
   :rtype: 1D-ndarray or list of 1D-ndarrays

   If ``fs`` contains more than one field a list of ndarrays is returned. Each of these ndarrays contains one value per gridpoint in each field.

.. py:function:: lookup(indexer, values)

   Build an output fieldset using the values in ``indexer`` as indices for a look-up in ``values``.

   :param index: indexer fieldset
   :type fs: :class:`Fieldset`
   :param values: values to choose from
   :type values: :class:`Fieldset` or 1D-ndarray
   :rtype: :class:`Fieldset`

   :func:`lookup` takes the grid values in ``indexer`` and uses them as index in ``values`` in the following way:

      * let us suppose a grid value in the i-th ``indexer`` field is N (for float values the integer part is taken)
      * what happens depends on the type of ``values``:

         * if ``values`` is a :class:`Fieldset` the value at the same gridpoint in the (N-1)-th field in ``values`` is written into the i-th output field at the given gridpoint (here field indexing starts at 0)
         * if ``values`` is an ndarray the value at (N-1)-th position in the ``values`` array is written into the i-th output field at the given gridpoint
   
   The output will have has as many fields as there are in ``indexer``.

   Any missing values in ``indexer`` will cause the function to fail with a "value out of range" error message.

.. py:function:: mask(fs, area)

   For each field in ``fs`` creates a field containing grid point values of 0 or 1 according to whether they are outside or inside the ``area``.

   :param fs: input fieldset
   :type fs: :class:`Fieldset`
   :param list area: area as [N, W, S, E]
   :rtype: :class:`Fieldset`
   
   :Example:

      Non-rectangular masks, and even convex masks can be created by using the operators **and**, **or** and **not**. To create the following mask:

      .. image:: images/mask_1.png
         :width: 300px

      First decompose it into basic rectangles:

      .. image:: images/mask_2.png
         :width: 300px

      Then create a mask for each of them and use **and** and **or** to compose the desired mask like this:

      .. code-block:: python
         
         import metview as mv

         # Define basic rectangles
         a = [50,-120,10,-30]
         b = [20,20,50,10]
         c = [50,50,40,100]
         d = [35,-60,-40,100]

         # The field defining the grids
         f = mv.read(path_to_your_grib_file)

         # First compute the union of a,c and d
         m = mv.mask(f,a) or mv.mask(f,d) or mv.mask(f,c)

         # Then remove b
         m = m and not mv.mask(f,b)


.. fieldset max ( fieldset )
.. fieldset min ( fieldset )

.. Returns the fieldset of maximum (minimum) value of the input fieldset at each grid point or spectral coefficient. A missing value in either input fieldset will result in a missing value in the corresponding place in the output fieldset.


.. fieldset max ( fieldset,fieldset )
.. fieldset min ( fieldset,fieldset )

.. Returns the fieldset of maximum (minimum) value of the two input fieldsets at each grid point or spectral coefficient. A missing value in either input fieldset will result in a missing value in the corresponding place in the output fieldset.


.. fieldset max ( fieldset,number )
.. fieldset min ( fieldset,number )

.. Returns the fieldset of the maximum (minimum) of the number and the fieldset value at each grid point or spectral coefficient. Missing values in the input fieldset are transferred to the output fieldset.


.. geopoints max ( fieldset,geopoints )
.. geopoints min ( fieldset,geopoints )

.. Returns geopoints of maximum (minimum) of the fieldset value and the geopoint value at each grid point or spectral coefficient. Missing values, either in the fieldset or in the original geopoints variable, result in a value of geo_missing_value .


.. number maxvalue ( fieldset )
.. number maxvalue ( fieldset,list )
.. number minvalue ( fieldset )
.. number minvalue ( fieldset,list )

.. Returns the maximum (minimum) value of all the values of all the fields of the fieldset. The versions that take a list as a second parameter require a geographical area (north, west, south, east); only points within this area will be included in the calculation. Only non-missing values are considered in the calculation. If there are no valid values, the function returns nil.


.. matrix or list matrix ( fieldset )

.. Generates a matrix containing the values of the input field, or a list of matrices if there are more than one field in the fieldset. Only works with regular lat/long grids.


.. py:function:: mean(fs)

   Computes the point-wise mean of ``fs``. 
   
   :param fs: input fieldset
   :type fs: :class:`Fieldset`
   :rtype: :class:`Fieldset`
   
   The result is a :class:`Fieldset` with a single field in each gridpoint containing the mean of all the values belonging to the same gridpoint throughout the fields in ``fs``. A missing value in any field will result in a missing value in the corresponding place in the output. 
   
   With N fields in ``fs`` by denoting the i-th value in the k-th field by :math:`f_{i}^{k}` the output values can be written as:

   .. math::

         m_{i} = \frac {1}{N} \sum_{k}^{N}f_{i}^{k}

.. py:function:: mean_ew(fs)

   Computes the mean for each line of constant latitude in ``fs``.
   
   :param fs: input fieldset
   :type fs: :class:`Fieldset`
   :rtype: :class:`Fieldset`

   The result is a fieldset where the value at each point is the mean of all the points at that latitude. Missing values are excluded; if there are no valid values, then the grib missing value indicator will be returned for those points.

.. py:function:: merge (fs, fs1)

   Merge several fieldsets. 
   
   :param fs: input fieldset
   :type fs: :class:`Fieldset`
   :rtype: :class:`Fieldset`

   The output is a fieldset with as many fields as the total number of fields in all merged fieldsets. Merging with None does nothing, and is used to initialise when building a fieldset from scratch.

.. py:function:: ml_to_hl(fs, z, zs, h, ref_level, method)

   Interpolates a fieldset on model levels (i.e. on hybrid or eta levels used by the IFS) onto height levels (in m) above sea or ground level. 
   
   :param fs: the fieldset to be interpolated
   :type fs: :class:`Fieldset`
   :param z: the geopotential fieldset on model levels  (it must contain the same levels as ``fs`` but their order can be different) 
   :type z: :class:`Fieldset`
   :param zs: the surface geopotential field (if the ``ref_level`` is set to "sea" it should be set to None).
   :type zs: :class:`Fieldset` or None
   :param h: the list of target height levels (they can came in any given order)
   :type h: list or :class:`Fieldset`
   :param str ref_level: specifies the reference level for the target heights. The possible values are "sea" and "ground"
   :param str method: specifies the interpolation method. The possible values are "linear" and "log". 
   :rtype: :class:`Fieldset`
      
   At gridpoints where the interpolation is not possible missing value is returned.  

   .. note::
      Geopotential is not archived operationally on model levels in MARS at ECMWF. To compute it use :func:`mvl_geopotential_on_ml`. 
      
   :Example:
   
      This code illustrates how to use :func:`ml_to_hl` together with :func:`mvl_geopotential_on_ml` with data retrieved from MARS:

      .. code-block:: python

         # retrieve the data on model levels - surface geopotential (zs)
         # is taken from the analyis on level 1!
         ret_core = {
            "levtype": "ml", "date": 20191023, "time": 12 "grid": [2,2]}

         fs_ml = mv.retrieve(**ret_core, 
                  type="fc",
                  levelist=[1,"TO",137],
                  step=12,
                  param=["t", "q", "lnsp"])

         t = mv.read(data=fs_ml, param="t")
         q = mv.read(data=fs_ml, param="q")
         lnsp = mv.read(data=fs_ml, param="lnsp")

         zs = mv.retrieve(**ret_core,
               type="an",
               levelist=1,
               param="z")

         # compute geopotential on model levels
         z = mv.mvl_geopotential_on_ml(t, q, lnsp, zs)

         # interpolate the t field onto a list of height levels above sea level
         hlevs = [1000, 2000, 3000, 4000, 5000]
         th = mv.ml_to_hl (t, z, None, hlevs, "sea", "linear")

.. py:function:: mod(fs1, fs2)

   Returns a fieldset in each point containing the remainder of dividing ``fs1`` by ``fs2``.
   
   with as many fields as the input fieldsets; the grid point values of the output fieldset are the remainder of the division of the first fieldset by the second fieldset (the function operating field by field). 
   
   :param fs1: the divident fieldset
   :type fs1: :class:`Fieldset`
   :param fs2: the divisor fieldset
   :type fs2: :class:`Fieldset`
   :rtype: :class:`Fieldset`
   
   Where the gridpoint values of ``fs2`` are larger than those of ``fs1``, the output gridpoint value is set to the integer part of ``fs1``. A missing value in either ``fs1`` or ``fs2`` will result in a missing value in the corresponding place in the output fieldset. Note that only the integer parts of the inputs are considered in the calculation, meaning that a second parameter of 0.5 would cause a division by zero.

   With N fields in ``fs1`` and ``fs2`` by denoting the i-th value in the k-th field by :math:`x_{i}^{k}` and  :math:`y_{i}^{k}`, respectively, the output values can be written as:

   .. math::

         m_{i} = mod(x_{i}^{k}, y_{i}^{k})

.. py:function:: mvl_geopotential_on_ml(t, q, lnsp, zs)

   Computes geopotential on model levels.

   :param t: the temperature fields on all the model levels in ascending numeric order (e.g. 1-137)
   :type t: :class:`Fieldset`
   :param q: the specific humidity fields on all the model levels in ascending numeric order (e.g. 1-137)
   :type q: :class:`Fieldset`
   :param lnsp: the logarithm of surface pressure field (model level 1!).
   :type lnsp: :class:`Fieldset`
   :param zs: the surface geopotential field (model level 1!)
   :type zs: :class:`Fieldset`
   :rtype: :class:`Fieldset`

   All fields must be **gridpoint** data - no spherical harmonics, and they must all be on the same grid, with the same number of points. The :func:`mvl_geopotential_on_ml` assumes that there are no other dimensions contained in the data, e.g. all fields should have the same date and time. The return value is a :class:`Fieldset` of geopotential on model levels.

   .. note::
      **Surface geopotential** is defined on model level 1 in MARS at ECMWF! For most recent dates it is available for the 0 forecats step. However, generally it is only available as an **analysis** field!  
      
   :Example:
   
      This code illustrates how to use :func:`mvl_geopotential_on_ml` with data retrieved from MARS:

      .. code-block:: python

         # retrieve the data on model levels - surface geopotential (zs) is
         # only available in the analyis on level 1!
         ret_core = {
            "levtype": "ml", "date": 20191023, "time": 12 "grid": [2,2]}

         fs_ml = mv.retrieve(**ret_core, 
                  type="fc",
                  levelist=[1,"TO",137],
                  step=12,
                  param=["t", "q", "lnsp"])

         t = mv.read(data=fs_ml, param="t")
         q = mv.read(data=fs_ml, param="q")
         lnsp = mv.read(data=fs_ml, param="lnsp")

         zs = mv.retrieve(**ret_core,
               type="an",
               levelist=1,
               param="z")

         # compute geopotential on model levels
         z = mv.mvl_geopotential_on_ml(t, q, lnsp, zs)

.. py:function:: mvl_ml2hPa(lnsp, fs, pressures)

   Interpolates ``fs`` from ECMWF model levels onto a set of pressure levels defined by ``pressures``. 
   
   :param lnsp: the logarithm of surface pressure field (model level 1!).
   :type lnsp: :class:`Fieldset`
   :param fs: the fieldset to be interpolated (must contain model levels!). Does not have to be sorted by level.
   :type fs: :class:`Fieldset`
   :param list pressures: the list of target pressure levels in hPa. Does not have to be sorted by level.
   :rtype: :class:`Fieldset`
  
   Locations where interpolation is not possible are returned as missing. 
    
   :Example:
   
      This code illustrates how to use :func:`mvl_ml2hPa` with data retrieved from MARS:

      .. code-block:: python

         # retrieve the data in model levels
         ret_core = {"type": "fc", "levtype": "ml", "step": 12, "grid": [1.5,1.5]}
         t_ml = mv.retrieve(**ret_core, param="t", levelist=[1, "to", 137])
         lnsp = mv.retrieve(**ret_core, param="lnsp", levelist=1)

         # interpolate onto a list of pressure levels
         p_levels = [1000, 900, 850, 500, 300, 100, 10, 1, 0.1]
         t_pres = mv.mvl_ml2hPa(lnsp, t_ml, p_levels)


.. number or list nearest_gridpoint ( fieldset,list[,string] )
.. number or list nearest_gridpoint ( fieldset,number,number[,string] )
.. vector or list nearest_gridpoint ( fieldset,vector,vector[,string] )

.. Returns the value of the nearest point to a given location (or locations) in each field of a fieldset. The field must be a gridded field. If a list is given, it must contain two numbers - latitude and longitude. If two numbers are given, the first is the latitude, the second the longitude. For batch processing of multiple locations, two vectors can be given, the first is a vector of latitudes, the second the longitudes; this can be much more efficient than multiple calls with a single location each. If the fieldset has only one field, a number (or vector) is returned; otherwise a list of numbers (or a list of vectors) is returned.

.. By default, when the nearest gridpoint value is a missing value or the location is out of the grid area, nil is returned in the case of a single coordinate, or vector_missing_value in the case of a vector. If an extra parameter 'valid' is added to the function call, then of the surrounding points, the nearest valid one is returned; nil will still be returned if all the surrounding points are missing.

.. Note that a similar function, interpolate(), also exists.


.. geopoints nearest_gridpoint ( fieldset,geopoints )

.. Generates a set of geopoints from a field. The first field of the input fieldset is used. The result is a set of geopoints whose values are those of the nearest gridpoints in the field to the geopoints given as a second parameter. Where it is not possible to generate a sensible value due to lack of valid data in the fieldset, the internal geopoints missing value is used (this value can be checked for with the built-in variable geo_missing_value or removed with the function remove_missing_values). Note that a similar function, interpolate() , also exists.

.. py:function:: nearest_gridpoint_info(fs, lat_or_location, [lon, [valid]])

   Returns the value and location of the nearest point to a given location in each field in ``fs``. 
   
   :param fs: input fieldset
   :type fs: :class:`Fieldset`
   :param lat_or_location: 
   :type lat_or_location: float or list
   :param lon: 
   :type lon: float
   :param str valid: the only possible value is "valid"
   :rtype: list
   
   The location can be specified by ``lat`` or ``lon`` or as a list of [lat, lon] via the ``location`` argument. 
   The return value is a list containing the following values for each field:
   
   * if the nearest gridpoint value is non missing a dictionary is returned with the members of **value**, **latitude** and **longitude**. 
   * if the nearest gridpoint has missing value the return value depends on ``valid``:
   
      * if ``valid`` is not specified None is returned
      * if ``valid`` is specified the dictionary for the nearest valid point from the surrounding gridpoints is returned. If all the surrounding points are missing None is returned
   
   :Example:

      .. code-block:: python

         import metview as mv
         f = mv.read("my_grib_file")
         info = mv.nearest_gridpoint_info(f, 51.46, -1.33)
         for v in info:
            print(v)

.. py:function:: neg(fs)

   Returns the fieldset of the negative of ``fs`` at each grid point or spectral coefficient.
   
   :param fs: input fieldset
   :type fs: :class:`Fieldset`
   :rtype: :class:`Fieldset`

   Missing values are retained, unaltered by the calculation.

   .. note::
      The following lines of codes are equivalent:

      .. code-block:: python

         import metview as mv
         fs = mv.neg(fs)
         fs = -fs 

.. py:function:: nobitmap(fs, value)

   Returns a copy of ``fs`` with all of its missing values replaced with ``value``. 
   
   :param fs: input fieldset
   :type fs: :class:`Fieldset`
   :param float value: value to replace missing values with
   :rtype: :class:`Fieldset`

   .. note::
      See also :func:`bitmap`.


.. fieldset percentile(...)

.. Computes the specified percentiles for a given fieldset. This is a Metview icon function, for detailed documentation please see Percentile.

.. py:function:: pressure(lnsp, [levels, fs_target])

   Computes the pressure (in Pa) from the logarithm of surface pressure (lnsp) on a list of ECMWF model levels. 
   
   :param lnsp: input fieldset containing an lnsp field (its ecCodes paramId must be 152).
   :type lnsp: :class:`Fieldset`
   :param levels: the target model level or levels 
   :type levels: int or list of ints
   :param fs_target: fielsdet defining the target model levels
   :type fs_target:  :class:`Fieldset`
   :rtype: :class:`Fieldset`

   If only ``lnsp`` is specified the pressure is computed for the full model level range defined by the GRIB header of ``lnsp``.

   If ``levels`` is specified it defines the output model level(s). 

   If ``fs_target`` is specified the target levels are taken from its fields.

   Missing values in ``lnsp`` are retained in the output fieldset.

   .. warning::
      This function is obsolete, use :func:`unipressure` instead.

.. py:function:: rmask(fs, circle_or_lat, [lon, radius])

   For each field in ``fs`` creates a field containing grid point values of 0 or 1 according to whether their distance to given geographical location is larger or smaller than a given radius. 0 is assigned to points outside the radius and 1 to points inside the radius.
   
   :param fs: input fieldset
   :type fs: :class:`Fieldset`
   :param circle_or_lat: the circle as list in the form of [lat, lon, radius] or the latitude coordinate of the centre of the circle
   :type circle_or_lat: list of float
   :param float lon: longitude coordinate of the centre of the circle
   :param float radius: radius of the circle in m
   :rtype: :class:`Fieldset`

   .. note::
      See also :func:`mask` to define a rectangular mask.  

.. py:function:: rms(fs)

   Computes the root mean square of ``fs``. 
   
   :param fs: input fieldset
   :type fs: :class:`Fieldset`
   :rtype: :class:`Fieldset`
   
   A missing value in any field in ``fs`` will result in a missing value in the corresponding grid point in the output fieldset. 
   
   With n fields in ``fs`` by denoting the i-th value in the k-th field by :math:`x_{i}^{k}` the output values can be written as:

   .. math:: 
      
         r_{i} = \sqrt {\frac {1}{n} \sum_{k}^{n} (x_{i}^{k})^{2}}

   .. note::
      The following lines are equivalent:

      .. code-block:: python

         y = mv.rms(x)
         y = mv.sqrt(mv.mean(x^2)
   
.. py:function:: second_derivative_x(fs)

   Computes the second zonal (from West to East) partial derivative of each field in ``fs``. 
   
   :param fs: input fieldset
   :type fs: :class:`Fieldset`
   :rtype: :class:`Fieldset`

   The computations for a field f are based on the following formula:
   
   .. math::

      \frac {\partial^2 f}{\partial x^2} = \frac{1}{R^2 \ cos^2\phi}\frac{\partial^2 f}{\partial \lambda^2} 

   where:

   * R is the radius of the Earth
   * :math:`\phi` is the latitude
   * :math:`\lambda` is the longitude.    

   The derivatives are computed with a second order finite-difference approximation. The resulting fields contain missing values on the poles. 
   
   .. warning::
      :func:`second_derivative_x` is only implemented for regular latitude-longitude grids.

.. py:function:: second_derivative_y(fs)

   Computes the second meridional (from South to North) partial derivative of each field in ``fs``. 
   
   :param fs: input fieldset
   :type fs: :class:`Fieldset`
   :rtype: :class:`Fieldset`
   
   The computations for a field f are based on the following formula:

   .. math::
   
      \frac {\partial^2 f}{\partial y^2} = \frac{1}{R^2}\frac{\partial^2 f}{\partial \phi^2} 

   where:
   
   * R is the radius of the Earth
   * :math:`\phi` is the latitude

   The derivatives are computed with a second order finite-difference approximation. The resulting fields contain missing values on the poles. 
   
   .. warning::
      :func:`second_derivative_y` is only implemented for regular latitude-longitude grids.


.. fieldset set_values ( fieldset,vector )
.. fieldset set_values ( fieldset,list )
.. fieldset set_values ( fieldset,vector,string )
.. fieldset set_values ( fieldset,list,string )

.. Creates a new fieldset with all the fields' values replaced by those supplied. If supplied as a single vector, the values are set in all fields; if a list of vectors is supplied then there must be the same number of vectors as there are fields in the fieldset. The default behaviour is to produce an error if the input fieldset and vector have different numbers of values. If, however, a third parameter (set to the string 'resize') is passed to the function, the resulting fieldset will instead be resized to have the same number of values as the input vector - this can be useful when creating a new fieldset from a template. Missing values in the vector(s) are retained as missing values in the fieldset.



.. py:function:: sgn (fs)

   Returns the fieldset of the sign of the values of ``fs`` at each grid point or spectral coefficient: -1 for negative values, 1 for positive and 0 for null values. Missing values are retained, unaltered by the calculation.

   :param fs: input fieldset
   :type fs: :class:`Fieldset`
   :rtype: :class:`Fieldset`

.. py:function:: sin(fs)

   Returns the fieldset of the sine of ``fs`` at each grid point.

   :param fs: input fieldset
   :type fs: :class:`Fieldset`
   :rtype: :class:`Fieldset`

   Input fieldset must have values in radians. Missing values are retained, unaltered by the calculation.

.. py:function:: sinlat(fs)

   Returns the fieldset of the sine of the latitude of ``fs`` at each grid point. 

   :param fs: input fieldset
   :type fs: :class:`Fieldset`
   :rtype: :class:`Fieldset` 

   Missing values are retained, unaltered by the calculation. 

   :Example:

      The following code shows how to compute the absolute vorticity from vorticity with :func:`sinlat`:
      
      .. code-block:: python
         
         import metview as mv
         import math

         omega = 2 * math.pi / 86400
         coriolis = 2 * omega * mv.sinlat(vort)
         absvort = vort + coriolis

.. py:function:: sort(fs, [keys, [orders]])

   Sorts ``fs`` according to the specified options.

   :param fs: input fieldset
   :type fs: :class:`Fieldset`
   :param keys: sorting key(s)
   :type keys: str or list
   :param orders: sorting order(s)
   :type orders: str or list
   :rtype: :class:`Fieldset` 

   The list of MARS keys the can be used for the sorting are as follows (theye are specified in order of precedence): 

      * date
      * time
      * step
      * number
      * levelist
      * param
   
   Here **number** is the ENS forecast member number, while **param** is the ecCodes paramID (int).

   If no options are specified :func:`sort` sorts ``fs`` in ascending order according to the allowed MARS keys.

   If ``keys`` are specified (either as a list or a str) they modify the precedence of the sorting keys.

   The optional ``orders`` can specify the sorting direction: ">" means descending, while "<" means ascending order. ``orders`` can be either a str or a list:

   * if it is a str the sorting direction applies to all the ``keys``
   * if it is a list ``keys`` must also be a list with the same number of elements - the sorting directions apply to each sorting key specified.

.. py:function:: sqrt(fs)

   Returns the fieldset of the square root of ``fs`` at each grid point. Missing values are retained, unaltered by the calculation.

   :param fs: input fieldset
   :type fs: :class:`Fieldset`
   :rtype: :class:`Fieldset`


.. py:function:: stdev(fs)

   Computes the grid point-wise standard deviation of ``fs``. 
   
   :param fs: input fieldset
   :type fs: :class:`Fieldset`
   :rtype: :class:`Fieldset`
   
   A missing value in any field in ``fs`` will result in a missing value in the corresponding grid point in the output fieldset. 
   
   With N fields in ``fs`` by denoting the i-th value in the k-th field by :math:`x_{i}^{k}` the output values can be written as:

   .. math:: 
      
         z_{i} = \sqrt {\frac {1}{N} \sum_{k}^{N} (x_{i}^{k})^{2} - (\frac {1}{N} \sum_{k}^{N} x_{i}^{k} )^2}

   .. note::
      The following lines are equivalent:

      .. code-block:: python

         y = mv.stdev(x)
         y = mv.sqrt(mv.mean(x*x)-mv.mean(x)^2)
         y = mv.sqrt(mv.var(x))


.. py:function:: stdev_a(fs,[area])

   Computes the standard deviation of ``fs`` over a weighted area. 
   
   :param fs: input fieldset
   :type fs: :class:`Fieldset`
   :param list area: area as [N,W,S,E] to perform the computations
   :rtype: float or list 
   
   If the ``area`` is not specified the whole field will be used in the calculation. The result is a number for a single field or a list for a multi-field :class:`Fieldset`.

.. py:function:: sum(fs)

   Computes the grid point-wise sum of the values in ``fs``. 

   :param fs: input fieldset
   :type fs: :class:`Fieldset`
   :rtype: :class:`Fieldset`

   The output is a :class:`Fieldset` with one field only. A missing value in any field will result in a missing value in the corresponding gridpoint in the output fieldset. 
   
   With N fields in ``fs`` by denoting the i-th value in the k-th field by :math:`x_{i}^{k}` the output values can be written as:

   .. math:: 
      
         s_{i} = \sum_{k}^{N} x_{i}^{k}
   
.. vector or list surrounding_points_indexes ( fieldset,list[,string] )
.. vector or list surrounding_points_indexes ( fieldset,number,number[,string] )
.. vector or list surrounding_points_indexes ( fieldset,vector,vector[,string] )

.. Returns the indexes of the four gridpoints surrounding the given location, ordered by increasing distance from the target point. If a list is given, it must contain two numbers - latitude and longitude. If two numbers are given, the first is the latitude, the second the longitude. The field must be a gridded field. If the fieldset has only one field, a single vector of indexes is returned; otherwise a list of vectors is returned. In the case where the field is a reduced Gaussian grid and the input location is at the North or South pole, beyond the most extreme row of points, there will be a 'circle' of surrounding points, and all of these indexes are returned.

.. For batch processing of multiple locations, two vectors can be given, the first is a vector of latitudes, the second the longitudes; this can be much more efficient than multiple calls with a single location each. If the fieldset has only one field, a single vector is returned; otherwise a list of vectors is returned.

.. By default, if any of the surrounding points are missing, the function will return nil. To prevent this, and to return all the points regardless, add the option 'all' as the last parameter of the function call.


.. py:function:: tan(fs)

   Return the tangent of ``fs`` at each grid point. 

   :param fs: input fieldset
   :type fs: :class:`Fieldset`
   :rtype: :class:`Fieldset`

   Values in ``fs`` are supposed to be specified in radians. Missing values are retained, unaltered by the calculation. For values which the tangent function is not defined for (e.g. :math:`\pi/2`) a missing value is returned.

.. py:function:: tanlat(fs)

   Returns the fieldset of the tangent of the latitude of ``fs`` at each grid point. 

   :param fs: input fieldset
   :type fs: :class:`Fieldset`
   :rtype: :class:`Fieldset` 

   Missing values are retained, unaltered by the calculation. The resulting fields contain missing values on the poles.

.. fieldset thickness ( fieldset )
.. fieldset thickness ( fieldset,number )
.. fieldset thickness ( fieldset,list )
.. fieldset thickness ( fieldset,fieldset )

.. This function creates fields of thickness from the logarithm of the surface pressure (lnsp ) and a list of model levels. Note that this function only works with lat/long grids and assumes that the parameter for lnsp is 152. A newer, more flexible version of this function exists - see unithickness () .

..         The first argument is always a fieldset containing an lnsp field. If no other parameter is given, the list of levels will range from 1 to (number of vertical coordinates/2)-1 as coded in the GRIB header of the lnsp .
..         The second argument specifies the levels at which the output fields must be generated. To generate a single level, pass a number. For more than one level, either pass a list of levels or a fieldset. If a fieldset is passed as the second parameter, the level information is extracted from each field of the fieldset.

.. Missing values in the lnsp field are retained in the output fieldset.


.. fieldset unipressure ( fieldset )
.. fieldset unipressure ( fieldset,fieldset )
.. fieldset unipressure ( fieldset,list )
.. fieldset unipressure ( fieldset,number )
.. fieldset unipressure ( fieldset,fieldset,number )
.. fieldset unipressure ( fieldset,list,number )

.. This function creates fields of pressure from the logarithm of the surface pressure (lnsp) and a list of model levels. Unlike pressure() , this function works with all grid types known to Metview (not just lat/long); it also allows the user to override the parameter number for lnsp (default 152).

..         The first argument is always a fieldset containing an lnsp field. If no other parameter is given, then pressure is computed for all model levels that are described in the GRIB header of fieldset .
..         If number is given (always the last parameter) it is the lnsp parameter code (default is 152).
..         list should contain model levels for which pressure is to be computed. Note that also for a single model level one has to use a list (this is a signature difference compared to the old function pressure() ).
..         If fieldset is given as the second parameter then pressure is computed for those model levels found in the second fieldset.

.. Missing values in the lnsp field are retained in the output fieldset.


.. fieldset unithickness ( fieldset )
.. fieldset unithickness ( fieldset,fieldset )
.. fieldset unithickness ( fieldset,list )
.. fieldset unithickness ( fieldset,number )
.. fieldset unithickness ( fieldset,fieldset,number )
.. fieldset unithickness ( fieldset,list,number )

.. This function creates fields of thickness from the logarithm of the surface pressure (lnsp) and a list of model levels. Unlike thickness() , this function works with all grid types known to Metview (not just lat/long); it also allows the user to override the parameter number for lnsp (default 152).

..         The first argument is always a fieldset containing an lnsp field. If no other parameter is given, then thickness is computed for all model levels that are described in the GRIB header of fieldset .
..         If number is given (always the last parameter) it is the lnsp parameter code (default is 152).
..         list should contain model levels for which thickness is to be computed. Note that also for a single model level one has to use a list (this is a signature difference compared to the old function thickness() ).
..         If fieldset is given as the second parameter then thickness is computed for those model levels found in the second fieldset.

.. Missing values in the lnsp field are retained in the output fieldset.

.. py:function:: univertint(fs, [input_or_code, [levels_or_code]])

   Performs a vertical integration for data on pressure levels or on ECMWF (hybrid) model levels. 

   :param fs: input (or lnsp) fieldset
   :type fs: :class:`Fieldset`
   :param input_or_code: input fieldset or paramId for lnsp
   :type input_or_code: :class:`Fieldset` or number
   :param levels_or_code: level range or paramId for lnsp
   :type levels_or_code: list or number
   :rtype: :class:`Fieldset` containing one field only

   :func:`univertint` has to be called in a different way depending on the type of vertical levels in the input data.

   * Pressure levels: the function has to be called with the ``fs`` argument only.
   * Model levels: 

      * if ``fs`` is the only argument it must also contain a logarithm of surface pressure (**lnsp**) field. 
      * when ``fs`` is the input fieldset it must also contain an lnsp field. In this case the optional ``input_or_code`` can specify the ecCodes **paramId** used to identify the **lnsp** field (by default the value of 152 is used).
      * when ``fs`` is not the input fieldset but contains the **lnsp** field ``input_or_code`` must contain the input fieldset. The optional ``levels_or_code`` in this case can be either of these:
      
         * the ecCodes **paramId** number for lnsp used to identify the lnsp field (by default the value of 152 is used)
         * a **list** with two numbers [top, bottom] to specify the level range for the integration. 
         
   A missing value in any field will result in a missing value in the corresponding place in the output fieldset.

   The computations are based on the following formula:

   .. math::
      
      \int_{bottom}^{top} f \frac{dp}{g}

   where:

   * f: input fieldset
   * p: pressure
   * g: acceleration of gravity (9.80665 m/s2).


.. py:function:: valid_date(fs)

   Returns the valid dates (including the time components) for each field in ``fs``.
   
   :param fs: input fieldset
   :type fs: :class:`Fieldset`
   :rtype: datetime.datetime or list of datetime.datetime objects

   If ``fs`` has only one field, a date is returned; otherwise a list of dates are returned.

.. py:function:: values(fs)

   Returns the grid point values in ``fs`` as an ndarray. 
   
   :param fs: input fieldset
   :type fs: :class:`Fieldset`
   :rtype: 1D-ndarray or list of 1D-ndarrays
   
   If ``fs`` contains more than one field a list of ndarrays is returned. Each of these arrays contains as many elements as there are grid points in each field. Missing values are included in the results as Nan.

   :Example:

   .. code-block:: python

      # fs is a fieldset of n fields
      vals = mv.values(fs)
      
      # values in first field
      first_vals = vals[0]

      # first value in in first field
      first_gridpoint = first_vals[0]

      # or equivalently
      first_gridpoint = vals[0][0]

.. py:function:: var(fs)

   Computes the variance in each grid point in ``fs``. 
   
   :param fs: input fieldset
   :type fs: :class:`Fieldset`
   :rtype: :class:`Fieldset`
   
   The output is a :class:`Fieldset` with one field only. A missing value in any field in ``fs`` will result in a missing value in the corresponding grid point in the output fieldset. 
   
   With n fields in ``fs`` by denoting the i-th value in the k-th field by :math:`x_{i}^{k}` the output values can be written as:

   .. math:: 
      
         v_{i} = \frac {1}{n} \sum_{k}^{n} (x_{i}^{k})^2 - \frac {1}{n} (\sum_{k}^{n} x_{i}^{k})^2

   .. note:: 
      The following lines are equivalent:

      .. code-block:: python

         y = mv.var(x)
         y = mv.mean(x*x)-mv.mean(x)^2


.. py:function:: var_a(fs, [area])
 
   Computes the variance of ``fs`` over a weighted area. 
   
   :param fs: input fieldset
   :type fs: :class:`Fieldset`
   :param list area: area as [N,W,S,E] to perform the computations
   :rtype: float or list 
   
   If the ``area`` is not specified the whole field will be used in the calculation. The result is a number for a single field or a list for a multi-field :class:`Fieldset`.

.. fieldset vertint ( fieldset )
.. fieldset vertint ( fieldset,fieldset )

.. This function performs a vertical integration of the input fieldset, which must contain a range of model levels for the same parameter. A missing value in any field will result in a missing value in the corresponding place in the output fieldset. If the function is called with the fieldset as its single argument, it must also contain the logarithm of the surface pressure (lnsp ). If the function is called with two parameters, the first one is a fieldset containing an lnsp field, the second one is the multi-level fieldset.

.. The function computes :

.. \int_{bottom}^{top} f \frac{dp}{g}

.. where

..         f is the fieldset
..         p is the pressure
..         g is the acceleration of gravity (9.80665 m/s2).

.. The following example computes the total amount of liquid water in the atmosphere by integrating the cloud liquid water content (clwc ) over all levels of the model

.. # Retrieve clwc
.. clwc = retrieve(
..    levtype : "ml",
..    levelist : [1,"to",31],
..    param : "clwc",
..    date : -1,
..    grid : [2.5,2.5]
.. )

.. # Retrieve lnsp
.. lnsp = retrieve(
..    levtype : "ml",
..    levelist : 1,
..    param : "lnsp",
..    date : -1,
..    grid : [2.5,2.5]
.. )

.. # Integrate the field
.. x = vertint(lnsp,clwc)
.. plot(x)

   
.. py:function:: vorticity(fx, fy)

   Computes the vertical component of the curl differential operator for 2-dimensional vector fields.
   
   :param fx: zonal (west-east) vector component fieldset
   :type fs: :class:`Fieldset`
   :param fx: meridional (south-north) vector component fieldset
   :type fs: :class:`Fieldset`
   :rtype: :class:`Fieldset`  
   
   For wind fields (i.e. when the input fieldsets are u and v wind components) this computes the relative vorticity (:math:`\zeta`). The computations for a vector field f=(fx ,fy ) are based on the following formula:

   .. math::
      
      \zeta =\frac{1}{R \ cos\phi}\frac{\partial f_y}{\partial \lambda} - \frac{1}{R}\frac{\partial f_x}{\partial \phi} + \frac{f_x}{R}tan\phi

   where:
   
   * R is the radius of the Earth (in m)
   * :math:`\phi` is the latitude
   * :math:`\lambda` is the longitude

   The derivatives are computed with a second order finite-difference approximation. The resulting fields contain missing values on the poles. If the input fields are horizontal wind components the ecCodes paramId of the resulting field is set to 138 (relative vorticity).

   .. warning::
      :func:`vorticity` is only implemented for regular latitude-longitude grids. 

