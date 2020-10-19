merge
===========

.. py:function:: merge (fs, fs1)

   Merge several fieldsets. 
   
   :param fs: input fieldset
   :type fs: :class:`Fieldset`
   :rtype: :class:`Fieldset`

   The output is a fieldset with as many fields as the total number of fields in all merged fieldsets. Merging with None does nothing, and is used to initialise when building a fieldset from scratch.