'''
Shift Left vs Shift Right.

1.
welcome =           "|H|e|l|l|o| |W|o|r|l|d|" # it has an ID, Type, Value
Forward Indexing =   |0|1|2|3|4|5|6|7|8|9|10|
Backward Indexing =  |-11|-10|-9|-8|-7|-6|-5|-4|-3|-2|-1|
To get 'H' from welcome
welcome[0] or welcome[-11]

2.
Initializing positive infinity and Negative infinity
x = float("inf")
y = float("-inf")

3.
Array is a collection of Homogenous data
List is a collection of Heterogenous data(Mutable-add,delete elements). eg: x=[1,'qwe',435.32]
Tuple does not support item assignment(Immutable-cannot add, delete elements). eg: x=('a',123,12.34)
Set is a mutable datatype with unordered, non duplicate values - Associated Data structure. eg: x={'apple','banana'}
Immutable set. eg: animal = frozenset(['tiger','lion'])
Dictionary is an unordered collection of datas, with Key Value pair.

4. Built-in Functions
Iteration - Navigating through each and every element in the sequence

a. Iterator - Values of an Iterator can be accessed only once and in sequential order
x = [6, 3, 1]
s = iter(x)
print(next(s))      # -> 6
print(next(s))      # -> 3
print(next(s))      # -> 1
print(next(s))      # -> StopIteration Error
(OR)
while True:
    try:
        print(next(s))
    except StopIteration:
        break

b. List Comprehensions - Apply a method to all or specific elements of a list, and filter elements of a list satisfying specific criteria.
x = [6, 3, 1]
y = [ i**2 for i in x ]   # List Comprehension expression
print(y)              # -> [36, 9, 1]

c. Generator - A Generator object is an iterator, whose values are created at the time of accessing them;
can be obtained either from a generator expression or a generator function.
x = [6, 3, 1]
g = (i**2 for i in x)  # generator expression
print(next(g))         # -> 36
(OR)
def gen_123():
    yield 12
    yield 23
    yield 34

print(type(gen_123()))
gen1 = gen_123()
print(next(gen1))  #12
print(next(gen1))  #23
print(next(gen1))  #34
print(next(gen1)) #error
(OR)
for i in gen1
    print(i)


Abstracting Data:
Direct access to data can be restricted by making required attributes or methods private,
just by prefixing it's name with one or two underscores.
An attribute or a method starting with:
    no underscores is a public one.
    a single underscore is private, however, still accessible from outside.
    double underscores is strongly private and not accessible from outside.

the following statement sets the metaclass of class A to B? ----To be done
'''
"""
Abstraction/Encapsulation/Inheritance/Polymorphism
unittest/Assert statements
Regular Expression
Working with Database
Working with Excel as TestData file
List/Dictionary Comprehension
"""

#print([ chr(i) for i in [65, 66, 67] ])

#print(itertools.takewhile(lambda x: x<5, [1,4,6,4,1])) - not working, have to check


