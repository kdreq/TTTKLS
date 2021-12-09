# # Lab Tic-Tac-Toe 

# [Tic Tac Toe](https://en.wikipedia.org/wiki/Tic-tac-toe) is a game.
# Players take turns placing tokens (a 'O' or 'X') into a 3x3 grid.
# Whoever gets three in a row first wins.

# You will write a **Player** class and **Game** class to model Tic Tac Toe, and a function **main** that models gameplay taking in user inputs through REPL.


# The Player class has the following properties: 
# * **name** = *player name*
# * **token** = *'X' or 'O'*

# The Game class has the following properties:


# You can represent the board however you like, such as a 2D list, tuples, or dictionary.

# The Game class has the following methods:
# * 
# ```py
# >>> print(board)
# X| | 
# O|X|O
#  | | 
# ```



# ```py
# >>> board.move(2, 1, player_1)
#  | | 
#  | |X
#  | | 
# ```



# ```py
# X| | 
# O|X|O
#  | |X
# >>> board.calc_winner()
# X
# ```

# * `is_full()` Returns true if the game board is full.

# ```py
# X|O|X
# X|X|O
# O|O|X
# >>> board.is_full()
# True
# ```



# ```py
# X|O|X
# X|X|O
# O|O|X
# >>> board.is_game_over()
# True

# X|O|
#  | |X
#  | |
# >>> board.is_game_over()
# False
# ```
"""
Assumptions =
1. 2 live players
2.Player Class
3.Game Class

print("Let's Play Tic Tac Toe!")

class Player:
    def __init__(self, name, token):
        self.name =  name
        self.token = token 'x'  || 'o'

class Game:
    def __init__(self,boardstuff):
        self.boardstuff = boardstuff
        

user_1 = Player
user_2 = Player 
"""
# * **board** = *your representation of the board*
#`__repr__()` Returns a pretty string representation of the game board
# * `is_game_over()` Returns true if the game board is full or a player has won.
# * `calc_winner()` What token character string has won or `None` if no one has.
# * `move(x, y, player)` Place a player's token character string at a given coordinate 
# ------(top-left is 0, 0), x is horizontal position, y is vertical position.-------
# Three lists 
# row1
# 11,21,31
# row2
# 21,22,23
# row3
# 31,32,33

# [|||]
# [|||]
# [|||]

class Test:
    def __init__(self, board):
        self.board = board
    
    def __repr__(self):
        return "%s" % (self.board)
#x = Test(["x", "|", "o", "|", "x"])
x = Test(["xox"])
print(x)