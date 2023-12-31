import argparse

from core.drawer import Drawer
from interface.examples_generator import MathFunctionGenerator
from interface.ui import FunctionInput


class CommandManager:
    def __init__(self):
        self.is_example = self.get_args()
        if not self.is_example:
            function_input = FunctionInput()
            self.function = function_input.value
            self.pretty_value = function_input.pretty_value
        else:
            generator = MathFunctionGenerator()
            self.function = generator.get_random_function()
            self.pretty_value = generator.pretty_value
        self.drawer = Drawer()

    def get_args(self):
        parser = argparse.ArgumentParser(description="Math Function Drawer")
        parser.add_argument(
            "--example",
            "-e",
            action="store_true",
            help="Run program with random function example",
        )
        args = parser.parse_args()
        return args.example

    def run(self):
        self.drawer.set_function(function_input=self.function, pretty_value=self.pretty_value)
        self.drawer.plot_function()


if __name__ == "__main__":
    command_manager = CommandManager()
    command_manager.run()
