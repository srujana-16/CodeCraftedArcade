import math
import time
from player import HumanPlayer, RandomComputerPlayer, SmartComputerPlayer


class TicTacToe():
    def __init__(self):
        self.board = self.make_board()
        self.current_winner = None

    @staticmethod
    def make_board():
        return [' ' for _ in range(9)]                                                                           # Using a single list to represent a 3x3 board

    def print_board(self):
        for row in [self.board[i*3:(i+1) * 3] for i in range(3)]:
            print('| ' + ' | '.join(row) + ' |')

    @staticmethod
    def print_board_nums():
        # 0 | 1 | 2
        # 3 | 4 | 5
        # 6 | 7 | 8
        # Tells which number corresponds to which box on the board
        number_board = [[str(i) for i in range(j*3, (j+1)*3)] for j in range(3)]
        for row in number_board:
            print('| ' + ' | '.join(row) + ' |')


    def make_move(self, square, letter):
        # If valid move, then assign square to letter 
        if self.board[square] == ' ':
            self.board[square] = letter
            if self.winner(square, letter):
                self.current_winner = letter
            return True
        return False

    def winner(self, square, letter):
        # Check the rows 
        row_ind = math.floor(square / 3)
        row = self.board[row_ind*3:(row_ind+1)*3]
        if all([s == letter for s in row]):
            return True
        
        # Check columns 
        col_ind = square % 3
        column = [self.board[col_ind+i*3] for i in range(3)]
        if all([s == letter for s in column]):
            return True
        
        # Check diagonals 
        # Only when the square is an even number (these are the only moves for a diagonal win)
        if square % 2 == 0:
            diagonal1 = [self.board[i] for i in [0, 4, 8]]                                                      # Right diagonal
            if all([s == letter for s in diagonal1]):
                return True
            diagonal2 = [self.board[i] for i in [2, 4, 6]]                                                      # Left diagonal 
            if all([s == letter for s in diagonal2]):
                return True
        return False

    # Checks if there are empty spaces 
    def empty_squares(self):
        return ' ' in self.board

    # Returns the number of empty squares 
    def num_empty_squares(self):
        return self.board.count(' ')

    # 
    def available_moves(self):
        return [i for i, x in enumerate(self.board) if x == " "]


def play(game, x_player, o_player, print_game=True):

    if print_game:
        game.print_board_nums()

    letter = 'X'                                                                                               # Starting player 

    # Iterate until board has empty squares as loop is anyway broken when there is a winner
    while game.empty_squares():

        # Get the move from either of the player
        if letter == 'O':
            square = o_player.get_move(game)
        else:
            square = x_player.get_move(game)

        if game.make_move(square, letter):
            if print_game:
                print(letter + ' makes a move to square {}'.format(square))
                game.print_board()
                print('')

            if game.current_winner:
                if print_game:
                    print(letter + ' wins the game!')
                return letter                                                                                  #  Winner is declared, so exit the loop
            
            letter = 'O' if letter == 'X' else 'X'                                                             # Alternates between the players

        # Break to make the transitions smooth 
        time.sleep(.8)

    # Print tie when no more available moves 
    if print_game:
        print('It\'s a tie!')



if __name__ == '__main__':
    x_player = SmartComputerPlayer('X')
    o_player = HumanPlayer('O')
    t = TicTacToe()
    play(t, x_player, o_player, print_game=True)