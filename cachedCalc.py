class Calculator:
    def __init__(self):
        self.cache = {}

    def _cache_operation(self, op_name):
        if op_name not in self.cache:
            self.cache[op_name] = []

    def add(self, num1, num2):
        return num1 + num2

    def subtract(self, num1, num2):
        return num1 - num2

calc = Calculator()
calc.add(2, 8)

print(calc.cache)