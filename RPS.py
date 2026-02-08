# Name: Carter Guthrie
# Date: 2/8/2025
# Assignment: Lab 3
# Purpose: Rock, Paper, Scissors game with stats tracking

import random

def main():
    wins = 0
    ties = 0
    losses = 0
    
    playing = True
    
    while playing:
        # Randomly choose computer choice
        options = ['R', 'P', 'S']
        computer_choice = random.choice(options)
        
        # Prompt user for selection
        user_choice = input("Enter (R)ock, (P)aper, or (S)cissors: ").upper()
        
        # Determine winner
        if user_choice == computer_choice:
            print(f"Computer chose {computer_choice}. It's a tie!")
            ties += 1
        elif (user_choice == 'R' and computer_choice == 'S') or \
             (user_choice == 'P' and computer_choice == 'R') or \
             (user_choice == 'S' and computer_choice == 'P'):
            print(f"Computer chose {computer_choice}. You win!")
            wins += 1
        else:
            print(f"Computer chose {computer_choice}. You lose!")
            losses += 1
            
        # Ask to play again
        again = input("Play again? (y/n): ").lower()
        if again != 'y':
            playing = False

    # Print the stats
    print("\nWins \t Ties \t Losses")
    print("---- \t ---- \t ------")
    print(f"{wins} \t {ties} \t {losses}")

if __name__ == '__main__':
    main()