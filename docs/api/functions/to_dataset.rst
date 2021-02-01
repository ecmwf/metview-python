to_dataset
***************

.. py:function:: to_dataset()
.. py:function:: Fieldset.to_dataset()
   :noindex:
   
   Converts a :class:`Fieldset` into an xarray Dataset.

   :rtype: xarray dataset


    The conversion is based on the Open Source `cfgrib <https://github.com/ecmwf/cfgrib>`_ package which is planned to be ultimately integrated into xarray.

   :Example:

    This script:
      
    .. code-block:: python

        import metview as mv
 
        t2m_fc = mv.retrieve(
            type    = 'fc',
            levtype = 'sfc',
            param   = ['2t', '2d'],
            date    = -5,
            step    = list(range(0, 48+1, 6)),
            grid    = [1,1]
        )
        
        xa = t2m_fc.to_dataset()
        print(xa)

    produces the following output:

    .. code-block:: console

        <xarray.Dataset>
        Dimensions:    (latitude: 181, longitude: 360, step: 9, time: 1)
        Coordinates:
        * time       (time) datetime64[ns] 2018-05-10T12:00:00
        * step       (step) timedelta64[ns] 0 days 00:00:00 0 days 06:00:00 ...
        * latitude   (latitude) float64 90.0 89.0 88.0 87.0 86.0 85.0 84.0 83.0 ...
        * longitude  (longitude) float64 0.0 1.0 2.0 3.0 4.0 5.0 6.0 7.0 8.0 9.0 ...
        Data variables:
            2t         (time, step, latitude, longitude) float32 ...
            2d         (time, step, latitude, longitude) float32 ...
        Attributes:
            Conventions:  CF-1.7
            comment:      GRIB to CF translation performed by xarray-grib


    This is another example:

    .. code-block:: python

        import metview as mv

        grib = mv.read('temperature_on_pl.grib')
        x = grib.to_dataset() # x is now an xarray dataset
        fs = mv.mean(x*2) # *2 is done by xarray, mean() is done by Metview


.. mv-minigallery:: to_dataset
