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


def count_number_of_times_sum_of_measurements_in_sliding_window_increases(data):
    index, counter = 0, 0

    while index + 3 < len(data):
        first_sliding_window = data[index] + data[index + 1] + data[index + 2]
        second_sliding_window = data[index + 1] + data[index + 2] + data[index + 3]
 
        if first_sliding_window < second_sliding_window:
            counter += 1

        index += 1
  
    return counter