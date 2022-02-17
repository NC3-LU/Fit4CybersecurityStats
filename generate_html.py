#! /usr/bin/env python
# -*- coding: utf-8 -*-

from jinja2 import Environment, PackageLoader
from bokeh.resources import JSResources, CSSResources
from bokeh.embed import file_html

from instance.production import INSTANCES
from fit4cybersecuritystats.fetchers import survey_per_company_sector
from fit4cybersecuritystats.charts import survey_per_company_sector_chart


env = Environment(loader=PackageLoader("fit4cybersecuritystats"))


if __name__ == "__main__":
    # Point of entry in execution mode
    markdown_content = ""
    for instance in INSTANCES:
        stats_data = survey_per_company_sector(instance)
        plot = survey_per_company_sector_chart(stats_data)
        # grab the static resources
        js_resources = JSResources(mode="inline", minified=True, components=["bokeh"])
        css_resources = CSSResources(mode="inline", minified=True, components=["bokeh"])
        html = file_html(plot, (js_resources, css_resources), "my plot")
        # print(html)
        with open("./{}-chart.html".format(instance[0]), 'w') as f:
            f.write(str(html))
    print("HTML pages written.")
