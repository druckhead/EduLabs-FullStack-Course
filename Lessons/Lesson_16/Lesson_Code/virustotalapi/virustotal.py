import os
import base64
import dotenv
import requests
import urllib.parse

dotenv.load_dotenv()


class VirusTotalExceptions(Exception):
    pass


class BadRequest(VirusTotalExceptions):
    pass


def _encode_url(url: str):
    """
    :param url: str -> url of website
    :return: url_id -> base64 encoded url
    """
    url_id = base64.urlsafe_b64encode(url.encode()).decode().strip("=")
    return url_id


class VirusTotal:
    def __init__(self):
        self._base_url = ""
        self._base_headers = {
            "accept": "application/json",
            "x-apikey": os.getenv("KEY"),
        }

    def scan_url(self, url: str):
        request_url = "https://www.virustotal.com/api/v3/urls"
        headers = self._base_headers.copy()
        headers['content-type'] = "application/x-www-form-urlencoded"

        payload = f"url={urllib.parse.quote(url, safe='', encoding='utf8')}"

        response = requests.post(request_url, data=payload, headers=headers)
        if response.status_code == 200:
            return response.json()
        else:
            raise BadRequest()

    def url_analysis(self, url: str):
        url_id = _encode_url(url)
        base_url = "https://www.virustotal.com/api/v3/urls"

        request_url = f"{base_url}/{url_id}"
        headers = self._base_headers

        response = requests.get(request_url, headers=headers)
        if response.status_code == 200:
            return response.json()
        else:
            raise BadRequest()

    def rescan(self, url: str):
        url_id = _encode_url(url)
        request_url = f"https://www.virustotal.com/api/v3/urls/{url_id}/analyse"
        headers = self._base_headers

        response = requests.post(request_url, headers=headers)
        if response.status_code == 200:
            return response.json()
        else:
            raise BadRequest()


if __name__ == '__main__':
    vt = VirusTotal()
    url = "https://www.google.com"
    # print(vt.url_analysis(url))
    # print(vt.scan_url(url))
    # print(vt.rescan(url))
