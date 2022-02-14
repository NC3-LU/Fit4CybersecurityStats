#! /usr/bin/env python
# -*- coding: utf-8 -*-

from math import pi

import pandas as pd

from bokeh.palettes import Category20c
from bokeh.plotting import figure
from bokeh.transform import cumsum


def survey_per_company_sector_chart(stats):
    data = (
        pd.Series(stats).reset_index(name="value").rename(columns={"index": "sector"})
    )
    data["angle"] = data["value"] / data["value"].sum() * 2 * pi
    try:
        data["color"] = Category20c[len(stats)]
    except KeyError:
        # if length is < 3
        data["color"] = ("#3182bd",)

    p = figure(
        height=800,
        width=1200,
        title="Pie Chart",
        toolbar_location=None,
        tools="hover",
        tooltips="@sector: @value",
        x_range=(-0.5, 1.0),
    )

    p.wedge(
        x=0,
        y=1,
        radius=0.4,
        start_angle=cumsum("angle", include_zero=True),
        end_angle=cumsum("angle"),
        line_color="white",
        fill_color="color",
        legend_field="sector",
        source=data,
    )

    p.axis.axis_label = None
    p.axis.visible = False
    p.grid.grid_line_color = None
    p.background_fill_color = None
    p.border_fill_color = None
    # export_png(p, filename="plot.png")
    # show(p)
    return p
