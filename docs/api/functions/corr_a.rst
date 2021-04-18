corr_a
==========

.. py:function:: corr_a(fs1, fs2, [area])    
   
   Computes the correlation between ``fs1`` and ``fs2`` over a weighted ``area``. 
   
   :param fs1: first input fieldset
   :type fs1: :class:`Fieldset`
   :param fs2: second input fieldset
   :type fs2: :class:`Fieldset`
   :param list area: area as [N,W,S,E] to perform the computations
   :rtype: number or list 
   
   If ``area`` is not specified the whole field will be used in the calculation. The result is a number for a single field or a list for a multi-field :class:`Fieldset`.

   With n fields in ``fs`` by denoting the i-th value in the k-th field by :math:`x_{i}^{k}` the output values can be written as:

   .. math:: 
      
          z_{i} = \frac {1}{N} \sum_{k}^{N}x_{i}^{k}y_{i}^{k} - \frac {1}{N} \sum_{k}^{N}x_{i}^{k} \frac {1}{N} \sum_{k}^{N}y_{i}^{k}
          
          v_{i} = \frac {1}{n} \sum_{k}^{n} (x_{i}^{k})^2 - \frac {1}{n} (\sum_{k}^{n} x_{i}^{k})^2

   .. note::
      The following lines are equivalent although the first one is more efficient:
      
      .. code-block:: python

         z = corr_a (x, y)
         z = covar_a (x, y) / (sqrt(var_a(x)) * sqrt(var_a(y)))

.. mv-minigallery:: corr_a
