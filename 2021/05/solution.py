import numpy as np


def transform_data(data):
    transformed_data, new_line_segment = [], []

    for line in data:
        line = line.split(" -> ")

        for line_segment in line:
            new_line_segment.append(
                tuple(int(number) for number in line_segment.split(","))
            )

        transformed_data.append(tuple(new_line_segment))
        new_line_segment = []

    return transformed_data


def get_diagram(lines):
    size = np.amax(np.array(lines)) + 1

    return np.array([[0 for _ in range(0, size)] for _ in range(0, size)])


def _get_array(first, second):
    if first < second:
        result = np.array([index for index in range(first, second + 1)], dtype=np.intp)
    else:
        result = np.array(
            [index for index in reversed(range(second, first + 1))], dtype=np.intp
        )

    return result


def _fill_lines_with_variable_rows(diagram, first, second):
    (x1, y1), (x2, y2) = first, second

    if y1 == y2:
        rows = _get_array(x1, x2)
        columns = np.array([y1], dtype=np.intp)

        diagram[rows, columns] += 1

    return diagram


def _fill_lines_with_variable_columns(diagram, first, second):
    (x1, y1), (x2, y2) = first, second

    if x1 == x2:
        rows = np.array(x1, dtype=np.intp)
        columns = _get_array(y1, y2)

        diagram[rows, columns] += 1

    return diagram


def _add_straight_lines_to_diagram(diagram, first, second):
    diagram = _fill_lines_with_variable_rows(diagram, first, second)

    diagram = _fill_lines_with_variable_columns(diagram, first, second)

    return diagram


def fill_diagram_with_straight_lines(diagram, lines):
    for coordinates in lines:
        diagram = _add_straight_lines_to_diagram(
            diagram, coordinates[0], coordinates[1]
        )

    return diagram


def checkit(first, second):
    checker = []

    for x, y in zip(first, second):
        checker.append((x, y))

    return checker


def _add_diagonal_lines_to_diagram(diagram, first, second):
    (x1, y1), (x2, y2) = first, second

    if x1 == y1 and x2 == y2:
        rows = _get_array(x1, x2)
        columns = _get_array(y1, y2)

        diagram[rows, columns] += 1
    elif x1 != x2 and y1 != y2:
        rows = _get_array(x1, x2)
        columns = _get_array(y1, y2)

        diagram[rows, columns] += 1

    return diagram


def fill_diagram_with_diagonal_lines(diagram, lines):
    for coordinates in lines:
        diagram = _add_diagonal_lines_to_diagram(
            diagram, coordinates[0], coordinates[1]
        )

    return diagram


def get_counted_occurrences(diagram):
    unique, counts = np.unique(diagram, return_counts=True)
    counted_occurrences = dict(zip(unique, counts))
    amount_of_points = 0

    for k in counted_occurrences.keys():
        if k > 1:
            amount_of_points += counted_occurrences[k]

    return amount_of_points
