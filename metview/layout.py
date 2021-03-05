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

import metview as mv

LOG = logging.getLogger(__name__)


class Layout:

    GRID_DEF = {1: [1, 1], 2: [2, 1], 3: [3, 1], 4: [2, 2]}

    def build_grid(self, page_num=0, rows=None, columns=None, layout=None, view=None):
        if rows is None and columns is None:
            if layout is not None and layout != "":
                v = layout.split("x")
                if len(v) == 2:
                    try:
                        rows = int(v[0])
                        columns = int(v[1])
                        LOG.debug(f"rows={rows} columns={columns}")
                    except:
                        raise Exception(f"Invalid layout specification ({layout}")
                    if page_num > 0 and rows * columns < page_num:
                        raise Exception(
                            f"Layout specification={layout} does not match number of scenes={page_num}"
                        )
            else:
                if page_num in self.GRID_DEF:
                    rows, columns = self.GRID_DEF[page_num]
                else:
                    raise

        return self._build_grid(rows=rows, columns=columns, view=view)

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

    def build_diff(self, view):
        page_1 = mv.plot_page(
            top=5,
            bottom=50,
            left=25,
            right=75,
            view=view
            )

        page_2 = mv.plot_page(
            top=52,
            bottom=97,
            right=50,
            view=view
            )

        page_3 = mv.plot_page(
            top=52,
            bottom=97,
            left=50,
            right=100,
            view=view
        )

        return mv.plot_superpage(pages=[page_1, page_2, page_3])

    def build_xs(self, line, map_view):
        page = mv.plot_page(
            top=5,
            bottom=35,
            view=map_view
        )

        xs_view = mv.mxsectview(
            line=line,
            bottom_level=1000,
            top_level=150
            #wind_perpendicular : "off",
            #wind_parallel :"on",
            #wind_intensity :"off"
            )

        page_1 = mv.plot_page(
            top=35,
            view=xs_view
        )

        return mv.plot_superpage(pages=[page_1,page])

