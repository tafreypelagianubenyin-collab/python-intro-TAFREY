# PEP 8 style
import random

number = random.randint(1, 100)
attempts = 0

while True:
    guess = int(input("Guess the number between 1 and 100: "))
    attempts += 1

    if guess > number:
        print("Too high")
    elif guess < number:
        print("Too low")
    else:
        print("Correct!")
        print("Number of attempts:", attempts)
        break