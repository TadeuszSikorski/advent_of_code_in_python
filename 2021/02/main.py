from sys import path as syspath
from os import path as ospath

syspath.append(ospath.abspath(ospath.join("..", "..")))
from lib import get_data

syspath.append(ospath.abspath(ospath.join("")))
import solution as s


data = get_data("data.txt")

transformed_data = s.transform_data(data)

print(s.multiply_horizontal_position_and_depth(transformed_data))

print(s.multiply_horizontal_position_and_depth_from_new_rules(transformed_data))