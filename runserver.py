#! /usr/bin/env python
# -*- coding: utf-8 -*-

from flask import render_template
from bokeh.embed import components
from bokeh.resources import INLINE

from fit4cybersecuritystats.bootstrap import application
from fit4cybersecuritystats.fetcher import survey_per_company_sector
from fit4cybersecuritystats.charts import survey_per_company_sector_chart


@application.route("/")
def index():
    return render_template("index.html")


@application.route("/stats/")
def stats():
    """Returns a page with charts generated with data from several remote
    Fit4Cybersecurity instances.
    """
    components_instances = {}
    for instance in application.config["INSTANCES"]:
        try:
            # get the stats from remote Fit4Cybersecurity instances
            stats = survey_per_company_sector((instance[0], instance[1]))
        except Exception:
            continue
        # generate chart with stats data
        fig = survey_per_company_sector_chart(stats)
        # create components for the HTML tempate
        components_instances[instance[0]] = components(fig) + (instance[1],)
        # bokeh.embed.components returns the script and div HTML tags

    # grab the static resources
    js_resources = INLINE.render_js()
    css_resources = INLINE.render_css()

    # render template
    html = render_template(
        "stats.html",
        components_instances=components_instances,
        js_resources=js_resources,
        css_resources=css_resources,
    )
    return html


@application.route("/human.txt", methods=["GET"])
def human():
    """Human dot txt page."""
    return render_template("human.txt"), 200, {"Content-Type": "text/plain"}


if __name__ == "__main__":
    application.run(host=application.config["HOST"], port=application.config["PORT"])
