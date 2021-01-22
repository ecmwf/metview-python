vertint
==========

.. py:function:: vertint(fs)
.. py:function:: vertint(lnsp, fs)
   :noindex:

   Performs a vertical integration on ECMWF (hybrid) model levels. 

   :param fs: input fieldset
   :type fs: :class:`Fieldset`
   :param lnsp: lnsp fieldset
   :type lnsp: :class:`Fieldset`
   :rtype: :class:`Fieldset` containing one field only

   ``fs`` must contain a **contiguous range** of model levels for the same parameter. A missing value in any field will result in a missing value in the corresponding place in the output fieldset. 
   
   When no ``lnsp`` is specified ``fs`` must also contain an lnsp field with an ecCodes paramId of 152. 

   The computations are based on the following formula:

   .. math::
      
      \int_{bottom}^{top} f \frac{dp}{g}

   where:

   * f: input fieldset
   * p: pressure
   * g: acceleration of gravity (9.80665 m/s2).

   .. warning::
      This function is obsolete, use :func:`univertint` instead.

.. mv-minigallery:: vertint
