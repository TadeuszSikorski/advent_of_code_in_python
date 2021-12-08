from sys import path as syspath
from os import path as ospath

syspath.append(ospath.abspath(ospath.join("..", "..")))
from lib import get_data

syspath.append(ospath.abspath(ospath.join("")))
import solution as s


data = get_data("data.txt")

transformed_data = s.transform_data(data)

diagram = s.get_diagram(transformed_data)

diagram = s.fill_diagram_with_straight_lines(diagram, transformed_data)

print(s.get_counted_occurrences(diagram))

diagram = s.fill_diagram_with_diagonal_lines(diagram, transformed_data)

print(s.get_counted_occurrences(diagram))