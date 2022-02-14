#! /usr/bin/env python
# -*- coding: utf-8 -*-

from urllib.parse import urljoin
import requests


DATE_FROM = ""
DATE_TO = ""


def survey_per_company_sector(instance):
    url = urljoin(instance[1], "/stats/survey_per_company_sector.json")
    result = requests.get(url)
    assert result.status_code == 200, "error when getting data"
    return result.json()
