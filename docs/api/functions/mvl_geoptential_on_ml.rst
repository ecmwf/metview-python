mvl_geopotential_on_ml
=========================

.. py:function:: mvl_geopotential_on_ml(t, q, lnsp, zs)

   Computes geopotential on model levels.

   :param t: temperature fields on the **full model level range** in ascending numeric order (e.g. 1-137)
   :type t: :class:`Fieldset`
   :param q: the specific humidity fields on the **full model level range** in ascending numeric order (e.g. 1-137)
   :type q: :class:`Fieldset`
   :param lnsp: logarithm of surface pressure field (model level 1!).
   :type lnsp: :class:`Fieldset`
   :param zs: surface geopotential field (model level 1!)
   :type zs: :class:`Fieldset`
   :rtype: :class:`Fieldset`

   All fields must be **gridpoint** data - no spherical harmonics, and they must all be on the same grid, with the same number of points. :func:`mvl_geopotential_on_ml` assumes that there are no other dimensions contained in the data, e.g. all fields should have the same date and time. The return value is a :class:`Fieldset` of geopotential on model levels.

   .. note::
      **Surface geopotential** is defined on model level 1 in MARS at ECMWF! For most recent dates it is available for the 0 forecats step. However, generally it is only available as an **analysis** field!  
      
   :Example:
   
      This code illustrates how to use :func:`mvl_geopotential_on_ml` with data retrieved from MARS:

      .. code-block:: python

         import metview as mv
         
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

.. mv-minigallery:: mvl_geopotential_on_ml
