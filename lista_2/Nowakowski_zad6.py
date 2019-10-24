import math

from lista_2.Nowakowski_zad5 import Calculator


class ScienceCalculator(Calculator):

    def __init__(self, number):
        super().__init__(number)

    def element(self):
        super().result = super().result * super().result

    def power(self, i):
        super().result = math.pow(super().result, i)


calc = ScienceCalculator(8)
calc.add(2)
print(calc.result)
