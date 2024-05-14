import pytest
from functions_minesweeper import *


def test_count_adjacent_mines_in_corner():
    """
    This test checks if the function count_adjacent_mines_in_corner deals with a mine in the top left corner
    correctly.
    """
    board = [
        "X", "O", "O", "O", "O",
        "O", "O", "O", "O", "O",
        "O", "O", "O", "O", "O",
        "O", "O", "O", "O", "O",
        "O", "O", "O", "O", "O",
    ]

    count = count_adjacent_mines(board, 0, 4)
    assert (count == 0)


def test_insert_mines():
    """
    This test checks if the function insert_mines performs correctly.
    """
    board = [
        "O", "O", "O", "O", "O",
        "O", "O", "O", "O", "O",
        "O", "O", "O", "O", "O",
        "O", "O", "O", "O", "O",
        "O", "O", "O", "O", "O",
    ]
    positions = [[0, 0], [1, 1], [2, 2], [3, 3], [4, 4]]
    board = insert_mines(board, positions)
    for position in positions:
        i = position[0] * 5 + position[1]  # Change the row and column number into list index.
        assert (board[i] == "X")


def test_count_adjacent_mines():
    """
    This test checks if the function count_adjacent_mines performs correctly (counting diagonally adjacent mines too).
    """
    board = [
        "X", "O", "X", "O", "X",
        "O", "O", "O", "O", "X",
        "O", "O", "X", "O", "O",
        "O", "O", "O", "X", "O",
        "O", "O", "O", "O", "O",
    ]
    positions = [[1, 0], [3, 2], [2, 3], [1, 3]]
    for i in range(4):
        count = count_adjacent_mines(board, positions[i][0], positions[i][1])
        assert (count == i + 1)


def test_play_turn():
    """
    This test checks if the function play_turn performs correctly.
    """
    # Test case 1: Selecting a mine
    board1 = ["O", "O", "X", "O", "O",
              "O", "O", "O", "O", "O",
              "O", "X", "O", "O", "O",
              "O", "O", "O", "O", "O",
              "O", "O", "O", "O", "O"]
    row1, col1 = 0, 2
    updated_board1, mine_hit1 = play_turn(board1, row1, col1)
    assert updated_board1 == ["O", "O", "#", "O", "O",
                              "O", "O", "O", "O", "O",
                              "O", "X", "O", "O", "O",
                              "O", "O", "O", "O", "O",
                              "O", "O", "O", "O", "O"]
    assert mine_hit1 is True

    # Test case 2: Selecting an empty space with adjacent mines
    board2 = ["O", "O", "X", "O", "O",
              "O", "O", "O", "O", "O",
              "O", "X", "O", "O", "O",
              "O", "O", "O", "O", "O",
              "O", "O", "O", "O", "O"]
    row2, col2 = 1, 1
    updated_board2, mine_hit2 = play_turn(board2, row2, col2)
    assert updated_board2 == ["O", "O", "X", "O", "O",
                              "O", "2", "O", "O", "O",
                              "O", "X", "O", "O", "O",
                              "O", "O", "O", "O", "O",
                              "O", "O", "O", "O", "O"]
    assert mine_hit2 is False

    # Test case 3: Selecting an empty space without adjacent mines
    board3 = ["O", "O", "X", "O", "O",
              "O", "O", "O", "O", "O",
              "O", "X", "O", "O", "O",
              "O", "O", "O", "O", "O",
              "O", "O", "O", "O", "O"]
    row3, col3 = 4, 4
    updated_board3, mine_hit3 = play_turn(board3, row3, col3)
    assert updated_board3 == ["O", "O", "X", "O", "O",
                              "O", "O", "O", "O", "O",
                              "O", "X", "O", "O", "O",
                              "O", "O", "O", "O", "O",
                              "O", "O", "O", "O", " "]
    assert mine_hit3 is False


def test_check_win():
    """
    This test checks if the function check_win performs correctly.
    """
    # Test case 1: all squares except the mines have been checked:
    board1 = [" ", "1", "X", "2", "1",
              "1", "2", "2", "2", "X",
              "1", "X", "2", "2", "2",
              "2", "2", "2", "X", "1",
              "X", "1", "1", "1", "1"]
    result1 = check_win(board1)
    assert result1 is True

    # Test case 2: there are still squares left to be checked:
    board2 = [" ", "1", "X", "1", " ",
              "1", "1", "2", "1", " ",
              "1", "X", "2", "1", "1",
              "1", "1", "2", "X", "1",
              "O", "O", "O", "O", "O"]
    result2 = check_win(board2)
    assert result2 is False
