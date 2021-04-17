datainfo
============

.. py:function:: datainfo(fs)   

   Returns a dictionary containing some metadata for each field in ``fs``. 
   
   :param fs: input fieldset
   :type fs: :class:`Fieldset`
   :rtype: list of dict
   
   The returned dict contains the following members: 
   
   * index: the index of the field in the fieldset (indexing starts at 0)
   * number_present: the number of non-missing values
   * number_missing: the number of missing values
   * proportion_present: the normalised proportion of the non-missing values to the total number of values ([0-1])
   * proportion_missing: normalised the proportion of the missing values to the total number of values ([0-1])
   

.. mv-minigallery:: datainfo
