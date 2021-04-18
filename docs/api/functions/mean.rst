mean
==========

.. py:function:: mean(fs)

   Computes the point-wise mean of ``fs``. 
   
   :param fs: input fieldset
   :type fs: :class:`Fieldset`
   :rtype: :class:`Fieldset`
   
   The result is a :class:`Fieldset` with a single field in each gridpoint containing the mean of all the values belonging to the same gridpoint throughout the fields in ``fs``. A missing value in any field will result in a missing value in the corresponding place in the output. 
   
   With N fields in ``fs`` by denoting the i-th value in the k-th field by :math:`f_{i}^{k}` the output values can be written as:

   .. math::

         m_{i} = \frac {1}{N} \sum_{k}^{N}f_{i}^{k}


.. py:function:: mean(gpt)

    Computes the mean of all the values in the values column of ``gpt``. 
    
    :param gpt: input geopoints
    :type gpt: :class:`Geopoints`
    :rtype: number or None
    
    Missing values are bypassed in this calculation. If there are no valid values, then None is returned.

.. mv-minigallery:: mean