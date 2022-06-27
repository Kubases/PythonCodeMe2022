class Animals:
    def __init__(self):
        self.is_animal = True


class Mammals(Animals):
    def __init__(self, num_of_legs):
        super().__init__()
        self.num_of_legs = num_of_legs


class Dog(Mammals):
    def __init__(self, fur):
        super().__init__(4)
        self.fur = fur


class Human(Mammals):
    def __init__(self, fur):
        super().__init__(2)
        self.fur = fur


me = Human(False)
print(me.num_of_legs)
print(me.is_animal)
