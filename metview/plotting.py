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
from metview.style import MapConf
from metview.title import Title

# logging.basicConfig(level=logging.INFO, format="%(levelname)s - %(message)s")
# logging.basicConfig(level=logging.DEBUG, format="%(levelname)s - %(message)s")
LOG = logging.getLogger(__name__)


# ======================================================
# Plot maps with generic contents
# ======================================================

def plot_maps(
    *args, layout=None, view=None, title_font_size=0.4, frame=-1, animate=True
):
    # mv.setoutput("jupyter")
    # dw = Layout().build_grid(page_num=3, view=view)
    # mv.plot(dw)
    # return

    # define the view
    if view is None:
        view = MapConf().view(area="base")

    # print(f"view={view}")

    # in the positional arguments each item defines a plot_page (aka scene)
    plot_def = list(args)
    
    # build the layout
    num_plot = len(plot_def)
    dw = Layout().build_grid(page_num=num_plot, layout=layout, view=view)

    # the plot description
    desc = []

    title = Title(font_size=title_font_size)

    # build each scene
    for i, sc_def in enumerate(plot_def):
        desc.append(dw[i])
        if not isinstance(sc_def, list):
            sc_def = [sc_def]

        data_items = []
        # loop for the parameters
        for item in sc_def:
            if isinstance(item, tuple):
                data, vd = item
            else:
                data = item
                # if isinstance(data, Track):
                if False:
                    tr = data.build()
                    # print("TRACK=", tr)
                    desc.extend(tr)
                    continue
                else:
                    vd = data.visdef()

            data_items.append(data)

            # LOG.debug(f"par={data.param} fields={data.fields}")
            if frame != -1:
                fs = data[frame]
            else:
                fs = data
            LOG.debug(f"data={data} len={len(fs)}")
            LOG.debug("  shortName={}".format(mv.grib_get(fs, ["shortName"])))
            desc.append(fs)
            if vd is not None:
                desc.append(vd)

        # if data_items:
        #     t = title.build(data_items)
        #     LOG.debug(f"t={t}")
        #     desc.append(t)

    LOG.debug(f"desc={desc}")

    if animate and mv.plot.plot_to_jupyter:
        mv.animate(desc)
    else:
        return mv.plot(desc)
