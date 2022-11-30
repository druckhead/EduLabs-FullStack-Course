from src.Lesson_Code.usd_converter.USDConverter import USDConverter
from src.Homework.C3_Classes_bank.bank_account import BankAccount


class Bank:
    def __init__(self):
        self.converter: USDConverter = USDConverter()
        self.accounts: dict[str, BankAccount] = {}

    def add_account(self, account: BankAccount):
        if self.accounts.get(account.account_num) is None:
            self.accounts[account.account_num] = {}
        self.accounts[account.account_num] = account

    def get_account(self, account_num: str):
        return self.accounts.get(account_num)

    def get_converter(self):
        return self.converter
