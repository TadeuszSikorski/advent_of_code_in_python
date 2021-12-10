from sys import path as syspath
from os import path as ospath

syspath.append(ospath.abspath(ospath.join("..", "..")))
from lib import get_data, transform_data

syspath.append(ospath.abspath(ospath.join("")))
import solution as s


data = get_data("data.txt")

transformed_data = transform_data(data)

print(s.calculate_least_cost_of_moving_to_best_position(transformed_data))

print(s.calculate_cheapest_cost_of_moving_to_best_position(transformed_data))
