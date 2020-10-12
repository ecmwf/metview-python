Geopoints functions
*********************


.. .. py:function:: abs(gpt)
    
..    Returns the absolute value of ``gpt``. 

..    :param fs: input geopoints
..    :type fs: :class:`Geopoints`
..    :rtype: :class:`Geopoints`

..    Missing values retain their value.

.. geopoints asin ( geopoints )
.. geopoints acos ( geopoints )
.. geopoints atan  ( geopoints )

.. Returns the geopoints of the arc trigonometric function of the input geopoints. Result is in radians. Missing values retain their value of geo_missing_value.

.. py:function:: columns(gpt)

    Returns the name of the columns in ``gpt``.
    
    :param fs: input geopoints
    :type fs: :class:`Geopoints`
    :rtype: list

.. .. py:function:: cos(gpt)

..     Returns the cosine of ``gpt``. 
    
..     :param fs: input geopoints
..     :type fs: :class:`Geopoints`
..     :rtype: :class:`Geopoints`
    
..     The values in ``gpt`` are supposed to be specified in radians. Missing values retain their value.

.. py:function:: count(gpt)

    Returns the the number of elements (i.e. data rows) in ``gpt``.
    
    :param fs: input geopoints
    :type fs: :class:`Geopoints`
    :rtype: float

    .. note::
        Use Python's built-in len instead of :func:`count`.

..  py:function:: create_geo(number_of_points, [format, [number_of_values_columns, [value_columns]]])
..  py:function:: create_geo(number_of_points, **kwargs)
    :noindex:

    Creates a new :class:`Geopoints` with the given ``number_of_points``, all set to default values and coordinates.

    :param fs: input geopoints
    :type fs: :class:`Geopoints`
    :param int number_of_points: number of points
    :param str format: geopoints format (see below)
    :param int number_of_value_columns: the number of value columns for the "ncols" formatted
    :param list value_columns: the name of the value columns for the "ncols" format
    :param kwargs: see below
    :rtype: float

    It is intended that this function be used in conjunction with the "set_* geopoints" functions in order to populate the geopoints with data. 
    
    If no ``format`` is specified a "traditional" 6-column format geopoints is created. Otherwise ``format`` defines the actual format. The possible values are as follows: 'polar_vector', 'xy_vector ', 'xyv ' and 'ncols'. 
    
    If ``format`` is "ncols", then the number of value columns can be given by ``number_of_value_columns`` (default is 1). In this case, the ``value_columns`` can be used to provide a list of names of the value columns.

    An alternative, and more efficient way to create a new geopoints variable if you already have the data to populate it, is to provide a set of keyword arguments (``kwargs``) as shown in the examples below. Using this syntax, you can completely create a new geopoints variable with all its column data in one go. This is much more efficient than creating an empty geopoints variable and then populating it using the "set_" functions.

    :Examples:

        .. code-block:: python

            import metview as mv
            import numpy as np

            # default geopoints format, 8 values
            g = mv.create_geo(8) 
            
            # "xyv" formatted geopoints with 9 values
            g = mv.create_geo(9, "xyv")

            # "ncols" format with 3 named columns, each containing 4 values        
            g = mv.create_geo(4, "ncols", 3, ['t', 'z', 'precip']) 

            # default geopoints format, with keyword arguments
            g = mv.create_geo(type='standard',
                        latitudes=np.array([4, 5, 6]),
                        longitudes=np.array([2.3, 1.1, 6.5]),
                        levels=850,  # all rows will have 850 as their level
                        values=np.array([1.1, 2.2, 3.3]),
                        times=None)
            
            # "xyv" geopoints format, with keyword arguments
            g = mv.create_geo(type="xyv",
                        latitudes=np.array([4, 5, 6]),
                        longitudes=np.array([2.3, 1.1, 6.5]),
                        values=np.array([1.1, 2.2, 3.3]))

            # "ncols" geopoints format, with keyword arguments            
            g = mv.create_geo(type="ncols",
                        latitudes=np.array([4, 5, 6]),
                        longitudes=np.array([2.3, 1.1, 6.5]),
                        levels=850,  # all rows will have 850 as their level
                        times=None,
                        stnids=['aberdeen', 'aviemore', 'edinburgh'],
                        temp=np.array([273.15, 269.78, 281.45]),
                        precip=[4, 5, 1],  # lists also work, but are less efficient
                        speed=np.array([2, 3, 5]))

.. py:function:: dates(gpt)

    Returns the dates from ``gpt``.
    
    :param fs: input geopoints
    :type fs: :class:`Geopoints`
    :rtype: list of datetime.datetime

.. py:function:: distance(gpt, lat, lon)
.. py:function:: distance(gpt, coords)
   :noindex:

   Returns a :class:`Geopoints` with the value in each grid point being the distance in **metres** from a given geographical location (the reference). 
   
   :param fs: input geopoints
   :type fs: :class:`Geopoints`
   :param float lat: latitude of the reference point 
   :param float lon: longitude of the reference point
   :param coords: coordinates of the reference point as [lat, lon]
   :type coords: list
   :rtype: :class:`Geopoints`
   
   The reference location should be specified in degrees. A geopoint with either latitude or longitude set to missing value will have a distance of missing value.

.. py:function:: db_info(gpt, key, [column_name])

    Returns metadata about the database retrieval which generated ``gpt``. 
    
    :param fs: input geopoints
    :type fs: :class:`Geopoints`
    :param str key: the metadata key
    :param str column_name: name of the column if ``key`` is "column"
    :rtype: str or list of str

    ``key`` specifies the piece of information to extract; possible values are:

    * name: the name of the database system, e.g. ODB
    * path: the path to the database
    * query: a list of str containing the multi-line data query
    * column: the name of the database column used to populate a given element of the geopoints. In this case ``column_name`` must be provided, naming the geopoints element of interest - possible values are "lat", "lon", "level", "date", "time", "value" and "value".
    * alias: similar to "column" above, but returns the name of the database alias used instead of the full column name

    .. note::
        This information is derived from the **DB_INFO** section (if it exists) in the geopoints file header (see Storing Data Origin Information in a Geopoints File).

.. .. py:function:: exp(gpt)

..     Returns the exponential of ``gpt``. 
    
..     :param fs: input geopoints
..     :type fs: :class:`Geopoints`
..     :rtype: :class:`Geopoints`
    
..     Missing values retain their value.

.. py:function:: geosort(gpt)

    Returns a new :class:`Geopoints` that contains ``gpt`` sorted geographically from North to South (and West to East in points with the same latitude value, then by height, with lowest numerical values first).

    :param fs: input geopoints
    :type fs: :class:`Geopoints`
    :rtype: :class:`Geopoints`

.. .. py:function:: int(gpt)

..     Returns the integer part of ``gpt``. 
    
..     :param fs: input geopoints
..     :type fs: :class:`Geopoints`
..     :rtype: :class:`Geopoints`
    
..     Missing values retain their value.

.. py:function:: intbits(gpt, bit, [number_of_bits])

    Takes the integer part of the values of ``gpt`` and extracts a specified ``bit`` (or bits).

    :param fs: input geopoints
    :type fs: :class:`Geopoints`
    :param int bit: the bit to extract (1 is the least significant bit!)
    :param int number_of_bits: the number of bits to extract (starting at ``bit``)
    :rtype: :class:`Geopoints`

    If only ``bit`` is specified it will always be returned as 1 or 0, regardless of its position in the integer.
    
    With ``number_of_bits`` a group of bits can be extracted. The result will be treated as if the first bit was the least significant bit of the result. 
    
    :Example:
    
        These examples show how intbits work on individual numbers:

        .. code-block:: python

            import metview as mv

            # To extract the 1st, 2nd and 3rd bits from
            # an int separately:
            
            # in bit-form, this is 00000110 with the least significant
            # bit at the right
            n = 6 

            flag = mv.intbits (n, 1) # flag is now 0
            flag = mv.intbits (n, 2) # flag is now 1
            flag = mv.intbits (n, 3) # flag is now 1

            # To extract the 1st and 2nd bits together 
            # to make a single int:
            flag = mv.intbits (n, 1, 2) # flag is now 2

            # To extract the 2nd and 3rd bits together 
            # to make a single int:
            flag = mv.intbits (n, 2, 2) # flag is now 3

            # To extract the 3rd and 4th bits together 
            # to make a single int:
            flag = mv.intbits (n, 3, 2) # flag is now 1

    The number of bits available depends on the machine architecture and Metview's compilation options, but at the time of writing it should be 32. This function does not treat missing values differently from any other values (for efficiency with large datasets).

.. py:function:: latitudes(gpt)

    Returns the latitudes column of ``gpt`` as an ndarray.
    
    :param fs: input geopoints
    :type fs: :class:`Geopoints`
    :rtype: ndarray

.. py:function:: levels(gpt)

    Returns the levels column of ``gpt`` as an ndarray.
    
    :param fs: input geopoints
    :type fs: :class:`Geopoints`
    :rtype: ndarray

.. py:function:: longitudes(gpt)

    Returns the longitudes column of ``gpt`` as an ndarray.
    
    :param fs: input geopoints
    :type fs: :class:`Geopoints`
    :rtype: ndarray

.. .. py:function:: log(gpt)

..     Returns the natural logarithm of ``gpt``. 
    
..     :param fs: input geopoints
..     :type fs: :class:`Geopoints`
..     :rtype: :class:`Geopoints`
    
..     For values the logarithm is not defined a missing value is set in the output. Missing values in ``gpt`` retain their value.

.. .. py:function:: log10(gpt)

..     Returns the base 10 logarithm of ``gpt``. 
    
..     :param fs: input geopoints
..     :type fs: :class:`Geopoints`
..     :rtype: :class:`Geopoints`
    
..     For values the logarithm is not defined a missing value is set in the output. Missing values in ``gpt`` retain their value.


.. py:function:: mean(gpt)

    Computes the mean of all the values in the values column of ``gpt``. 
    
    :param gpt: input geopoints
    :type gpt: :class:`Geopoints`
    :rtype: float or None
    
    Missing values are bypassed in this calculation. If there are no valid values, then None is returned.

.. py:function:: mask(gpt, area)

    Creates a :class:`Geopoints` containing values of 0 or 1 according to whether they are inside (1) or outside (0) the ``area``.
    
    :param gpt: input geopoints
    :type gpt: :class:`Geopoints`
    :param list area: area as [N, W, S, E]
    :rtype: :class:`Geopoints`
   
    Points with missing latitudes or longitudes are considered to be outside any area. See the documentation for the fieldset version of this function to see how to compose more complex regions than a simple rectangular area.

.. .. py:function:: neg(gpt)

..     Returns the negative of ``gpt``. 
    
..     :param fs: input geopoints
..     :type fs: :class:`Geopoints`
..     :rtype: :class:`Geopoints`
    
..     Missing values in ``gpt`` retain their value.

..     .. note::
..         These lines of codes are equivalent:

..         .. code-block:: python

..             f = mv.neg(g)
..             f = -g

.. py:function:: offset(gpt, lat_offset, lon_offset)
.. py:function:: offset(gpt, offset)

    Creates a new :class:`Geopoints` from ``gpt`` with the locations offset by the specified amounts.

    :param gpt: input geopoints
    :type gpt: :class:`Geopoints`
    :param float lat_offset: latitude offset
    :param float lon_offset: longitude offset
    :type list offset:  latitude and longitude offsets as [lat_offset, lon_offset]
    :rtype: :class:`Geopoints`

.. .. py:function:: sgn(gpt)

..     Returns the sign of ``gpt``:  -1 for negative , 1 for positive and 0 for 0 values.
    
..     :param fs: input geopoints
..     :type fs: :class:`Geopoints`
..     :rtype: :class:`Geopoints`
    
..     Missing values in ``gpt`` retain their value.

.. .. py:function:: sin(gpt)

..     Returns the sine of ``gpt``.
    
..     :param fs: input geopoints
..     :type fs: :class:`Geopoints`
..     :rtype: :class:`Geopoints`
    
..     Values in ``gpt``are interpreted as radians. Missing values retain their value.

.. .. py:function:: sqrt(gpt)

..     Returns the square root of ``gpt``. 
    
..     :param fs: input geopoints
..     :type fs: :class:`Geopoints`
..     :rtype: :class:`Geopoints`
    
..     For values the square root is not defined a missing value is set in the output. Missing values in ``gpt`` retain their value.

.. .. py:function:: tan(gpt)

..     Returns the tangent of ``gpt``.
    
..     :param fs: input geopoints
..     :type fs: :class:`Geopoints`
..     :rtype: :class:`Geopoints`
    
..     Values in ``gpt`` are interpreted as radians. For values the tangent is not defined a missing value is set in the output. Missing values retain their original value.


.. geopoints filter ( geopoints,geopoints )

.. A filter function to extract a subset of its geopoints input using a second geopoints as criteria. The two input geopoints must have the same number of values. The resulting output geopoints contains the values of the first geopoints where the value of the second geopoints is non-zero. It is usefully employed in conjunction with the comparison operators :

.. freeze = filter(temperature,temperature < 273.15)

.. The variable freeze will contain a subset of temperature where the value is below 273.15 . The following example shows how to plot a geopoints set with different colours :


.. # Filter from "temperature" points at, above, below 273.15
.. cold = filter( temperature,temperature<273.15 )
.. zero = filter( temperature,temperature=273.15 )
.. warm = filter( temperature,temperature>273.15 


.. # Create three symbol plotting definitions
.. red = psymb( symbol_colour : "red" )
.. blue = psymb( symbol_colour : "blue" )
.. black = psymb( symbol_colour : "black" )


.. # Plot everything
.. plot(zero,black,cold,blue,warm,red)


.. geopoints filter ( geopoints,vector )

.. A filter function to extract a subset of its geopoints input using the values in a vector as criteria. The vector should contain the same number of elements as there are in the geopoints. An example, which uses a named column for the filter criteria is:

.. new_gpt = filter(gpt, gpt['precip'] > 5)  # "gpt['precip'] > 5" returns a vector of 1s and 0s


.. geopoints filter ( geopoints,number )
.. geopoints filter ( geopoints,list )

.. A filter function to extract a subset of its geopoints input using model levels as criteria.

..         If the second argument is a number, the function extracts all the geopoints for which the level is equal to the number.
..         If the second argument is a list of two numbers [n1,n2] , the function extracts all the geopoints for which the level lies in the n1-n2 interval.


.. geopoints filter ( geopoints,date )
.. geopoints filter ( geopoints,list )

.. A filter function to extract a subset of its geopoints input using dates as criteria.

..         If the second argument is a date, the function extracts all the geopoints for which the date is equal to the one specified as the second argument.
..         If the second argument is a list of two dates [d1,d2] , the function extracts all the geopoints for which the date lies in the d1-d2 interval.


.. geopoints filter ( geopoints,list )

.. A filter function to extract a subset of its geopoints input using a geographical area as criteria.

.. The second argument is a list of four numbers (lat/long coordinates) defining a geographical area - [North,West,South,East] . The function extracts all the geopoints that fall within the specified area.



.. geopoints interpolate ( fieldset,geopoints )

.. Generates a set of geopoints from a field. The first parameter must contain a single field. The field is interpolated for each position of the geopoints given as a second parameter. Where it is not possible to generate a sensible value due to lack of valid data in the fieldset, the internal geopoints missing value is used (this value can be checked for with the built-in variable geo_missing_value or removed with the function remove_missing_values ). This function will return a missing value where the geopoints have missing lat/lon.



.. geopoints max ( geopoints,geopoints )
.. geopoints min ( geopoints,geopoints )

.. Returns the geopoints of maximum (minimum) value at each point. Missing values retain their value of geo_missing_value.


.. geopoints max ( geopoints,number )
.. geopoints min ( geopoints,number )

.. Returns the geopoints of the maximum (minimum) of number and the geopoints value at each point. Missing values retain their value of geo_missing_value.


.. geopoints max ( geopoints,fieldsets )
.. geopoints min ( geopoints,fieldsets )

.. Returns geopoints of maximum (minimum) of the geopoints value and the geopoints value at each grid point or spectral coefficient. Missing values, either in the fieldset or in the original geopoints variable, result in a value of geo_missing_value.


.. number maxvalue ( geopoints )
.. number minvalue ( geopoints )

.. Returns the maximum (minimum) value of all geopoints values. Missing values are bypassed in this calculation. If there are no valid values, then nil is returned.



.. geopoints nearest_gridpoint ( fieldset,geopoints[,string] )

.. Generates a set of geopoints from a field. The first field of the input fieldset is used. The result is a set of geopoints whose locations are taken from the original geopoints, but whose values are those of the nearest gridpoints in the field to the geopoints given as a second parameter. By default, when the nearest gridpoint value is a missing value or the location is out of the grid area, the internal geopoints missing value is used (this value can be checked for with the built-in variable geo_missing_value or removed with the function remove_missing_values). If an extra parameter 'valid' is added to the function call, then of the surrounding points, the nearest valid one is returned; geo_missing_value will still be returned if all the surrounding points are missing. This function will return a missing value where the geopoints have missing lat/lon.


.. py:function:: polar_vector(gpt_magnitude, gpt_dir)

    Combines two single-parameter :class:`Geopoints` into a new :class:`Geopoints` of 'polar_vector' type.
    
    :param gpt_magnitude: geopoints containing the magnitude values
    :type gpt_magnitude: :class:`Geopoints`
    :param gpt_dir: geopoints containing the direction values
    :type gpt_dir: :class:`Geopoints`
    :rtype: :class:`Geopoints` of 'polar_vector' type.

    ``gpt_magnitude`` and ``gpt_dir`` should contain the same number of points.


.. py:function:: remove_duplicates(gpt)

    Returns a new :class:`Geopoints` that contains just one instance of any duplicate geopoint in ``gpt``. 

    :param gpt: input geopoints
    :type gpt: :class:`Geopoints`
    :rtype: :class:`Geopoints`

.. py:function:: remove_missing_latlons(gpt)

    Returns a new :class:`Geopoints` that contains just the points that do not have missing latitudes or longitudes in ``gpt``. 

    :param gpt: input geopoints
    :type gpt: :class:`Geopoints`
    :rtype: :class:`Geopoints`


.. py:function:: remove_missing_values (gpt)

    Returns a new :class:`Geopoints` that contains just the non-missing values in ``gpt``.
    
    :param gpt: input geopoints
    :type gpt: :class:`Geopoints`
    :rtype: :class:`Geopoints`
    
    A geopoint is considered to be missing if either its **value** or **value2** members are missing.

.. py:function:: set_latitudes(gpt, latitudes)

    Creates a new :class:`Geopoints` with all the latitudes in ``gpt`` replaced by ``latitudes``.

    :param gpt: input geopoints
    :type gpt: :class:`Geopoints`
    :param latitudes: latitudes to be written into ``gpt``
    :type latitudes: float or ndarray
    :rtype: :class:`Geopoints`

    If ``latitudes`` is a number all the latitudes are replaced with it. If ``latitudes`` is an array shorter than the geopoints count then only the first values that have a corresponding value in ``latitudes`` are changed.

.. py:function:: set_longitudes(gpt, longitudes)

    Creates a new :class:`Geopoints` with all the longitudes in ``gpt`` replaced by ``longitudes``.

    :param gpt: input geopoints
    :type gpt: :class:`Geopoints`
    :param latitudes: longitudes to be written into ``gpt``
    :type latitudes: float or ndarray
    :rtype: :class:`Geopoints`

    If ``longitudes`` is a number all the longitudes are replaced with it. If ``longitudes`` an array and is shorter than the geopoints count then only the first values that have a corresponding value in ``longitudes`` are changed.

.. py:function:: set_levels(gpt, levels)

    Creates a new :class:`Geopoints` with all the levels in ``gpt`` replaced by ``levels``.

    :param gpt: input geopoints
    :type gpt: :class:`Geopoints`
    :param levels: levels to be written into ``gpt``
    :type levels: float or ndarray
    :rtype: :class:`Geopoints`

    If ``levels`` is a number all the levels are replaced with it.  If ``levels`` is an array and shorter than the geopoints count then only the first values that have a corresponding value in ``levels`` are changed.

.. geopoints set_dates ( geopoints, number or vector or list )
.. geopoints set_stnids ( geopoints, list )
.. geopoints set_times ( geopoints, number or vector or list )
.. geopoints set_values ( geopoints, number or vector or list )
.. geopoints set_values ( geopoints, number or string, number or vector or list )

.. Returns a new geopoints variable with either its latitude, longitude, level, date, time, stnid, value, value2 or another value column modified.

.. All these functions take two or three parameters: first one must be a geopoints variable. If three parameters are given, the second should be either the index or name of the values column to update. The last parameter defines the new values, and can be a number, a vector or a list of numbers (or dates, if set_dates()). If a number is given then all the corresponding values (latitude, longitude, level, or ...) are replaced by the given value.

.. If a vector or list is given as the last parameter then the corresponding values are replaced from the given vector or list. If the vector or list is shorter than the geopoints count then only the first values that have a corresponding value in the vector or list are changed.

.. NOTE: for dates, 8 digit integers must be used. If the list contains non-numbers, then a missing value is written into the corresponding geopoints value.

.. Examples of usage:
.. new_gpt_a = set_latitudes(gpt_a, |30, 40, 50|)
.. new_gpt_b = set_values(gpt_b, |12.4, 13.3, 1.1|)
.. new_gpt_c = set_values(gpt_c, 4, |3.3, 4.4, 5.5|) # update the 4th value column
.. new_gpt_d = set_values(gpt_d, 'precip', |0.3, 0.2, 0.1|) # update the column labelled 'precip'

.. Note that the above functions generate a new geopoints variable, leaving the original one intact. If you wish to modify the original variable, then a more efficient way is to directly access the columns using the following syntax, following the examples above:
.. gpt['latitude'] = |30, 40, 50|
.. gpt['value'] = |12.4, 13.3, 1.1|
.. gpt[name_of_column_4] = |3.3, 4.4, 5.5|
.. gpt['precip'] = |0.3, 0.2, 0.1|


.. list stnids ( geopoints )

.. Extracts the station id strings from all the geopoints and returns them as a list. If a given point does not have a station id, then a nil will be returned in its place in the list.


.. geopoints subsample ( geopoints, geopoints )

.. Returns a geopoints variable containing the same locations (latitude, longitude and height) as the second geopoints variable, but whose values are from the first geopoints variable (or a missing value if point not found in the first variable). Note that the resulting geopoints variable is sorted in the same way as performed by the geosort() function. This means that you need to be careful if performing functions between the results of a subsample() operation and another geopoints variable; if the locations in the two geopoints are the same, then you should geosort() the second geopoints beforehand. Points with missing latitudes or longitudes will still be in the output, but the rule is that such a point is defined not to be at the same location as another point, even if its lat/lon are also missing. Advice: remove missing lat/lon points using remove_missing_latlons() before using subsample() or geosort().

.. You can use function remove_missing_values() if you need to get rid of the missing valued points in the returned geopoints variable.


.. number sum ( geopoints )

.. Computes the sum of the geopoints. Missing values are bypassed in this calculation. If there are no valid values, then nil is returned.


.. vector times ( geopoints )

.. Extracts the times of all the geopoints and returns them as a vector.


.. vector or list values ( geopoints )
.. vector or list values ( geopoints, number )
.. vector or list values ( geopoints, string )

.. Extracts the values of all the geopoints and returns them as a vector. If the values are strings, then the result is a list of strings. A value column other than the first one can be specified either by index (1-based in Macro or 0-based in Python) or by name, e.g. values(gpt, 4) or values(gpt, 'geopotential'). See the description of the NCOLS subformat on the Geopoints page for more details of storing multiple value columns. Another syntax is to use direct indexing, e.g.

.. a = gpt['geopotential']


.. vector value2 ( geopoints )

.. Extracts the second values of all the geopoints and returns them as a vector.


.. list value_columns ( geopoints )

.. Returns a list containing the names of just the non-coordinate value columns in the given geopoints variable.


.. geopoints xy_vector ( geopoints, geopoints )

.. .. Combines two single-parameter geopoints variables into a u/v style geopoints variable. Both input geopoints variables should contain the same number of points.