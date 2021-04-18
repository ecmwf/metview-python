find
==========

.. py:function:: find(fs, value, [area_or_mask])
.. py:function:: find(fs, range, [area_or_mask])
   :noindex:

   Returns a list of locations (lat/lon pairs) where the values of ``fs`` equal to or within the range of ``value_or_range``. 
   
   :param fs: input fieldset 
   :type fs: :class:`Fieldset`
   :param number value: the value defining the search condition
   :param list range: the range defining the search condition
   :param area_or_mask: area or mask field restricting the search
   :type area_or_mask: list or :class:`Fieldset`
   :rtype: list of lists

   The primary search condition is defined by ``value`` or ``range``:

   * if ``value`` is specified the locations where ``fs`` equals to this number are returned
   * if ``range`` is specified as a list of [v1, v2] the locations where ``fs`` values are within the closed range of [v1, v2] are returned

   The optional ``area_or_mask`` argument can pose an additional search condition:

   * if ``area_or_mask`` is a list of four numbers it defines the area as [North,West,South,East] for the search
   * if ``area_or_mask`` is a :class:`Fieldset` with one field it defines a mask for the search, e.i. only those gridpoints are checked where the mask value is non-zero.
   
   Missing values in ``fs`` are not returned.

.. mv-minigallery:: find
