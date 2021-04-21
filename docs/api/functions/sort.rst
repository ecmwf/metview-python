sort
=========

.. py:function:: sort(fs, [keys, [orders]])

   Sorts ``fs`` according to the specified options.

   :param fs: input fieldset
   :type fs: :class:`Fieldset`
   :param keys: sorting key(s)
   :type keys: str or list
   :param orders: sorting order(s)
   :type orders: str or list
   :rtype: :class:`Fieldset` 

   The list of MARS keys that can be used for the sorting are as follows (theye are specified in order of precedence): 

      * date
      * time
      * step
      * number
      * levelist
      * param
   
   Here **number** is the ENS forecast member number, while **param** is the ecCodes paramID (int).

   If no options are specified :func:`sort` sorts ``fs`` in ascending order according to the allowed MARS keys.

   If ``keys`` are specified (either as a list or a str) they modify the precedence of the sorting keys.

   The optional ``orders`` can specify the sorting direction: ">" means descending, while "<" means ascending order. ``orders`` can be either a str or a list:

   * if it is a str the sorting direction applies to all the ``keys``
   * if it is a list ``keys`` must also be a list with the same number of elements - the sorting directions apply to each sorting key specified.

.. mv-minigallery:: sort
