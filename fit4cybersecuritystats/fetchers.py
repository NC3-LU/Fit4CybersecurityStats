#! /usr/bin/env python
# -*- coding: utf-8 -*-

from typing import Union, List, Dict, Any, Type
from urllib.parse import urljoin
import requests

TIMEOUT = 5
DATE_FROM = ""
DATE_TO = ""

JSON = Union[Dict[str, Any], List[Any], int, str, float, bool, Type[None]]


def fetch(url: str) -> JSON:
    """Send a HTTP GET request to a remote Fit4Cybersecurity instance in order to
    get stats data."""
    result = requests.get(url, timeout=TIMEOUT)
    assert result.status_code == 200, "Error when getting data from remote."
    return result.json()


def survey_per_company_sector(instance) -> JSON:
    url = urljoin(instance[1], "/stats/survey_per_company_sector.json")
    result = fetch(url)
    return result


def survey_per_company_size(instance) -> JSON:
    url = urljoin(instance[1], "/stats/survey_per_company_size.json")
    result = fetch(url)
    return result
