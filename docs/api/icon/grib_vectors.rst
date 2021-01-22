
grib_vectors
=========================

.. container::
    
    .. container:: leftside

        .. image:: /_static/GRIBVECTORS.png
           :width: 48px

    .. container:: rightside

		Combines scalar GRIB fields (:class:`Fieldset`) into vector fields for the purpose of **plotting**\ . The user supplies GRIB data of vector X and Y components (cartesian coordinates) or intensity/direction (polar coordinates) with the option of colouring the vectorial representation (arrows) according to the magnitude of a user supplied scalar quantity. The classic example is to plot a wind field from u/v components coloured according to temperature.


		.. note:: This function performs the same task as the `Grib Vectors <https://confluence.ecmwf.int/display/METV/grib+vectors>`_ icon in Metview’s user interface. It accepts its parameters as keyword arguments, described below.


.. py:function:: grib_vectors(**kwargs)
  
    Combines scalar GRIB fields (:class:`Fieldset`) into vector fields for the purpose of plotting.


    :param type: Specifies the type of the vector field to make. When it is set to "vector_field" the result is defined by ``u_component`` and ``v_component``. Otherwise when the value is "polar_field" the result is defined by ``intensity`` and ``direction``.
    :type type: {"vector_field", "polar_field"}, default: "vector_field"

    :param u_component: Specifies the :class:`Fieldset` to be used as the vector field's x component. Available when ``type`` is "vector_field".
    :type u_component: :class:`Fieldset`

    :param v_component: Specifies the :class:`Fieldset` to be used as the vector field's y component. Available when ``type`` is "vector_field".
    :type v_component: :class:`Fieldset`

    :param intensity: Specifies the :class:`Fieldset` to be used as the vector field's intensity component. Available when ``type`` is "polar_field".
    :type intensity: :class:`Fieldset`

    :param direction: Specifies the :class:`Fieldset` to be used as the vector field's direction component. Available when ``type`` is "polar_field".
    :type direction: :class:`Fieldset`

    :param colouring_field: Specifies the :class:`Fieldset` that the colouring is based on. If not supplied, the computed magnitude of the vector components will be used for colouring.
    :type colouring_field: :class:`Fieldset`

    :rtype: :class:`Request`
.. include:: /gallery/backref/grib_vectors.rst