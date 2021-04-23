to_dataframe
***************

.. py:function:: to_dataframe()
.. py:function:: Geopoints.to_dataframe()
   :noindex:

   Converts a :class:`Geopoints` into a Pandas dataframe.

   :rtype: Pandas dataframe


   :Example:
      
    .. code-block:: python

        import metview as mv
        
        gpt = mv.read("gpts.gpt") # returns a Geopoints
        df = gpt.to_dataframe()   # returns a Pandas Dataframe
        print(df.head())


.. mv-minigallery:: to_dataframe
