#! /usr/bin/env python
# -*- coding: utf-8 -*-

from urllib.parse import urljoin
import requests
from jinja2 import Environment, FileSystemLoader

INSTANCES = [
    ("Fit4Cybersecurity", "https://fit4cybersecurity.cases.lu/"),
    ("Fit4Privacy", "https://fit4privacy.cases.lu"),
    ("Fit4Privacy Demo", "https://fit4cybersecurity-demo.cases.lu"),
]

DATE_FROM = ""
DARE_TO = ""


env = Environment(loader=FileSystemLoader("templates"))


def survey_per_company_sector(instance):
    url = urljoin(instance[1], "/stats/survey_per_company_sector.json")
    result = requests.get(url)
    assert result.status_code == 200, "error when getting data"
    template = env.get_template("survey_per_company_sector.md")
    markdown_content = template.render(
        instance_name=instance[0],
        stats_data=result.json()
    )
    return markdown_content


def survey_per_company_size(instance):
    return ""


markdown_content = ""
for instance in INSTANCES:
    markdown_content_company_sector = survey_per_company_sector(instance)
    markdown_content += markdown_content_company_sector
    # print(markdown_content_company_sector)

    markdown_content_company_size = survey_per_company_size(instance)
    markdown_content += markdown_content_company_size

    print(markdown_content)
