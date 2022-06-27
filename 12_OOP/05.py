from abc import ABC, abstractmethod


class Vehicle(ABC):
    @abstractmethod
    def show_vehicle(self):
        pass


class Bike(Vehicle):
    def __init__(self):
        self.num_of_wheels = 2
        self.type_of_document = 'Not required'

    def show_vehicle(self):
        print(self.num_of_wheels, self.type_of_document)


class Car(Vehicle):
    def __init__(self):
        self.num_of_wheels = 4
        self.type_of_document = 'B1'

    def show_vehicle(self):
        print(self.num_of_wheels, self.type_of_document)


class Lorry(Vehicle):
    def __init__(self):
        self.num_of_wheels = 6
        self.type_of_document = 'C1'

    def show_vehicle(self):
        print(self.num_of_wheels, self.type_of_document)


def main():
    b = Bike()
    c = Car()
    l = Lorry()
    vehicle_list = [b, c, l]
    for vehicle in vehicle_list:
        vehicle.show_vehicle()


if __name__ == '__main__':
    main()
