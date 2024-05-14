from pprint import pprint
from random import sample

mines = ["文 丑", "张 闿", "袁 基", "左 慈", "孙 策", "张道陵", "甘 宁", "郭 嘉", "贾 诩"]


def initialise_board():
    """
    This function initialises the minesweeper grid.
    :param: None
    :return: The initialised minesweeper board as a list.
    :rtype: list
    """
    board0 = ["O O O"] * 36  # Initialises the grid to be a list of 25 "O"s.
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
        if board_hide[i] in mines:
            board_hide[i] = "O O O"  # Replace the mines with "O" for display.

    pprint(board_hide, width=55, compact=True)
    return


def insert_mines(board, positions):
    """
    This function inserts mines to the board at the specified positions.
    :param list board: a list representing the board.
    :param list positions: the positions of the mines. A list of lists. The first index in each
           nested list represents the row (0-4), and the second index represents the column (0-4).
    :return: a list representing the updated board.
    """
    mine_num = len(positions)
    mines_in_play = sample(mines, mine_num)
    counter = 0
    for position in positions:
        i = position[0] * 6 + position[1]  # Change the row and column number into list index.
        board[i] = mines_in_play[counter]
        counter += 1
    return board, mines_in_play


def count_adjacent_mines(board, row, column, mines_in_play):
    """
    This function counts the number of mines, "X", adjacent (not including diagonals) to the selected row, column
    position.
    :param list board: a list representing the in-play board
    :param int row: the row number (0-4) of the square being checked for adjacent mines.
    :param int column: the column number (0-4) of the square being checked for adjacent mines.
    :param list mines_in_play: the mines
    :return: The number of adjacent mines.
    :rtype: int
    """
    i = row * 6 + column  # Change the row and column number into list index.
    mine_num = 0
    # Check above:
    if row != 0 and board[i - 6] in mines_in_play:
        mine_num += 1
    # Check below:
    if row != 5 and board[i + 6] in mines_in_play:
        mine_num += 1
    # Check left:
    if column != 0 and board[i - 1] in mines_in_play:
        mine_num += 1
    # Check right:
    if column != 4 and board[i + 1] in mines_in_play:
        mine_num += 1
    # Check top left:
    if row != 0 and column != 0 and board[i - 7] in mines_in_play:
        mine_num += 1
    # Check top right:
    if row != 0 and column != 5 and board[i - 5] in mines_in_play:
        mine_num += 1
    # Check below left:
    if row != 5 and column != 0 and board[i + 5] in mines_in_play:
        mine_num += 1
    # Check below right:
    if row != 4 and column != 4 and board[i + 7] in mines_in_play:
        mine_num += 1

    return mine_num


def play_turn(board, row, column, mines_in_play):
    """
    This function plays a turn using the provided row and column on the provided board.
    If a hidden mine is selected, it will be changed to a "#" character. Otherwise, the number of mines adjacent to the
    selected position will replace the existing character. If there are no adjacent mines, a space character will be
    used.
    :param list board: a list representing the board
    :param int row: the row number of the position selected on the board
    :param int column: the column number of the position selected on the board
    :param list mines_in_play: the mines
    :return:
        1. A list representing the updated board.
        2. A bool with a value True if a mine was selected and False otherwise.
    """
    i = row * 6 + column  # Change the row and column number into list index.
    if board[i] in mines_in_play:
        board[i] = "告 退"  # "#" to indicate a mine that"s been hit.
        return board, True
    elif board[i] == "O O O":
        # Check the selected square for adjacent mines:
        mine_num = count_adjacent_mines(board, row, column, mines_in_play)
        if mine_num == 0:
            board[i] = "     "  # Space representing no adjacent mines.
            return board, False
        else:
            board[i] = "  " + str(mine_num) + "  "
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
    if "O O O" not in board:
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
    board0, mines_in_play = insert_mines(board, positions)
    mine_board = board0[:]
    display_board(board0)
    # Start playing:
    while "告 退" not in board and not check_win(board0):
        position = input("下一步去往（请输入 0~5 的行数与列数）：")
        row = int(position[0])      # Assuming user input always starts with the row number and ends with the column
        column = int(position[-1])  # number here.
        play_turn(board0, row, column, mines_in_play)
        display_board(board0)
    else:
        if check_win(board0):
            print("文丑、张闿、袁基、左慈、孙策、张道陵、甘宁、郭嘉、贾诩等人都不在的话，我就入内了。")
            pprint(mine_board, width=55, compact=True)  # Display the board with mines ("X") on it.
            return
        else:
            print("此人乃妖孽！在下告退！\n///GAME OVER///")
            pprint(board, width=55, compact=True)  # Display the board with mines ("X") on it.
            return
