import random

def number_guessing_game():
    print("Welcome to the Number Guessing Game!")
    print("I have selected a random number between 1 and 100.")
    print("Try to guess it in as few attempts as possible!\n")

    # Generate a random number between 1 and 100
    random_number = random.randint(1, 100)
    attempts = 0

    while True:
        try:
            # Get user's guess
            guess = int(input("Enter your guess: "))
            attempts += 1

            if guess < random_number:
                print("Too low! Try again.")
            elif guess > random_number:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You've guessed the number in {attempts} attempts.")
                break
        except ValueError:
            print("Please enter a valid number.")

# Run the game
if __name__ == "__main__":
    number_guessing_game()
