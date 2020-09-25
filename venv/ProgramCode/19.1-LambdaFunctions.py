"""
A lambda function is a small anonymous function.
A lambda function can take any number of arguments, but can only have one expression.
x = lambda a, b, c : a + b + c
print(x(5, 6, 2))
"""

#function that takes one argument, and that argument will be multiplied with an unknown number
def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2) #function that always doubles the number you send in
mytripler = myfunc(3) #function that always triples the number you send in

print(mydoubler(11))
print(mytripler(11))

print(itertools.dropwhile(lambda x: x<5, [1,4,6,4,1]))