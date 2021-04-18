covar_a
==========

.. py:function:: covar_a(fs1, fs2, [area])   

   Computes the covariance of ``fs1`` and ``fs2`` over a weighted area. 
   
   :param fs1: first input fieldset
   :type fs1: :class:`Fieldset`
   :param fs2: second input fieldset
   :type fs2: :class:`Fieldset`
   :param list area: area as [N,W,S,E] to perform the computations
   :rtype: number or list 
   
   If the ``area`` is not specified the whole field will be used in the calculation. The result is a number for a single field or a list for a multi-field :class:`Fieldset`.


.. mv-minigallery:: covar_a
