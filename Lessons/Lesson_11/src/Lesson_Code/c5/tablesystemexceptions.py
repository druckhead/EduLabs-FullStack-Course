class _TableSystemException(Exception):
    pass


class TableIsAlreadyReservedError(_TableSystemException):
    pass


class TableOverbookedError(_TableSystemException):
    pass


class TableIsAlreadyAvailableError(_TableSystemException):
    pass


class TableNotFoundError(_TableSystemException):
    pass
