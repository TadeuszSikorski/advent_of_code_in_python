def transform_data(data):
    transformed_data = []

    for number in data[0].split(","):
        transformed_data.append(int(number))

    return transformed_data


def _follow_life_cycle_of_lanternfish(data):
    new_fish = 0

    for index, number in enumerate(data):
        if number != 0:
            data[index] -= 1
        else:
            data[index] = 6
            new_fish += 1

    for number in range(0, new_fish):
        data.append(8)

    return data


def start_internal_timer(number_of_day, data):
    current_day = 1
    current_state = data

    while current_day < number_of_day + 1:
        current_state = _follow_life_cycle_of_lanternfish(current_state)

        current_day += 1

    return len(current_state)
