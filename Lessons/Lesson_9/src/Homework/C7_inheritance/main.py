from apartments import ApartmentForSale, ApartmentForRent

if __name__ == "__main__":
    a = ApartmentForRent("a", "indoor", 30, 1, 11_000)
    print(a.is_for_rent())
    a.close_deal()
    print(a.is_for_rent())
    print(f"Annual Rent: {a.get_annual_rent_price()}")
    print(f"Agency Fee: {a.get_agency_fee()}")

    print()

    a2 = ApartmentForSale("b", "outdoor garage", 50, 10, 1000, 10_000_000, True, True)
    print(a2.is_for_sale())
    a2.close_deal()
    print(a2.is_for_sale())
    print(f"Annual Municipality Tax: {a2.get_annual_municipality_tax()}")
    print(f"Agency Fee: {a2.get_agency_fee()}")
