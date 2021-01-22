lookup
===========

.. py:function:: lookup(indexer, values)

   Build an output fieldset using the values in ``indexer`` as indices for a look-up in ``values``.

   :param index: indexer fieldset
   :type fs: :class:`Fieldset`
   :param values: values to choose from
   :type values: :class:`Fieldset` or 1D-ndarray
   :rtype: :class:`Fieldset`

   :func:`lookup` takes the grid values in ``indexer`` and uses them as index in ``values`` in the following way:

      * let us suppose a grid value in the i-th ``indexer`` field is N (for float values the integer part is taken)
      * what happens depends on the type of ``values``:

         * if ``values`` is a :class:`Fieldset` the value at the same gridpoint in the (N-1)-th field in ``values`` is written into the i-th output field at the given gridpoint (here field indexing starts at 0)
         * if ``values`` is an ndarray the value at the (N-1)-th position in the ``values`` array is written into the i-th output field at the given gridpoint
   
   The output will have has as many fields as there are in ``indexer``.

   Any missing values in ``indexer`` will cause the function to fail with a "value out of range" error message.

.. mv-minigallery:: lookup
