mvl_regular_layout
====================

.. py:function:: mvl_regular_layout(view, page_columns, page_rows, subpage_columns, subpage_rows, [plot_area])

   Creates a list of :func:`plot_page` objets arranged in a regular grid (defined by ``page_columns`` and ``page_rows``) using the specified ``view``.
   
   :param view: the view that each plot grid cell will contain
   :type view: :class:`Request`
   :param page_columns: number of columns in the grid
   :type page_columns: number
   :param page_rows: number of rows in the grid
   :type page_rows: number
   :param subpage_columns: number of columns within a :func:`plot_page`
   :type subpage_columns: number
   :param subpage_rows: number of rows within a :func:`plot_page`
   :type subpage_rows: number
   :param plot_area: the plot area the layout occupies in the parent :func:`plot_superpage`
   :type plot_area: list
   :rtype: list
   
   On top of the main layout grid, each :func:`plot_page` grid cell contains a set of (one or more) :func:`plot_subpage` objects, each arranged in a regular grid (defined by ``subpage_columns`` and ``subpage_rows``). The output is suitable for input to :func:`plot_superpage`. When ``plot_area`` is specified it defines the plot area the layout will occupy in the output. It is given as a list of [TOP, BOTTOM, LEFT, RIGHT] where the values are specified in percentages (0-100).
   

.. mv-minigallery:: mvl_regular_layout

