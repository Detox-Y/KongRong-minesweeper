from functions_minesweeper import *
from random import randint

mine_num = 0
mode = input("孔融在广陵王的书房门口了。\n请选择书房中有几位地雷（游戏难度）：\n简单：E 中等：M 困难：H 地狱：NB\n")
while mode.upper() not in ["E", "M", "H", "NB"]:  # Mode selection is made to not be case-sensitive here.
    mode = input("请选择: ")
else:
    if mode.upper() == "E":
        mine_num = 3  # 3 mines for easy
    elif mode.upper() == "M":
        mine_num = 4  # 4 mines for medium
    elif mode.upper() == "H":
        mine_num = 6  # 4 mines for medium
    else:
        mine_num = 9  # 6 mines for hard

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
input("\n** 按任意键退出 **")
