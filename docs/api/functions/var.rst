var
=========

.. py:function:: var(fs)

   Computes the point-wise variance in ``fs``. 
   
   :param fs: input fieldset
   :type fs: :class:`Fieldset`
   :rtype: :class:`Fieldset`
   
   The output is a :class:`Fieldset` with one field only. A missing value in any field in ``fs`` will result in a missing value in the corresponding grid point in the output fieldset. 
   
   With n fields in ``fs`` by denoting the i-th value in the k-th field by :math:`x_{i}^{k}` the output values can be written as:

   .. math:: 
      
         v_{i} = \frac {1}{n} \sum_{k}^{n} (x_{i}^{k})^2 - \frac {1}{n} (\sum_{k}^{n} x_{i}^{k})^2

   .. note:: 
      The following lines are equivalent:

      .. code-block:: python

         y = mv.var(x)
         y = mv.mean(x*x)-mv.mean(x)**2


.. mv-minigallery:: var
