# Rock Paper Scissors Game - Python Beginner Project
import random
import sys

print("Welcome to Rock, Paper, Scissors!")

# Score counters
win_count = 0
lose_count = 0
tie_count = 0

while True:
    # Show current score
    print(f"{win_count} Wins, {lose_count} Losses, {tie_count} Ties")

    # Ask for player move
    while True:
        print("Choose your move: (r)ock, (p)aper, (s)cissors or (q)uit")
        user_choice = input("> ").lower()
        if user_choice in ['r', 'p', 's']:
            break
        elif user_choice == 'q':
            sys.exit()
        else:
            print("Invalid input. Please enter r, p, s, or q.")

    # Display player's move
    moves = {'r': 'ROCK', 'p': 'PAPER', 's': 'SCISSORS'}
    print(moves[user_choice], "versus...")

    # Generate computer move
    computer_choice = random.choice(['r', 'p', 's'])
    print(moves[computer_choice])

    # Decide result
    if user_choice == computer_choice:
        print("It's a tie!")
        tie_count += 1
    elif (user_choice == 'r' and computer_choice == 's') or \
         (user_choice == 'p' and computer_choice == 'r') or \
         (user_choice == 's' and computer_choice == 'p'):
        print("You win!")
        win_count += 1
    else:
        print("You lose!")
        lose_count += 1
