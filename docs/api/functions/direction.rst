direction
==============

.. py:function:: direction(u, v)

   Computes the meteorological wind direction in each grid point of ``u`` and ``v``.

   :param u: u wind component
   :type u: :class:`Fieldset`
   :param v: v wind component
   :type v: :class:`Fieldset`
   :rtype: :class:`Fieldset`

   The resulting values are directions, in degrees clockwise from North, where a value of 0 represents a wind from the North and a value of 90 represents a wind from the East. A missing value in either ``u`` or ``v``  will result in a missing value in the corresponding place in the output fieldset.


.. mv-minigallery:: direction
