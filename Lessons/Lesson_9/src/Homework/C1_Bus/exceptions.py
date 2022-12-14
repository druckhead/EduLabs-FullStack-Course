class BaseBusCompanyException(Exception):
    pass

class MissingSearchKeyError(BaseBusCompanyException):
    pass

class MissingRideIDError(BaseBusCompanyException):
    pass