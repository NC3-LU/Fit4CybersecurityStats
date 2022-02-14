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
    return "Hello world!"


@application.route("/stats/")
def stats():
    # bokeh.embed.components returns the script and div HTML tags for the page
    components_instances = {}
    for instance in application.config["INSTANCES"]:
        stats = survey_per_company_sector((instance[0], instance[1]))
        fig = survey_per_company_sector_chart(stats)
        components_instances[instance[0]] = components(fig) + (instance[1],)

    # grab the static resources
    js_resources = INLINE.render_js()
    css_resources = INLINE.render_css()

    # render template
    html = render_template(
        "index.html",
        components_instances=components_instances,
        js_resources=js_resources,
        css_resources=css_resources,
    )
    return html


if __name__ == "__main__":
    application.run(host=application.config["HOST"], port=application.config["PORT"])
