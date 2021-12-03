from sys import path as syspath
from os import path as ospath

syspath.append(ospath.abspath(ospath.join("..", "..")))
from lib import get_data

syspath.append(ospath.abspath(ospath.join("")))
import solution as s


data = get_data("data.txt")

print(s.calculate_power_consumption(data))

print(s.calculate_life_support_rating(data))
