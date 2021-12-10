def _calculate_cost_of_moving_to_best_position(positions, best_position):
    cost_moving_to_best_position = 0

    for position in positions:
        if position > best_position:
            cost_moving_to_best_position += position - best_position
        else:
            cost_moving_to_best_position += best_position - position

    return cost_moving_to_best_position


def calculate_least_cost_of_moving_to_best_position(positions):
    best_positions = {}

    for best_position in range(min(positions), max(positions) + 1):
        if best_position not in best_positions.keys():
            best_positions[best_position] = 0

        best_positions[best_position] = _calculate_cost_of_moving_to_best_position(
            positions, best_position
        )

    return min(best_positions.values())


def _calculate_newest_cost_of_moving_to_best_position(positions, best_position):
    newest_cost_moving_to_best_position = 0

    for position in positions:
        if position > best_position:
            newest_cost_moving_to_best_position += sum(
                [number for number in range(1, (position - best_position) + 1)]
            )
        else:
            newest_cost_moving_to_best_position += sum(
                [number for number in range(1, (best_position - position) + 1)]
            )

    return newest_cost_moving_to_best_position


def calculate_cheapest_cost_of_moving_to_best_position(positions):
    best_positions = {}

    for best_position in range(min(positions), max(positions) + 1):
        if best_position not in best_positions.keys():
            best_positions[best_position] = 0

        best_positions[
            best_position
        ] = _calculate_newest_cost_of_moving_to_best_position(positions, best_position)

    return min(best_positions.values())
