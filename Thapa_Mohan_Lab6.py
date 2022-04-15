from geometricObject import GeometricObject
import math


class Circle(GeometricObject):
    def __init__(self,radius = 1.0, color = "white", filled = True):
        GeometricObject.__init__(self, color, filled )
        self.radius = radius 

    def __str__(self):
        return "Circle: " + "radius = " + str(self.radius) +" " +GeometricObject.__str__(self)

    def getArea(self):
        return math.pi * ((self.radius)**2)

    def getPerimeter(self):
        return 2 * math.pi * self.radius



class Triangle(GeometricObject):
    def __init__(self, side1 = 1.0, side2 = 1.0, side3 = 1.0, color = "white", filled = True):
        GeometricObject.__init__(self, color, filled )
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3
    def __str__(self):
        return "Triangle: " + "side1 = " + str(self.side1) + " " + "side2 = " + str(self.side2) + "side3 = " + str(self.side3) + " " +GeometricObject.__str__(self) 

    def getArea(self):
        s = (self.side1 + self.side2 + self.side3)/2
        area = math.sqrt(s * (s - self.side1) * (s - self.side2) * (s - self.side3))
        return area

    def getPerimeter(self):
        return self.side1 + self.side2 + self.side3


class Rectangle(GeometricObject):
    def __init__(self, side1 = 1.0, side2 = 1.0, color = "white", filled = True):
        GeometricObject.__init__(self, color, filled )
        self.side1 = side1
        self.side2 = side2
    
    def __str__(self):
        return "Rectangle: " + "side1 = " + str(self.side1) + " " + "side2 = " + str(self.side2) +  " " + GeometricObject.__str__(self) 

    def getArea(self):
        return self.side1 * self.side2

    def getPerimeter(self):
        return 2 * (self.side1 + self.side2)
    



def main():
    #Testing Circle class
    c = Circle(5, "blue", False)
    print(c)
    print()
    
    print("Entering input values for a circle")
    r = float(input('Enter value for radius: '))

    c1 = Circle(r)
    
    print(c1)
    print("%.2f" % c1.getArea())
    print("%.2f" % c1.getPerimeter())
    print(c1.getColor())
    print(c1.isFilled())

    #Testing Triangle class
    print("\nEntering input values for a triangle")
    s1 = float(input('Enter value for side1: '))
    s2 = float(input('Enter value for side2: '))
    s3 = float(input('Enter value for side3: '))
    color = input('Enter color of the triangle: ')
    filled = input('Is the triangle filled (1/0)? ')
    filled = (filled == "1")
    t1 = Triangle(s1, s2, s3, color, filled)

    print(t1)
    print("%.2f" % t1.getArea())
    print("%.2f" % t1.getPerimeter())
    print(t1.getColor())
    print(t1.isFilled())

    #Testing Rectangle class
    print("\nEntering input values for a rectangle")
    s1 = float(input('Enter value for side1: '))
    s2 = float(input('Enter value for side2: '))
    color = input('Enter color of the rectangle: ')
    filled = input('Is the rectangle filled (1/0)? ')
    filled = (filled == "1")
    r1 = Rectangle(s1, s2, color, filled)

    print(t1)
    print("%.2f" % r1.getArea())
    print("%.2f" % r1.getPerimeter())
    print(r1.getColor())
    print(r1.isFilled())

main()



