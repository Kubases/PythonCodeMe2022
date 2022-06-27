class mammal:

    def __init__(self, name, num_of_legs, len_of_pregnancy):
        self.name = name
        self.num_of_legs = num_of_legs
        self.len_of_pregnancy = len_of_pregnancy


def main():
    horse = mammal('horse', 4, 11)
    wolf = mammal('wolf', 4, 2)


if __name__ == '__main__':
    main()
