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
from metview.style import Style, StyleDb, MapConf, GeoView
from metview.title import Title
from metview.track import Track

# logging.basicConfig(level=logging.INFO, format="%(levelname)s - %(message)s")
# logging.basicConfig(level=logging.DEBUG, format="%(levelname)s - %(message)s")
# logging.basicConfig(level=logging.DEBUG)
LOG = logging.getLogger(__name__)


def _make_layers(*args, form_layout=False):
    # in the positional arguments we have two options:
    # 1. we only have non-list items. They belong to a single plot page.
    # 2. we only have list items. Each list item defines a separate plot page.
    plot_def = []
    if form_layout:
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
    layers = []
    for d in plot_def:
        data = None
        layer = []
        for item in d:
            if isinstance(item, (mv.Fieldset, Track)):
                data = item
                layer.append({"data": data, "vd": []})
            elif data is not None:
                assert len(layer) > 0
                layer[-1]["vd"].append(item)
        layers.append(layer)

    if form_layout:
        return layers
    else:
        return layers[0] if layers else []


def _make_visdef(data, vd, style_db="param", plot_type="map"):
    if isinstance(data, mv.Fieldset):
        if len(vd) == 0:
            vd = StyleDb.get_db(name=style_db).visdef(data, plot_type=plot_type)
        else:
            for i, v in enumerate(vd):
                if isinstance(v, Style):
                    vd[i] = v.to_request()

        vd = [x for x in vd if x is not None]
        return vd
    else:
        return []

def _make_view(view):
    if view is None:
        view = MapConf().view(area="base").to_request()
    elif isinstance(view, GeoView):
        view = view.to_request()
    return view

def plot_maps(
    *args, layout=None, view=None, title_font_size=None, legend_font_size=None, frame=-1, animate=True
):
    """
    Plot maps with generic contents
    """

    title_font_size = 0.4 if title_font_size is None else title_font_size
    legend_font_size = 0.35 if legend_font_size is None else legend_font_size

    # define the view
    view = _make_view(view)

    # in the positional arguments we have two options:
    # 1. we only have non-list items. They belong to a single plot page.
    # 2. we only have list items. Each list item defines a separate plot page.
    plot_def = _make_layers(*args, form_layout=True)

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

            if isinstance(data, Track):
                data = data.build(style=vd)
                
            desc.append(data)
            vd = _make_visdef(data, vd, style_db="param", plot_type="map")
            if vd:
                desc.extend(vd) 

            # if not isinstance(data, Track):
            #     if len(vd) == 0:
            #         vd = StyleDb.get_db().visdef(data)
            #     for i, v in enumerate(vd):
            #         if isinstance(v, Style):
            #             vd[i] = v.to_request()
            #     if vd is not None and all(x is not None for x in vd):
            #         desc.extend(vd)

        if data_items:
            legend = mv.mlegend(legend_text_font_size=legend_font_size)
            desc.append(legend)
            t = title.build(data_items)
            # LOG.debug(f"t={t}")
            desc.append(t)

    LOG.debug(f"desc={desc}")

    animate = animate and mv.plot.plot_to_jupyter
    return mv.plot(desc, animate=animate)


def plot_diff_maps(
    *args, layout=None, view=None, overlay=None, title_font_size=None, legend_font_size=None, frame=-1, animate=True
):
    """
    Plot difference maps
    """

    # handle default arguments
    title_font_size = 0.4 if title_font_size is None else title_font_size
    legend_font_size = 0.35 if legend_font_size is None else legend_font_size
   
    # define the view
    view = _make_view(view)
    
    # build the layout
    dw = Layout().build_diff(view=view)

    data = {}
    vd = {}

    # the positional arguments has the following order:
    # data1, visdef1.1 visdef1.2 ... data2, visdef2.1, visdef2.2 ...
    # the visdef objects are optional!
    assert len(args) >= 2
    assert isinstance(args[0], mv.Fieldset)
    layers = _make_layers(*args, form_layout=False)
    assert len(layers) == 2
    # LOG.debug(f"layers={layers}")
    data["0"] = layers[0]["data"]
    data["1"] = layers[1]["data"]
    vd["0"] = _make_visdef(data["0"], layers[0]["vd"])
    vd["1"] = _make_visdef(data["1"], layers[1]["vd"])

    # overlay data
    ov_data = {}
    ov_vd = {}
    if overlay is not None:
        # single value, list or tuple: a data item that will be plotted into each map
        if not isinstance(overlay, dict):
            if isinstance(overlay, tuple):
                ov_args = list(overlay)
            else:
                ov_args = [overlay] if not isinstance(overlay, list) else overlay
            print(ov_args)
            ov_layers = _make_layers(*ov_args, form_layout=False) 
            print(ov_layers)
            assert len(ov_layers) == 1
            d = ov_layers[0]["data"]
            if isinstance(d, Track):
                d = d.build(style=ov_layers[0]["vd"])                
            for k in ["d", "0", "1"]:
                ov_data[k] = d
                ov_vd[k] = _make_visdef(d, ov_layers[0]["vd"])
        else:
            pass

    # LOG.debug("len_0={}".format(len(data["0"])))
    # LOG.debug("len_1={}".format(len(data["0"])))

    # the plot description
    desc = []

    title = Title(font_size=title_font_size)

    # compute diff
    data["d"] = data["0"] - data["1"]
    data["d"]._param_info = data["1"].param_info
    vd["d"] = _make_visdef(data["d"], [], plot_type="diff")

    # LOG.debug("len_d={}".format(len(data["d"])))

    for i, k in enumerate(["d", "0", "1"]):
        desc.append(dw[i])
        d = data[k] if frame == -1 else data[k][frame]
        desc.append(d)
        if vd[k]:
            desc.append(vd[k])

        # add overlay
        if k in ov_data:
            if isinstance(ov_data[k], mv.Fieldset):
                dd = ov_data[k] if frame == -1 else ov_data[k][frame]
            else:
                dd = ov_data[k]
            desc.append(dd)    
            if k in ov_vd and ov_vd[k]:
               desc.append(ov_vd[k]) 

        t = title.build(d)
        legend = mv.mlegend(legend_text_font_size=legend_font_size)
        desc.append(legend)
        desc.append(t)

    LOG.debug(f"desc={desc}")

    animate = animate and mv.plot.plot_to_jupyter
    return mv.plot(desc, animate=animate)


def plot_xs(
    *args,
    map_data=None,
    line=[],
    layout="",
    view=None,
    title_font_size=None,
    legend_font_size=None,
    frame=-1,
    animate=True,
):
    """
    Plot cross section with map
    """

    title_font_size = 0.4 if title_font_size is None else title_font_size
    legend_font_size = 0.35 if legend_font_size is None else legend_font_size

    assert len(line) == 4

    view = _make_view(view)
    
    assert len(args) >= 1
    assert isinstance(args[0], mv.Fieldset)
    layers = _make_layers(*args, form_layout=False)
    assert len(layers) > 0

    # build the layout
    dw = Layout().build_xs(line=line, map_view=view)

    # the plot description
    desc = []

    title = Title(font_size=title_font_size)

    # build cross section plot
    desc.append(dw[0])
    for layer in layers:
        data = layer["data"]
        vd = _make_visdef(data, layer["vd"], plot_type="xs")
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

        if vd:
            desc.extend(vd)

        # t = title.build_fc(dv.conf.conf)
        # desc.append(t)

    # LOG.debug(f"desc={desc}")

    # build side map plot
    desc.append(dw[1])

    t = None
    if map_data is not None and len(map_data) > 0:
        layers = _make_layers(map_data, form_layout=False)
        data_items = []
        for layer in layers:
            data = layer["data"]
            vd = _make_visdef(data, layer["vd"])

            if isinstance(data, mv.Fieldset):
                data_items.append(data)
                if frame != -1:
                    data = data[frame]

            desc.append(data)
            if vd:
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


# plot_stamp_maps(fs, vd, an=[], fc=[], )


def plot_stamp(
    *args,
    an=[],
    fc=[],
    layout=None,
    view=None,
    title_font_size=0.4,
    frame=-1,
    animate=True,
    diff_base=None
):
    """
    Plot ENS stamp maps
    """
    
    # define the view
    view = _make_view(view)

    desc = []
    data = {}
    vd = {}

    if diff_base is not None:
        assert isinstance(diff_base, mv.Fieldset)

    if len(args) > 0:
        assert isinstance(args[0], mv.Fieldset)
        layers = _make_layers(*args, form_layout=False)
        assert len(layers) == 1

        # prepare ens
        data["ens"] = layers[0]["data"]
        assert data["ens"] is not None
        if diff_base is not None:
            vd["ens"] = _make_visdef(data["ens"], [], style_db="diff")    
        else:
            vd["ens"] = _make_visdef(data["ens"], layers[0]["vd"])

    # prepare an and fc
    d = {"an": an, "fc": fc}
    for k, v in d.items():
        if v:
            layers = _make_layers(v, form_layout=False)
            if layers:
                data[k] = layers[0]["data"]
                vd[k] = layers[0]["vd"]
                if diff_base is not None:
                    vd[k] = vd["ens"]     
                else:
                    if len(vd[k]) == 0 and "ens" in vd:
                        vd[k] = vd["ens"]
                    else:
                        vd[k] = _make_visdef(data[k], vd[k])

    # determine ens number
    members = []
    if "ens" in data:
        members = data["ens"].unique("number")
        LOG.debug(f"members={members}")
        if len(members) == 0:
            raise Exceception("No ENS data found in input!")

    # determine number of maps
    num = len(members) + sum([1 for x in ["an", "fc"] if x in data])

    # build the layout
    dw = Layout().build_stamp(num, layout=layout, view=view)

    if len(dw) < num + 1:
        raise Exception(f"Layout has less maps (={len(dw)}) than expected (={num})")

    title = Title(font_size=title_font_size)

    # ens members
    for i, m in enumerate(members):
        desc.append(dw[i])
        d = data["ens"].select(number=m)
        if diff_base is not None:
            d = d - diff_base
        desc.append(d)

        if vd["ens"]:
            desc.extend(vd["ens"])

        t = title.build_stamp(d, member=str(i))
        desc.append(t)

    # add an and fc
    n = len(members)
    for t in ["an", "fc"]:
        if t in data:
            desc.append(dw[n])
            d = data[t]
            if diff_base is not None:
                d = d - diff_base
            desc.append(d)
            if vd[t]:
                desc.append(vd[t])
            t = title.build_stamp(data[t], member="")
            desc.append(t)
            n += 1

    for i in range(n, len(dw)):
        desc.append(dw[i])

    if len(members) > 0 and "ens" in data:
        cont = mv.mcont(contour="off", contour_label="off")
        dummy = d = data["ens"].select(number=members[0])
        t = title.build(dummy)
        desc.extend([dw[-1], t, dummy, cont])

    animate = animate and mv.plot.plot_to_jupyter
    return mv.plot(desc, animate=animate)
