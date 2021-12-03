def _count_rate(report):
    counters = {}

    for numbers in report:
        position = 0

        while position < len(numbers):
            if (position, 0) not in counters.keys():
                counters[(position, 0)] = 0

            if (position, 1) not in counters.keys():
                counters[(position, 1)] = 0

            if numbers[position] == "0":
                counters[(position, 0)] += 1
            else:
                counters[(position, 1)] += 1

            position += 1

    return counters


def count_gamma_rate(report):
    gamma_rate = ""
    counters = _count_rate(report)

    for position in range(0, len(report[0])):
        if counters[(position, 0)] < counters[(position, 1)]:
            gamma_rate += "1"
        else:
            gamma_rate += "0"

    return gamma_rate


def count_epsilon_rate(gamma_rate):
    epsilon_rate = ""

    for bit in gamma_rate:
        if bit == "0":
            epsilon_rate += "1"
        else:
            epsilon_rate += "0"

    return epsilon_rate


def calculate_power_consumption(report):
    gamma_rate = count_gamma_rate(report)
    epsilon_rate = count_epsilon_rate(gamma_rate)

    return int(gamma_rate, 2) * int(epsilon_rate, 2)


def _get_numbers_that_meet_criteria(report, position, bit):
    meeting_criteria = []

    for numbers in report:
        if numbers[position] != bit:
            meeting_criteria.append(numbers)

    return meeting_criteria


def _count_rating(report, criteria):
    rating = report.copy()
    position = 0

    while position < len(rating[0]):
        counters = _count_rate(rating)

        if (
            counters[(position, 0)] < counters[(position, 1)]
            or counters[(position, 0)] == counters[(position, 1)]
        ):
            rating = _get_numbers_that_meet_criteria(rating, position, criteria[0])
        else:
            rating = _get_numbers_that_meet_criteria(rating, position, criteria[1])

        position += 1

        if len(rating) == 1:
            break

    return rating[0]


def count_oxygen_generator_rating(report):
    return _count_rating(report, ("0", "1"))


def count_CO2_scrubber_rating(report):
    return _count_rating(report, ("1", "0"))


def calculate_life_support_rating(report):
    oxygen_generator_rating = count_oxygen_generator_rating(report)
    CO2_scrubber_rating = count_CO2_scrubber_rating(report)

    return int(oxygen_generator_rating, 2) * int(CO2_scrubber_rating, 2)
