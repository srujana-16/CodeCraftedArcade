# Implementation of rock. paper and scissors game

import random

def play():
    user = input("Let's play rock, paper, scissors! \n\nWhat's your choice? \n Choices are:\n'r' for rock, 'p' for paper, 's' for scissors\n Enter your choice:")
    computer = random.choice(['r', 'p', 's'])

    # If it's a tie:
    if user == computer:
        return 'It\'s a tie'

    # User wins:
    if is_win(user, computer):
        return 'You won!!'

    return 'You lost :('
# Returns true if player wins
def is_win(player, opponent):
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') \
        or (player == 'p' and opponent == 'r'):
        return True

print(play())