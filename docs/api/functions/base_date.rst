base_date
==============

.. py:function:: base_date(fs)

   Returns the base dates (including the time components) of the given fields. 

   :param fs: input fieldset
   :type fs: :class:`Fieldset`
   :rtype: datetime.datetime or list of datetime.datetime objects

   If ``fs`` has only one field, a date is returned; otherwise a list of dates is returned.


.. mv-minigallery:: base_date