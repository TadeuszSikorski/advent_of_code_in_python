import numpy as np


def _get_numbers(data):
    numbers = []

    for number in data[0].split(","):
        numbers.append(int(number))

    return numbers


def _get_boards(data):
    boards = []
    board, row = [], []

    for index in range(2, len(data)):
        if len(data[index]) != 0:
            row = data[index].split(" ")
            new_row = []

            for number in row:
                if len(number) != 0:
                    new_row.append(int(number))
            board.append(new_row)
        if len(board) == 5:
            boards.append(board)
            board = []

    return boards


def find_winning_board(data):
    numbers, boards = _get_numbers(data), _get_boards(data)
    number_out_of_range = max(numbers) + 1
    complete_row = [number_out_of_range for _ in range(0, 5)]

    for number in numbers:
        boards = np.array(boards)
        boards = np.where(boards == number, number_out_of_range, boards)

        for board in boards:
            winner_board = np.array(board)

            if complete_row in winner_board.tolist():
                winner_board = np.where(
                    winner_board == number_out_of_range, 0, winner_board
                )

                return number, winner_board.tolist()
            else:
                for index in range(0, len(winner_board)):
                    if complete_row == winner_board[:, index].tolist():
                        winner_board = np.where(
                            winner_board == number_out_of_range, 0, winner_board
                        )

                        return number, winner_board.tolist()


def find_last_winning_board(data):
    numbers, boards = _get_numbers(data), _get_boards(data)
    number_out_of_range = max(numbers) + 1
    complete_row = [number_out_of_range for _ in range(0, 5)]

    selected_numbers, breaker = [], 0
    final_statement = {}

    for board in boards:
        winner_board = np.array(board)

        for number in numbers:
            if breaker == 1:
                breaker = 0
                break

            winner_board = np.where(
                winner_board == number, number_out_of_range, winner_board
            )

            selected_numbers.append(number)

            if complete_row in winner_board.tolist():
                winner_board = np.where(
                    winner_board == number_out_of_range, 0, winner_board
                )
                final_statement[len(selected_numbers)] = (
                    selected_numbers[-1],
                    winner_board.tolist(),
                )
                selected_numbers = []
                break
            else:
                for index in range(0, len(winner_board)):
                    if complete_row == winner_board[:, index].tolist():
                        winner_board = np.where(
                            winner_board == number_out_of_range, 0, winner_board
                        )
                        final_statement[len(selected_numbers)] = (
                            selected_numbers[-1],
                            winner_board.tolist(),
                        )
                        selected_numbers = []
                        breaker = 1

    return final_statement[max(final_statement.keys())]


def calculate_final_score(winning_data):
    number, winner_board = winning_data

    sum_of_all_unmarked_numbers = sum(
        [number for row in winner_board for number in row]
    )

    return number * sum_of_all_unmarked_numbers
