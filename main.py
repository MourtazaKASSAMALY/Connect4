from Game import Game
import numpy as np


if __name__ == "__main__":

    player1input = input("Choose a name for player 1: ")
    player2input = input("Choose a name for player 2: ")

    connect4game = Game(player1input, player2input)

    connect4game.empty_grid()

    player_index = 0

    while True:
        if player_index == 0:
            print("   ", connect4game.player1.name, end="")  # add two spaces to
            connect4game.display_grid()

            column = 0  # drop_token of column = 0 will always return False
            while not connect4game.drop_token(column, connect4game.player1):
                userinput = input("Choose a column to play: ").lower()
                if userinput == "quit" or userinput == "exit" or userinput == "break" or userinput == "stop": break
                column = int(userinput)

            if connect4game.player1.winner:
                connect4game.display_grid()
                print("***************************")
                print("      ", connect4game.player1.name, " WINS !      ")
                print("***************************")
                break

        elif player_index == 1:
            print("   ", connect4game.player2.name, end="")  # add two spaces to
            connect4game.display_grid()

            column = 0  # drop_token of column = 0 will always return False
            while not connect4game.drop_token(column, connect4game.player2):

                if connect4game.player2.name != "Computer":
                    userinput = input("Choose a column to play: ").lower()
                    if userinput == "quit" or userinput == "exit" or userinput == "break" or userinput == "stop": break
                    column = int(userinput)
                else:
                    column = np.random.randint(1, 8)
                    print("Computer chooses to play at column ", column)

            if connect4game.player2.winner:
                connect4game.display_grid()
                print("***************************")
                print("      ", connect4game.player2.name, " WINS !      ")
                print("***************************")
                break

        player_index = (player_index + 1) % 2

        print('\n', '--------------------------------------', '\n')
