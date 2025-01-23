import random

def get_computer_choice():
    choices = ['Rock', 'Paper', 'Scissors']
    return random.choice(choices)

def get_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 'Rock' and computer_choice == 'Scissors') or \
         (user_choice == 'Scissors' and computer_choice == 'Paper') or \
         (user_choice == 'Paper' and computer_choice == 'Rock'):
        return 'User wins!'
    else:
        return 'Computer wins!'

def rock_paper_scissors():
    user_choice = input("Enter your choice (Rock, Paper, or Scissors): ").capitalize()
    computer_choice = get_computer_choice()
    print(f"Computer choice: {computer_choice}")
    result = get_winner(user_choice, computer_choice)
    print(result)

# Example usage
rock_paper_scissors()


'''In this program:

get_computer_choice function: 

This function uses the random module to randomly select the computer's choice from the list of choices (Rock, Paper, Scissors).

get_winner function: 

This function determines the winner based on the user's choice and the computer's choice. It checks the conditions for a tie, a user win, and a computer win.

rock_paper_scissors function: 

This is the main function that gets the user's choice, 

calls the get_computer_choice function, 

and prints the computer's choice. 

It then determines and prints the result by calling the get_winner function.

Example usage: The rock_paper_scissors function is called to start the game.'''