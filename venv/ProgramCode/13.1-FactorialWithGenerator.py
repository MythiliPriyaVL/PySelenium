'''
Define the generator function factorial_gen, which is capable of yielding factorial values of natural numbers.

Create a generator fs from factorial_gen.

Ensure, the first two values to be yielded by fs are 1 and 1, corresponding to factorial of 0 and 1 respectively.
Call next method on fs and print the returned value.
Repeat the above step 3 more times, and display each returned value in a separate line.

'''

def fac_gen(limit):
    a,fac = 1,1
    while True :
        yield fac
        fac *= a
        a += 1

fs = fac_gen(5)

print(fs.__next__())
print(fs.__next__())
print(fs.__next__())
print(fs.__next__())
print(fs.__next__())
print(fs.__next__())