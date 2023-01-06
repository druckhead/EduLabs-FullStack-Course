import os
import base64
import dotenv
import requests
import urllib.parse
from datetime import datetime, timedelta
import pytz
from Lesson_16.Homework.virustotalapi.exceptions.exceptions import *

dotenv.load_dotenv()


def _encode_url(url: str):
    """
    :param url: str -> url of website
    :return: url_id -> base64 encoded url
    """
    url_id = base64.urlsafe_b64encode(url.encode()).decode().strip("=")
    return url_id


class VirusTotal:
    _base_url = ""
    _base_headers = {
        "accept": "application/json",
        "x-apikey": os.getenv("KEY"),
    }

    def __init__(self):
        # link -> data
        self._cache: dict[str, dict] = {}

    def scan_url(self, url: str):
        request_url = "https://www.virustotal.com/api/v3/urls"
        headers = self._base_headers.copy()
        headers['content-type'] = "application/x-www-form-urlencoded"

        payload = f"url={urllib.parse.quote(url, safe='', encoding='utf8')}"

        response = requests.post(request_url, data=payload, headers=headers)
        if response.status_code == 200:
            return response.json()
        else:
            raise BadRequest(response=response)

    def url_analysis(self, url: str, days=180):
        if url in self._cache:
            last_analysis_epoch = self._cache[url]['data']['attributes']['last_analysis_date']
            # convert epoch to utc and make datetime tz aware
            last_analysis_utc = datetime.utcfromtimestamp(last_analysis_epoch).astimezone(pytz.UTC)
            now = datetime.utcnow().astimezone(tz=pytz.UTC)
            # if param days past since last analysis, clear cached link
            if now >= last_analysis_utc + timedelta(days=days):
                self._cache.pop(url)
                raise AnalysisExpired(url=url,
                                      last_analysis=last_analysis_utc,
                                      expire_date=last_analysis_utc + timedelta(days=days))

            return self._cache[url]

        url_id = _encode_url(url)
        base_url = "https://www.virustotal.com/api/v3/urls"

        request_url = f"{base_url}/{url_id}"
        headers = self._base_headers

        response = requests.get(request_url, headers=headers)
        if response.status_code == 200:
            if url not in self._cache:
                self._cache[url] = response.json()
            return self._cache[url]
        else:
            raise BadRequest(response=response)
