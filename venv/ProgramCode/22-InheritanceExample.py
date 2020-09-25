# Inheritance describes is a kind of relationship between two or more classes,
# abstracting common details into super class and storing specific ones in the subclass.
#Every child class inherits all the behaviours exhibited by their parent class

class Person:
    #The __init__ method is a constructor and runs as soon as an object of a class is instantiated.
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

#Employee class is derived from Person
class Employee(Person):
    all_employees = []
    def __init__(self, fname, lname, empid):
        #Employee class utilizes __init __ method of the parent class Person to create its object
        Person.__init__(self, fname, lname)
        self.empid = empid
        Employee.all_employees.append(self)

p1 = Person('George', 'smith')
print(p1.fname, '-', p1.lname)
e1 = Employee('Jack', 'simmons', 456342)
e2 = Employee('John', 'williams', 123656)
print(e1.fname, '-', e1.empid)
print(e2.fname, '-', e2.empid)