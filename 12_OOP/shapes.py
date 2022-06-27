from abc import ABC, abstractmethod


class AbstractShape(ABC):
    @abstractmethod
    def sides(self):
        pass


class Triangle(AbstractShape):
    def sides(self):
        return 3


class Square(AbstractShape):
    def sides(self):
        return 4

    def area(self):
        return self.sides() * self.sides()


t = Triangle()
print(t.sides())
s = Square()
print(s.area())
