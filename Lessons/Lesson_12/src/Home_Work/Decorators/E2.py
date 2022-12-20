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
    def working_hours_only(days: list[str], open_time: time, close_time: time):
        def wrapper(func: Callable):
            def decorator(*args, **kwargs):
                curr_time = datetime.utcnow().time()
                curr_day = curr_time.strftime("%a")
                if curr_day not in days:
                    raise BankClosedError(
                        f"Today is {curr_day}. The Bank is closed.\n"
                        f"Come back on {days[0]} between {open_time}-{close_time}")
                if open_time <= curr_time <= close_time:
                    result = wrapper(*args, **kwargs)
                    return result
                else:
                    raise BankClosedError(
                        f"Time: {curr_time.strftime('%H:%M:%S')}\nBank is closed.\n"
                        f"Come back tomorrow between: {open_time}-{close_time}")

            return decorator

        return wrapper

    @working_hours_only(["Sun", "Mon", "Tue", "Wed", "Thu", "Fri"], time(hour=9), time(hour=17))
    def withdraw(self, amount):
        print("called withdraw", amount)
        return amount

    @working_hours_only(["Sun", "Mon", "Tue", "Wed", "Thu", "Fri"], time(hour=9), time(hour=17))
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
