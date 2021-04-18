accumulate
************

.. py:function:: accumulate(fs)
.. py:function:: Fieldset.accumulate()
   :noindex:

   Computes the sum of all the values for each field in ``fs``.

   :param fs: input fieldset
   :type fs: :class:`Fieldset`
   :rtype: number or list or None

   If there is only one field in ``fs`` it returns a number, otherwise a list is returned. Only non-missing values are considered in the calculation. For fields with no valid values NaN is returned.
   

.. mv-minigallery:: accumulate
