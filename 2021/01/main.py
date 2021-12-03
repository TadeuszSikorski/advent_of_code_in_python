from sys import path as syspath
from os import path as ospath

syspath.append(ospath.abspath(ospath.join("..", "..")))
from lib import get_data

syspath.append(ospath.abspath(ospath.join("")))
import solution as s


data = get_data("data.txt")

transformed_data = s.transform_data(data)

print(s.count_number_of_times_depth_measurement_increases(transformed_data))

print(
    s.count_number_of_times_sum_of_measurements_in_sliding_window_increases(
        transformed_data
    )
)
