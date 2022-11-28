from datetime import datetime, date, time
from person import Person
from custom_exceptions import *
from src.Lesson_Code.usd_converter.USDConverter import USDConverter


# TODO comment code


class BankAccount:
    def __init__(self, bank_name: str, bank_branch: str, account_holder: Person, account_num: str,
                 max_credit_limit: float, is_allowed_usd: bool = False):
        self.transactions: dict[None | date, dict[None | time, dict[str, float | dict[str, float | str]]]] = {}

        self.account_holder: Person = account_holder

        self.bank_name: str = bank_name
        self.bank_branch: str = bank_branch

        self.account_num = account_num

        self.is_allowed_usd = is_allowed_usd
        if self.is_allowed_usd:
            self.usd_balance: float = 0
        else:
            self.usd_balance: float | None = None

        self.balance: float = 0
        self.max_credit_limit = max_credit_limit

    def open_us_balance(self):
        if self.is_allowed_usd:
            raise AlreadyHasAccountError
        self.is_allowed_usd = True
        self.usd_balance = 0

    def get_curr_balance(self):
        return self.balance

    def get_curr_usd_balance(self):
        if self.is_allowed_usd:
            return self.usd_balance
        return None

    def get_transaction(self, on_date: date):
        return self.transactions.get(on_date)

    def deposit(self, amount: float):
        self.balance += amount

        curr_date_time = datetime.today()
        curr_date: date = curr_date_time.date()
        curr_time: time = curr_date_time.time()

        if self.transactions.get(curr_date) is None:
            self.transactions[curr_date] = {}
        if self.transactions[curr_date].get(curr_time) is None:
            self.transactions[curr_date][curr_time] = {}
        self.transactions.get(curr_date).get(curr_time)["deposit"] = amount
        self.transactions.get(curr_date).get(curr_time)["balance_after_transaction"] = self.balance

    def withdraw(self, amount):
        if -self.max_credit_limit > self.balance - amount:
            raise MaxCreditLimitExceededError
        self.balance -= amount
        curr_date_time = datetime.today()
        curr_date: date = curr_date_time.date()
        curr_time: time = curr_date_time.time()

        if self.transactions.get(curr_date) is None:
            self.transactions[curr_date] = {}
        if self.transactions[curr_date].get(curr_time) is None:
            self.transactions[curr_date][curr_time] = {}
        self.transactions.get(curr_date).get(curr_time)["withdraw"] = (-amount)
        self.transactions.get(curr_date).get(curr_time)["balance_after_transaction"] = self.balance

    # TODO convert function
    def convert(self, converter: USDConverter, from_curr: str, to_curr: str, amount: float):
        converted = converter.convert(from_curr, to_curr, amount)
        if from_curr == "ILS":
            self.balance -= amount
            self.usd_balance += converted
        elif from_curr == "USD":
            self.usd_balance -= amount
            self.balance += converted

        curr_date_time = datetime.today()
        curr_date: date = curr_date_time.date()
        curr_time: time = curr_date_time.time()

        if self.transactions.get(curr_date) is None:
            self.transactions[curr_date] = {}
        if self.transactions[curr_date].get(curr_time) is None:
            self.transactions[curr_date][curr_time] = {}
        if self.transactions.get(curr_date).get(curr_time).get("conversion") is None:
            self.transactions.get(curr_date).get(curr_time)["conversion"] = {}
        self.transactions.get(curr_date).get(curr_time)["conversion"]["from_currency"] = from_curr
        self.transactions.get(curr_date).get(curr_time)["conversion"]["to_currency"] = to_curr
        self.transactions.get(curr_date).get(curr_time)["conversion"][f"amount_in_{from_curr}"] = amount
        self.transactions.get(curr_date).get(curr_time)["conversion"][f"converted_to_{to_curr}"] = converted
        self.transactions.get(curr_date).get(curr_time)["conversion"]["balance_after_transaction"] = self.balance
        self.transactions.get(curr_date).get(curr_time)["conversion"][
            f"usd_balance_after_transaction"] = self.usd_balance

    def transfer(self, other, account_number: str, amount: float):
        if not isinstance(other, BankAccount):
            raise NotABankAccountError
        if self.balance - amount < -self.max_credit_limit:
            raise MaxCreditLimitExceededError
        if other.account_num != account_number:
            raise WrongAccountNumberError

        curr_date_time = datetime.today()
        curr_date: date = curr_date_time.date()
        curr_time: time = curr_date_time.time()

        self.balance -= amount
        other.balance += amount

        if self.transactions.get(curr_date) is None:
            self.transactions[curr_date] = {}
        if self.transactions[curr_date].get(curr_time) is None:
            self.transactions[curr_date][curr_time] = {}
        if self.transactions.get(curr_date).get(curr_time).get("transfer") is None:
            self.transactions.get(curr_date).get(curr_time)["transfer"] = {}
        self.transactions.get(curr_date).get(curr_time)["transfer"]["to_account_num"] = account_number
        self.transactions.get(curr_date).get(curr_time)["transfer"]["amount"] = -amount
        self.transactions.get(curr_date).get(curr_time)["transfer"]["balance_after_transaction"] = self.balance

        if other.transactions.get(curr_date) is None:
            other.transactions[curr_date] = {}
        if other.transactions[curr_date].get(curr_time) is None:
            other.transactions[curr_date][curr_time] = {}
        if other.transactions.get(curr_date).get(curr_time).get("transfer") is None:
            other.transactions.get(curr_date).get(curr_time)["transfer"] = {}
        other.transactions.get(curr_date).get(curr_time)["transfer"]["from_account_num"] = self.account_num
        other.transactions.get(curr_date).get(curr_time)["transfer"]["amount"] = amount
        other.transactions.get(curr_date).get(curr_time)["transfer"]["balance_after_transaction"] = other.balance

    def get_cash_flow(self, time_unit: str, time_value: int) -> (float, float):
        income: float = 0
        outcome: float = 0

        for trans_date in self.transactions.keys():
            boolean = time_value == trans_date.month if time_unit == "month" else time_value == trans_date.year
            if boolean:
                for trans_time in self.transactions.get(trans_date):
                    if self.transactions.get(trans_date).get(trans_time).get("deposit") is not None:
                        income += self.transactions.get(trans_date).get(trans_time)["deposit"]
                    elif self.transactions.get(trans_date).get(trans_time).get("withdraw") is not None:
                        outcome += -self.transactions.get(trans_date).get(trans_time)["withdraw"]
        return income, outcome

    def __str__(self):
        acc_str = ""
        acc_str += f"***********************************\n"
        acc_str += f"Bank Name: {self.bank_name}\n"
        acc_str += f"Branch: {self.bank_branch}\n\n"
        acc_str += f"Acc. Num: {self.account_num}\n\n"
        acc_str += f"{self.account_holder}\n"
        acc_str += f"Balance: {self.balance:.2f}\n"
        if self.is_allowed_usd:
            acc_str += f"USD Balance: {self.usd_balance:.2f}\n"
        else:
            acc_str += "USD Balance: Not Active\n"
        acc_str += f"***********************************\n"
        return acc_str
