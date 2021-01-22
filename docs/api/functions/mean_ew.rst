mean_ew
=============

.. py:function:: mean_ew(fs)

   Computes the mean for each line of constant latitude in ``fs``.
   
   :param fs: input fieldset
   :type fs: :class:`Fieldset`
   :rtype: :class:`Fieldset`

   The result is a fieldset where the value at each point is the mean of all the points at that latitude. Missing values are excluded; if there are no valid values, then the grib missing value indicator will be returned for those points.


.. mv-minigallery:: mean_ew
