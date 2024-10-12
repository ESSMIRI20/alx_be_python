import math
class Shape:
    def __init__(self, length = 0, width = 0, radius = 0):
        self.lenght = length
        self.width = width
        self.radius = radius

class Rectangle(Shape):
    def __init__(self, length, width):
        super().__init__(length = length, width = width)
    def area(self):
        return self.lenght * self.width

class Circle(Shape):
    def __init__(self, radius):
        super().__init__(radius = radius)
    def area(self):
        return math.pi * self.radius ** 2