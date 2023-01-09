import argparse
import base64
import os
import urllib.parse
from datetime import datetime, timedelta
from json import dump, load
from time import sleep

import dotenv
import pytz
import requests
from tqdm import tqdm

from exceptions import *

dotenv.load_dotenv()


def _encode_url(url: str):
    """
    :param url: str -> url of website
    :return: url_id -> base64 encoded url
    """
    url_id = base64.urlsafe_b64encode(url.encode()).decode().strip("=")
    return url_id


class VirusTotal:
    _base_url = "https://www.virustotal.com/api/v3/urls"
    _base_headers = {
        "accept": "application/json",
        "x-apikey": os.getenv("KEY"),
    }

    def __init__(self):
        directory_path = os.path.join(os.curdir, "cache")
        if not os.path.exists(path=directory_path):
            os.mkdir(path=directory_path)

        fpath = os.path.join(directory_path, "cache.json")

        mode = "w" if not os.path.exists(path=fpath) else "r"
        if mode == "w":
            # link -> data
            self._cache: dict[str, dict] = {}
        elif mode == "r":
            try:
                with open(file=fpath, mode=mode) as cached_json:
                    self._cache = load(cached_json)
            except FileNotFoundError as fnf:
                print(fnf)
                # posible exit program

        self._parser = argparse.ArgumentParser(
            prog="VirusTotal Scanner",
            description="The program allows to check a URL with VirusTotal API",
            epilog="By, Daniel Raz",
        )

        # Define arguments so it will know how to parse

        self._parser.add_argument(
            "urls", nargs="+", help="One or more URLs to scan. Separated by comma"
        )

        self._parser.add_argument(
            "-k",
            "--apikey",
            action="store",
            help="Optionaly add your own custom apikey",
        )

        self._parser.add_argument(
            "-s", "--scan", action="store_true", help="force new scan"
        )

        self._parser.add_argument(
            "-v", "--verbose", action="store_true", help="verbose help message"
        )

        self._parser.add_argument(
            "-d",
            "--days",
            action="store",
            type=int,
            help="The amount of days to for the cache to persist",
            default=180,
        )

        self._parser.add_argument(
            "-c", "--clear", action="store_true", help="Clear the cached links"
        )

        self._parser.add_argument(
            "-i", action="store_true", help="Prompt before removal"
        )
        # end define args
        self._args = self._parser.parse_args(
            [
                "https://www.google.com",
                "https://www.youtube.com",
                "https://github.com",
                "-v",
                '-k',
                '2dbb81a2b4371095db1dec5d886f84bb585a558f36d0b2ad35589301940da3a6'
            ]
        )
        if self._args.verbose:
            print(
                self._args.urls,
                self._args.apikey,
                self._args.scan,
                self._args.verbose,
                self._args.days,
                self._args.clear,
                self._args.i,
            )

        if self._args.scan:
            self._scan_urls(urls=self._args.urls)
        reputatuons = self._url_analysis(urls=self._args.urls)
        
        print(*reputatuons, sep='\n')

        # save the cached urls
        try:
            with open(file=fpath, mode="w") as cached_urls:
                dump(self._cache, cached_urls)
        except Exception as exception:
            print("Unknown error occured")
            print(exception)
    
    def _get_analysis_score(self, url: str) -> int:
        """
        Calculate the analysis score from VirusTotal last_analysis_stats
        "param
        """
        
        reputation = self._cache.get(url).get('data').get('attributes').get('reputation')
    
        return reputation
        

    def _get_single_analysis(self, url: str, headers: dict) -> int:
        """
        Send a GET request to VirusTotal API to fetch scan data for url\n
        Return analysis score for url from VirusTotal API\n
        :param url: str -> url of website
        :return: analysis score -> int (0-100)
        """

        if self._args.verbose:
            print(f"Starting to fetch analysis for url {url}")

        if url in self._cache:

            if self._args.verbose:
                print(f"fetching from cache")
            sleep(0.1)
            last_analysis_epoch = self._cache[url]["data"]["attributes"][
                "last_analysis_date"
            ]

            # convert epoch to utc and make datetime tz aware
            last_analysis_utc = datetime.utcfromtimestamp(
                last_analysis_epoch
            ).astimezone(pytz.UTC)
            now = datetime.utcnow().astimezone(tz=pytz.UTC)

            # if param days past since last analysis, clear cached link
            if now >= last_analysis_utc + timedelta(days=self._args.days):
                self._cache.pop(url)
                raise AnalysisExpired(
                    url=url,
                    last_analysis=last_analysis_utc,
                    expire_date=last_analysis_utc + timedelta(days=self._args.days),
                )

            if self._args.verbose:
                print(f"done fetching analysis for url {url}")

        else:
            if self._args.verbose:
                print(
                    f"cache for url {url} not found.\n"
                    f"requesting analysis from VirusTotal"
                )

            url_id = _encode_url(url)

            request_url = f"{self._base_url}/{url_id}"

            response = requests.get(request_url, headers=headers)

            if response.status_code == 200:
                if url not in self._cache:
                    self._cache[url] = response.json()
            elif response.status_code == 404:
                raise AnalysisDataDoesNotExist(url=url)
            else:
                raise BadRequest(response=response)

            if self._args.verbose:
                print(f"got analysis for url {url} from VirusTotal")

        return self._get_analysis_score(url=url)

    def _scan_single_url(self, url: str, headers: dict) -> None:
        """
        Send a post request to VirusTotal API asking to scan url\n
        :param url: url to scan
        :return: None
        """

        if self._args.verbose:
            print(f"Starting to scan url {url}")

        payload = f"url={urllib.parse.quote(url, safe='', encoding='utf8')}"

        response = requests.post(self._base_url, data=payload, headers=headers)
        if response.status_code != 200:
            raise BadRequest(response=response)

        if self._args.verbose:
            print(f"Done scanning for url {url}")

    def _scan_urls(self, urls: list[str]):
        """
        Scan all the urls with a progress bar\n
        :param urls: a list of urls to scan
        :return: None
        """
        
        headers = self._base_headers.copy()
        
        if self._args.apikey is not None:
                headers['x-apikey'] = self._args.apikey


        if self._args.verbose:
            print(f"Starting to scan urls {urls}")

        for url in tqdm(urls):
            try:
                self._scan_single_url(url=url, headers=headers)
            except BadRequest as bad_scan_request:
                print(bad_scan_request)

        if self._args.verbose:
            print(f"Done scanning urls {urls}")

    def _url_analysis(self, urls: list[str]) -> list[tuple[str, int]]:
        scores: list[tuple[str, int]] = []
        
        headers = self._base_headers.copy()
        
        if self._args.apikey is not None:
            headers['x-apikey'] = self._args.apikey
        
        flag = None
        for url in tqdm(urls, desc="urls"):
            try:
                score = self._get_single_analysis(url=url, headers=headers)
            except AnalysisDataDoesNotExist as analysis_does_not_exist:
                flag = True
                print(analysis_does_not_exist)
            except AnalysisExpired as analysis_expired:
                flag = True
                print(analysis_expired)
            else:
                scores.append((url, score))

            if flag:
                try:
                    scan_headers = headers.copy()
                    scan_headers['content-type'] = "application/x-www-form-urlencoded"
                    self._scan_single_url(url=url, headers=scan_headers)
                except BadRequest as bad_scan_request:
                    print(bad_scan_request)
                else:
                    try:
                        self._get_single_analysis(url=url, headers=headers)
                    except BadRequest as bad_analysis_request:
                        print(bad_analysis_request)

            sleep(0.001)
        
        return scores


if __name__ == "__main__":
    vt = VirusTotal()
