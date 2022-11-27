class TooMuchFuelException(Exception):
    def __str__(self):
        return "TooMuchFuelException"


class NegativeFuelAmountException(Exception):
    def __str__(self):
        return "NegativeFuelAmountException"


class NegativeKMDrivenException(Exception):
    def __str__(self):
        return "NegativeKMDriven"


class DriveTooLongException(Exception):
    def __str__(self):
        return "DriveTooLongException"
