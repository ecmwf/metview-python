# (C) Copyright 2017- ECMWF.
#
# This software is licensed under the terms of the Apache Licence Version 2.0
# which can be obtained at http://www.apache.org/licenses/LICENSE-2.0.
#
# In applying this licence, ECMWF does not waive the privileges and immunities
# granted to it by virtue of its status as an intergovernmental organisation
# nor does it submit to any jurisdiction.
#


import logging
import math

import numpy as np
import pandas as pd

import metview as mv
from metview.layout import Layout
from metview.style import Visdef, Style, GeoView
from metview.title import Title
from metview.track import Track
from metview.scaling import Scaling

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


def _make_visdef(
    data,
    vd,
    use_eccharts=False,
    style_db="param",
    plot_type="map",
    data_id=None,
    pos_values=None,
):
    if isinstance(data, mv.Fieldset):
        if len(vd) == 0:
            if use_eccharts:
                return [mv.style.make_eccharts_mcont()]
            else:
                vd = mv.style.get_db(name=style_db).visdef(
                    data, plot_type=plot_type, data_id=data_id
                )
                if plot_type == "diff" and pos_values is not None and pos_values:
                    s = mv.style.get_db(name=style_db).style(
                        data, plot_type=plot_type, data_id=data_id
                    )
                    if s is not None and len(s.visdefs) == 2:
                        neg_values = [-x for x in reversed(pos_values)]
                        s.visdefs[0].set_values_list(neg_values)
                        s.visdefs[1].set_values_list(pos_values)
                        vd = s.to_request()
                else:
                    vd = mv.style.get_db(name=style_db).visdef(
                        data, plot_type=plot_type, data_id=data_id
                    )
        else:
            for i, v in enumerate(vd):
                if isinstance(v, Style):
                    v = v.set_data_id(data_id)
                    vd[i] = v.to_request()
                elif (
                    isinstance(v, mv.Request) and data_id is not None and data_id != ""
                ):
                    v = Visdef.from_request(v)
                    v.set_data_id(data_id)
                    vd[i] = v.to_request()
        if vd is not None:
            return [x for x in vd if x is not None]
        else:
            return []
    else:
        return []


def _get_data_area(data):
    bb = []
    for d in data:
        b = d.bounding_box()
        if len(b) == 4:
            if math.fabs(b[1] - b[0]) > 160:
                b[0] = -90
                b[2] = 90
            if math.fabs(b[3] - b[1]) > 340:
                b[1] = -180
                b[3] = 180
        if len(bb) == 0:
            bb = b.tolist()
        else:
            bb = [
                min(b[0], bb[0]),
                min(b[1], bb[1]),
                max(b[2], bb[2]),
                max(b[3], bb[3]),
            ]
    return bb


def _make_view(view, area, plot_type="map", data=None):
    data = [] if data is None else data

    if area == "data" and data:
        area = _get_data_area(data)
        if len(area) != 4:
            area = "base"

    if view is not None:
        if area is not None:
            view = mv.make_geoview(area=area, style=view["coastlines"])
    else:
        if area is not None:
            view = mv.make_geoview(area=area, plot_type=plot_type)
        else:
            view = mv.make_geoview(area="base", plot_type=plot_type)
    return view


def _prepare_grid(d1, d2):
    if d1._db is not None and d2._db is not None:
        # interpolate from d2 to d1
        if d1._db.name in d2._db.regrid_from:
            # print(f"regrid: {d1.label} -> {d2.label}")
            # d11 = d1 + 0
            d = mv.regrid(data=d1, grid_definition_mode="template", template_data=d2[0])
            d = mv.grib_set_long(d, ["generatingProcessIdentifier", 148])
            d._db = d1._db._clone()
            # print(f"{ len(d)}")
            # print(f"{ len(d2)}")
            # print(" {}".format(mv.grib_get(d[0], ["numberOfDataPoints"])))
            # print(" {}".format(mv.grib_get(d2[0], ["numberOfDataPoints"])))
            return (d, d2)
        # interpolate from d1 to d2
        elif d2._db.name in d1._db.regrid_from:
            # print(f"regrid: {d2.label} -> {d1.label}")
            # d22 = d2 + 0
            d = mv.regrid(data=d2, grid_definition_mode="template", template_data=d1[0])
            d = mv.grib_set_long(d, ["generatingProcessIdentifier", 148])
            d._db = d2._db._clone()
            return (d1, d)

    return (d1, d2)


def _y_max(data):
    return max([max(d) for d in data])


def _y_min(data):
    return min([min(d) for d in data])


def plot_maps(
    *args,
    layout=None,
    view=None,
    area=None,
    use_eccharts=False,
    title_font_size=0.4,
    legend_font_size=0.35,
    frame=-1,
    animate="auto",
):
    """
    Plot maps with generic contents
    """

    # in the positional arguments we have two options:
    # 1. we only have non-list items. They belong to a single plot page.
    # 2. we only have list items. Each list item defines a separate plot page.
    plot_def = _make_layers(*args, form_layout=True)

    # collect the data items
    data_items = []
    for i, sc_def in enumerate(plot_def):
        for layer in sc_def:
            data = layer["data"]
            if isinstance(data, mv.Fieldset):
                data_items.append(data[0])

    # define the view
    view = _make_view(view, area, data=data_items)

    # build the layout
    num_plot = len(plot_def)
    dw = Layout().build_grid(page_num=num_plot, layout=layout, view=view)

    # the plot description
    desc = []

    title = Title(font_size=title_font_size)

    # build each scene
    data_id = ("d0", 0)
    for i, sc_def in enumerate(plot_def):
        desc.append(dw[i])
        # define layers
        data_items = []
        use_data_id = (
            sum([1 for layer in sc_def if isinstance(layer["data"], mv.Fieldset)]) > 1
        )
        for layer in sc_def:
            data = layer["data"]
            vd = layer["vd"]
            if isinstance(data, mv.Fieldset):
                if use_data_id:
                    data_items.append((data, data_id[0]))
                else:
                    data_items.append(data)
                if frame != -1:
                    if data.ds_param_info.scalar:
                        data = data[frame]
                    else:
                        data = data[2 * frame : 2 * frame + 2]
            elif isinstance(data, Track):
                data = data.build(style=vd)

            desc.append(data)

            if isinstance(data, mv.Fieldset):
                vd = _make_visdef(
                    data,
                    vd,
                    use_eccharts=use_eccharts,
                    style_db="param",
                    plot_type="map",
                    data_id=data_id[0] if use_data_id else None,
                )
                if vd:
                    desc.extend(vd)

            data_id = (f"d{data_id[1]+1}", data_id[1] + 1)

        if data_items:
            legend = mv.mlegend(legend_text_font_size=legend_font_size)
            desc.append(legend)
            t = title.build(data_items)
            # LOG.debug(f"t={t}")
            desc.append(t)

    for i in range(len(plot_def), len(dw)):
        desc.append(dw[i])

    LOG.debug(f"desc={desc}")

    return mv.plot(desc, animate=animate)


def plot_diff_maps(
    *args,
    view=None,
    area=None,
    overlay=None,
    diff_style=None,
    pos_values=None,
    title_font_size=0.4,
    legend_font_size=0.35,
    frame=-1,
    animate="auto",
):
    """
    Plot difference maps
    """

    # handle default arguments
    pos_values = [] if pos_values is None else pos_values
    diff_style = [] if diff_style is None else diff_style
    if not isinstance(diff_style, list):
        diff_style = [diff_style]

    # define the view
    view = _make_view(view, area, plot_type="diff")

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
            # print(ov_args)
            ov_layers = _make_layers(*ov_args, form_layout=False)
            # print(ov_layers)
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
    data["0"], data["1"] = _prepare_grid(data["0"], data["1"])
    data["d"] = data["0"] - data["1"]

    data["d"]._ds_param_info = data["1"].ds_param_info
    if data["0"].label and data["1"].label:
        data["d"]._label = "{}-{}".format(data["0"].label, data["1"].label)
    else:
        data["d"]._label = ""
    vd["d"] = _make_visdef(
        data["d"], diff_style, plot_type="diff", pos_values=pos_values
    )

    # LOG.debug("len_d={}".format(len(data["d"])))

    for i, k in enumerate(["d", "0", "1"]):
        desc.append(dw[i])
        if frame == -1:
            d = data[k]
        else:
            d = data[k][frame]
            d._ds_param_info = data[k]._ds_param_info
            d._label = data[k]._label

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

        t = title.build(data[k])
        legend = mv.mlegend(legend_text_font_size=legend_font_size)
        desc.append(legend)
        desc.append(t)

    # print(desc)
    return mv.plot(desc, animate=animate)


def plot_xs(
    *args,
    map_line=True,
    map_data=None,
    line=[],
    layout="",
    view=None,
    area=None,
    title_font_size=0.3,
    legend_font_size=0.2,
    frame=-1,
    animate="auto",
):
    """
    Plot cross section with map
    """

    assert len(line) == 4
    assert len(args) >= 1
    assert isinstance(args[0], mv.Fieldset)
    layers = _make_layers(*args, form_layout=False)
    assert len(layers) > 0

    # build the layout - if no map_data is specified no map view is
    # added to the layout
    if not map_line and map_data is None:
        view = None
    else:
        view = _make_view(view, area)
    dw = Layout().build_xs(line=line, map_view=view)

    # the plot description
    desc = []

    title = Title(font_size=title_font_size)
    data_items = []

    # build cross section plot
    desc.append(dw[0])
    for layer in layers:
        data = layer["data"]
        vd = _make_visdef(data, layer["vd"], plot_type="xs")
        param_info = data.ds_param_info
        # print(f"param_info={param_info}")
        data_items.append(data)
        # print(f"data={len(data)}")
        if param_info is not None and param_info.name == "wind3d":
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
            if param_info is not None:
                if param_info.name == "t":
                    data = data - 273.16
                elif param_info.name == "pv":
                    data = data * 1e6
                elif param_info.name == "q":
                    data = data * 1e3
                elif param_info.name in ["vo", "absv"]:
                    data = data * 1e5
            desc.append(data)

        if vd:
            desc.extend(vd)
            # print(f"vd={vd}")

    t = title.build_xs(data_items)
    desc.append(t)

    # LOG.debug(f"desc={desc}")

    # build side map plot
    if map_line or map_data is not None:
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

        if map_line:
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
    return mv.plot(desc, animate=animate)


def plot_stamp(
    *args,
    an=[],
    fc=[],
    layout=None,
    view=None,
    area=None,
    title_font_size=0.4,
    frame=-1,
    animate="auto",
    diff_base=None,
):
    """
    Plot ENS stamp maps
    """

    # define the view
    view = _make_view(view, area)

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
        members = data["ens"]._unique_metadata("number")
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

    return mv.plot(desc, animate=animate)


def plot_rmse(*args, ref=None, area=None, title_font_size=0.4, y_max=None):
    """
    Plot RMSE curve
    """

    desc = []

    if not isinstance(ref, mv.Fieldset):
        raise Exception(f"Missing or invalid ref argument!")

    layers = _make_layers(*args, form_layout=False)

    # compute the rmse for each input layer
    data = []  # list of tuples
    rmse_data = []
    title_data = []
    has_ef = False

    for layer in layers:
        if isinstance(layer["data"], mv.Fieldset):
            # determine ens number
            members = layer["data"]._unique_metadata("number")
            # print(f"members={members}")
            # ens forecast
            if len(members) > 1:
                if has_ef:
                    raise Exception("Only one ENS fieldset can be used in plot_rmse()!")
                has_ef = True
                em_d = None  # ens mean
                for m in members:
                    pf_d = layer["data"].select(number=m)
                    ref_d, pf_d = _prepare_grid(ref, pf_d)
                    data.append(("cf" if m == "0" else "pf", layer["data"]))
                    rmse_data.append(mv.sqrt(mv.average((pf_d - ref_d) ** 2)))
                    em_d = pf_d if em_d is None else em_d + pf_d

                # compute rmse for ens mean
                data.append(("em", layer["data"]))
                rmse_data.append(
                    mv.sqrt(mv.average((em_d / len(members) - ref_d) ** 2))
                )

            # deterministic forecast
            else:
                ref_d, dd = _prepare_grid(ref, layer["data"])
                data.append(("fc", layer["data"]))
                rmse_data.append(mv.sqrt(mv.average((dd - ref_d) ** 2)))

            title_data.append(layer["data"])

    # define x axis params
    dates = ref.valid_date()
    x_min = dates[0]
    x_max = dates[-1]
    x_tick = 1
    x_title = ""

    # define y axis params
    y_min = 0
    if y_max is None:
        y_tick, _, y_max = Layout.compute_axis_range(0, _y_max(rmse_data))
    else:
        y_tick, _, _ = Layout.compute_axis_range(0, y_max)
    y_title = "RMSE [" + mv.grib_get_string(ref[0], "units") + "]"

    # print(f"y_tick={y_tick} y_max={y_max}")

    # define the view
    view = Layout().build_rmse(
        x_min, x_max, y_min, y_max, x_tick, y_tick, x_title, y_title
    )
    desc.append(view)

    # define curves
    ef_label = {"cf": "ENS cf", "pf": "ENS pf", "em": "ENS mean"}
    ef_colour = {"cf": "black", "pf": "red", "em": "kelly_green"}
    fc_colour = ["red", "blue", "green", "black", "cyan", "evergreen", "gold", "pink"]
    if has_ef:
        fc_colour = [x for x in fc_colour if x not in list(ef_colour.values())]

    pf_label_added = False
    colour_idx = -1
    legend_item_count = 0
    for i, d in enumerate(rmse_data):
        vis = mv.input_visualiser(
            input_x_type="date", input_date_x_values=dates, input_y_values=d
        )

        vd = {"graph_type": "curve"}
        line_colour = "black"
        line_width = 1

        if data[i][0] == "fc":
            line_width = 3
            colour_idx = (colour_idx + 1) % len(fc_colour)
            line_colour = fc_colour[colour_idx]
            # print(f"label={data[i][1][0].label}")
            vd["legend_user_text"] = data[i][1].label
            vd["legend"] = "on"
            legend_item_count += 1
        elif data[i][0] == "pf":
            line_width = 1
            line_colour = ef_colour["pf"]
            if not pf_label_added:
                pf_label_added = True
                vd["legend_user_text"] = ef_label.get("pf", "")
                vd["legend"] = "on"
                legend_item_count += 1
        elif data[i][0] in ["cf", "em"]:
            line_width = 3
            line_colour = ef_colour[data[i][0]]
            vd["legend_user_text"] = ef_label.get(data[i][0], "")
            vd["legend"] = "on"
            legend_item_count += 1

        vd["graph_line_colour"] = line_colour
        vd["graph_line_thickness"] = line_width

        desc.append(vis)
        desc.append(mv.mgraph(**vd))

    # add title
    title = Title(font_size=title_font_size)
    t = title.build_rmse(ref, title_data)
    if t is not None:
        desc.append(t)

    # add legend
    leg_left = 3.5
    # legY = 14
    leg_height = legend_item_count * (0.35 + 0.5) + (legend_item_count + 1) * 0.1
    leg_bottom = 17.5 - leg_height

    # Legend
    legend = mv.mlegend(
        legend_display_type="disjoint",
        legend_entry_plot_direction="column",  # "row",
        legend_text_composition="user_text_only",
        legend_border="on",
        legend_border_colour="black",
        legend_box_mode="positional",
        legend_box_x_position=leg_left,
        legend_box_y_position=leg_bottom,
        legend_box_x_length=4,
        legend_box_y_length=leg_height,
        legend_text_font_size=0.35,
        legend_box_blanking="on",
    )
    desc.append(legend)

    mv.plot(desc, animate=False)


def plot_cdf(*args, location=None, title_font_size=0.4, x_range=None):
    """
    Plot CDF curve
    """

    # check x range
    x_range = [] if x_range is None else x_range
    if x_range and len(x_range) not in [2, 3]:
        raise Exception(
            f"plot_cdf: invalid x_range specified. Format [x_min, x_max, [x_tick]]"
        )
    if len(x_range) == 2 and x_range[1] <= x_range[0]:
        raise Exception(
            f"plot_cdf: invalid x_range specified. x_min={x_range[0]} >= x_max={x_range[1]}"
        )

    layers = _make_layers(*args, form_layout=False)

    desc = []
    cdf_data = []
    cdf_label = []
    title_data = []
    y_values = np.arange(0, 101)
    plot_units = ""
    units_scaler = None

    # compute the cdf for each input layer
    for layer in layers:
        if isinstance(layer["data"], mv.Fieldset):
            # we assume each field has the same units and paramId
            if plot_units == "":
                meta = mv.grib_get(layer["data"][0], ["units", "paramId"])
                if meta and len(meta[0]) == 2:
                    meta = {"units": meta[0][0], "paramId": meta[0][1]}
                    units_scaler = Scaling.find_item(meta)
                    if units_scaler is not None:
                        plot_units = units_scaler.to_units
                    else:
                        plot_units = meta.get("units", "")

            # determine ens number and steps
            members = layer["data"]._unique_metadata("number")
            steps = layer["data"]._unique_metadata("step")
            # print(f"members={members}")
            # ens forecast
            if len(members) > 1:
                for step in steps:
                    v = layer["data"].select(step=step)
                    v = mv.nearest_gridpoint(v, location)
                    # print(f"step={step}")
                    x = np.percentile(v, y_values)
                    if units_scaler is not None:
                        x = units_scaler.scale_value(x)
                    # print(f" x={x}")
                    cdf_data.append(x)
                    cdf_label.append(layer["data"].label + f" +{step}h")

            # deterministic forecast
            else:
                raise Exception(f"plot_cds: only ENS data accepted as input!")

            title_data.append(layer["data"])

    # define x axis params
    if not x_range:
        x_tick, x_min, x_max = Layout.compute_axis_range(
            _y_min(cdf_data), _y_max(cdf_data)
        )
    elif len(x_range) == 2:
        x_min = x_range[0]
        x_max = x_range[1]
        x_tick, _, _ = Layout.compute_axis_range(x_min, x_max)
    elif len(x_range) == 3:
        x_min = x_range[0]
        x_max = x_range[1]
        x_tick = x_range[2]
    else:
        raise Exception(f"plot_cdf: invalid x_range={x_range} specified!")

    # print(f"x_tick={x_tick} x_min={x_min} x_max={x_max}")
    x_title = f"[{plot_units}]"

    # define y axis params
    y_min = 0
    y_max = 100
    y_tick = 10
    y_title = "Percentage [%]"

    # define the view
    view = Layout().build_xy(
        x_min, x_max, y_min, y_max, x_tick, y_tick, x_title, y_title
    )
    desc.append(view)

    # define curves
    line_colours = [
        "red",
        "blue",
        "green",
        "black",
        "cyan",
        "evergreen",
        "gold",
        "pink",
    ]
    line_styles = ["solid", "dash", "dotted"]

    colour_idx = -1
    style_idx = 0

    for i, d in enumerate(cdf_data):
        vis = mv.input_visualiser(input_x_values=d, input_y_values=y_values)
        colour_idx = (colour_idx + 1) % len(line_colours)

        vd = mv.mgraph(
            graph_type="curve",
            graph_line_colour=line_colours[colour_idx],
            graph_line_thickness=3,
            legend_user_text=cdf_label[i],
            legend="on",
        )

        desc.append(vis)
        desc.append(vd)

    # add title
    title = Title(font_size=title_font_size)
    t = title.build_cdf(title_data)
    if t is not None:
        desc.append(t)

    # add legend
    legX = 3.5
    legY = 14

    # Legend
    legend = mv.mlegend(
        legend_display_type="disjoint",
        legend_entry_plot_direction="column",
        legend_text_composition="user_text_only",
        legend_border="on",
        legend_border_colour="black",
        legend_box_mode="positional",
        legend_box_x_position=legX,
        legend_box_y_position=legY,
        legend_box_x_length=4,
        legend_box_y_length=3,
        legend_text_font_size=0.35,
        legend_box_blanking="on",
    )
    desc.append(legend)

    mv.plot(desc, animate=False)
