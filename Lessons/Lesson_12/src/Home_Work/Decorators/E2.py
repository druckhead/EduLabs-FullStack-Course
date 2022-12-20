from typing import Callable
from datetime import datetime, time


class BankExceptions(Exception):
    pass

class BankClosedError(BankExceptions):
    pass


class Bank:
    def __init__(self, bank_name):
        self.bank_name = bank_name

    @staticmethod
    def working_hours_only(func: Callable):
        def wrapped_callable(*args, **kwargs):
            curr_time = datetime.utcnow().time()
            open_time = time(hour=9, minute=0, second=0)
            close_time = time(hour=17, minute=0, second=0)
            curr_day = curr_time.strftime("%a")
            days = ['Sun', "Mon", "Tue", "Wed", "Thu"]
            if curr_day not in days:
                raise BankClosedError(f"Today is {curr_day}. The Bank is closed.\nCome back on {days[0]}")
            if open_time <= curr_time <= close_time:
                result = func(*args, **kwargs)
                return result
            else:
                raise BankClosedError(f"Time: {curr_time.strftime('%H:%M:%S')}\nBank is closed. Open Hours: {open_time}-{close_time}")

        return wrapped_callable

    @working_hours_only
    def withdraw(self, amount):
        print("called withdraw", amount)
        return amount

    @working_hours_only
    def deposit(self, amount):
        print("called deposit", amount)
        return amount

    @staticmethod
    def feedback(self, feedback_text):
        print("called feedback")


if __name__ == '__main__':
    b = Bank("godzilla")
    try:
        b.withdraw(3)
    except BankClosedError as err:
        print(err)
