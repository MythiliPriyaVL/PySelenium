"""
Define a class Circle, whose objects are initialized with radius as it's attribute.
Ensure that the object creation raises RadiusInputError, a user defined exception, when the input radius is not a number.
Use try ... except clauses.
Create a Circle c1 using the statement c1 = Circle('hello'), and execute the script.
The error message "'hello' is not a number" should be displayed to user.
"""
class RadiusInputError(Exception):
    pass

class Circle:
    def __init__(self, radius):
        try:
            #if(isinstance(radius, int)):
            if(radius is not int): #Not working, has to be debugged.
            #if (radius.isnumeric()):
            #if (radius.isdigit()):
                raise RadiusInputError
            else:
                self.radius = radius

        except RadiusInputError:
            print("'",radius,"' is not a number")

c1 = Circle('hello')
c2 = Circle(10)
print(c2.radius)
