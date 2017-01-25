class Calculator:
    def __init__(self):
        self.cache = {}

    def _cache_operation(self, op_name, x, y, result):
        if op_name not in self.cache:
            self.cache[op_name] = []

        for previous_x, previous_y, res in self.cache[op_name]:
            if previous_x == x and previous_y == y:
                return res

        self.cache[op_name].append((x, y, result))

        return result

    def add(self, num1, num2):
        return self._cache_operation('add', num1, num2, (num1 + num2))

    def subtract(self, num1, num2):
        return self._cache_operation('subtract', num1, num2, (num1 - num2))

calc = Calculator()
calc.add(2, 8)
calc.subtract(5, 4)
calc.subtract(5, 4)
calc.subtract(5, 4)

print(calc.cache)