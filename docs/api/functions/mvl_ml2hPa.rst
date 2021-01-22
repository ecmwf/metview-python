mvl_ml2hPa
=============

.. py:function:: mvl_ml2hPa(lnsp, fs, pressures)

   Interpolates ``fs`` from ECMWF model levels onto a set of pressure levels defined by ``pressures``. 
   
   :param lnsp: logarithm of surface pressure field (model level 1!).
   :type lnsp: :class:`Fieldset`
   :param fs: fieldset to be interpolated (must contain model levels!). Does not have to be sorted by level.
   :type fs: :class:`Fieldset`
   :param list pressures: list of target pressure levels in hPa. Does not have to be sorted.
   :rtype: :class:`Fieldset`
  
   At locations where the interpolation is not possible a missing value is returned.
    
   :Example:
   
      This code illustrates how to use :func:`mvl_ml2hPa` with data retrieved from MARS:

      .. code-block:: python

         import metview as mv

         # retrieve the data on model levels
         ret_core = {"type": "fc", "levtype": "ml", "step": 12, "grid": [1.5,1.5]}
         t_ml = mv.retrieve(**ret_core, param="t", levelist=[1, "to", 137])
         lnsp = mv.retrieve(**ret_core, param="lnsp", levelist=1)

         # interpolate onto a list of pressure levels
         p_levels = [1000, 900, 850, 500, 300, 100, 10, 1, 0.1]
         t_pres = mv.mvl_ml2hPa(lnsp, t_ml, p_levels)


.. mv-minigallery:: mvl_ml2hPa
