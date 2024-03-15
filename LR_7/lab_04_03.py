import math

class Geometric:
    def calculateArea(self):
        print("Calculating area")
    
class Square(Geometric):
    def __init__(self, a):
        self.side = a
    def _perimeter(self):
        print("Perimeter of Square {}: {}\n".format(self.side, self.side*4))
    def calculateArea(self):
        print("Area of Square {}: {}\n".format(self.side, pow(self.side,2)))
        
class Circle(Geometric):
    def __init__(self, radius):
        self.__radius = radius 
    
    def calculateArea(self):
        area = math.pi * (self.__radius ** 2)
        print("Area of Circle with radius {}: {:.2f}\n".format(self.__radius, area))
        
geom = Geometric()
geom.calculateArea()

sq = Square(5)
sq.calculateArea()
sq._perimeter()

circle = Circle(3)
circle.calculateArea()

print("Check subclass: ", issubclass(Square, Geometric))
print("Check subclass: ", issubclass(Circle, Geometric))
print("Check instance sq->Square: ", isinstance(sq, Square))
print("Check instance sq->Geometric: ", isinstance(sq, Geometric))
print("Check instance circle->Circle: ", isinstance(circle, Circle))
print("Check instance circle->Geometric: ", isinstance(circle, Geometric))
print("Check instance circle->dict: ", isinstance(circle, dict))

#11