#! /usr/bin/env python
# -*- coding: utf-8 -*-


from flask import Flask, render_template
from bokeh.embed import components
from bokeh.resources import INLINE

from main import INSTANCES, survey_per_company_sector
from fit4cybersecuritystats.charts import survey_per_company_sector_chart


app = Flask(__name__)


@app.route("/")
def bokeh():
    # components will embed the script and div HTML tags for the page
    components_instances = {}
    for instance in INSTANCES:
        _, stats = survey_per_company_sector((instance[0], instance[1]))
        fig = survey_per_company_sector_chart(stats)
        components_instances[instance[0]] = components(fig)

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
    app.run(debug=True)
