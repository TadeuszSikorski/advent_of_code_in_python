from sys import path as syspath
from os import path as ospath

syspath.append(ospath.abspath(ospath.join("..", "..")))
from lib import get_data

syspath.append(ospath.abspath(ospath.join("")))
import solution as s


data = get_data("data.txt")

print(s.check_floor(data[0]))

print(s.check_position(data[0], -1))
