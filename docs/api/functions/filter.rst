filter
=========

..  py:function:: filter(gpt, cond)

    Returns a subset of ``gpt`` according to the filter conditions defined in ``cond``. 

    :param gpt: input geopoints
    :type gpt: :class:`Geopoints`
    :param cond: filter conditions
    :type cond: number or datetime.datetime or list or ndarray or :class:`Geopoints`
    :rtype: :class:`Geopoints`

    The actual filtering is based on the type of ``cond``:

    * if ``cond`` is a :class:`Geopoints` it must have the same number of values as ``gpt``. The result will contain the  values of ``gpt`` where the value of ``cond`` is non-zero. It is usually combined with the comparison operators.

        :Example:

            This code shows how to filter the negative values in a :class:`Geopoints` containing temperature in K.

            .. code-block:: python

                import metview as mv

                t = mv.read("temp.gpt")
                freeze = mv.filter(t,t < 273.16)

    * if ``cond`` is an **ndarray** it must have the same number of values as ``gpt``. The result will contain the  values of ``gpt`` where the value of ``cond`` is non-zero. It is usually combined with the comparison operators.

        :Example:
            .. code-block:: python

                import metview as mv

                gpt = mv.read("my_date.gpt")

                # "gpt["precip"] > 5" returns a vector of 1s and 0s
                new_gpt = mv.filter(gpt, gpt["precip"] > 5) 

    * if ``cond`` is **number** or **list** of numbers in the format of **[min_level, max_level]** it defines a filter on the level column of ``gpt``.  The result will contain the values of ``gpt`` where the level equals to ``cond`` (if it is  a number) or in the interval specified by ``cond`` (if it is a list). 

    * if ``cond`` is **datetime.datetime** or **list** of it in the format of **[min_date, max_date]** it defines a filter on the date column of ``gpt``.  The result will contain the values of ``gpt`` where the date equals to ``cond`` (if it is a datetime.datetime) or in the interval specified by ``cond`` (if it is a list). 

    * if ``cond`` is a **list**  in the format of **[North, West, South, East]** format it defines a filter with a geographical area.  The result will contain the values of ``gpt`` where the locations are within ``cond``.

.. mv-minigallery:: filter
