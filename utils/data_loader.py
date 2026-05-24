import json


def load_test_data(path):

    with open(path) as file:
        return json.load(file)