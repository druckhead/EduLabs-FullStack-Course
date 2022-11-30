from seat_chooser import __is_near_window


def calc_price(__class: str, __row: int, __seat_letter: str, __meal: str, __luggage_weight: float) -> (
        float, float, float):
    __price = 0.0
    __extras_price = 0.0
    __base_price = 0.0

    match __class:
        case "first_class":
            __price += 4000
            __base_price = __price
        case "business_class":
            __base_price = 2300
            if 5 <= __row <= 7:
                __price += 3000
                __extras_price = 700
            elif 8 <= __row <= 10:
                __price += 2300
            if __is_near_window(__class, __seat_letter) is True:
                __price += 55
                __extras_price += 55
            if __luggage_weight > 50:
                __price += (10 * (__luggage_weight - 50))
                __extras_price += (10 * (__luggage_weight - 50))
            if __meal == "first_class_meal":
                __price += 42
                __extras_price += 42
        case "economy_class":
            __base_price = 1200
            if 11 <= __row <= 20:
                __price += 1700
                __extras_price += 500
            elif 21 <= __row <= 40:
                __price += 1500
                __extras_price += 300
            elif 41 <= __row <= 60:
                __price += 1200
            if __is_near_window(__class, __seat_letter) is True:
                __price += 10
                __extras_price += 10
            if __row == 12 or __row == 22 or __row == 42:
                __price += 15
                __extras_price += 15
            if __luggage_weight > 20:
                __price += (10 * (__luggage_weight - 20))
                __extras_price += (10 * (__luggage_weight - 20))
            if __meal == "economy_class_meal":
                __price += 7
                __extras_price += 7
            elif __meal == "business_class_meal":
                __price += 22
                __extras_price += 22
            elif __meal == "first_class_meal":
                __price += 42
            __extras_price += 42

    return __price, __extras_price, __base_price


# d = {
#     'business': {
#         'meal': {},
#         (11, 20) : {'price_extra': 1700, 'extras_price': 500,}
#     },
#     'first' :{
#
#     }
# }
#
#
# for k, v in d:
#     if __row in range(k[0], k[1]):
#         price += d['price_extra']
#         extras_price += d['extras_price']
