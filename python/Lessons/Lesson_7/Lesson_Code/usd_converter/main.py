from USDConverter import *

if __name__ == "__main__":
    conv = USDConverter()
    conv.display_all_rates()

    conv.add_exchange_rate("USD", 1)

    conv.add_exchange_rate("NILS", 3.42)
    conv.display_all_rates()

    print(conv.display_rate("NILS"))
    print(f"{conv.convert('USD', 'NILS', 20):.2f}")
    print(f"{conv.convert('NILS', 'USD', 20):.2f}")

    conv.add_exchange_rate("YEN", 139.1)
    conv.display_all_rates()
    print(f"{conv.convert('YEN', 'USD', 20):.2f}")
    print(f"{conv.convert('USD', 'YEN', 20):.2f}")
