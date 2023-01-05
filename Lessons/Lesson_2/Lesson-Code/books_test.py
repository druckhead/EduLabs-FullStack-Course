import random

tests = []
n = 10
# create a list with a set of 10 tuples containing the book amounts
# i.e (history, science fiction, comics)

# create a list of length n tuples
for i in range(n):
    tests.append((random.randint(0, 15), random.randint(0, 15), random.randint(0, 15)))

print("\nCalculate the values according to the data provided in each box"
      " and compare your answers to the answers printed")

for test in tests:
    sum_before_discount = 0.0
    discount = 0.0
    discounted_price = 0.0

    # assign book count to variables from each tuple in the list according to test iteration
    history_count = test[0]
    science_fiction_count = test[1]
    comics_count = test[2]

    # -------------------------------- NOT INCLUDING INPUTS -------------------------------------
    # -------------------------------- NOT INCLUDING PRINTS -------------------------------------
    # ------------------------------  ENTER YOUR CODE BELOW -------------------------------------

    # -------------------------------------------------------------------------------------------

    # PRINT THE DATA FOR EACH TEST
    print(f"\n{tests.index(test) + 1}\n--------------------------------------------------------------------")
    print(f"(history count: {history_count}, "
          f"science fiction count: {science_fiction_count}, "
          f"comic book count: {comics_count})\n"
          )
    # PRINT YOUR ANSWERS
    # DON'T FORGET TO CHANGE VARIABLE NAMES TO MATCH YOURS
    print(f"the price before discount: {sum_before_discount}\n"
          f"Total discount: {round(discount, 2)}\n"
          f"Price after discount: {round(discounted_price, 2)}"
          )

    print("--------------------------------------------------------------------")
