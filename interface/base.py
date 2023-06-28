class BaseInput:
    def __init__(self):
        self.value = None
        self.pretty_value = None

    def evaluate_expression(self, expression: str) -> str:
        return (
            expression.replace("^", "**")
            .replace("sin", "np.sin")
            .replace("cos", "np.cos")
            .replace("e ^ x", "np.exp(x)")
            .replace("log", "np.log")
        )

    def pretty_expression(self, expression: str) -> str:
        return (
            expression.replace("**", "^")
            .replace("np.sin", "sin")
            .replace("np.cos", "cos")
            .replace("np.exp(x)", "e ^ x")
            .replace("np.log", "log")
        )
