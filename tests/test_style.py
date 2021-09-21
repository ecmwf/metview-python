# (C) Copyright 2017- ECMWF.
#
# This software is licensed under the terms of the Apache Licence Version 2.0
# which can be obtained at http://www.apache.org/licenses/LICENSE-2.0.
#
# In applying this licence, ECMWF does not waive the privileges and immunities
# granted to it by virtue of its status as an intergovernmental organisation
# nor does it submit to any jurisdiction.
#


import metview as mv
from metview import bindings
from metview.style import Style, Visdef


def test_visdef_object():
    vd = Visdef(
        "msymb",
        {
            "symbol_type": "text",
            "symbol_table_mode": "advanced",
            "symbol_advanced_table_text_font_colour": "black",
        },
    )

    # clone
    v = vd.clone()
    assert v.verb == vd.verb
    assert v.params == vd.params
    assert id(v) != id(vd)
    assert id(v.params) != id(vd.params)

    # change
    vd.change("msymb", "symbol_advanced_table_text_font_colour", "red")
    assert vd.params["symbol_advanced_table_text_font_colour"] == "red"
    vd.change("mcont", "symbol_advanced_table_text_font_colour", "blue")
    assert vd.params["symbol_advanced_table_text_font_colour"] == "red"

    # from request
    r = mv.msymb(
        {
            "symbol_type": "text",
            "symbol_table_mode": "advanced",
            "symbol_advanced_table_text_font_colour": "black",
        }
    )

    v = Visdef.from_request(r)
    assert v.verb == vd.verb
    for k, v in v.params.items():
        assert r[k.upper()].lower() == v.lower()


def test_style_object():
    vd = Visdef(
        "msymb",
        {
            "symbol_type": "text",
            "symbol_table_mode": "advanced",
            "symbol_advanced_table_text_font_colour": "black",
        },
    )

    # create
    s = Style("super", vd)
    assert s.name == "super"
    assert len(s.visdefs) == 1
    assert s.visdefs[0].params["symbol_advanced_table_text_font_colour"] == "black"

    # update
    ns = s.update({"symbol_advanced_table_text_font_colour": "red"})
    assert id(ns) != id(s)
    assert s.visdefs[0].params["symbol_advanced_table_text_font_colour"] == "black"
    assert ns.visdefs[0].params["symbol_advanced_table_text_font_colour"] == "red"

    ns = s.update({"symbol_advanced_table_text_font_colour": "red"}, verb="mcont")
    assert id(ns) != id(s)
    assert s.visdefs[0].params["symbol_advanced_table_text_font_colour"] == "black"
    assert ns.visdefs[0].params["symbol_advanced_table_text_font_colour"] == "black"

    ns = s.update({"symbol_advanced_table_text_font_colour": "red"}, verb="msymb")
    assert id(ns) != id(s)
    assert s.visdefs[0].params["symbol_advanced_table_text_font_colour"] == "black"
    assert ns.visdefs[0].params["symbol_advanced_table_text_font_colour"] == "red"

    # multiple visdefs

    vd1 = Visdef(
        "msymb",
        {
            "symbol_type": "text",
            "symbol_table_mode": "advanced",
            "symbol_advanced_table_text_font_colour": "black",
        },
    )
    vd2 = Visdef("mgraph", {"graph_line_colour": "blue", "graph_line_thickness": 4})

    s = Style("super", [vd1, vd2])
    assert s.name == "super"
    assert len(s.visdefs) == 2
    assert s.visdefs[0].params["symbol_advanced_table_text_font_colour"] == "black"
    assert s.visdefs[1].params["graph_line_colour"] == "blue"

    # update
    ns = s.update({"symbol_advanced_table_text_font_colour": "red"}, verb="msymb")
    assert id(ns) != id(s)
    assert s.visdefs[0].params["symbol_advanced_table_text_font_colour"] == "black"
    assert ns.visdefs[0].params["symbol_advanced_table_text_font_colour"] == "red"

    ns = s.update(
        {
            "graph_line_colour": "yellow",
        },
        verb="mgraph",
    )
    assert id(ns) != id(s)
    assert s.visdefs[1].params["graph_line_colour"] == "blue"
    assert ns.visdefs[1].params["graph_line_colour"] == "yellow"


def test_style_set_grib_id():
    # mcont
    vd = Visdef(
        "mcont",
        {
            "legend": "on",
        },
    )

    s = Style("super", vd)
    ns = s.set_data_id("11")
    assert id(s) != id(ns)
    assert ns.visdefs[0].verb == "mcont"
    assert ns.visdefs[0].params["grib_id"] == "11"
    assert s.visdefs[0].params.get("grib_id", None) is None

    # mwind
    vd = Visdef(
        "mwind",
        {
            "legend": "on",
        },
    )

    s = Style("super", vd)
    ns = s.set_data_id("12")
    assert id(s) != id(ns)
    assert ns.visdefs[0].verb == "mwind"
    assert ns.visdefs[0].params["grib_id"] == "12"
    assert s.visdefs[0].params.get("grib_id", None) is None

    # other
    vd = Visdef(
        "msymb",
        {
            "legend": "on",
        },
    )

    s = Style("super", vd)
    ns = s.set_data_id("10")
    assert id(s) == id(ns)
    assert s.visdefs[0].params.get("grib_id", None) is None
