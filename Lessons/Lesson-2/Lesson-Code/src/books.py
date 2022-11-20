# Implement a program that helps Jack to manage his books store.
# Jack has 3 types of books in his store - science fiction, comics, and history books.
# The initial prices for the books are as follows:

# Science fiction books: $58
# Comics: $32
# History books: $24

# There are discounts for clients who buy multiple books. The discounts work as follows:
# 10% off science fiction books if a customer buys 3 or more science fiction books.
# The discount is on science fiction books only.
# 2 + 1 on history books
# $20 off if the total price of the purchase (after applying discounts)
# if it exceeds $300 BEFORE applying the discounts

# Write a code that helps Jack to calculate the total sum of the purchase before the discount,
# the discount, and the total  a customer has to pay after the reduction of the discount.
# Your program should receive an amount of science fiction books, comics, and history books,
# and should print out the price before the discount, total discount, and price after discount.

sum_before_discount = 0.0
discount = 0.0
discounted_price = 0.0

history_count = int(input("Enter the amount of history books purchased by the customer: "))
science_fiction_count = int(input("Enter the amount of science fiction books purchased by the customer: "))
comics_count = int(input("Enter the amount of comic books purchased by the customer: "))

sum_before_discount += (science_fiction_count * 58)
if science_fiction_count >= 3:
    discounted_price += (sum_before_discount * 0.9)
sum_before_discount += (history_count * 24)
if history_count % 3 == 0:
    discounted_price += ((history_count - history_count // 3) * 24)
sum_before_discount += comics_count * 32

discounted_price += comics_count * 32

if sum_before_discount > 300:
    discounted_price -= 20

discount = sum_before_discount - discounted_price

print(f"\nthe price before discount: {sum_before_discount}\n"
      f"Total discount: {round(discount, 2)}\n"
      f"Price after discount: {round(discounted_price, 2)}")
