import math
class Shape:
    def __init__(self, length = 0, width = 0, radius = 0):
        self.length = length
        self.width = width
        self.radius = radius

class Rectangle(Shape):
    def area(self):
        return self.length * self.width

class Circle(Shape):
    def __init__(self, radius):
        super().__init__(radius = radius)
    def area(self):
        return math.pi * self.radius ** 2