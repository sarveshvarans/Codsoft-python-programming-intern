import random

def game():
    options = ['rock', 'paper', 'scissors']
    computer_choice = random.choice(options)
    user_score = 0
    computer_score = 0

    while True:
        user_choice = int(input("Enter your choice (1 for Rock, 2 for Paper, 3 for Scissors): "))
        
        if user_choice not in [1, 2, 3]:
            print("Invalid input. Please enter a number between 1 and 3.")
            continue

        user_choice = options[user_choice - 1]
        print(f"You chose {user_choice}.")

        if user_choice == computer_choice:
            print("It's a tie!")
        elif (user_choice == 'rock' and computer_choice == 'scissors') or \
             (user_choice == 'paper' and computer_choice == 'rock') or \
             (user_choice == 'scissors' and computer_choice == 'paper'):
            user_score += 1
            print("You win!")
        else:
            computer_score += 1
            print("Computer wins!")

        print(f"Your score: {user_score}, Computer score: {computer_score}")

        play_again = input("Do you want to play again? (yes/no): ")
        if play_again.lower() != 'yes':
            break

game()