Metview in Jupyter
===================

Metview fits perfectly well into a Jupyter notebook environment! Just make sure that everything is
installed (see :doc:`installation guide<install>`), fire up a notebook, import metview and you're
ready to go! See the :doc:`notebook gallery <notebook_gallery>` for examples.

If you wish to view a plot inline in the notebook, you will need to call

   .. code-block:: python

      mv.setoutput("jupyter")

before you call the :py:func:`plot` command. As this will generate PNG images in the background,
you can add the parameters for the :py:func:`png_output` function here too, e.g.

   .. code-block:: python

      mv.setoutput("jupyter", output_width=1200)

As an added bonus, if you are plotting :py:class:`Fieldset` s that contain multiple fields,
you can add `animate=True` to the arguments to the :py:func:`plot` command. This will produce
a widget that allows you to scroll and animate through the different fields. You need to make
sure that your environment has the necessary jupyter and ipywidgets packages installed for
this to work!