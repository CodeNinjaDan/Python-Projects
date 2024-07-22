import time
from Player import HumanPlayer, RandomComputerPlayer, ProComputerPlayer

class TicTacToe():
    def __init__(self):
        self.board = [' ' for _ in range(9)] #single list to rep a 3x3 board
        self.current_winner = None #keep track of winner

    def print_board(self):
        #getting the rows
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
            print('| ' + ' | '.join(row) + ' |')

    @staticmethod
    def print_board_nums():
        # 0 | 1 | 2 tells us what number corresponds to what box
        number_board = [[str(i) for i in range(j*3, (j+1)*3)] for j in range(3)]
        for row in number_board:
            print(' | ' + ' | '.join(row) + ' |')

    def make_move(self, square, letter):
        # if move is valid, then make the move (assign square to letter)
        # then return True, else False
        if self.board[square] == ' ':
            self.board[square] = letter
            if self.winner(square, letter):
                self.current_winner = letter
            return True
        return False 
    
    def winner (self, square, letter):
        # check rows for the winner 
        row_ind = square // 3
        row = self.board[row_ind*3 : (row_ind + 1) * 3]
        if all([spot == letter for spot in row]):
            return True
        
        # check column
        col_ind = square % 3
        column = [self.board[col_ind+i*3] for i in range(3)]
        if all([spot == letter for spot in column]):
            return True

        # check diagonals
        # only where square is an even number
        if square % 2 == 0:
            diagonal1 = [self.board[i] for i in [0, 4, 8]]
            if all([spot == letter for spot in diagonal1]):  
                return True
            diagonal2 = [self.board[i] for i in  [2, 4, 6]] 
            if all([spot == letter for spot in diagonal2]):
                return True
            
        return False

    def empty_squares(self):
        return ' ' in self.board
    
    def num_empty_squares(self):
        return self.board.count(' ')
    
    def available_moves(self):
        return [i for i, spot in enumerate(self.board) if spot == ' ']
    # moves = []
    # for (i, spot) in enumarate(self.board):
    #     # ['x', 'x', 'o'] --> [(0, 'x'), (1, 'x')]
    #     if spot == ' ':
    #        moves.append(i)
    #return moves

def play(game, x_player, o_player, print_game=True):

    if print_game:
        game.print_board_nums()

    letter = 'X' #starting letter
    # iterate while there are still empty squares
    while game.empty_squares():
        #get move from appropriate player
        if letter == 'O':
            square = o_player.get_move(game)
        else:
            square = x_player.get_move(game)
        
        if game.make_move(square, letter):
            if print_game:
                print(letter + f'makes a move to {square}')
                game.print_board()
                print('')

            if game.current_winner:
                if print_game:
                    print(letter + 'wins!')
                return letter

        letter = 'O' if letter == 'X' else 'X' # switches player 
        #  if letter == 'X'
        #      letter = "O'
        #  else:
        #      letter = 'X'
        if print_game:
          time.sleep(0.7)

    if print_game:
        print("It's a tie!")
# Computers against each other 
if __name__ == '__main__':
    x_wins = 0
    o_wins = 0
    ties = 0
    for _ in range(1000):
        x_player = RandomComputerPlayer('X')
        o_player = ProComputerPlayer('O')
        t = TicTacToe()
        result = play(t, x_player, o_player, print_game=False)
        if result == 'X':
            x_wins += 1
        elif result == 'O':
            o_wins += 1
        else:
            ties += 1
    print(f'After 1000 iterations, we see {x_wins} X wins, {o_wins} O wins, and {ties} ties')

# Human Pro computer
"""

if __name__ == '__main__':
    x_player = HumanPlayer('X')
    o_player = ProComputerPlayer('O')
    t = TicTacToe()
    play(t, x_player, o_player, print_game=True)

"""

