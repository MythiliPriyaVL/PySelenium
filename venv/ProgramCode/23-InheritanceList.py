#Inheritance feature can be also used to extend the built-in classes like list or dict.

# The following example extends list and creates EmployeesList, which can identify employees,
# having a given search word in their first name

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

class Employee(Person):
    all_employees = EmployeesList()
    def __init__(self, fname, lname, empid):
        Person.__init__(self, fname, lname)
        self.empid = empid
        Employee.all_employees.append(self)

e1 = Employee('Jack', 'simmons', 456342)
e2 = Employee('George', 'Brown', 656721)
print(Employee.all_employees.search('or'))