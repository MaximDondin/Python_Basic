from abc import ABC, abstractmethod
import math

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        c_area = math.pi * self.radius ** 2
        return round(c_area, 2)
    def __str__(self):
        return f'Площадь круга с радиусом: {self.radius}\n{round(math.pi, 2)} * {self.radius}^2 = {self.area()}\n'

class Rectangle(Shape):
    def __init__(self, height, width):
        self.height = height
        self.width = width
    def area(self):
        r_area = self.height * self.width
        return round(r_area, 2)
    def __str__(self):
        return f'Площадь прямоугольника со сторонами: {self.height} и {self.width}\n{self.height} * {self.width} = {self.area()}\n'


class Triangle(Shape):
    def __init__(self, height, footing):
        self.height = height
        self.footing = footing
    def area(self):
        r_area = (self.height * self.footing) / 2
        return round(r_area, 2)
    def __str__(self):
        return f'Площадь треугольника с основанием: {self.footing} и высотой проведенной к этому основанию: {self.height}\n({self.footing} * {self.height}) / 2 = {self.area()}\n'

сircle = Circle(2)
rectangle = Rectangle(4, 5)
triangle = Triangle(7, 10)
print(сircle)
print(rectangle)
print(triangle)