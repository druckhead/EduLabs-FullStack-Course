from pprint import pprint


class USDConverter:
    def __init__(self, name:str):
        self.rates: dict[str, float] = dict()

    def display_all_rates(self) -> None:
        pprint(self.rates)

    def display_rate(self, currency: str) -> float :
        if currency in self.rates:
            return self.rates.get(currency)
        # does not exist in rates
        return -1

    def add_exchange_rate(self, new_currency: str, rate: float) -> bool:
        if self.rates.get(new_currency) is None:
            self.rates[new_currency.upper()] = rate
            return True
        return False

    def update_rate(self, currency, new_rate) -> bool:
        if self.rates.get(currency) is not None:
            self.rates[currency] = new_rate
            return True
        return False

    def delete_rate(self, rate_to_delete: str) -> bool:
        if rate_to_delete in self.rates:
            self.rates.pop(rate_to_delete)
            return True
        return False

    def convert(self, from_currency, to_currency, amount) -> float | None:
        if from_currency not in self.rates or to_currency not in self.rates:
            return None
        if to_currency == "USD":
            return amount / self.rates.get(from_currency)
        return amount * self.rates.get(to_currency)

