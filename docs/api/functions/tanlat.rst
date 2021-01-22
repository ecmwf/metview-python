tanlat
=========

.. py:function:: tanlat(fs)

   Returns the fieldset of the tangent of the latitude of ``fs`` at each grid point. 

   :param fs: input fieldset
   :type fs: :class:`Fieldset`
   :rtype: :class:`Fieldset` 

   Missing values are retained, unaltered by the calculation. The resulting fields contain missing values on the poles.


.. mv-minigallery:: tanlat
