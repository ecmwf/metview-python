nearest_gridpoint_info
========================

.. py:function:: nearest_gridpoint_info(fs, lat, lon, [mode])
.. py:function:: nearest_gridpoint_info(fs, location, [mode])
   :noindex:

   Returns the value and location of the nearest grid point to a given location in each field in ``fs``. 
   
   :param fs: input fieldset
   :type fs: :class:`Fieldset`
   :param lat: target latitude
   :type lat: number
   :param lon: target longitude
   :type lon: number
   :param location: single target location defined as a list of [lat, lon]
   :type location: list
   :param str mode: specifies the way missing values are handled. The only allowed value is "valid".
   :rtype: list of dict
   
   The return value is a **list** containing the following values for each field:
   
   If the nearest gridpoint value is non missing a dictionary is returned with these members:
   
   * latitude: latitude of the nearest gridpoint
   * longitude: longitude of the nearest gridpoint
   * index: index of nearest gridpoint within the field 
   * distance: distance between the nearest gridpoint and the specified location in km
   * value: value at the nearest gridpoint

   If the nearest gridpoint has missing value the return value depends on ``mode``:
   
      * if ``mode`` is not specified None is returned
      * if ``mode`` is "valid" the dictionary for the nearest valid point from the surrounding gridpoints is returned. If all the surrounding points are missing None is returned
   
   :Example:

      .. code-block:: python

         import metview as mv
         
         # read grib with 2 fields on a 1.5x1.5 degree grid
         f = mv.read("my_data.grib")
         
         # get nearest gridpoint info
         info = mv.nearest_gridpoint_info(f, 47, 19)
         print(info)

         >>> [{'latitude': 46.5, 'longitude': 19.5, 
               'index': 6973.0, 'distance': 67.3506,
               'value': 291.144}, 
              {'latitude': 46.5, 'longitude': 19.5, 
               'index': 6973.0, 'distance': 67.3506,
               'value': 294.011'}]

.. mv-minigallery:: nearest_gridpoint_info
