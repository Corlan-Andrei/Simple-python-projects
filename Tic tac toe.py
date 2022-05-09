import random

# First, I need to create logic tha will hold and update information
# in this game.
# Starting with defining and displaying the board:
def display_board(board):

    print("3  " , board[6], "|", board[7], "|", board[8])
    print("  ----------")
    print("2  " , board[3], "|", board[4], "|", board[5])
    print("  ----------")
    print("1  " , board[0], "|", board[1], "|", board[2])
    print("  A  ", " B  ", "C ")


# Creating Player 1 and Player 2:
def choosing_player():

    mark = "None"

    while mark not in ["X","O"]:

        mark = input("Player one, choose between the letter X or the letter O: ").upper()

        if mark not in ["X","O"]:

            print("Uh, you might want to try again chief.")

    player_1 = mark

    # It feels silly typing out stuff like this.
    if player_1 == "X":
        player_2 = "O"
    else:
        player_2 = "X"

    return (player_1, player_2)


# Defining valid coordinates for strategic Tic Tac Toe gameplay:
def choose_coordinate():

    coord = "None"

    while coord not in ["A1", "A2", "A3", "B1", "B2", "B3", "C1", "C2", "C3"]:
        coord = input("Now, pick a coordinate: ")

        if coord not in ["A1", "A2", "A3", "B1", "B2", "B3", "C1", "C2", "C3"]:

            print("The coordinates need to be valid. Please try again.")

    return coord


# Defining vertical, horizontal and diagonal winning conditions:
def win_lose(board,mark):

        return ((board[0] == mark and board[1] == mark and board[2] == mark) or
                (board[3] == board[4] == board[5] == mark) or
                (board[6] == board[7] == board[8] == mark) or
                (board[0] == board[3] == board[6] == mark) or
                (board[1] == board[4] == board[7] == mark) or
                (board[2] == board[5] == board[8] == mark) or
                (board[0] == mark and board[4] == mark and board[8] == mark) or
                (board[2] == board[4] == board[6] == mark))


# Coin flip of who goes first:
def who_goes_first():

    if random.randint(0, 1) == 0:
        return "Player 1"

    else:
        return "Player 2"



def restart():

    return input("Do you want to play again? (Yes/No): ").lower().startswith("y")


def space_check(board, position):

    return board[position] == ' '


def tie_check(board):

    for i in range(0,10):

        if space_check(board, i):
            return False

    return True


def update_board(board,mark,coord):

    if coord == "A1":
        board[0] = mark

    elif coord == "B1":
        board[1] = mark

    elif coord == "C1":
        board[2] = mark

    elif coord == "A2":
        board[3] = mark

    elif coord == "B2":
        board[4] = mark

    elif coord == "C2":
        board[5] = mark

    elif coord == "A3":
        board[6] = mark

    elif coord == "B3":
        board[7] = mark

    elif coord == "C3":
        board[8] = mark



# With that done, time to move onto the logic used to actually play the game:
print("Welcome to Tic Tac Toe!")

while True:

    game_board = [" "] * 9
    player1, player2 = choosing_player()
    turn = who_goes_first()
    print( turn +" will go first.")

    start_game = input("Are you ready to start the game? Yes/No")

    if start_game.lower()[0] == "y":
        game_on = True

    else:
        game_on = False

    # Up to here, a game board has been created with 9 cells,
    # Players 1 and 2 have been created, as well as who goes first,
    # And, just for fun, you're given the option to start the game
    # whenever you feel like it.

    while game_on:

        if turn == "Player 1":

            display_board(game_board)
            position = choose_coordinate()
            update_board(game_board, player1, position)

            if win_lose(game_board, player1):
                display_board(game_board)
                print("Congrats on winning the match!")
                game_on = False

            # The game is on, it's Player 1's turn and we print the board,
            # ask the player to choose a coordinate, update the board afterwards,
            # and then immediately check if a winning move has been made.

            else:

                if tie_check(game_board):
                    display_board(game_board)
                    print("The board is full, the match is a tie.")
                    break

                # If a winning move has not been made, we check to see if
                # There is a tie, and if it isn't a tie, we switch to Player 2

                else:
                    turn = "Player 2"

        else:

            # Rinse and repeat the previous steps, just for Player 2 this time.

            display_board(game_board)
            position = choose_coordinate()
            update_board(game_board, player2, position)

            if win_lose(game_board, player2):
                display_board(game_board)
                print("Congrats on winning the match!")
                game_on = False

            else:

                if tie_check(game_board):
                    display_board(game_board)
                    print("The board is full, the match is a tie.")
                    break

                else:
                    turn = "Player 1"

    # When the game is done and we break out of hte while loop, see if
    # the players want to play again.

    if not restart():
        break
