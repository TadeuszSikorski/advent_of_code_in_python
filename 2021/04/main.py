from sys import path as syspath
from os import path as ospath

syspath.append(ospath.abspath(ospath.join("..", "..")))
from lib import get_data

syspath.append(ospath.abspath(ospath.join("")))
import solution as s


data = get_data("data.txt")

winning_board = s.find_winning_board(data)

print(s.calculate_final_score(winning_board))

last_winning_board = s.find_last_winning_board(data)

print(s.calculate_final_score(last_winning_board))