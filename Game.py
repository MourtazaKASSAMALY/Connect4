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
        self.nb_columns = 7
        self.nbs_aligned_to_win = 4
        self.EMPTY = 0
        self.RED = 1
        self.YELLOW = 2
        self.symbols = (" ", "*", "o")
    
        # Initialize grid

        self.grid = []
        for row in range(self.nb_rows + 2):
            self.grid.append(list((self.nb_columns+2)*[0]))

        # Initialize players

        self.player1 = Player(color=self.RED, name=player1name)
        self.player2 = Player(color=self.YELLOW, name=player2name)
    
    def empty_grid(self):
        for i in range(self.nb_rows + 2):
            for j in range(self.nb_columns + 2):
                self.grid[i][j] = self.EMPTY
        
    def display_columns_numbers(self):
        print(" ", end=" ")  # empty space to format the screen
        for j in range(1, self.nb_columns + 1):
            print(j, end=" ")  # display the number of each column and avoid skipping a line
        print("")  # skip a line
  
    def display_grid(self):
        print("")  # skip a line
        print("  ", "Connect 4")  # add two spaces to

        self.display_columns_numbers()

        for i in range(self.nb_rows, 0, -1):
            print(i, end=" ")
            for j in range(1, self.nb_columns + 1):
                print(self.symbols[self.grid[i][j]], end=" ")
            print(i)
        self.display_columns_numbers()

    def is_move_allowed(self, column):
        """
        Params:
            col : int
            Index of the column to check for availability
        Return:
            bool: bool
            Indicates if the column is available for a player move
        """

        if column < 1 or column > self.nb_columns:  # make sure we are not off the gris
            return False
        else:  # make sure the first row of the column is empty
            return self.grid[self.nb_rows][column] == self.EMPTY

    def drop_token(self, column, player):
        """
        Params:
            col : int
            Index of the column to drop a token
            player: Player
            Player object that will own the move
        Return:
            bool: bool
            Indicates if the column is available for a player move
        """

        if not self.is_move_allowed(column):
            return False

        # find the row in which the token will fall
        row = 1
        while self.grid[row][column] != self.EMPTY:
            row = row + 1

        self.grid[row][column] = player.color
        return True
