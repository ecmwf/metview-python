sum
======

.. py:function:: sum(fs)

   Computes the point-wise sum of the values in ``fs``. 

   :param fs: input fieldset
   :type fs: :class:`Fieldset`
   :rtype: :class:`Fieldset`

   The output is a :class:`Fieldset` with one field only. A missing value in any field will result in a missing value in the corresponding gridpoint in the output fieldset. 
   
   With N fields in ``fs`` by denoting the i-th value in the k-th field by :math:`x_{i}^{k}` the output values can be written as:

   .. math:: 
      
         s_{i} = \sum_{k}^{N} x_{i}^{k}


.. py:function:: sum(gpt)

    Computes the sum of all the values in the values column of ``gpt``. 
    
    :param gpt: input geopoints
    :type gpt: :class:`Geopoints`
    :rtype: number
    
    Missing values are bypassed in this calculation. If there are no valid values None is returned.

.. mv-minigallery:: sum
