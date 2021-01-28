
divrot
=========================

.. container::
    
    .. container:: leftside

        .. image:: /_static/DIVROT.png
           :width: 48px

    .. container:: rightside

		Computes the rotational wind from spectral (shperical harmonics) vorticity GRIB fields.


		.. note:: This function performs the same task as the `Rotational or Divergent Wind <https://confluence.ecmwf.int/display/METV/Rotational+or+Divergent+Wind>`_ icon in Metview’s user interface. It accepts its parameters as keyword arguments, described below.


.. py:function:: divrot(**kwargs)
  
    Computes the rotational wind from spectral (spherical harmonics) vorticity GRIB fields.


    :param data: Specifies the vorticity GRIB fields. Must be spectral (spherical harmonics) data.
    :type data: :class:`Fieldset`

    :param truncation: Specifies the triangular truncation to be applied to the spherical harmonics input data prior to conversion to lat/lon.
    :type truncation: number, default: 216

    :param smoothing: Specifies whether to apply spatial smoothing to the spherical harmonics prior to transformation to grid points. This operation is performed after the truncation specified in ``truncation``. The smoothing filter is of the form: 
		
		.. math::
		  
		  exp^{(-\frac {n(n+1)}{fltc(fltc+1)})^{mfltexp}}
		
		where:
		
		* n: is the wavenumber
		* fltc, mfltexp: see below
		
		This is roughly equivalent to a :math:`\nabla^{2 \times mfltexp}` operator in grid point space.
    :type smoothing: {"yes", "no"}, default: "no"

    :param fltc: Specifies the value of the parameter fltc to be used in the smoothing filter. Only available if ``smoothing`` set to "yes".
    :type fltc: number, default: 19.4

    :param mfltexp: Specifies the value of the parameter ``mfltexp`` to be used in the smoothing filter. Only available if ``smoothing`` is set to "yes". The default value is 2, roughly equivalent to a  :math:`\nabla^{4}` operator in grid point space.
    :type mfltexp: number, default: 2

    :rtype: :class:`Fieldset`


.. mv-minigallery:: divrot

