#! /usr/bin/env python
from jinja2 import Environment
from jinja2 import PackageLoader

from fit4cybersecuritystats.fetchers import survey_per_company_sector
from instance.production import INSTANCES


DATE_FROM = ""
DATE_TO = ""

env = Environment(loader=PackageLoader("fit4cybersecuritystats"))


def content_per_company_sector(instance):
    stats_data = survey_per_company_sector(instance)
    template = env.get_template("markdown/survey_per_company_sector.md")
    markdown_content = template.render(instance_name=instance[0], stats_data=stats_data)
    return markdown_content, stats_data


def content_per_company_size(instance):
    return ""


if __name__ == "__main__":
    # Point of entry in execution mode
    markdown_content = ""
    for instance in INSTANCES:
        markdown_content_company_sector, _ = content_per_company_sector(instance)
        markdown_content += markdown_content_company_sector
        # print(markdown_content_company_sector)

        markdown_content_company_size = content_per_company_size(instance)
        markdown_content += markdown_content_company_size

        print(markdown_content)
