absolute_vorticity
========================

.. py:function:: absolute_vorticity(rvo)

   Computes the absolute vorticity from a relative vorticity :class:`Fieldset`.
   
   :param rvo: relative vorticity (1/s)
   :type rvo: :class:`Fieldset`
   :rtype: :class:`Fieldset`  
   
   The computation of absolute vorticity is based on the following formula:

    .. math::
      
        2\Omega sin\phi + rvo 

    where:

    * :math:`\phi` is the latitude
    * :math:`\Omega` is the Earth's angular velocity (1/s).

   The ecCodes paramId of the resulting fields is set to 3041 (absolute vorticity).

.. mv-minigallery:: absolute_vorticity
