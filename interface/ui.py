import tkinter as tk
from tkinter import ttk
from interface.base import BaseInput

class FunctionInput(BaseInput):
    def __init__(self) -> None:
        self.value = None
        self.pretty_value = None
        self.root = tk.Tk()
        self.root.title("Math Function Input")

        # Set the initial size and position of the window
        self.root.geometry("500x300")  # Width x Height
        self.root.configure(bg="#F0F0F0")  # Set background color

        # Create a frame for better organization
        self.frame = ttk.Frame(self.root, padding=30)
        self.frame.pack()

        # Expression input label
        self.label = ttk.Label(self.frame, text="Enter a function:", font=("Arial", 14, "bold"))
        self.label.grid(row=0, column=0, padx=10, pady=10)

        # Expression input entry field
        self.entry = ttk.Entry(self.frame, font=("Arial", 12))
        self.entry.grid(row=1, column=0, padx=10, pady=(20, 10))  # Increase top margin

        # Configure the input field size
        self.entry.configure(width=30)  # Adjust the width as needed

        # Submit button
        self.button = ttk.Button(self.frame, text="Enter", command=self.get_expression)
        self.button.grid(row=2, column=0, padx=10, pady=10)

        self.root.mainloop()

    def get_expression(self) -> str:
        self.pretty_value = self.entry.get()
        self.value = self.evaluate_expression(self.pretty_value)
