Python 3.6.1 (v3.6.1:69c0db5, Mar 21 2017, 18:41:36) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 

from Player import Player

class Game:
	def __init__(self, player1name, player2name):
  	"""
    Params:
    	player1name : str 
    		Name of the first player, can be empty if it refers to the computer
      player2name : str 
    		Name of the second player, can be empty if it refers to the computer
  	"""
  
		# Some constants
    
    self.nb_rows = 6
    self.nb columns = 7
    self.nbs_aligned_to_win = 4
    self.EMPTY = 0
    self.RED = 1
    self.YELLOW = 2
    self.symbols = (" ", "*", "o")
    
    # Initialize grid
    
  	self.grid = []
    for row in range(nb_rows + 2):
    	self.grid.append(list((nb_cols+2)*[0]))
      
    # Initialize players 
    
    Player1 = Player(color=RED, name=player1name)
    Player2 = Player(color=YELLOW, name=player2name)
    
	def empty_grid(self):
  	for i in range(nb_rows + 2):
    	for j in range(nb_cols + 2):
      	self.grid[i][j] = self.EMPTY
        
	def display_columns_numbers(self):
		print(" ", end=" ")  # empty space to format the screen
    for j in range(1, nb_cols + 1):  
    	print(j, end=" ")  # display the number of each column and avoid skipping a line
    print("")  # skip a line
  
	def display_grid(self):
  	print() # skip a line
    print("  ", "Connect 4") # add two spaces to 
    self.display_columns_numbers()
    for i in range(self.nb_lignes, 0, -1):
    	print(i, end=" ")
      for j in range(1, self.nb_colonnes + 1):
      	print(self.symbols[self.grid[i][j]), end=" ")
      print(i)
    self.display_columns_numbers()
    
