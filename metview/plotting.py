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
# logging.basicConfig(level=logging.DEBUG)
LOG = logging.getLogger(__name__)


def extract_plot_def(*args, layout=False):
    # in the positional arguments we have two options:
    # 1. we only have non-list items. They belong to a single plot page.
    # 2. we only have list items. Each list item defines a separate plot page.
    if layout:
        plot_def = list(args)
        lst_cnt = sum([1 for x in plot_def if isinstance(x, list)])
        if not lst_cnt in [0, len(plot_def)]:
            raise Exception(
                f"Invalid plot arguments! Cannot mix list and non-list positional arguments."
            )

        if lst_cnt == 0:
            plot_def = [plot_def]
    else:
        plot_def = [list(args)]

    # plot def at this point a list of lists. Each list item describes a
    # map page item!
    for i in range(len(plot_def)):
        data = None
        layer = []
        for item in plot_def[i]:
            if isinstance(item, mv.Fieldset):
                data = item
                layer.append({"data": data, "vd": []})
            elif data is not None:
                assert len(layer) > 0
                layer[-1]["vd"].append(item)
        plot_def[i] = layer

    return plot_def


def plot_maps(
    *args, layout=None, view=None, title_font_size=0.4, frame=-1, animate=True
):
    """
    Plot maps with generic contents
    """

    # define the view
    if view is None:
        view = MapConf().view(area="base")

    # in the positional arguments we have two options:
    # 1. we only have non-list items. They belong to a single plot page.
    # 2. we only have list items. Each list item defines a separate plot page.
    plot_def = extract_plot_def(*args, layout=True)

    # plot_def = list(args)
    # lst_cnt = sum([1 for x in plot_def if isinstance(x, list)])
    # if not lst_cnt in [0, len(plot_def)]:
    #     raise Exception(
    #         f"Invalid plot arguments! Cannot mix list and non-list positional arguments."
    #     )

    # if lst_cnt == 0:
    #     plot_def = [plot_def]

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
        data_items = []
        for layer in sc_def:
            data = layer["data"]
            vd = layer["vd"]
            if isinstance(data, mv.Fieldset):
                data_items.append(data)
                if frame != -1:
                    data = data[frame]
            if len(vd) == 0:
                vd = StyleDb.visdef(data)

            desc.append(data)
            if vd is not None and all(x is not None for x in vd):
                desc.extend(vd)

        # layers = []
        # data_items = []
        # for item in sc_def:
        #     if isinstance(item, mv.Fieldset):
        #         layers.append([item])
        #         data_items.append(item)
        #     elif isinstance(item, Track):
        #         tr = item.build()
        #         layers.append(item)
        #     elif layers:
        #         layers[-1].append(item)

        # # add data and visdefs to plot definition
        # for layer in layers:
        #     data = layer[0]
        #     if len(layer) > 1:
        #         vd = layer[1:]
        #     else:
        #         vd = StyleDb.visdef(data)

        #     if isinstance(data, mv.Fieldset):
        #         if frame != -1:
        #             data = data[frame]

        #     desc.append(data)
        #     if vd is not None:
        #         desc.extend(vd)

        if data_items:
            t = title.build(data_items)
            # LOG.debug(f"t={t}")
            desc.append(t)

    LOG.debug(f"desc={desc}")

    animate = animate and mv.plot.plot_to_jupyter
    return mv.plot(desc, animate=animate)


def plot_diff_maps(
    *args, layout=None, view=None, title_font_size=0.4, frame=-1, animate=True
):
    """
    Plot difference on maps
    """

    # define the view
    if view is None:
        view = MapConf().view(area="base")

    # build the layout
    dw = Layout().build_diff(view=view)

    # the positional arguments has the follwing order:
    # data1, visdef1.1 visdef1.2 ... data2, visdef2.1, visdef2.2 ...
    # the visdef objects are optional!
    assert len(args) >= 2
    assert isinstance(args[0], mv.Fieldset)
    plot_def = extract_plot_def(*args, layout=False)
    assert len(plot_def) == 1
    plot_def = plot_def[0]
    assert len(plot_def) == 2
    data1 = plot_def[0]["data"]
    data2 = plot_def[1]["data"]
    vd1 = plot_def[0]["vd"]
    vd2 = plot_def[1]["vd"]

    LOG.debug(f"len_1={len(data1)}")
    LOG.debug(f"len_2={len(data2)}")

    # data1 = args[0]
    # data2 = None
    # vd1 = []
    # vd2 = []
    # for i in range(1, len(args)):
    #     if isinstance(args[i], mv.Fieldset):
    #         data2 = args[i]
    #         vd1 = args[1:i]
    #         if len(args) > i+1:
    #             vd2 = args[i+1:]
    #         break

    # assert data2 is not None
    # assert all([False for x in vd1 if isinstance(x, mv.Fieldset)])
    # assert all([False for x in vd2 if isinstance(x, mv.Fieldset)])
    if len(vd1) == 0:
        vd1 = StyleDb.get_db().visdef(data1)
    if len(vd2) == 0:
        vd2 = StyleDb.get_db().visdef(data2)

    # the plot description
    desc = []

    title = Title(font_size=title_font_size)

    # compute diff
    data = data1 - data2
    data._param_info = data1.param_info

    # generate diff plot
    desc.append(dw[0])
    if frame != -1:
        data = data[frame]
    # LOG.debug(data)
    # LOG.debug(mv.grib_get(data, ["shortName"]))
    vd = StyleDb.get_db(name="diff").visdef(data)
    desc.append(data)
    desc.append(vd)
    t = title.build(data)
    desc.append(t)

    # generate plot for data1
    desc.append(dw[1])
    if frame != -1:
        data1 = data1.fields[frame]
    # LOG.debug(fs)
    desc.append(data1)
    desc.append(vd1)
    t = title.build(data1)
    desc.append(t)

    # generate plot for data2
    desc.append(dw[2])
    if frame != -1:
        data2 = data2.fields[frame]
    # LOG.debug(fs)
    desc.append(data2)
    desc.append(vd2)
    t = title.build(data2)
    desc.append(t)

    LOG.debug(f"desc={desc}")

    animate = animate and mv.plot.plot_to_jupyter
    animate = False
    return mv.plot(desc, animate=animate)


def plot_xs(
    *args,
    map_data=None,
    line=[],
    layout="",
    view=None,
    title_font_size=0.4,
    frame=-1,
    animate=True,
):
    """
    Plot cross section with map
    """

    assert len(line) == 4

    if view is None:
        view = MapConf().view(area="base")

    assert len(args) >= 1
    assert isinstance(args[0], mv.Fieldset)
    plot_def = extract_plot_def(*args, layout=False)
    assert len(plot_def) == 1
    assert len(plot_def[0]) > 0

    # if not isinstance(plot_def, list):
    #     plot_def = [plot_def]

    # build the layout
    # num_plot = len(plot_def)
    dw = Layout().build_xs(line=line, map_view=view)

    # ts = nil

    # the plot description
    desc = []

    title = Title(font_size=title_font_size)

    # build cross section plot
    desc.append(dw[0])
    for pd_item in plot_def[0]:
        data = pd_item["data"]
        vd = pd_item["vd"]
        # desc.append(dw[i])
        # LOG.debug("i={} {}".format(i, sc_def))
        # LOG.debug(f"desc={desc}")
        # if not isinstance(sc_def, list):
        #     sc_def = [sc_def]

        if len(vd) == 0:
            vd = StyleDb.get_db().visdef(data, plot_type="xs")

        # for item in sc_def:
        # if isinstance(item, tuple):
        #     data, vd = item
        # else:
        #     data = item
        #     vd = data.visdef(plot_type="xs")
        param = data.param_info
        LOG.debug(f"param={param}")

        if param is not None and param.name == "wind3d":
            xs_d = mv.mcross_sect(
                data=data,
                line=line,
                wind_parallel="on",
                w_wind_scaling_factor_mode="compute",
                w_wind_scaling_factor="100",
                # bottom_level=1015,
                # top_level=250,
                # vertical_scaling = "log",
                # vertical_axis= vertical_axis
            )
            desc.append(xs_d)
        else:
            # if frame != -1:
            #     fs = data.fields[frame]
            # else:
            #     fs = data.fields[0]
            # fs = data.fieldset

            if param is not None:
                if param.name == "t":
                    data = data - 273.16
                elif param.name == "pv":
                    data = data * 1e6
                elif param.name == "q":
                    data = data * 1e3
                elif param.name in ["vo", "absv"]:
                    data = data * 1e5
            desc.append(data)

        if vd is not None and all(x is not None for x in vd):
            desc.extend(vd)

            # t = title.build_fc(dv.conf.conf)
            # desc.append(t)

    LOG.debug(f"desc={desc}")

    # build side map plot
    desc.append(dw[1])

    t = None
    if map_data is not None and len(map_data) > 0:
        plot_def = extract_plot_def(map_data, layout=False)
        assert len(plot_def) <= 1
        if len(plot_def) == 1:
            data_items = []
            for pd_item in plot_def[0]:
                data = pd_item["data"]
                vd = pd_item["vd"]
                if len(vd) == 0:
                    vd = StyleDb.get_db().visdef(data)

                if isinstance(data, mv.Fieldset):
                    data_items.append(data)
                    if frame != -1:
                        data = data[frame]

                desc.append(data)
                if vd is not None and all(x is not None for x in vd):
                    desc.extend(vd)

            if data_items:
                t = title.build(data_items)

    # define xsection line graph
    graph = mv.mgraph(
        graph_line_colour="red", graph_line_thickness=3, graph_symbol="off"
    )

    lv = mv.input_visualiser(
        input_plot_type="geo_points",
        input_longitude_values=[line[1], line[3]],
        input_latitude_values=[line[0], line[2]],
    )

    desc.extend([lv, graph])

    if t is not None:
        desc.append(t)

    LOG.debug(f"desc={desc}")
    animate = animate and mv.plot.plot_to_jupyter
    return mv.plot(desc, animate=animate)
