from Game import Game
import numpy as np
import matplotlib.pyplot as plt


# --------------------------------------------------------------------------


player_index = 0
text_to_display = ""

player1input = input("Choose a name for player 1: ")
player2input = input("Choose a name for player 2: ")

connect4game = Game(player1input, player2input)
connect4game.empty_grid()

fig = plt.figure()
ax = fig.add_subplot(111)


# --------------------------------------------------------------------------

def plot_grid():
    global ax
    global connect4game
    global player_index
    global text_to_display

    grid = connect4game.grid

    ax.clear()

    ax.grid(color='k', linestyle='-', linewidth=2)
    ax.set_xlim(0, 7)
    ax.set_ylim(0, 6)

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == connect4game.RED:
                ax.plot(j-1/2., i-1/2., marker='o', color='red', markersize=30)
            if grid[i][j] == connect4game.YELLOW:
                ax.plot(j-1/2., i-1/2., marker='o', color='yellow', markersize=30)

    if connect4game.finished:
        ax.text(1, 2, text_to_display, size=20, rotation=-25,
                bbox=dict(boxstyle="square", ec=(1., 0.5, 0.5), fc=(1., 0.8, 0.8)))


# --------------------------------------------------------------------------


# Simple mouse click function to store coordinates
def onclick(event):
    global connect4game
    global player_index
    global text_to_display

    if connect4game.finished or (connect4game.EMPTY not in np.array(connect4game.grid)[1:7, 1:8]): return

    ix, iy = event.xdata, event.ydata

    # ------- 1st player -------

    if player_index == 0:
        column = int(ix) + 1
        if not connect4game.drop_token(column, connect4game.player1): player_index = (player_index - 1) % 2

        if connect4game.player1.winner:
            connect4game.finished = True
            text_to_display = "      " + connect4game.player1.name + " WINS !      "

    # ------- 2nd player -------

    elif player_index == 1:
        column = int(ix) + 1
        if not connect4game.drop_token(column, connect4game.player2): player_index = (player_index - 1) % 2

        if connect4game.player2.winner:
            connect4game.finished = True
            text_to_display = "      " + connect4game.player2.name + " WINS !      "

    # ------- Player index updated -------

    player_index = (player_index + 1) % 2

    # ------- Deals with playing against a computer -------

    if player_index == 1 and connect4game.player2.name == "Computer" and not connect4game.finished:
        column = 0  # drop_token of column = 0 will always output False
        while not connect4game.drop_token(column, connect4game.player2):
            column = np.random.randint(1, 8)
        print("Computer chooses to play at column ", column)
        player_index = (player_index + 1) % 2

        if connect4game.player2.winner:
            connect4game.finished = True
            text_to_display = "      " + connect4game.player2.name + " WINS !      "

    plot_grid()
    plt.show()
    return


# --------------------------------------------------------------------------


cid = fig.canvas.mpl_connect('button_press_event', onclick)
plot_grid()
plt.show()
