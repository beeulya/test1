# TODO решите задачу
import json


def task() -> float:
    filename: str = "input.json"
    with open(filename) as file:
        json_input = json.load(file)

    sum_data = sum([data["score"]*data["weight"]for data in json_input])
    return round(sum_data, 3)


print(task())
