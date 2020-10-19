thermo_data_values
====================

..  py:function:: thermo_data_values(data, time_dim_index)

    Convenience function to access profiles from ``data`` for a given ``time_dimension_index``.
    
    :param data: thermo data object containing vertical profiles
    :type data: thermo data
    :param time_dim_index: the (zero-based) index of the selected time dimension from ``data``
    :type time_dim_index: int
    :rtype: dict
    
    See the Parcel method on Skew-T Example from the Gallery for its usage.