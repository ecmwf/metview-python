
spec_graph
=========================

.. container::
    
    .. container:: leftside

        .. image:: /_static/SPECTRA.png
           :width: 48px

    .. container:: rightside

		Defines the visualisation of the spectrum as a function of Legendre polynomial order from spectral (spherical harmonics) GRIB data. Only the first field in a :class:`Fieldset` is used.


		.. note:: This function performs the same task as the `Spectra <https://confluence.ecmwf.int/display/METV/Spectra>`_ icon in Metview’s user interface. It accepts its parameters as keyword arguments, described below.


.. py:function:: spec_graph(**kwargs)
  
    Defines visualisation for the spectrum of the first field in the input spectral GRIB data.


    :param data: Specifies the spectral (spherical harmonics) GRIB data.
    :type data: :class:`Fieldset`

    :param truncation: specifies the highest wave number in spectra plots.
    :type truncation: number, default: 216

    :rtype: :class:`Request`


.. minigallery:: metview.spec_graph
    :add-heading:

