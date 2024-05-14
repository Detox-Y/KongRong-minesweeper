from functions_minesweeper import *
from random import randint

mine_num = 0
mode = input("Welcome to Minesweeper 233!\nPlease select game mode.\nE for Easy, M for Medium, H for Hard: ")
while mode.upper() not in ["E", "M", "H"]:  # Mode selection is made to not be case-sensitive here.
    mode = input("Invalid entry. Please select again: ")
else:
    if mode.upper() == "E":
        mine_num = 3  # 3 mines for easy
    elif mode.upper() == "M":
        mine_num = 4  # 4 mines for medium
    else:
        mine_num = 6  # 6 mines for hard

positions = []
i = 0
while i < mine_num:
    # Using randint to randomly generate mine positions:
    position = [randint(0, 4), randint(0, 4)]
    if position not in positions:
        positions.append(position)
        i += 1

play_game(positions)
# I tried to convert this script into an exe file, so I can send it out to my friends to have a play.
# This command is here so that the cmd window doesn't close automatically after the game is won/lost.
input("\n** Press Any Key to Exit **")
