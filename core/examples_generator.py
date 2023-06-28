import random


class MathFunctionGenerator:
    def __init__(self):
        self.functions = []
        self.read_from_file(file_path="functions.txt")

    def create_function(self, new_function: str):
        new_function = self.evaluate_expression(expression=new_function)
        self.functions.append(new_function)

    def evaluate_expression(self, expression: str) -> str:
        return (
            expression.replace("^", "**")
            .replace("sin", "np.sin")
            .replace("cos", "np.cos")
            .replace("e ^ x", "np.exp(x)")
            .replace("log", "np.log")
        )

    def read_from_file(self, file_path: str):
        with open(file_path, "r") as file:
            [self.create_function(new_function=line) for line in file]

    def get_random_function(self) -> str:
        index = random.randint(0, len(self.functions) - 1)
        return self.functions[index]
