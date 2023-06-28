import tkinter as tk

from interface.base import BaseInput


class FunctionInput(BaseInput):
    def __init__(self) -> None:
        self.value = None
        self.pretty_value = None
        self.root = tk.Tk()
        self.root.title("Math Function Input")

        # Expression input label
        self.label = tk.Label(self.root, text="Enter a function:")
        self.label.pack()

        # Expression input entry field
        self.entry = tk.Entry(self.root)
        self.entry.pack()

        # Submit button
        self.button = tk.Button(self.root, text="Enter", command=self.get_expression)
        self.button.pack()
        self.root.mainloop()

    def get_expression(self) -> str:
        self.pretty_value = self.entry.get()
        self.value = self.evaluate_expression(self.pretty_value)
