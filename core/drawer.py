import matplotlib.pyplot as plt
import numpy as np


class Drawer:
    def __init__(self, function_input: str | None = None) -> None:
        self.function_input = function_input
        self.pretty_value = None

    def set_function(self, function_input: str, pretty_value: str):
        self.function_input = function_input
        self.pretty_value = pretty_value

    def plot_function(self):
        # Create x values from -10 to 10
        x = np.linspace(-10, 10, 400)

        try:
            # Evaluate the user-defined function for each x value
            y = eval(self.function_input)
            # Plot the graph
            self.draw(x=x, y=y)

        except Exception:
            print("Invalid function input. Please try again.")

    def draw(self, x: list, y: list):
        plt.plot(x, y)
        plt.xlabel("x")
        plt.ylabel("f(x)")
        plt.title(f"Graph of the function: {self.pretty_value}")
        plt.grid(True)
        plt.show()
