from sys import path as syspath
from os import path as ospath

syspath.append(ospath.abspath(ospath.join("..", "..")))
from lib import get_data

syspath.append(ospath.abspath(ospath.join("")))
import solution as s

data = get_data("data.txt")

transformed_data = s.transform_data(data)

print(s.start_internal_timer(80, transformed_data))

print(s.start_internal_timer(256, transformed_data))
