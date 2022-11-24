from os import system

from greeting import print_greeting
from customer_details import get_name
from flight_class import get_customer_class
from seat_chooser import choose_row, choose_seat
from meal_chooser import choose_meal
from luggage import get_luggage_weight
from price_calc import calc_price
from order_details import order_details
from discount import gamification

if __name__ == "__main__":
    # ensure same tabsize on different machines
    system("tabs -4")

    print_greeting()

    first_name, last_name = get_name()

    customer_class: str = get_customer_class()

    row: int = choose_row(customer_class)

    seat_letter: str = choose_seat(customer_class)

    meal: str = choose_meal(customer_class)

    luggage_weight: float = get_luggage_weight()

    total_price, extras_price, base_price = calc_price(customer_class, row, seat_letter, meal, luggage_weight)

    print(order_details(first_name, last_name, customer_class, row, seat_letter, meal, luggage_weight, total_price,
                        base_price, extras_price))

    gamification(total_price, first_name, last_name)