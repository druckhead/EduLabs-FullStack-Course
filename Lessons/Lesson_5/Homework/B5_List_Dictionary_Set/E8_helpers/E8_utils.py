from src.B5_List_Dictionary_Set.E8_helpers.E8_consts import *


# dict structure
# catalog = {
#     1: {
#         "vehicle_type": 'private',
#         "production_year": '2009',
#         "model": "S-60",
#         "motor_type": "Petrol",
#         "color": "Green"
#     },
#     2: {
#         "vehicle_type": 'semi',
#         "production_year": '2019',
#         "model": "Vnr-900",
#         "motor_type": "Diesel",
#         "color": "Silver"
#     }
# }


def pretty_dict(_d: dict, sep: str) -> str:
    pretty_str = ""
    for key, value in _d.items():
        pretty_str += f"{key}{sep} {value}\n"

    return pretty_str


def customer_details():
    vehicle_type = input(f"\nEnter the vehicle type.\n"
                         f"{pretty_dict(VEHICLE_OPTIONS, sep='.')}\n"
                         f">>> ")

    production_year = input(f"\nEnter the year of production.\n\n"
                            f">>> ")

    model_dict = MODEL_PRIVATE if vehicle_type == "1" else MODEL_SEMI
    model = input("\nChose a model type.\n" + pretty_dict(model_dict, sep='.') + "\n>>> ")

    motor_type = input(f"\nEnter the motor type for the vehicle.\n"
                       f"{pretty_dict(MOTOR_TYPE, sep='.')}\n"
                       f">>> ")

    color = input(f"\nEnter the color of the vehicle.\n"
                  f"{pretty_dict(VEHICLE_COLORS, sep='.')}\n"
                  f">>> ")

    vehicle = dict()
    vehicle["vehicle_type"] = VEHICLE_OPTIONS[vehicle_type]
    vehicle["production_year"] = production_year
    vehicle["model"] = model_dict[model]
    vehicle["motor_type"] = MOTOR_TYPE[motor_type]
    vehicle["color"] = VEHICLE_COLORS[color]

    return vehicle


def volvo_catalog(_car_catalog_dict):
    size = len(_car_catalog_dict)
    _car_catalog_dict[size + 1] = customer_details()
    return _car_catalog_dict


def print_catalog(_d: dict) -> None:
    print("*" * 25)
    print(f"{'CATALOG': ^25}")
    for key in _d.keys():
        print("*" * 25)
        print()
        print(f"{key}.")
        print(pretty_dict(_d.get(key), sep=':'))
        print("*" * 25)


def main() -> None:
    car_catalog = dict()

    print(WELCOME_MSG)

    while True:
        choice = input(f"\nWhat would you like to do?\n"
                       f"{pretty_dict(MAIN_MENU_OPTIONS, sep='.')}\n"
                       f">>> "
                       )

        match choice:
            case '1':
                if len(car_catalog) > 0:
                    print()
                    print_catalog(car_catalog)
                else:
                    print("\nThe Volvo catalog is currently empty...")
            case '2':
                volvo_catalog(car_catalog)
            case '3':
                print(BYE_MSG)
                break
