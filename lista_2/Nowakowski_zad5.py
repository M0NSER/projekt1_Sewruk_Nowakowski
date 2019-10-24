class Calculator:
    result = 1

    def __init__(self, number):
        self.result = number

    def add(self, number):
        self.result += number

    def difference(self, number):
        self.result -= number

    def multiply(self, number):
        self.result *= number

    def divide(self, number):
        self.result /= number

