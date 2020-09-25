'''
Abstraction means working with something you know how to use without knowing how it works internally.
Encapsulation allows binding data and associated methods together in a unit i.e class.

These principles together allows a programmer to define an interface for applications,
i.e. to define all tasks the program is capable to execute and their respective input and output data.

A good example is a television set. We don’t need to know the inner workings of a TV, in order to use it.
All we need to know is how to use the remote control (i.e the interface for the user to interact with the TV).
'''
class Person:
    #The __init__ method is a constructor and runs as soon as an object of a class is instantiated.
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

class EmployeesList(list):
    def search(self, name):
        matching_employees = []
        for employee in self:
            if name in employee.fname:
                matching_employees.append(employee.fname)
        return matching_employees

'''
Direct access to data can be restricted by making required attributes or methods private, 
just by prefixing it's name with one or two underscores.

An attribute or a method starting with:
no underscores is a public one.
a single underscore is private, however, still accessible from outside.
double underscores is strongly private and not accessible from outside.
'''
class Employee(Person):
    all_employees = EmployeesList()
    def __init__(self, fname, lname, empid):
        Person.__init__(self, fname, lname)
        self.__empid = empid #strongly private and not accessible from outside
        Employee.all_employees.append(self)

    #empid attribute of Employee class is made private and is accessible outside the class only using the method getEmpid.
    def getEmpid(self):
        return self.__empid

e1 = Employee('Jack', 'simmons', 456342)
print(e1.fname, e1.lname) #Jack simmons
print(e1.getEmpid()) #456342
print(e1.__empid) #AttributeError: Employee instance has no attribute '__empid'