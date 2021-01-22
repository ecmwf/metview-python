stdev
=========

.. py:function:: stdev(fs)

   Computes the point-wise standard deviation of ``fs``. 
   
   :param fs: input fieldset
   :type fs: :class:`Fieldset`
   :rtype: :class:`Fieldset`
   
   A missing value in any field in ``fs`` will result in a missing value in the corresponding grid point in the output fieldset. 
   
   With N fields in ``fs`` by denoting the i-th value in the k-th field by :math:`x_{i}^{k}` the output values can be written as:

   .. math:: 
      
         z_{i} = \sqrt {\frac {1}{N} \sum_{k}^{N} (x_{i}^{k})^{2} - (\frac {1}{N} \sum_{k}^{N} x_{i}^{k} )^2}

   .. note::
      The following lines are equivalent:

      .. code-block:: python

         y = mv.stdev(x)
         y = mv.sqrt(mv.mean(x*x)-mv.mean(x)^2)
         y = mv.sqrt(mv.var(x))

.. mv-minigallery:: stdev
