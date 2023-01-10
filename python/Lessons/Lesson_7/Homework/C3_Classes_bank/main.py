from bank import Bank
from bank_account import BankAccount

from person import Person

from pprint import pprint

from datetime import datetime

if __name__ == "__main__":
    bank = Bank()
    bank.converter.add_exchange_rate("ILS", 1)
    bank.converter.add_exchange_rate("USD", 0.29)

    p = Person("8271610", "Captain Hook", "The Magical NeverLand", "05934783742")
    acc = BankAccount("HaPo-alim", "626", p, "0928137", 5000)

    bank.add_account(acc)

    print(bank.get_account("0928137"))
    pprint(bank.get_account('0928137').get_transaction(datetime.today().date()))

    bank.get_account("0928137").deposit(10_000)

    bank.get_account("0928137").withdraw(2_500)

    bank.get_account("0928137").deposit(2_123)

    print("\n\n")

    p1 = Person("64928364", "Peter Pan", "The Magical NeverLand", "05972822199")
    acc1 = BankAccount("Le-umi", "320", p, "123456789", 15_000)
    bank2 = Bank()
    bank2.add_account(acc1)

    print("The transactions for the chosen date are")
    pprint(bank.get_account('0928137').get_transaction(datetime.today().date()))
    print()
    print("The transactions for the chosen date are")
    pprint(bank2.get_account('123456789').get_transaction(datetime.today().date()))

    print("\n\n")

    bank.get_account("0928137").transfer(bank2.get_account("123456789"), "123456789", 2512.24)

    print("The transactions for the chosen date are\n")
    pprint(bank.get_account('0928137').get_transaction(datetime.today().date()))
    print()
    print("The transactions for the chosen date are\n")
    pprint(bank2.get_account('123456789').get_transaction(datetime.today().date()))

    print("\n\n")

    bank.get_account("0928137").open_us_balance()
    bank.get_account("0928137").convert(bank.get_converter(), "ILS", "USD", 100)
    print("The transactions for the chosen date are\n")
    pprint(bank.get_account('0928137').get_transaction(datetime.today().date()))

    print("\n\n")

    print(bank.get_account("0928137"))

    time_unit = "month"
    time_value = 11
    monthly_in_out = bank.get_account("0928137").get_cash_flow(time_unit, time_value)
    print(f"For {time_unit} {time_value}\n"
          f"{time_unit}ly income: {monthly_in_out[0]}\n"
          f"{time_unit}ly outcome: {monthly_in_out[1]}")
