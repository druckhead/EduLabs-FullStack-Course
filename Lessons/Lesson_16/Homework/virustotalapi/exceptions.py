from requests import Response
from datetime import datetime


class VirusTotalExceptions(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)


class BadRequest(VirusTotalExceptions):
    def __init__(self, response: Response) -> None:
        super().__init__(f"Request received bad response from server\n"
                         f"{response.status_code}: {response.text}"
                         )
        
class AnalysisDataDoesNotExist(VirusTotalExceptions):
    def __init__(self, url: str) -> None:
        super().__init__(f"No analysis found for: {url}")


class AnalysisExpired(VirusTotalExceptions):
    def __init__(self, url: str, last_analysis: datetime, expire_date: datetime) -> None:
        super().__init__(f"Cache for: {url} expired. "
                         f"{abs((last_analysis - expire_date).days)} days ago.\n"
                         f"Last analysis date: {last_analysis}\n"
                         f"Expire date: {expire_date}"
                         )
