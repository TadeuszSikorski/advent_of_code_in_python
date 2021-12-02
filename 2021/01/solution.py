def transform_data(data):
    transformed_data = []
    
    for line in data:
        transformed_data.append(int(line))

    return transformed_data


def count_number_of_times_depth_measurement_increases(data):
    index, counter = 0, 0
  
    while index + 1 < len(data):
        if data[index] < data[index + 1]:
            counter += 1

        index += 1
  
    return counter


def _count_sum_of_sliding_window(data, indices):
    return data[indices[0]] + data[indices[1]] + data[indices[2]]


def count_number_of_times_sum_of_measurements_in_sliding_window_increases(data):
    index, counter = 0, 0

    while index + 3 < len(data):
        first_indices = [index, index + 1, index + 2]
        second_indices = [index + 1, index + 2, index + 3]
 
        if _count_sum_of_sliding_window(data, first_indices) < _count_sum_of_sliding_window(data, second_indices):
            counter += 1

        index += 1
  
    return counter