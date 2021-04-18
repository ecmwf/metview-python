var_a
==============

.. py:function:: var_a(fs, [area])
 
   Computes the variance of ``fs`` over a weighted area. 
   
   :param fs: input fieldset
   :type fs: :class:`Fieldset`
   :param list area: area as [N,W,S,E] to perform the computations
   :rtype: number or list 
   
   If the ``area`` is not specified the whole field will be used in the calculation. The result is a number for a single field or a list for a multi-field :class:`Fieldset`.


.. mv-minigallery:: var_a
