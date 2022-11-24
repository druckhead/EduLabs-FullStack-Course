from random import randint


def name_length(fname: str, lname: str) -> int:
    return len(fname + lname)


def lottery_discount(price: float, fname: str, lname: str) -> float | str:
    rand_number = randint(1, 5)
    lucky_number = int(input("Enter a random number from 1 to 9\n"))
    chance = (rand_number * name_length(fname, lname)) % lucky_number
    if chance <= 5:
        discount = (100 - chance) / 100
        return f"Price after discount is: ${(discount * price):.2f}"
    else:
        return "You lose! You didn't get a discount\n"


def gamification(price: float, fname: str, lname: str) -> None:
    choice = input("would you like to play gamification to win a discount? (Y/N)").lower().strip()
    while choice != 'y' and choice != 'n':
        print("Invalid input.")
        choice = input("would you like to play gamification to win a discount? (Y/N)").lower().strip()
    if choice == "y":
        print()
        print(f"{lottery_discount(price,fname, lname)}")

