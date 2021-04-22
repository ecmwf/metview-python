unithickness
==============

.. py:function:: unithickness(lnsp, [levels], [lnsp_code])
.. py:function:: unithickness(lnsp, fs_levels, [lnsp_code])
   :noindex:

   Computes the pressure thickness in Pa of a list of ECMWF model levels from ``lnsp`` (logarithm of surface pressure). 

   :param lnsp: lnsp fieldset defined on model level 1
   :type lnsp: :class:`Fieldset`
   :param fs_levels: fieldset defining the target model levels
   :type fs_levels: :class:`Fieldset`
   :param lnsp_code: ecCodes paramId for lnsp
   :type lnsp_code: number
   :param levels: list of target model levels whose thickness will be computed
   :type levels: list
   :rtype: :class:`Fieldset`

   ``lnsp`` must contain an lnsp field, which is identified by its ecCodes paramId. By default the value of 152 is used but it can be overridden by the optional ``lnsp_code``.
   
   The list of target model levels depends on the actual arguments:

   * if no ``fs_levels`` is specified the thickness is computed for all the model levels defined by the GRIB header in ``lnsp``.   
   * if ``fs_levels`` is specified the thickness is computed for all the model levels in ``fs_levels``.
   * if ``levels`` is specified it defines the list of target model levels whose thickness will be computed. 
         
   A missing value in ``lnsp`` will result in a missing value in the corresponding place in the output fieldset.



.. mv-minigallery:: unithickness
