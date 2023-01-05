class MaxCreditLimitExceededError(Exception):
    def __str__(self):
        return "MaxCreditLimitExceededError"

    def __repr__(self):
        return "MaxCreditLimitExceededError"


class NoTransactionsError(Exception):
    def __str__(self):
        return "NoTransactionsError"

    def __repr__(self):
        return "NoTransactionsError"


class NotABankAccountError(Exception):
    def __str__(self):
        return "NotABankAccountError"

    def __repr__(self):
        return "NotABankAccountError"


class WrongAccountNumberError(Exception):
    def __str__(self):
        return "WrongAccountNumberError"

    def __repr__(self):
        return "WrongAccountNumberError"


class AlreadyHasAccountError(Exception):
    def __str__(self):
        return "AlreadyHasAccountError"

    def __repr__(self):
        return "AlreadyHasAccountError"
