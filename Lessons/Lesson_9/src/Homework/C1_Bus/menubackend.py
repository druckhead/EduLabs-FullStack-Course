import pickle
from bestbuscompany import BestBusCompany


class Menu:

    def __init__(self, bus_company: BestBusCompany) -> None:
        self._bus_company = bus_company

    @property
    def bus_company(self) -> BestBusCompany:
        return self._bus_company

    def quit(self) -> None:
        self._save()

    def _save(self) -> None:
        try:
            with open("bus_company.pickle", 'wb') as fh:
                pickle.dump(self._bus_company, fh)
        except FileNotFoundError as err:
            print(err)
