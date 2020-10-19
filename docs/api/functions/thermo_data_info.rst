thermo_data_info
==================

..  py:function:: thermo_data_info(data)

    Convenience function to extract metadata from ``data``. 

    :param data: thermo data object containing vertical profiles
    :type data: thermo data
    :rtype: dict
    
    :func:`thermo_data_info` returns a dict that can be used to e.g. build the title for thermodynamic diagrams. See the Parcel method on Skew-T Example from the Gallery for its usage.