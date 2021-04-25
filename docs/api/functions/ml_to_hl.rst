ml_to_hl
============

.. py:function:: ml_to_hl(fs, z, zs, h, ref_level, method)

   Interpolates ``fs`` on model levels (i.e. on hybrid or eta levels used by the IFS) onto height levels (in m) above sea or ground level. 
   
   :param fs: fieldset to be interpolated
   :type fs: :class:`Fieldset`
   :param z: geopotential fieldset on model levels (it must contain the same levels as ``fs`` but their order can be different) 
   :type z: :class:`Fieldset`
   :param zs: surface geopotential field (if ``ref_level`` is set to "sea" it should be set to None).
   :type zs: :class:`Fieldset` or None
   :param h: list of target height levels (they can came in any given order)
   :type h: list or :class:`Fieldset`
   :param str ref_level: specifies the reference level for the target heights. The possible values are "sea" and "ground"
   :param str method: specifies the interpolation method. The possible values are "linear" and "log". 
   :rtype: :class:`Fieldset`
      
   At gridpoints where the interpolation is not possible a missing value is returned.  

   .. note::
      Geopotential is not archived operationally on model levels in MARS at ECMWF. To compute it use :func:`mvl_geopotential_on_ml`. 
      
   :Example:
   
      This code illustrates how to use :func:`ml_to_hl` together with :func:`mvl_geopotential_on_ml` with data retrieved from MARS:

      .. code-block:: python

         import metview as mv 

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


.. mv-minigallery:: ml_to_hl