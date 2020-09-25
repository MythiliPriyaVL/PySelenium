"""
https://www.python-course.eu/python3_magic_methods.php

Improvise the class definition of Point such that any Point object is displayed in the format point : (x, y, z).
Hint : Define the method __str__ inside the class Point.
Print the object p1 using statement print(p1).

Define the method distance, inside the class Point, which determines distance between two points.
Use formula distance = sqrt( (x1-x2)**2 + (y1-y2)**2 + (z1 -z2)**2 ).
Create two Point objects p2 = Point(4, 5, 6), p3 = Point(-2, -1, 4) and determine distance of p2 from p3 using defined distance method.
Print the distance value.

Improvise Point class definition such that,

adding any two Point objects using + operator, results in a new Point object with corresponding x, y and z values being added.
Hint : Define __add__ method inside the class Point.
Execute the statement print(p2 + p3)
"""
import math

class Point:
    def __init__(self,x,y,z):
        self.x =x
        self.y =y
        self.z = z

    def __str__(self):
        return "point : ({},{},{})".format(self.x,self.y,self.z)

    def distance(self,other):
        dist = math.sqrt((self.x-other.x)**2+(self.y-other.y)**2+(self.z-other.z)**2)
        return dist

    def __add__(self,other):
        rx=self.x+other.x
        ry=self.y+other.y
        rz=self.z+other.z
        return Point(rx,ry,rz)

p1 = Point(4,2,9)
print(p1)

p2 = Point(4,5,6)
p3 = Point(-2,-1,4)

print(str(p2.distance(p3)))

print(p2+p3)