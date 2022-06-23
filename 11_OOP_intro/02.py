class Flowers:
    kingdom = 'Plantae'

    def __init__(self, color, species, flowering_season):
        self.color = color
        self.species = species
        self.flowering_season = flowering_season

    def show(self):
        print(f'{self.species} of {self.color} color, which flowers in {self.flowering_season} from kingdom: {self.kingdom}')


def main():
    flower_list = list()
    flower_list.append(Flowers('white', "orchid", 'summer'))
    flower_list.append(Flowers('yellow', 'tulip', 'spring'))
    for row in flower_list:
        row.show()


if __name__ == '__main__':
    main()
