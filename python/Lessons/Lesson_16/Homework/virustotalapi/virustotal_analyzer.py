import argparse
import base64
import os
import urllib.parse
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime, timedelta
from json import dump, load
from threading import Lock
from time import sleep

import dotenv
import pytz
import requests
from exceptions import *
from tqdm import tqdm

dotenv.load_dotenv()


def _encode_url(url: str):
    """
    Paramaters:
        url: string representation of a url of a website

    Returns:
        base64 encoded url
    """
    url_id = base64.urlsafe_b64encode(url.encode()).decode().strip("=")
    return url_id


class VirusTotal:
    """
    def __init__(self, args: argparse.Namespace) -> None:
    """

    _base_url = "https://www.virustotal.com/api/v3/urls"
    _base_headers = {
        "accept": "application/json",
        "x-apikey": os.getenv("KEY"),
    }

    def __init__(self, args: argparse.Namespace) -> None:
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

        self._args = args

        self._lock = Lock()

    @property
    def cache(self):
        return self._cache

    def _save_cache(self) -> None:
        directory_path = os.path.join(os.curdir, "cache")
        fpath = os.path.join(directory_path, "cache.json")

        try:
            with open(file=fpath, mode="w") as cached_urls:
                dump(self._cache, cached_urls)
        except Exception as exception:
            print("Unknown error occured")
            print(exception)

    def clear_cache(self):
        """
        Clear all urls in the cache
        """
        keys = list(self._cache.keys())
        if len(keys) != 0:
            for key in keys:
                self._cache.pop(key)
        if self._args.verbose:
            print("deleted all cached urls.")

        self._save_cache()

    @staticmethod
    def _process_quota(quota_response: dict) -> str:
        data: dict = quota_response.get("data")
        string = ""
        for k, v in data.items():
            user = v.get("user")
            string += f"{k}\ncalls used: {user.get('used')}\ncalls allowed: {user.get('allowed')}\n"
            string += "\n"

        return string

    def get_overall_quotas(self, apikey: str) -> str:
        """
        Send a get request to VirusTotal API to get the user quota information

        Paramaters:
            apikey: string representation of a user apikey

        Returns:
            a formatted sting depicting of the used quota by the apikey given

        Raises:
            BadRequest exception if the request was unsuccessful
        """
        headers = self._base_headers.copy()
        if self._args.apikey is not None:
            headers["x-apikey"] = self._args.apikey

        request_url = f"https://www.virustotal.com/api/v3/users/{apikey}/overall_quotas"

        response = requests.get(url=request_url, headers=headers)
        if response.status_code == 200:
            response_dict = response.json()
            return self._process_quota(response_dict)
        else:
            raise BadRequest(response=response)

    def _get_analysis_score(self, url: str) -> tuple[str, int]:
        """
        Calculate the analysis score from VirusTotal last_analysis_stats
        """

        reputation = (
            self._cache.get(url).get("data").get("attributes").get("reputation")
        )

        return url, reputation

    def _get_single_analysis(self, url: str, headers: dict) -> int:
        """
        Send a GET request to VirusTotal API to to get url analysis results

        Paramaters:
            url:
                a url to analyze using the VirusTotal API

            headers:
                the headers to pass to the request

        Raises:
            AnalysisExpired:
                if too much time has passed since the last analysis date

            AnalysisDoesNotExist:
                if the analyze data for the url does not exist in VirusTotal's data

            QuotaReacedError:
                if reached maximum quota for apikey

            BadRequest:
                if there was some other error with the request
        """

        if self._args.verbose:
            print(f"Starting to fetch analysis for url {url}")

        if url in self._cache and self._args.scan is False:

            if self._args.verbose:
                print(f"fetching from cache")

            last_analysis_epoch = self._cache[url]["data"]["attributes"][
                "last_analysis_date"
            ]
            expired = self.check_last_analysis_date(
                url=url, last_analysis_epoch=last_analysis_epoch
            )

            if expired is not None:
                raise expired

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

                last_analysis_epoch = (
                    response.json()
                    .get("data")
                    .get("attributes")
                    .get("last_analysis_date")
                )
                try:
                    self.check_last_analysis_date(
                        url=url, last_analysis_epoch=last_analysis_epoch
                    )
                except AnalysisExpired as analysis_expired:
                    exit("shit")
                # TODO

                if url not in self._cache and self._args.scan is False:
                    with self._lock:
                        self._cache[url] = response.json()
                elif self._args.scan:
                    # if forced scan then update cache with new scan
                    with self._lock:
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

    def check_last_analysis_date(self, url: str, last_analysis_epoch: str):
        # convert epoch to utc and make datetime tz aware
        last_analysis_utc = datetime.utcfromtimestamp(last_analysis_epoch).astimezone(
            pytz.UTC
        )
        now = datetime.utcnow().astimezone(tz=pytz.UTC)

        # if param days past since last analysis, clear cached link
        if now >= last_analysis_utc + timedelta(days=self._args.days):
            return AnalysisExpired(
                url=url,
                last_analysis=last_analysis_utc,
                expire_date=last_analysis_utc + timedelta(days=self._args.days),
            )

    def _scan_single_url(self, url: str, headers: dict) -> None:
        """
        Send a post request to VirusTotal API asking to scan url

        Paramaters:
            url:
                a url to scan using the VirusTotal API

            headers:
                the headers to pass to the request

        Raises:
            QuotaReacedError:
                if reached maximum quota for apikey

            BadRequest:
                if there was some other error with the request
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

    def scan_urls(self, urls: list[str]):
        """
        Scan all the urls with a progress bar

        Paramaters:
            urls: a list of urls to scan using the VirusTotal API
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

    def url_analysis(self, urls: list[str]) -> list[tuple[str, int]]:
        """
        Analyze all the urls using the VirusTotal API

        Paramaters:
            urls: a list of urls to analyze using the VirusTotal API

        Returns:
            a list of tuples containing the url and the url score\n
            i.e. [("some_url, 368), (some_other_url, 223)]
        """

        scores: list[tuple[str, int]] = []

        headers = self._base_headers.copy()

        if self._args.apikey is not None:
            headers["x-apikey"] = self._args.apikey

        with tqdm(urls, desc="getting analysis") as urls_progress:
            with ThreadPoolExecutor() as executor:
                futures = []
                for url in urls:
                    future = executor.submit(self._get_single_analysis, url, headers)
                    futures.append(future)

                for url, future in zip(urls, as_completed(futures)):
                    flag = None
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
                        self._cache.pop(url)
                        flag = True
                        print(expired)
                    except BadRequest as bad_request:
                        print(bad_request)
                    else:
                        scores.append(score)
                        urls_progress.update(1)

                    if flag:
                        flag = False

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
                                scores.append(score)
                                urls_progress.update(1)
                    sleep(0.001)
        self._save_cache()

        return scores


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        prog="VirusTotal Scanner",
        description="The program allows to check a URL with VirusTotal API",
        epilog="By, Daniel Raz",
    )

    # Define arguments so it will know how to parse
    parser.add_argument(
        "urls", nargs="*", help="One or more URLs to scan. Separated by comma"
    )

    parser.add_argument(
        "-k",
        "--apikey",
        action="store",
        help="Optionaly add your own custom apikey",
    )

    parser.add_argument("-s", "--scan", action="store_true", help="force new scan")

    parser.add_argument(
        "-v", "--verbose", action="store_true", help="verbose help message"
    )

    parser.add_argument(
        "-d",
        "--days",
        action="store",
        type=int,
        help="The amount of days to for the cache to persist",
        default=180,
    )

    parser.add_argument(
        "-c", "--clear", action="store_true", help="Clear the cached links"
    )

    parser.add_argument("-i", action="store_true", help="Prompt before removal")

    parser.add_argument(
        "-q",
        "--quota",
        action="store_true",
        help="get the quota usage for the user",
    )

    parser.add_argument(
        "-ca", "--cache", action="store_true", help="show the cached urls"
    )
    # end define args

    args = parser.parse_args()

    if args.verbose:
        print(
            args.urls,
            args.apikey,
            args.scan,
            args.verbose,
            args.days,
            args.clear,
            args.i,
        )

    vt = VirusTotal(args=args)

    if args.cache:
        print(vt.cache.keys())
        exit(0)

    if args.clear:
        choice = None
        if args.i:
            choice = (
                input("are you sure you want to clear the cache? (y/n)\n" ">>> ")
                .lower()
                .strip()
            )
            while "y" != choice != "n":
                print(f"choice {choice} not available.")
                choice = (
                    input("are you sure you want to clear the cache? (y/n)\n" ">>> ")
                    .lower()
                    .strip()
                )
        if choice == "y":
            vt.clear_cache()

    if args.scan:
        vt.scan_urls(urls=args.urls)

    if args.quota:
        print()
        print(vt.get_overall_quotas(os.getenv("KEY")))

    if len(args.urls) > 0:
        reputatuons = vt.url_analysis(urls=args.urls)
        print(*reputatuons, sep="\n")
