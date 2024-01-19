import random

def guess_number():
    random_number = random.randint(1, 100)
    user_guess = None

    while user_guess != random_number:
        user_guess = int(input("Guess a number between 1 and 100: "))

        if user_guess == random_number:
            print("Congratulations! You guessed the correct number.")
        elif user_guess > random_number:
            print("Your guess is too high. Try again.")
        else:
            print("Your guess is too low. Try again.")

guess_number()