thermo_data_info
==================

..  py:function:: thermo_data_info(data)

    Convenience function to extract metadata from a thermo data object. 

    :param data: thermo data object containing vertical profiles
    :type data: :func:`thermo_bufr` or :func:`thermo_grib`
    :rtype: dict
    
    :func:`thermo_data_info` returns a dict that can be used to e.g. build the title for thermodynamic diagrams. 

.. mv-minigallery:: thermo_data_info