import math
import random


class Player():
    def __init__(self, letter):                                                                                    # Letter is x or o
        self.letter = letter

    def get_move(self, game):                                                                                      # Each player gets their next move
        pass


class HumanPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        valid_square = False
        val = None
        while not valid_square:
            square = input(self.letter + '\'s turn. Input your move from 0-9: ')
            
            # If value is not an integer or not available - error message is displayed 
            try:
                val = int(square)
                if val not in game.available_moves():
                    raise ValueError
                valid_square = True
            except ValueError:
                print('Invalid entry. Try a new input.')
        return val


class RandomComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        square = random.choice(game.available_moves())                                                           # Get a random square for player's  next move
        return square


# Minimax algorithm  
class SmartComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        if len(game.available_moves()) == 9:
            square = random.choice(game.available_moves())                                                       # Randomly choose a square
        else:
            square = self.minimax(game, self.letter)['position']                                                 # Getting the square based on the algo 
        return square

    # state - representation of the game
    def minimax(self, state, player):
        max_player = self.letter  # yourself
        other_player = 'O' if player == 'X' else 'X'

        # First check if the previous move is a winner (base case)
        # Returns position and score 
        if state.current_winner == other_player:
            return {'position': None, 'score': 1 * (state.num_empty_squares() + 1) if other_player == max_player else -1 * (
                        state.num_empty_squares() + 1)}
        elif not state.empty_squares():                                                                        # No empty squares left
            return {'position': None, 'score': 0}

        if player == max_player:
            best = {'position': None, 'score': -math.inf}                                                      # Each score should maximize
        else:
            best = {'position': None, 'score': math.inf}                                                       # Each score should minimize
        
        # 1 - make a move, try that spot
        # 2 - after making that move, recurse through possibilities using minimax
        # 3 - undo the move
        # 4 - update the dictionaries if necessary 
        for possible_move in state.available_moves():
            state.make_move(possible_move, player) # 1

            sim_score = self.minimax(state, other_player)  # 2 

            state.board[possible_move] = ' ' # 3
            state.current_winner = None
            sim_score['position'] = possible_move                                                             # this represents the move optimal next move

            if player == max_player:  # 4
                if sim_score['score'] > best['score']:
                    best = sim_score
            else:
                if sim_score['score'] < best['score']:
                    best = sim_score
        return best