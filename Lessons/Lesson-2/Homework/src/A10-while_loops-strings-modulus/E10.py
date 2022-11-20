# Generate a random number between 1 and 100 (including 1 and 100).
# Ask the user to guess the number, then tell them whether they guessed too low,
# too high, or exactly right.

import random
rand_num = random.randint(1, 100)

num_guesses = 0

user_guess = None
while user_guess != rand_num and user_guess != 'exit':
    num_guesses += 1
    user_guess = input("Guess the number between 1 and 100 or 'exit' to quit: ")
    if user_guess.isnumeric():
        user_guess = int(user_guess)
        if user_guess > rand_num:
            print("Your guess is too high! Try guessing lower")
        elif user_guess < rand_num:
            print("Your guess is too low! Try guessing higher")
        else:
            print("Your guess is just right!")

print(f"You guessed a total of {num_guesses} times")
