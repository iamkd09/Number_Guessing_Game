# Here we will be creating a project which is a number guessing game using python 

import random  # using random

def get_valid_guess():
    while True:
        try:
            guess = int(input("Take a guess: "))
            if 1 <= guess <= 100:
                return guess
            else:
                print("Please enter a number between 1 and 100.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def play_game():
    secret_number = random.randint(1, 100)
    attempts = 0
    max_attempts = 10

    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100. Can you guess it?")

    while attempts < max_attempts:
        guess = get_valid_guess()
        attempts += 1

        if guess == secret_number:
            print(f"Congratulations! You guessed the number in {attempts} attempts.")
            return attempts
        elif guess < secret_number:
            print("Too low, try again.")
        else:
            print("Too high, try again.")

        print(f"You have {max_attempts - attempts} attempts left.")

    print(f"Sorry, you've used all your attempts. The number was {secret_number}.")
    return None

def main():
    high_score = None

    while True:
        attempts = play_game()
        if attempts is not None:
            if high_score is None or attempts < high_score:
                high_score = attempts
                print(f"New high score: {high_score} attempts!")
        
        play_again = input("Do you want to play again? (Y/N): ").strip().lower()
        if play_again != 'y':
            print("Thank you for playing!")
            break

if __name__ == "__main__":
    main()
