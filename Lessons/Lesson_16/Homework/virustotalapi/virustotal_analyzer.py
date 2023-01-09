import argparse
import base64
import os
import urllib.parse
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime, timedelta
from json import dump, load
from time import sleep

import dotenv
import pytz
import requests
from exceptions import *
from tqdm import tqdm

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
        self._args = self._parser.parse_args()
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

        if self._args.clear:
            choice = None
            if self._args.i:
                choice = (
                    input("are you sure you want to clear the cache? (y/n)\n" ">>> ")
                    .lower()
                    .strip()
                )
                while "y" != choice != "n":
                    print(f"choice {choice} not available.")
                    choice = (
                        input(
                            "are you sure you want to clear the cache? (y/n)\n" ">>> "
                        )
                        .lower()
                        .strip()
                    )
            if choice == "y":
                self._clear_cache()

        if self._args.scan:
            self._scan_urls(urls=self._args.urls)

        reputatuons = self._url_analysis(urls=self._args.urls)

        print(*reputatuons, sep="\n")

        # save the cached urls
        try:
            with open(file=fpath, mode="w") as cached_urls:
                dump(self._cache, cached_urls)
        except Exception as exception:
            print("Unknown error occured")
            print(exception)

    def _clear_cache(self):
        keys = list(self._cache.keys())
        if len(keys) != 0:
            for key in keys:
                self._cache.pop(key)
        if self._args.verbose:
            print("deleted all cached urls.")

    def _get_analysis_score(self, url: str) -> tuple[str, int]:
        """
        Calculate the analysis score from VirusTotal last_analysis_stats
        "param
        """

        reputation = (
            self._cache.get(url).get("data").get("attributes").get("reputation")
        )

        return url, reputation

    def _get_single_analysis(self, url: str, headers: dict) -> int:
        """
        Send a GET request to VirusTotal API to fetch scan data for url\n
        Return analysis score for url from VirusTotal API\n
        :param url: str -> url of website
        :return: analysis score -> int (0-100)
        """

        if self._args.verbose:
            print(f"Starting to fetch analysis for url {url}")

        if url in self._cache and self._args.scan is False:

            if self._args.verbose:
                print(f"fetching from cache")

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
            elif response.status_code == 429:
                raise QuoataReachedError(response=response)
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
        if response.status_code == 429:
            raise QuoataReachedError(response=response)
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
            headers["x-apikey"] = self._args.apikey

        if self._args.verbose:
            print(f"Starting to scan urls {urls}")

        with tqdm(urls, total=len(urls), desc="scanning") as urls_progress:
            with ThreadPoolExecutor() as executor:
                futures = []
                for url in urls:
                    futures.append(executor.submit(self._scan_single_url, url, headers))
                    sleep(0.001)

                for future in as_completed(futures):
                    urls_progress.update(1)

        if self._args.verbose:
            print(f"Done scanning urls {urls}")

    def _url_analysis(self, urls: list[str]) -> list[tuple[str, int]]:
        scores: list[tuple[str, int]] = []

        headers = self._base_headers.copy()

        if self._args.apikey is not None:
            headers["x-apikey"] = self._args.apikey

        flag = None

        with tqdm(urls, desc="getting analysis") as urls_progress:
            with ThreadPoolExecutor() as executor:
                futures = []
                for url in urls:
                    future = executor.submit(self._get_single_analysis, url, headers)
                    futures.append(future)
                    sleep(0.001)

                for future in as_completed(futures):
                    try:
                        score = future.result()
                    except QuoataReachedError as quota_reached:
                        print(quota_reached)
                        print(f"quiting program")
                        exit(0)
                    except AnalysisDataDoesNotExist as no_valid_analysis:
                        flag = True
                        print(no_valid_analysis)
                    except AnalysisExpired as expired:
                        flag = True
                        print(expired)
                    except BadRequest as bad_request:
                        print(bad_request)
                    else:
                        scores.append(score)
                        urls_progress.update(1)

                    if flag:
                        scan_headers = headers.copy()
                        scan_headers[
                            "content-type"
                        ] = "application/x-www-form-urlencoded"

                        try:
                            self._scan_single_url(url=url, headers=scan_headers)
                        except QuoataReachedError as quota_reached:
                            print(quota_reached)
                            print("quiting program")
                            exit(0)
                        except BadRequest as bad_scan_request:
                            print(bad_scan_request)
                        else:
                            try:
                                score = self._get_single_analysis(
                                    url=url, headers=headers
                                )
                            except QuoataReachedError as quota_reached:
                                print(quota_reached)
                                print("quiting program")
                                exit(0)
                            except BadRequest as bad_analysis_request:
                                print(bad_analysis_request)
                            else:
                                scores.appends(score)

        return scores


if __name__ == "__main__":
    vt = VirusTotal()
