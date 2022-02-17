#! /usr/bin/env python
# -*- coding: utf-8 -*-

from flask import render_template, request
from bokeh.embed import components
from bokeh.resources import INLINE

from fit4cybersecuritystats.bootstrap import application
from fit4cybersecuritystats.fetchers import (
    survey_per_company_sector,
    survey_per_company_size,
)
from fit4cybersecuritystats.charts import survey_per_company_sector_chart


@application.route("/")
def index():
    return render_template("web/index.html")


@application.route("/stats/")
def stats():
    """Returns a page with charts generated with data from several remote
    Fit4Cybersecurity instances.
    """
    date_from = request.args.get("from", "2022-01-01")
    sectors_components_instances = {}
    size_components_instances = {}
    for instance in application.config["INSTANCES"]:
        try:
            # get the stats from remote Fit4Cybersecurity instances
            stats_sectors = survey_per_company_sector(
                (instance[0], instance[1]), {"from": date_from}
            )
        except Exception:
            continue
        # generate chart with stats data
        fig_sectors = survey_per_company_sector_chart(stats_sectors)
        sectors_components_instances[instance[0]] = components(fig_sectors) + (
            instance[1],
        )

        try:
            # get the stats from remote Fit4Cybersecurity instances
            stats_sizes = survey_per_company_size(
                (instance[0], instance[1]), {"from": date_from}
            )
        except Exception:
            continue
        fig_sizes = survey_per_company_sector_chart(stats_sizes)
        size_components_instances[instance[0]] = components(fig_sizes) + (instance[1],)

    # grab the static resources
    js_resources = INLINE.render_js()
    css_resources = INLINE.render_css()

    # render template
    html = render_template(
        "web/stats.html",
        sectors_components_instances=sectors_components_instances,
        size_components_instances=size_components_instances,
        js_resources=js_resources,
        css_resources=css_resources,
    )
    return html


@application.route("/human.txt", methods=["GET"])
def human():
    """Human dot txt page."""
    return render_template("web/human.txt"), 200, {"Content-Type": "text/plain"}


if __name__ == "__main__":
    application.run(host=application.config["HOST"], port=application.config["PORT"])
