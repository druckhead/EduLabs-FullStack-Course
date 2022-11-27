from custom_exceptions import *


class Vehicle:
    def __init__(self, manufacturer: str, fuel_capacity: float, max_fuel_capacity: float, fuel_consumption: float,
                 km_driven: float = 0):
        self.manufacturer = manufacturer
        self.fuel_capacity = fuel_capacity
        self.max_fuel_capacity = max_fuel_capacity
        self.fuel_consumption = fuel_consumption
        self.km_driven = km_driven

    def fill_tank(self, amount: float):
        if amount <= 0:
            raise NegativeFuelAmountException()
        if amount + self.fuel_capacity > self.max_fuel_capacity:
            raise TooMuchFuelException()
        self.fuel_capacity += amount

    def drive(self, km_driven: float):
        if km_driven < 0:
            raise NegativeKMDrivenException
        if self.fuel_capacity - ((1 / self.fuel_consumption) * km_driven) < 0:
            raise DriveTooLongException
        self.fuel_capacity -= ((1 / self.fuel_consumption) * km_driven)
        self.km_driven += km_driven


class Car(Vehicle):
    def __init__(self, manufacturer: str, fuel_capacity: float, max_fuel_capacity: float, fuel_consumption: float):
        super().__init__(manufacturer, fuel_capacity, max_fuel_capacity, fuel_consumption)


class Truck(Vehicle):
    def __init__(self, manufacturer: str, fuel_capacity: float, max_fuel_capacity: float, fuel_consumption: float):
        super().__init__(manufacturer, fuel_capacity, max_fuel_capacity, fuel_consumption)


class Plane(Vehicle):
    def __init__(self, manufacturer: str, fuel_capacity: float, max_fuel_capacity: float, fuel_consumption: float):
        super().__init__(manufacturer, fuel_capacity, max_fuel_capacity, fuel_consumption)


if __name__ == "__main__":
    mazda3 = Car("Mazda", 0, 45, 15.5)
    print(f"The current capacity is: {mazda3.fuel_capacity}L")
    mazda3.fill_tank(30)
    print("Fill 30 liters")
    print(f"The current capacity is: {mazda3.fuel_capacity}L")
    # mazda3.drive(400)
    # print(f"Tried to drive 400km and failed, the capacity is still: {mazda3.fuel_capacity}L")
    mazda3.drive(350)
    print(f"Drove 350km, the current capacity is: {mazda3.fuel_capacity:.2f}L")

    print()

    try:
        mazda3.drive(150)
        print("Drove 100KM")
    except DriveTooLongException:
        print("You are trying to drive too long")

    print(f"The current capacity is: {mazda3.fuel_capacity:.2f}L")



