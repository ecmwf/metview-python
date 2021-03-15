# (C) Copyright 2017- ECMWF.
#
# This software is licensed under the terms of the Apache Licence Version 2.0
# which can be obtained at http://www.apache.org/licenses/LICENSE-2.0.
#
# In applying this licence, ECMWF does not waive the privileges and immunities
# granted to it by virtue of its status as an intergovernmental organisation
# nor does it submit to any jurisdiction.
#

import copy
import datetime
import logging
import os

import pandas as pd
import yaml

import metview as mv
from metview.layout import Layout
from metview.style import StyleDb, MapConf
from metview.title import Title
from metview.track import Track

# logging.basicConfig(level=logging.INFO, format="%(levelname)s - %(message)s")
# logging.basicConfig(level=logging.DEBUG, format="%(levelname)s - %(message)s")
LOG = logging.getLogger(__name__)


# ======================================================
# Plot maps with generic contents
# ======================================================


def plot_maps(
    *args, layout=None, view=None, title_font_size=0.4, frame=-1, animate=True
):
    # define the view
    if view is None:
        view = MapConf().view(area="base")

    # in the positional arguments we have two options:
    # 1. we only have non-list items. They belong to a single plot page.
    # 2. we only have list items. Each list item defines a separate plot page.
    plot_def = list(args)
    lst_cnt = sum([1 for x in plot_def if isinstance(x, list)])
    if not lst_cnt in [0, len(plot_def)]:
        raise Exception(
            f"Invalid plot arguments! Cannot mix list and non-list positional arguments."
        )

    if lst_cnt == 0:
        plot_def = [plot_def]

    # build the layout
    num_plot = len(plot_def)
    dw = Layout().build_grid(page_num=num_plot, layout=layout, view=view)

    # the plot description
    desc = []

    title = Title(font_size=title_font_size)

    # build each scene
    for i, sc_def in enumerate(plot_def):
        desc.append(dw[i])
        # define layers
        layers = []
        data_items = []
        for item in sc_def:
            if isinstance(item, mv.Fieldset):
                layers.append([item])
                data_items.append(item)
            elif isinstance(item, Track):
                tr = item.build()
                layers.append(item)
            elif layers:
                layers[-1].append(item)

        # add data and visdefs to plot definition
        for layer in layers:
            data = layer[0]
            if len(layer) > 1:
                vd = layer[1:]
            else:
                vd = StyleDb.visdef(data)

            if isinstance(data, mv.Fieldset):
                if frame != -1:
                    data = data[frame]

            desc.append(data)
            if vd is not None:
                desc.extend(vd)

        if data_items:
            t = title.build(data_items)
            # LOG.debug(f"t={t}")
            desc.append(t)

    LOG.debug(f"desc={desc}")

    animate = animate and mv.plot.plot_to_jupyter
    return mv.plot(desc, animate=animate)
