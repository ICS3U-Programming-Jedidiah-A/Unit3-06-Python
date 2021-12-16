#!/usr/bin/env python3
# Created By: Jedidiah
# Date: Dec 14, 2021
# This program guesses a number between 1 and 10.
import random


def main():
    # set the correct number
    correct = random.randint(1, 10)

    # get user input
    user_number_string = input("Enter your number: ")
    print()

    # error checking
    try:
        # convert user number to int
        user_number = int(user_number_string)
        # check the numbers is equal to correct
        if user_number == correct:
            print("you guessed right")
        # check the numbers is not equal to hidden
        elif user_number <= -1:
            print("number must be between 1 and 10.")
        elif user_number >= 10:
            print("number must be between 1 and 10.")
        else:
            print("The correct answer is")
            print(correct)
    except Exception:
        print("This was not a number")
    finally:
        print("Thanks for playing")


if __name__ == "__main__":
    main()
