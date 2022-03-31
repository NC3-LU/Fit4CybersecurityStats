#! /usr/bin/env python
import argparse

from bokeh.embed import file_html
from bokeh.resources import CSSResources
from bokeh.resources import JSResources
from jinja2 import Environment
from jinja2 import PackageLoader

from fit4cybersecuritystats.charts import survey_per_company_sector_chart
from fit4cybersecuritystats.fetchers import survey_per_company_sector
from instance.production import INSTANCES


env = Environment(loader=PackageLoader("fit4cybersecuritystats"))


if __name__ == "__main__":
    # Point of entry in execution mode
    parser = argparse.ArgumentParser(prog="Fit4CyberSecurity Stats")
    parser.add_argument(
        "-o",
        "--output",
        dest="output_path",
        required=True,
        help="Ouput file path.",
    )
    arguments = parser.parse_args()

    # Grab the static resources
    js_resources = JSResources(mode="inline", minified=True, components=["bokeh"])
    css_resources = CSSResources(mode="inline", minified=True, components=["bokeh"])
    plots = []
    for instance in INSTANCES:
        stats_data = survey_per_company_sector(instance)
        plots.append(survey_per_company_sector_chart(stats_data))

    # html = file_html(plots, (js_resources, css_resources), "Fit4CyberSecurity")
    renderJS = True
    template = env.get_template("html/index.html")
    html = file_html(
        plots,
        (js_resources, css_resources),
        template=template,
        template_variables={
            "js_data": js_resources.render_js() if renderJS else "",
            "text_heading": "<h1>Fit4Cybersecurity</h1>",
            "text_download": "",
            "text_footing": "",
        },
    )

    # print(html)
    with open(arguments.output_path, "w") as f:
        f.write(str(html))
    print(f"HTML page written in {arguments.output_path}.")
