# Implement a functions fizz_buzz that receives an integer num
# and returns list of strings ret_val of length num, such that:
# ret_val[i] == "FizzBuzz" if i is divisible by 3 and 5.
# ret_val[i] == "Fizz" if i is divisible by 3.
# ret_val[i] == "Buzz" if i is divisible by 5.
# ret_val[i] == i (as a string) if none of the above conditions are true.


def fizz_buzz(num: int):
    if num == 0:
        return [f'{num}']
    __list: list = []
    string = ""
    for i in range(1, num + 1):
        if i % 3 == 0 and i % 5 == 0:
            string += "Fizzbuzz"
        elif i % 3 == 0:
            string += "Fizz"
        elif i % 5 == 0:
            string += "Buzz"
        else:
            string += f"{i}"
        __list.append(string)
        string = ""
    return __list


if __name__ == "__main__":
    for i in range(0, 35):
        print(fizz_buzz(i))
        print()
