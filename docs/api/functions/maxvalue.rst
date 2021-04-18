maxvalue
============

.. py:function:: maxvalue(fs, [area])

   Computes the maximum of all the values in ``fs``.

   :param fs: input fieldset
   :type fs: :class:`Fieldset`
   :param list area: area as [North, West, South, East]
   :rtype: number or None

   If ``area`` is specified only points within it will be included in the computation. Missing values are ignored, and if there are no valid values at all, :func:`maxvalue` returns None.

.. mv-minigallery:: maxvalue
