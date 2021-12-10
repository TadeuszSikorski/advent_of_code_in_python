def get_data(filename):
    with open(filename, encoding="utf-8") as file:
        return file.read().splitlines()


def transform_data(data):
    transformed_data = []

    for number in data[0].split(","):
        transformed_data.append(int(number))

    return transformed_data
