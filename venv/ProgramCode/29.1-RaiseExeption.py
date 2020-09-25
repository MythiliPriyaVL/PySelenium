# The raise keyword is used to raise an exception.
'''
x = -1

if x < 0:
    print(x)
    raise Exception("Sorry, no numbers below zero")

'''
x = "hello"

if type(x) is not int:
    raise TypeError("Only integers are allowed")

try:
    a = 2; b = 'hello'
    if not (isinstance(a, int)
            and isinstance(b, int)):
        raise TypeError('Two inputs must be integers.')
    c = a**b
except TypeError as e:
    print(e)