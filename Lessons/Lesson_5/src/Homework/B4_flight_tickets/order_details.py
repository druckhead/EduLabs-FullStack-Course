from utils import pretty_underscore_string
from seat_chooser import __is_near_window

# TODO check for code duplication

def __order_final_price(__total_price: float, __base_price: float, __extras_price: float) -> str:
    __total_price_str = f"*{f'Base Price: ${int(__base_price)}':^58}*\n"
    __total_price_str += f"*{f'Extras Price: ${__extras_price:.2f}':^58}*\n"
    __total_price_str += f"*{f'Total Price: ${__total_price:.2f}':^58}*\n"
    __total_price_str += f"{'*' * 60}"
    return __total_price_str


def __order_extras(__first_name: str, __last_name: str, __class: str, __row: int, __seat_letter: str, __meal: str,
                   __luggage_weight: float, __total_price: float) -> str:
    __extras_string = f"*{'Extras':^58}*\n"
    if __class == 'first_class':
        __extras_string += f"*{'No additional extra fees.':^58}*\n"
    elif __class == 'business_class':
        if 5 <= __row <= 7:
            __extras_string += f"*{'Lines 5-7 have an additional fee of $700':^58}*\n"
        if __is_near_window(__class, __seat_letter):
            __extras_string += f"*{'A window seat has an additional fee of $55':^58}*\n"
        if __meal == "first_class_meal":
            __extras_string += f"*{'A First Class meal has an extra fee of: $42':^58}*\n"
        if __luggage_weight > 50:
            __extras_string += f"*{f'Luggage overweight by: {(__luggage_weight - 50):.2f} KG. Fee: ${(10 * (__luggage_weight - 50)):.1f}':^58}*\n"
            'Fee: ${10 * (__luggage_weight - 50):^58'
    else:
        if 11 <= __row <= 20:
            __extras_string += f"*{'Lines 11-20 have an additional fee of $500':^58}*\n"
        elif 21 <= __row <= 40:
            __extras_string += f"*{'Lines 21-40 have an additional fee of $300':^58}*\n"
        if __is_near_window(__class, __seat_letter):
            __extras_string += f"*{'A window seat has an additional fee of $10':^58}*\n"
        if __row == 12 or __row == 22 or __row == 42:
            __extras_string += f"*{'A seat with extra leg room has an extra fee of: $15':^58}*\n"
        if __luggage_weight > 20:
            __extras_string += f"*{f'Luggage overweight by: {(__luggage_weight - 20):.2f} KG. Fee: ${10 * (__luggage_weight - 20)}':^58}*\n"
        if __meal == "first_class_meal":
            __extras_string += f"*{'A First Class meal has an extra fee of: $42':^58}*\n"
        elif __meal == "business_class_meal":
            __extras_string += f"*{'A Business Class meal has an extra fee of: $22':^58}*\n"
        elif __meal == "economy_class_meal":
            __extras_string += f"*{'An Economy Class meal has a fee of: $7':^58}*\n"
    __extras_string += f"*{' ' * 58}*\n"
    __extras_string += f"{'*' * 60}\n"
    return __extras_string


def order_details(__first_name: str, __last_name: str, __class: str, __row: int, __seat_letter: str, __meal: str,
                  __luggage_weight: float, __total_price: float, __base_price: float, __extras_price: float) -> str:
    print()
    __order_str = f"{'*' * 60}\n" \
                f"*\t\t\t\t\t\t\t\t\t AmericanAirlines\t   *\n" \
                f"*{' ' * 58}*\n" \
                f"*\tName: {__last_name}, {__first_name}{' ' * (60 - 14 - len(__first_name + __last_name))} *\n" \
                f"*\t{pretty_underscore_string(__class)}{' ' * (60 - 6 - len(pretty_underscore_string(__class)))} *\n" \
                f"*\tSeat: {__row}{__seat_letter}{' ' * (60 - 12 - (len(str(__row) + __seat_letter)))} *\n" \
                f"*\tMeal: {pretty_underscore_string(__meal)}{' ' * (60 - 11 - len(pretty_underscore_string(__meal)))}*\n" \
                f"*\tLuggage Weight: {__luggage_weight}KG{' ' * (60 - 21 - len(str(__luggage_weight)) - 2)}*\n" \
                f"*{' ' * 58}*\n" \
                f"{'*' * 60}\n"

    __order_str += __order_extras(__first_name, __last_name, __class, __row, __seat_letter, __meal, __luggage_weight,
                                __total_price)
    __order_str += __order_final_price(__total_price, __base_price, __extras_price)

    return __order_str
