thickness
============

.. py:function:: thickness(lnsp, [levels])
.. py:function:: thickness(lnsp, fs_levels)
   :noindex:

   Computes the pressure thickness (in Pa) of a list of ECMWF model levels from ``lnsp`` (Logarithm of Surface Pressure). 
   
   :param lnsp: fieldset containing an lnsp field (its ecCodes paramId must be 152)
   :type lnsp: :class:`Fieldset`
   :param levels: the target model level or levels 
   :type levels: number or list of numbers
   :param fs_levels: fielsdet defining the target model levels
   :type fs_levels:  :class:`Fieldset`
   :rtype: :class:`Fieldset`

   If only ``lnsp`` is specified the thickness is computed for all the model levels defined by the GRIB header of ``lnsp``.

   If ``levels`` is specified it defines the output model level(s). For a **single level** ``levels`` must be number, while for **multiple levels** it must be a list.

   If ``fs_levels`` is specified the target levels are taken from its fields.

   Missing values in ``lnsp`` are retained in the output fieldset.

   .. warning::
      This function is obsolete, use :func:`unithickness` instead.


.. mv-minigallery:: thickness
