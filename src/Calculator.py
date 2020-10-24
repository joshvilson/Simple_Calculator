def addition(a, b):
    a = int(a)
    b = int(b)
    return b + a


def subtraction(a, b):
    a = int(a)
    b = int(b)
    return b - a


class Calculator:
    result = 0

    def __init__(self):
        pass

    def subtract(self, a, b):
        self.result = subtraction(a, b)
        return self.result

    def add(self, a, b):
        self.result = addition(a, b)
        return self.result

    def multiplication(self, a, b):
        self.result = multiplication(a, b)
        return self.result
