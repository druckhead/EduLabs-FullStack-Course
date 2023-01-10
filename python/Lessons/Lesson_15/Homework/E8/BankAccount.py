import threading
from functools import wraps


def lock_process(lock_type: str):
    def lock_process_wrapper(func):
        @wraps(func)
        def lock_process_decorator(*args, **kwargs):
            def get_lock(self):
                lock = None
                if lock_type == "write":
                    lock = self._wlock
                elif lock_type == "read":
                    lock = self._rlock
                return lock

            deposit_lock = get_lock(args[0])
            with deposit_lock:
                func(*args, **kwargs)

        return lock_process_decorator

    return lock_process_wrapper


class BankAccount:
    __CREDIT_LIMIT = 0

    def __init__(self, id_num: int, name: str):
        self.name = name
        self.id_num = id_num

        self.balance = 0.0
        self.transactions_list = []
        self._rlock = threading.Lock()
        self._wlock = threading.Lock()

    @lock_process(lock_type="write")
    def deposit(self, amount: int) -> None:
        """
        Deposit the amount in to the account balance
        :param amount:
        """
        self.balance += amount
        self.transactions_list.append(('deposit', amount))

    @lock_process(lock_type="write")
    def withdraw(self, amount: int):
        if self.balance - amount < self.__CREDIT_LIMIT:
            raise ValueError(f"{amount} causes to go under credit limit"
                             f": {self.__CREDIT_LIMIT}")
        self.balance -= amount
        self.transactions_list.append(('withdraw', amount))

    @lock_process(lock_type="read")
    def get_balance(self):
        return self.balance


if __name__ == '__main__':
    my_account = BankAccount(123456, "Israel Israeli")


    def multiple_transactions_deposit(account: BankAccount):
        for i in range(100, 2000000, 10):
            account.deposit(i)


    def multiple_transactions_withdraw(account: BankAccount):
        for i in range(100, 2000000, 10):
            account.withdraw(i)


    t1 = threading.Thread(target=multiple_transactions_deposit, args=(my_account,))
    t2 = threading.Thread(target=multiple_transactions_deposit, args=(my_account,))
    t3 = threading.Thread(target=multiple_transactions_withdraw, args=(my_account,))
    t4 = threading.Thread(target=multiple_transactions_withdraw, args=(my_account,))

    t1.start()
    t2.start()
    t3.start()
    t4.start()

    t1.join()
    t2.join()
    t3.join()
    t4.join()

    assert my_account.balance == 0, \
        f"Expected balance: 0, received: {my_account.balance}"
    assert len(my_account.transactions_list) == 799960, \
        f"Expected transactions: 799960, received: {len(my_account.transactions_list)}"
