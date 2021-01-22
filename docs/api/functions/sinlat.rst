sinlat
=========

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

.. mv-minigallery:: sinlat
