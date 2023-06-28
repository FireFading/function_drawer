import random

from interface.base import BaseInput


class MathFunctionGenerator(BaseInput):
    def __init__(self):
        self.functions = []
        self.value = None
        self.pretty_value = None
        self.read_from_file(file_path="functions.txt")

    def create_function(self, new_function: str):
        new_function = self.evaluate_expression(expression=new_function)
        self.functions.append(new_function)

    def read_from_file(self, file_path: str):
        with open(file_path, "r") as file:
            [self.create_function(new_function=line) for line in file]

    def get_random_function(self) -> str:
        index = random.randint(0, len(self.functions) - 1)
        self.value = self.functions[index]
        self.pretty_value = self.pretty_expression(self.functions[index])
        return self.value
