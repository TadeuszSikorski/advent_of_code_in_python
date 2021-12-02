def get_data(filename):
    with open(filename, encoding="utf-8") as file:
        return file.read().splitlines()