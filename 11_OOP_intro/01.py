class Dog:
    def __init__(self, name, fur_colour, race):
        self.name = name
        self.fur_colour = fur_colour
        self.race = race

    def bark(self):
        print(f'{self.name} barks')

    def swing_tail(self):
        print(f'{self.name} swings its tail')


def main():
    dogs = list()
    dogs.append(Dog("Burek", "Brown", "scrub"))
    dogs.append(Dog('Dyzio', 'white', 'Coton de Tulear'))
    for row in dogs:
        row.bark()
        row.swing_tail()


if __name__ == '__main__':
    main()
