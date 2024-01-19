import random

def guess_number_game(low, high):
    number_to_guess = random.randint(low, high)
    user_guess = None
    game_over = False

    print("Welcome to the guessing game!")
    print(f"I'm thinking of a number between {low} and {high}...")

    while not game_over:
        user_guess = int(input("Guess a number between {} and {}: ".format(low, high)))

        if user_guess < number_to_guess:
            print("Too low!")
        elif user_guess > number_to_guess:
            print("Too high!")
        else:
            print("Congratulations! You guessed the correct number.")
            game_over = True

if __name__ == "__main__":
    guess_number_game(1, 100)