class BaseBusCompanyException(Exception):
    pass


class MissingSearchKeyError(BaseBusCompanyException):
    pass


class MissingRideIDError(BaseBusCompanyException):
    pass


class BasePasswordException(Exception):
    pass


class InvalidPasswordError(BasePasswordException):
    pass


class TooManyWrongPasswordAttemptsError(BasePasswordException):
    pass
