from dataclasses import dataclass


class BMI:
    def __init__(self, weight, height):
        self.weight = weight
        self.height = height

    def calculate(self):
        return self.weight / self.height ** 2


a = BMI(80, 2)
print(a.calculate())


@dataclass
class BMI2:
    weight: float
    height: float

    def calculate(self):
        return self.weight / self.height ** 2


b = BMI2(80, 2)
print(a.calculate())
