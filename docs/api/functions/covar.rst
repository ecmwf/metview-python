covar
========

.. py:function:: covar(fs1, fs2)   

   Computes the point-wise covariance of ``fs1`` and ``fs2``. 
   
   :param fs1: first input fieldset
   :type fs1: :class:`Fieldset`
   :param fs2: second input fieldset
   :type fs2: :class:`Fieldset`
   :rtype: :class:`Fieldset`
   
   The result is a single field. With N fields in ``fs1`` and ``fs2`` by denoting the i-th value in the k-th field by :math:`x_{i}^{k}` and :math:`y_{i}^{k}` respectively, the output values can be written as:

   .. math:: 
      
         z_{i} = \frac {1}{N} \sum_{k}^{N}x_{i}^{k}y_{i}^{k} - \frac {1}{N} \sum_{k}^{N}x_{i}^{k} \frac {1}{N} \sum_{k}^{N}y_{i}^{k}

   A missing value in either ``fs1`` or ``fs2`` will result in a missing value in the corresponding place in the output.

   .. note::
      The following lines are equivalent although the first one is more efficient:
      
      .. code-block:: python

         z = covar(x,y)
         z = mean(x*y)-mean(x)*mean(y)



.. mv-minigallery:: covar
