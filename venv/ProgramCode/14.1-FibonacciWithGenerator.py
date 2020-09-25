'''Define the generator function fib_gen, which is capable of yielding values of infinite fibonacci series.
The first two values of fibonacci series are 0, and 1.
Create a generator fs from fib_gen function.
Call next method on fs and print the returned value.
Repeat the above step 3 more times, and display each returned value in a separate line.
'''

def fib_gen(limit):
    a,b = 0,1
    while a < limit :
        yield a
        a, b=b, a+b

fs = fib_gen(5)

print(fs.__next__())
print(fs.__next__())
print(fs.__next__())
print(fs.__next__())
print(fs.__next__())
print(fs.__next__())

