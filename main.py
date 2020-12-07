from Game import Game


if __name__ == "__main__":
    connect4game = Game("Player1", "")

    connect4game.empty_grid()
    connect4game.display_grid()

    while True:
        userinput = input("Choose a column to play: ").lower()

        if userinput == "quit" or userinput == "exit" or userinput == "break" or userinput == "stop":
            break

        column = int(userinput)

        connect4game.drop_token(column, connect4game.player1)
        connect4game.display_grid()
