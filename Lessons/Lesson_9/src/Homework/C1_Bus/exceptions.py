class BaseBusCompanyException(Exception):
    pass


class MissingSearchKeyError(BaseBusCompanyException):
    def __init__(self):
        super().__init__(f"No search key was given.\n"
                         f"Can't search without a search key")


class RideIDDoesntExistError(BaseBusCompanyException):
    def __init__(self, arg):
        super().__init__(f"Ride ID doesn't exist.\n"
                         f"{arg} is not an available ride ID in our bus route")


class BasePasswordException(Exception):
    pass


class InvalidPasswordError(BasePasswordException):
    def __init__(self):
        super().__init__(f"Incorrect password. Try Again")


class TooManyWrongPasswordAttemptsError(BasePasswordException):
    def __init__(self):
        super().__init__(f"Maximum wrong sign-in attempts have been attempted.\nYou have not been signed in.")


class BaseInputError(ValueError):
    pass

class NotALineNumberError(BaseInputError):
    def __init__(self, arg):
        super().__init__(f"Invalid input of: {arg}. Expected numeric line number")

class NotEnoughStopsError(BaseInputError):
    def __init__(self, arg):
        super.__init__(f"{arg} is not enough stops")

class NotAValidDelayError(BaseInputError):
    def __init__(self, arg):
        super.__init__(f"{arg} is not a valid delay in minutes")


class BaseKeyError(Exception):
    pass


class LineDoesntExistError(BaseKeyError):
    def __init__(self, arg):
        super().__init__(f"Invalid line number for bus routes\n"
                         f"Line #{arg} is not available at our company.")


class OriginDoesntExistError(BaseKeyError):
    def __init__(self, arg):
        super().__init__(f"Invalid Origin in bus routes\n"
                         f"{arg} is not available in our bus routes at the moment.")


class DestinationDoesntExistError(BaseKeyError):
    def __init__(self, arg):
        super().__init__(f"Invalid Destination in bus routes\n"
                         f"{arg} is not available in our bus routes at the moment.")


class BusStopDoesntExistError(BaseKeyError):
    def __init__(self, arg):
        super().__init__(f"Invalid but stop in bus routes\n"
                         f"bus stop at {arg} is not available in our bus routes at the moment.")
