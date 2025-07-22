# Simple number guessing game
import random

hidden_number = random.randint(1, 20)
print("I'm thinking of a number from 1 to 20.")

# Allow the player 6 attempts
for attempt in range(1, 7):
    print("Enter your guess:")
    user_guess = int(input("> "))

    if user_guess < hidden_number:
        print("Too low!")
    elif user_guess > hidden_number:
        print("Too high!")
    else:
        break  # Correct guess!

# Show result
if user_guess == hidden_number:
    print("Nice! You guessed it in", attempt, "tries!")
else:
    print("Out of tries! The number was", hidden_number)