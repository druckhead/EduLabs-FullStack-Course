# Match two digits then any character then two non digits
import re


def two_digit_any_char(string: str):
    return re.match("[0-9]{2}.[^0-9]{2}", string) is not None


if __name__ == '__main__':
    # FALSE
    print(two_digit_any_char("ajklshd"))
    # TRUE
    print(two_digit_any_char("12m&^"))
    # TRUE
    print(two_digit_any_char("000we"))
    # TRUE
    print(two_digit_any_char("99^a;"))
    # FALSE
    print(two_digit_any_char("55g@6"))
    # FALSE
    print(two_digit_any_char("5a;86"))