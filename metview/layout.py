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
