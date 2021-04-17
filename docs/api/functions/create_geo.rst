create_geo
=============

..  py:function:: create_geo(number_of_points, [format, [number_of_values_columns, [value_columns]]])
..  py:function:: create_geo(number_of_points, **kwargs)
    :noindex:

    Creates a new :class:`Geopoints` with the given ``number_of_points``, all set to default values and coordinates.

    :param fs: input geopoints
    :type fs: :class:`Geopoints`
    :param number number_of_points: number of points
    :param str format: geopoints format (see below)
    :param number number_of_value_columns: the number of value columns for the "ncols" formatted
    :param list value_columns: the name of the value columns for the "ncols" format
    :param kwargs: see below
    :rtype: :class:`Geopoints`

    It is intended that this function be used in conjunction with the "set_* geopoints" functions in order to populate the geopoints with data. 
    
    If no ``format`` is specified a "traditional" 6-column format geopoints is created. Otherwise ``format`` defines the actual format. The possible values are as follows: 'polar_vector', 'xy_vector ', 'xyv ' and 'ncols'. 
    
    If ``format`` is "ncols", then the number of value columns can be given by ``number_of_value_columns`` (default is 1). In this case, the ``value_columns`` can be used to provide a list of names of the value columns.

    An alternative, and more efficient way to create a new geopoints variable if you already have the data to populate it, is to provide a set of keyword arguments (``kwargs``) as shown in the examples below. Using this syntax, you can completely create a new geopoints variable with all its column data in one go. This is much more efficient than creating an empty geopoints variable and then populating it using the 'set_*' functions.

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

.. mv-minigallery:: create_geo