# Exercise 9

# Generate a random number between 1 and 9 (including 1 and 9).
# Ask the user to guess the number then tell them whether they guessed too low too high or exactly right.
# (Hint: remember to use the user input lessons from the very first exercise)
# Keep the game going until the user types “exit”
# Keep track of how many guesses the user has taken, and when the game ends, print this out.

import random

a = random.randint(1,9)
guess = 0
c = 0

while guess != a and guess != "exit":
    guess = input("Enter a guess from 1 to 9:\n")

    if guess == "exit":
        print("You have guessed", c, "times.")
        break

    guess = int(guess)
    c += 1

    if guess < a:
        print("You guessed too low.")
    elif guess > a:
        print("You guessed too high.")
    else:
        print("You guessed exactly right and it took only", c, "tries!")