univertint
=============


.. py:function:: univertint(fs, [lnsp_code])
.. py:function:: univertint(lnsp, fs, [levels])
   :noindex:

   Performs a vertical integration for pressure levels or ECMWF (hybrid) model levels. 

   :param fs: input fieldset
   :type fs: :class:`Fieldset`
   :param lnsp: lnsp fieldset defined on model level 1
   :type lnsp: :class:`Fieldset`
   :param lnsp_code: ecCodes paramId for lnsp
   :type lnsp_code: number
   :param levels: level range as a list of [top, bottom]
   :type levels: list
   :rtype: :class:`Fieldset` containing one field only

   :func:`univertint` has to be called in a different way depending on the type of vertical levels in ``fs``.

   * Pressure levels: the function has to be called with the ``fs`` argument only.
   * Model levels: 

      * when no ``lnsp`` is specified ``fs`` must also contain an lnsp field. In this case the optional ``lnsp_code`` can specify the ecCodes **paramId** used to identify the **lnsp** field (by default the value of 152 is used.
      * when ``lnsp`` is specified it defines the **lnsp** field.
      * the optional ``levels`` parameter is a **list** with two numbers [top, bottom] to specify the level range for the integration. If ``levels`` is not specified the vertical integration is performed for all the model levels in ``fs``.
         
   A missing value in any field will result in a missing value in the corresponding place in the output fieldset.

   The computations are based on the following formula:

   .. math::
      
      \int_{bottom}^{top} f \frac{dp}{g}

   where:

   * f: input fieldset
   * p: pressure
   * g: acceleration of gravity (9.80665 m/s2).

:Example: 

      .. code-block:: python

         import metview as mv

         # Retrieve cloud liquid water content 
         clwc = mv.retrieve(
            levtype : "ml",
            levelist : [1,"to",137],
            param : "clwc",
            date : -1,
            grid : [2,2]
         )

         # Retrieve lnsp
         lnsp = mv.retrieve(
            levtype : "ml",
            levelist : 1,
            param : "lnsp",
            date : -1,
            grid : [2,2]
         )

         # Compute total amount of liquid water
         r = mv.univertint(lnsp,clwc)



.. mv-minigallery:: univertint
