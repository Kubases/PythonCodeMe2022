class Canis:
    paws = 4

    def __init__(self):
        print('Canis is an animal')

    def show(self):
        print('🐕 🐕 🐕 🐕 🐕 🐕 🐕 🐕')


class Dog(Canis):
    kingdom = 'Animals'

    def __init__(self, name, age, breed):
        super().__init__()
        self.name = name
        self.age = age
        self.breed = breed
        self.paws = super().paws

    def bark(self, sound):
        print(sound * self.age)

    def show(self):
        super().show()
        txt = f'My dog {self.name}, age: {self.age} is breed {self.breed}'
        print(txt)


class Fox(Canis):
    def __init__(self):
        super().__init__()
        print('create fox')
        super().show()


dyzio = Dog('Dyzio', 3, 'mops')
dyzio.show()
print(dyzio.paws)
fox = Fox()
