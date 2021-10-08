#
# (C) Copyright 2020- ECMWF.
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

import metview as mv

LOG = logging.getLogger(__name__)


class Layout:

    GRID_DEF = {
        1: [1, 1],
        2: [2, 1],
        3: [3, 1],
        4: [2, 2],
        8: [3, 3],
        9: [3, 3],
        10: [4, 3],
    }

    def _grid_row_col(self, page_num=0, rows=None, columns=None, layout=None):
        if rows is None and columns is None:
            if layout is not None and layout != "":
                v = layout.split("x")
                if len(v) == 2:
                    try:
                        r = int(v[0])
                        c = int(v[1])
                        # LOG.debug(f"r{r} c={c}")
                    except:
                        raise Exception(f"Invalid layout specification ({layout}")
                    if page_num > 0 and r * c < page_num:
                        raise Exception(
                            f"Layout specification={layout} does not match number of scenes={page_num}"
                        )
            else:
                if page_num in self.GRID_DEF:
                    r, c = self.GRID_DEF[page_num]
                elif page_num >= 1:
                    r, c = self._compute_row_col(page_num)
                else:
                    raise Exception(f"Cannot create a layout for {page_num} pages!")
        return r, c

    def build_grid(self, page_num=0, rows=None, columns=None, layout=None, view=None):
        r, c = self._grid_row_col(
            page_num=page_num, rows=rows, columns=columns, layout=layout
        )

        if isinstance(view, mv.style.GeoView):
            v = view.to_request()
        else:
            v = view

        return self._build_grid(rows=r, columns=c, view=v)

    def _build_grid(self, rows=1, columns=1, view=None):
        assert rows >= 1 and columns >= 1
        if rows == 1 and columns == 1:
            return mv.plot_superpage(pages=[mv.plot_page(view=view)])
        else:
            return mv.plot_superpage(
                pages=mv.mvl_regular_layout(
                    view, columns, rows, 1, 1, [5, 100, 15, 100]
                )
            )

    def _compute_row_col(self, page_num):
        # has been checked for 100
        r = int(math.sqrt(page_num))
        c = r
        if c * r < page_num:
            if (page_num - c * r) % c == 0:
                c += (page_num - c * r) // c
            else:
                c += 1 + (page_num - c * r) // c
        return (r, c)

    def build_diff(self, view):
        page_1 = mv.plot_page(top=5, bottom=50, left=25, right=75, view=view)

        page_2 = mv.plot_page(top=52, bottom=97, right=50, view=view)

        page_3 = mv.plot_page(top=52, bottom=97, left=50, right=100, view=view)

        return mv.plot_superpage(pages=[page_1, page_2, page_3])

    def build_xs(self, line, map_view):
        xs_view = mv.mxsectview(
            line=line,
            bottom_level=1000,
            top_level=150
            # wind_perpendicular : "off",
            # wind_parallel :"on",
            # wind_intensity :"off"
        )

        page_1 = mv.plot_page(top=35 if map_view is not None else 5, view=xs_view)

        if map_view is not None:
            page = mv.plot_page(top=5, bottom=35, view=map_view)
            return mv.plot_superpage(pages=[page_1, page])
        else:
            return mv.plot_superpage(pages=[page_1])

    def build_stamp(self, page_num=0, layout="", view=None):

        if True:
            coast_empty = mv.mcoast(
                map_coastline="off", map_grid="off", map_label="off"
            )

            empty_view = mv.geoview(
                page_frame="off",
                subpage_frame="off",
                coastlines=coast_empty,
                subpage_x_position=40,
                subpage_x_length=10,
                subpage_y_length=10,
            )

            title_page = mv.plot_page(
                top=0, bottom=5, left=30, right=70, view=empty_view
            )

        r, c = self._grid_row_col(page_num=page_num, layout=layout)

        pages = mv.mvl_regular_layout(view, c, r, 1, 1, [5, 100, 15, 100])
        pages.append(title_page)
        return mv.plot_superpage(pages=pages)

        # g = self.build_grid(page_num=page_num, layout=layout, view=view)
        # return g

    def build_rmse(self, xmin, xmax, ymin, ymax, xtick, ytick, xtitle, ytitle):

        horizontal_axis = mv.maxis(
            axis_type="date",
            axis_orientation="horizontal",
            axis_position="bottom",
            # axis_title               :  'on',
            # axis_title_height        :   0.4,
            axis_grid="on",
            axis_grid_colour="grey",
            # axis_title_text          :  xtitle,
            # axis_title_quality       :  'high',
            axis_tick_interval=xtick,
            axis_tick_label_height=0.6,
            axis_date_type="days",
            axis_years_label="off",
            axis_months_label="off",
            axis_days_label_height="0.3",
        )

        vertical_axis = mv.maxis(
            axis_orientation="vertical",
            axis_position="left",
            axis_grid="on",
            axis_grid_colour="grey",
            axis_title="on",
            axis_title_height=0.4,
            axis_title_text=ytitle,
            # axis_title_quality       :  'high',
            axis_tick_interval=ytick,
            axis_tick_label_height=0.3,
        )

        cview = mv.cartesianview(
            page_frame="off",
            x_axis_type="date",
            y_axis_type="regular",
            y_automatic="off",
            x_automatic="off",
            y_min=ymin,
            y_max=ymax,
            x_date_min=xmin,
            x_date_max=xmax,
            horizontal_axis=horizontal_axis,
            vertical_axis=vertical_axis,
        )

        return cview

    def build_xy(self, xmin, xmax, ymin, ymax, xtick, ytick, xtitle, ytitle):

        horizontal_axis = mv.maxis(
            axis_orientation="horizontal",
            axis_position="bottom",
            axis_title="on",
            axis_title_height=0.5,
            axis_title_text=xtitle,
            # axis_title               :  'on',
            # axis_title_height        :   0.4,
            axis_grid="on",
            axis_grid_colour="grey",
            # axis_title_text          :  xtitle,
            # axis_title_quality       :  'high',
            axis_tick_interval=xtick,
            axis_tick_label_height=0.6,
            axis_date_type="days",
            axis_years_label="off",
            axis_months_label="off",
            axis_days_label_height="0.3",
        )

        vertical_axis = mv.maxis(
            axis_orientation="vertical",
            axis_position="left",
            axis_grid="on",
            axis_grid_colour="grey",
            axis_title="on",
            axis_title_height=0.6,
            axis_title_text=ytitle,
            # axis_title_quality       :  'high',
            axis_tick_interval=ytick,
            axis_tick_label_height=0.3,
        )

        cview = mv.cartesianview(
            page_frame="off",
            x_axis_type="regular",
            y_axis_type="regular",
            y_automatic="off",
            x_automatic="off",
            y_min=ymin,
            y_max=ymax,
            x_min=xmin,
            x_max=xmax,
            horizontal_axis=horizontal_axis,
            vertical_axis=vertical_axis,
        )

        return cview

    @staticmethod
    def compute_axis_range(v_min, v_max):
        count = 15
        d = math.fabs(v_max - v_min)
        if d > 0:
            b = d / count
            n = math.floor(math.log10(b))
            v = b / math.pow(10, n)
            # print("d={} b={} n={} v={}".format(d,b,n,v))

            if v <= 1:
                v = 1
            elif v <= 2:
                v = 2
            elif v <= 5:
                v = 5
            else:
                v = 10

            bin_size = v * math.pow(10, n)
            bin_start = math.ceil(v_min / bin_size) * bin_size
            if bin_start >= v_min and math.fabs(bin_start - v_min) < bin_size / 10000:
                bin_start = bin_start - bin_size / 100000
                av = v_min
            else:
                bin_start = bin_start - bin_size
                av = bin_start

            max_iter = 100
            act_iter = 0
            while av < v_max:
                av += bin_size
                act_iter += 1
                if act_iter > max_iter:
                    return (0, v_min, v_max)

            bin_end = av  # + bin_size / 100000
            return bin_size, bin_start, bin_end
        else:
            return (0, v_min, v_max)
