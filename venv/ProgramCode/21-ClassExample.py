#Example of a Class
'''
A Class is a template which contains
    instructions to build an object.
    methods that can be used by the object to exhibit a specific behaviour.
'''
class Person:
    'Represents a person.'
    def __init__(self, fname, lname):
        'Initialises two attributes of a person.'
        self.fname = fname
        self.lname = lname

p1 = Person('George', 'Smith')
#Output of print on object p1, tell you what class it belongs to and hints on memory address it is referenced to
print(p1)   # -> '<__main__.Person object at 0x0A...>'
print(p1.fname, '-', p1.lname)

class Person1:
    pass
p1 = Person1()
#The value which is set to an attribute can be anything: a Python primitive, a built-in data type, another object.
#It can even be a function or a class.
p1.fname = 'Jack'
p1.lname = 'Simmons'
print(p1.fname, '-', p1.lname)  # -> 'Jack - Simmons'

help(Person)