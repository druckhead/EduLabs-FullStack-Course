class VirusTotalExceptions(Exception):
    pass


class BadRequest(VirusTotalExceptions):
    pass

class AnalysisExpired(VirusTotalExceptions):
    pass