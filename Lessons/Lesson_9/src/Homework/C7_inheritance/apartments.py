from enum import Enum


class _DealState(Enum):
    open = "open"
    closed = "closed"


class _Apartment:
    __FEE = 0.2

    def __init__(self, address: str, parking_type: str, size_sqm: float, floor: int, has_balcony: bool = False,
                 is_penthouse: bool = False, is_villa: bool = False):
        self.__address = address
        self.__parking_type = parking_type
        self.__size_sqm = size_sqm
        self.__floor = floor

        self.__has_balcony = has_balcony
        self.__is_penthouse = is_penthouse
        self.__is_villa = is_villa

        self.__deal_state = _DealState.open

    def _get_deal_state(self):
        return self.__deal_state

    def _get_fee(self):
        return self.__FEE

    def close_deal(self):
        self.__deal_state = _DealState.closed

    def get_agency_fee(self):
        pass


class ApartmentForRent(_Apartment):
    def __init__(self, address: str, parking_type: str, size_sqm: float, floor: int, rent_per_month: float,
                 has_balcony: bool = False, is_penthouse: bool = False, is_villa: bool = False):
        super().__init__(address, parking_type, size_sqm, floor, has_balcony, is_penthouse, is_villa)

        self.__rent_price_per_month = rent_per_month

    def is_for_rent(self) -> bool:
        return self._get_deal_state() is self._get_deal_state().open

    def get_annual_rent_price(self) -> float:
        return self.__rent_price_per_month * 12

    def get_agency_fee(self):
        return self.__rent_price_per_month


class ApartmentForSale(_Apartment):
    def __init__(self, address: str, parking_type: str, size_sqm: float, floor: int, monthly_municipal_tax: float,
                 sale_price: float, has_balcony: bool = False, is_penthouse: bool = False, is_villa: bool = False):
        super().__init__(address, parking_type, size_sqm, floor, has_balcony, is_penthouse, is_villa)

        self.__monthly_municipal_tax = monthly_municipal_tax
        self.__sale_price = sale_price

    def is_for_sale(self) -> bool:
        return self._get_deal_state() is self._get_deal_state().open

    def get_sale_price(self):
        return self.__sale_price

    def get_annual_municipality_tax(self):
        return self.__monthly_municipal_tax * 12

    def get_agency_fee(self):
        return super()._get_fee() * self.__sale_price
