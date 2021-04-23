max
========

.. py:function:: max(fs)
.. py:function:: max(fs, other_fs)
.. py:function:: max(fs, value)
.. py:function:: max(fs, gpt)

   Computes the point-wise maximum of ``fs``.

   :param fs: input fieldset
   :type fs: :class:`Fieldset`
   :param other_fs: another input fieldset
   :type other_fs: :class:`Fieldset`
   :param number value: input numerical value
   :param gpt: input geopoints data
   :type gpt: :class:`Geopoints`
   :rtype: :class:`Fieldset` or :class:`Geopoints`

   The actual behaviour of :func:`max` depends on the arguments:

   * if ``fs`` is the only argument :func:`max` returns a :class:`Fieldset` with a single field containing the maximum value of ``fs`` at each grid point or spectral coefficient. A missing value anywhere in ``fs`` will result in a missing value in the corresponding place in the output.  
   * if ``other_fs`` is specified :func:`max` returns a :class:`Fieldset` containing the maximum of ``fs`` and ``other_fs`` at each grid point or spectral coefficient. A missing value anywhere in ``fs`` or ``other_fs`` will result in a missing value in the corresponding place in the output.
   * if ``value`` is specified :func:`max` returns a :class:`Fieldset` containing the maximum of ``fs`` and ``value`` at each grid point or spectral coefficient. A missing value anywhere in ``fs`` will result in a missing value in the corresponding place in the output.
   * if ``gpt`` is specified :func:`max` returns a :class:`Geopoints` containing the maximum of ``fs`` and ``gpt`` at each location in ``gpt``. A missing value anywhere in ``fs`` or ``gpt`` will result in a :class:`Geopoints` missing value in the corresponding place in the output.

..  py:function:: max(nc, nc_other)
..  py:function:: max(nc, value)

    Returns the :class:`NetCDF` of the maximum value of ``nc`` and ``nc_other`` or ``value``.

    :param nc: input nectdf
    :type nc: :class:`NetCDF`
    :param nc_other: another input nectdf
    :type nc_other: :class:`NetCDF`
    :param value: value
    :type value: number
    :rtype:  :class:`NetCDF`



.. mv-minigallery:: max
