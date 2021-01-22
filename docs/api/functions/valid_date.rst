valid_date
=================

.. py:function:: valid_date(fs)

   Returns the valid dates (including the time components) for each field in ``fs``.
   
   :param fs: input fieldset
   :type fs: :class:`Fieldset`
   :rtype: datetime.datetime or list of datetime.datetime objects

   If ``fs`` has only one field, a date is returned; otherwise a list of dates are returned.

.. mv-minigallery:: valid_date