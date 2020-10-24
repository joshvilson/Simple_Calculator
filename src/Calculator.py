def addition(a, b):
    a = int(a)
    b = int(b)
    return b + a


def subtraction(a, b):
    a = int(a)
    b = int(b)
    return b - a


def multiplication(a, b):
    a = int(a)
    b = int(b)
    return a * b

def division(a, b):
    a = int(a)
    b = int(b)
    return round(b / a, 9)


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

    def multiply(self, a, b):
        self.result = multiplication(a, b)
        return self.result

    def divide(self, a, b):
        self.result = division(a, b)
        return self.result
