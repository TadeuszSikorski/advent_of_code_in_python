def transform_data(data):
    transformed_data = []
    
    for line in data:
        direction, number = line.split()
      
        transformed_data.append(tuple([direction, int(number)]))

    return transformed_data


def multiply_horizontal_position_and_depth(data):
    horizontal_position, depth = 0, 0

    for line in data:
        if "forward" == line[0]:
            horizontal_position += line[1]
        
        if "down" == line[0]:
            depth += line[1]
        if "up" == line[0]:
            depth -= line[1]
    
    return horizontal_position * depth


def multiply_horizontal_position_and_depth_from_new_rules(data):
    horizontal_position, depth = 0, 0
    aim = 0

    for line in data:
        if "forward" == line[0]:
            horizontal_position += line[1]
            depth += aim * line[1]
        
        if "down" == line[0]:
            aim += line[1]
        if "up" == line[0]:
            aim -= line[1]
    
    return horizontal_position * depth