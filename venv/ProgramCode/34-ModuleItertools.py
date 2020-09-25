"""
Define a function even_or_odd, which takes an integer as input and returns the string even and odd,
if the given number is even and odd respectively.
Categorise the numbers of list n = [10, 14, 16, 22, 9, 3 , 37] into two groups namely even and odd based on above defined function.
Hint : Use groupby method of itertools module.
Iterate over the obtained groupby object and print it's group name and list of elements associated with a group.
"""

def even_or_odd(inputI):
    if(inputI%2==0):
        return "Even"
    else:
        return "Odd"

n=[10,14,16,22,9,3,37]