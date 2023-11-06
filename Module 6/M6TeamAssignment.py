import random

def play_game():
    # Generate a random number between 1 and 50
    random_number = random.randint(1, 50)

    # users guess and a counter for the number of guesses
    user_guess = int(input("Enter your guess (1-50): "))
    guesses = 1

    # Use a nested if-else statement to compare the user's guess to the random number
    while user_guess != random_number:
        if user_guess < random_number:
            print("Your guess is too low.")
        else:
            print("Your guess is too high.")

        user_guess = int(input("Try again: "))

        guesses += 1
    # Congratulate the user
    print("Well done you guessed it")

# Play the game
play_game()