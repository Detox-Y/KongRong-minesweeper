from pprint import pprint
from random import sample

mines = 


def initialise_board():
    """
    This function initialises the minesweeper grid.
    :param: None
    :return: The initialised minesweeper board as a list.
    :rtype: list
    """
    board0 = ["O"] * 25  # Initialises the grid to be a list of 25 "O"s.
    return board0


def display_board(board):
    """
    This function displays the in-play minesweeper list as a 5x5 grid.
    :param list board: the existing minesweeper board.
    :return: None
    """
    # Display the board first for referencing (during development only):
    # pprint(board, width=26, compact=True)
    # print()

    board_hide = board[:]  # Make a copy of the original board, so it remains unchanged.
    for i in range(len(board_hide)):
        if board_hide[i] == "X":
            board_hide[i] = "O"  # Replace the mines with "O" for display.

    pprint(board_hide, width=26, compact=True)
    return


def insert_mines(board, positions):
    """
    This function inserts mines to the board at the specified positions.
    :param list board: a list representing the board.
    :param list positions: the positions of the mines. A list of lists. The first index in each
           nested list represents the row (0-4), and the second index represents the column (0-4).
    :return: a list representing the updated board.
    """
    for position in positions:
        i = position[0] * 5 + position[1]  # Change the row and column number into list index.
        board[i] = "X"
    return board


def count_adjacent_mines(board, row, column):
    """
    This function counts the number of mines, "X", adjacent (not including diagonals) to the selected row, column
    position.
    :param list board: a list representing the in-play board
    :param int row: the row number (0-4) of the square being checked for adjacent mines.
    :param int column: the column number (0-4) of the square being checked for adjacent mines.
    :return: The number of adjacent mines.
    :rtype: int
    """
    i = row * 5 + column  # Change the row and column number into list index.
    mine_num = 0
    # Check above:
    if row != 0 and board[i - 5] == "X":
        mine_num += 1
    # Check below:
    if row != 4 and board[i + 5] == "X":
        mine_num += 1
    # Check left:
    if column != 0 and board[i - 1] == "X":
        mine_num += 1
    # Check right:
    if column != 4 and board[i + 1] == "X":
        mine_num += 1
    # Check top left:
    if row != 0 and column != 0 and board[i - 6] == "X":
        mine_num += 1
    # Check top right:
    if row != 0 and column != 4 and board[i - 4] == "X":
        mine_num += 1
    # Check below left:
    if row != 4 and column != 0 and board[i + 4] == "X":
        mine_num += 1
    # Check below right:
    if row != 4 and column != 4 and board[i + 6] == "X":
        mine_num += 1

    return mine_num


def play_turn(board, row, column):
    """
    This function plays a turn using the provided row and column on the provided board.
    If a hidden mine is selected, it will be changed to a "#" character. Otherwise, the number of mines adjacent to the
    selected position will replace the existing character. If there are no adjacent mines, a space character will be
    used.
    :param list board: a list representing the board
    :param int row: the row number of the position selected on the board
    :param int column: the column number of the position selected on the board
    :return:
        1. A list representing the updated board.
        2. A bool with a value True if a mine was selected and False otherwise.
    """
    i = row * 5 + column  # Change the row and column number into list index.
    if board[i] == "X":
        board[i] = "#"  # "#" to indicate a mine that"s been hit.
        return board, True
    elif board[i] == "O":
        mine_num = count_adjacent_mines(board, row, column)  # Check the selected square for adjacent mines.
        if mine_num == 0:
            board[i] = " "  # Space representing no adjacent mines.
            return board, False
        else:
            board[i] = str(mine_num)
            return board, False


def check_win(board):
    """
    This function determines if the player has won the game.
    This occurs when all positions that do not contain a mine have been selected.
    :param board: a list representing the board
    :type board: list
    :return: A bool representing if the game has been won (True) or has not been won (False).
    :rtype: bool
    """
    if "O" not in board:
        return True
    else:
        return False


def play_game(positions):
    """
    This function can play minesweeper from start to finish!
    :param positions: a list of lists indicating the positions that mines will be placed on the board.
    :return: None
    """
    board = initialise_board()
    # Insert mines at input positions:
    insert_mines(board, positions)
    display_board(board)
    # Start playing:
    while "#" not in board and not check_win(board):
        position = input("Where would you like to detect for mines (in row and column number): ")
        row = int(position[0])      # Assuming user input always starts with the row number and ends with the column
        column = int(position[-1])  # number here.
        play_turn(board, row, column)
        display_board(board)
    else:
        if check_win(board):
            print("You have won! All mines are now shown on the board.")
            pprint(board, width=26, compact=True)  # Display the board with mines ("X") on it.
            return
        else:
            print("You hit a mine! \n///GAME OVER///")
            pprint(board, width=26, compact=True)  # Display the board with mines ("X") on it.
            return
