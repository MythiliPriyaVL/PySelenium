#Polymorphism allows a subclass to override or change a specific behavior, exhibited by the parent class

class Person:
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

# Employee class with two methods getSalary and getBonus.
class Employee(Person):
    all_employees = EmployeesList()
    def __init__(self, fname, lname, empid):
        Person.__init__(self, fname, lname)
        self.empid = empid
        Employee.all_employees.append(self)
    def getSalary(self):
        return 'You get Monthly salary.'
    def getBonus(self):
        return 'You are eligible for Bonus.'

# ContractEmployee class derived from Employee.
# It overrides functionality of getSalary and getBonus methods found in it's parent class Employee.
class ContractEmployee(Employee):
    def getSalary(self):
        return 'You will not get Salary from Organization.'
    def getBonus(self):
        return 'You are not eligible for Bonus.'

e1 = Employee('Jack', 'simmons', 456342)
e2 = ContractEmployee('John', 'williams', 123656)
print(e1.getBonus())
print(e2.getBonus())