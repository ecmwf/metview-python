average
================

.. py:function:: average(fs)

   Computes the average of all the values for each field in ``fs``. 
   
   :param fs: input fieldset
   :type fs: :class:`Fieldset`
   :rtype: number or list or None

   If there is only one field in ``fs`` a number is returned, otherwise a list is returned. Only non-missing values are considered in the calculation. If there are no valid values, the function returns NaN for that field.

   .. note::
      :func:`average` simply returns the mathematical average of all the field values using the following formula:

      .. math:: 
      
         average = \frac {1}{N} \sum_{i}^{N}f_{i}
        
      To get the physically correct average based on the grid cell areas use :func:`integrate`.


.. mv-minigallery:: average
