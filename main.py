import random


def guess(lives):
    while lives > 0:
        guess_number = int(input("Make a guess: "))
        if guess_number == number:
            print(f"You got it! The answer was {number}")
            return

        if guess_number > number:
            print("Too High")

        elif guess_number < number:
            print("Too Low")
        lives -= 1
        print(f"You have {lives} attempts remaining to guess the number")

    print("You are out of moves. You loose")


print("Welcome to the Number Guessing Game!")
number = random.randint(1, 100)
print("I'm thinking of a number between 1 and 100.")
print(number)

guess(5)