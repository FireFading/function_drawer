import tkinter as tk


class FunctionInput:
    def __init__(self) -> None:
        self.value = None
        self.root = tk.Tk()
        self.root.title("Math Function Input")

        # Expression input label
        self.label = tk.Label(self.root, text="Enter a function:")
        self.label.pack()

        # Expression input entry field
        self.entry = tk.Entry(self.root)
        self.entry.pack()

        # Submit button
        self.button = tk.Button(self.root, text="Enter", command=self.evaluate_expression)
        self.button.pack()
        self.root.mainloop()

    def evaluate_expression(self) -> str:
        expression = self.entry.get()
        expression = (
            expression.replace("^", "**")
            .replace("sin", "np.sin")
            .replace("cos", "np.cos")
            .replace("e ^ x", "np.exp(x)")
            .replace("log", "np.log")
        )
        self.value = expression
