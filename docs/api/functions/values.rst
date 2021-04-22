values
============

.. py:function:: values(fs)

   Returns the grid point values in ``fs`` as an ndarray. 
   
   :param fs: input fieldset
   :type fs: :class:`Fieldset`
   :rtype: ndarray
   
   If ``fs`` contains more than one field a 2D-ndarrays is returned. Missing values are included in the results as nan.

   :Example:

      .. code-block:: python

         import metview as mv

         # fs is a fieldset of n fields
         vals = mv.values(fs)
         
         # values in the first field
         first_vals = vals[0]

         # first value in the first field
         first_gridpoint = first_vals[0]

         # or equivalently
         first_gridpoint = vals[0][0]



.. py:function:: values(gpt, [index_or_name])

    Returns the values in the specified values column of ``gpt``.

    :param gpt: input geopoints
    :type gpt: :class:`Geopoints`
    :param index_or_name: index or name of the values column to be returned from ``gpt``
    :type index_or_name: number or str
    :rtype: list or ndarray

    If ``index_or_name`` is specified and is a number it refers to the index of the column within the value columns (and not within all the columns in ``gpt``). E.g. 0 means the first value column. 
    
    ``index_or_name`` has to be used for :class:`Geopoints` of 'ncols' type. In all the other types the values column is uniquely identified.

    If the values column contains str the return will be a list, otherwise an ndarray is returned. 

    :Example:

        .. code-block:: python

            import metview as mv
            
            gpt = mv.read("my_data.gpt")

            # get values from the 4th column
            a = mv.values(gpt, 3)

            # get values from column named "geopotential"
            a = mv.values(gpt, "geopotential")

            # direct indexing can also be used
            a = gpt["geopotential"]


..  py:function::  values(nc, [index])

    Returns all the values of the current NetCDF variable in ``nc``.

    :param nc: input NetCDF
    :type nc: :class:`NetCDF`
    :param index: value index (zero-based)
    :type index: list
    :rtype: ndarray or list of str or list of datetime.datetime

    To define a hypercube for the value extraction ``index`` has to be specified as a list with the same number of elements as the number of dimensions of the current NetCDF variable. The elements (except one) should be numbers, specifying the indexes (0-based) into the respective dimensions from where the value(s) are to be taken. If all the elements are numbers, then they simply specify the coordinates for a single value (returned as a single-value array). Optionally, one of the elements can be set to the string 'all'; in this case, all the values from that dimension are returned. 
    
    :Example:
    
        If the current NetCDF variable is defined with 3 dimensions: Q(time, region, exp) then we can obtain the values for all times, for the second region and the fifth exp with this syntax:

        .. code-block:: python

            v = mv.values(nc, ['all', 1, 4])


.. mv-minigallery:: values