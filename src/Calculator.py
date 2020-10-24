def addition(a, b):
    return a + b

def substraction(a, b):
    return a - b

class Calculator:
    result = 0

    def __init__(self):
        pass

    def add(self, a, b):
        self.result = addition(a, b)
        return self.result

    def substract(self, a, b):
        self.result = substraction(a, b)
        return self.result
