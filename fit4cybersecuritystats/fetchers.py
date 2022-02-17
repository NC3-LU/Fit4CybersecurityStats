#! /usr/bin/env python
# -*- coding: utf-8 -*-

from typing import Union, List, Dict, Any, Type, Tuple
from urllib.parse import urljoin, urlencode, urlparse, parse_qsl, urlunparse
import requests

TIMEOUT = 5

JSON = Union[Dict[str, Any], List[Any], int, str, float, bool, Type[None]]


def fetch(url: str, params: Dict[str, str]) -> JSON:
    """Send a HTTP GET request to a remote Fit4Cybersecurity instance in order to
    get stats data."""
    if params:
        url_parts = list(urlparse(url))
        query = dict(parse_qsl(url_parts[4]))
        query.update(params)
        url_parts[4] = urlencode(query)
        url = urlunparse(url_parts)
    result = requests.get(url, timeout=TIMEOUT)
    assert result.status_code == 200, "Error when getting data from remote."
    return result.json()


def survey_per_company_sector(
    instance: Tuple[str, str], params: Dict[str, str] = {}
) -> JSON:
    """Retrieves the stats for the surveys by companies sectors."""
    url = urljoin(instance[1], "/stats/survey_per_company_sector.json")
    result = fetch(url, params)
    return result


def survey_per_company_size(
    instance: Tuple[str, str], params: Dict[str, str] = {}
) -> JSON:
    url = urljoin(instance[1], "/stats/survey_per_company_size.json")
    result = fetch(url, params)
    return result
