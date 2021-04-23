merge
===========

.. py:function:: merge (fs1, fs2, [f3, ...])

   Merge several fieldsets. 
   
   :param fs: input fieldsets
   :type fs: :class:`Fieldset`
   :rtype: :class:`Fieldset`

   The output is a :class:`Fieldset` with as many fields as the total number of fields in all merged fieldsets. Merging with None does nothing.

.. mv-minigallery:: merge