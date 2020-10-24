import math

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
    a = float(a)
    b = float(b)
    return round(b / a, 9)


def square(a):
    a = int(a)
    return a * a


def square_root(a):
    a = int(a) ** 0.5
    if a > 10:
        a = round(a, 8)
    else:
        a = round(a, 9)
    return a


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

    def square(self, a):
        self.result = square(a)
        return self.result

    def square_root(self, a):
        self.result = square_root(a)
        return self.result
