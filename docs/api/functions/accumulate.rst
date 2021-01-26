accumulate
************

.. py:function:: accumulate(fs)

   Computes the sum of all the values for each field in ``fs``.

   :param fs: input fieldset
   :type fs: :class:`Fieldset`
   :rtype: float or ndarray or None

   If there is only one field in ``fs`` it returns a number, otherwise a numpy array is returned. Only non-missing values are considered in the calculation. For fields with no valid values NaN is returned.
   

.. mv-minigallery:: accumulate
