"""
Choose Generators for Large Datasets

A list comprehension in Python works by loading the entire output list into memory.
For small or even medium-sized lists, this is generally fine.

If you wanted to sum the squares of the first billion integers?
If you tried list comprehension on your machine, then you may notice that your computer becomes non-responsive.
That’s because Python is trying to create a list with one billion integers, which consumes more memory than your computer would like.

A generator doesn’t create a single, large data structure in memory, but instead returns an iterable.
Your code can ask for the next value from the iterable as many times as necessary or until you’ve reached the end of your sequence,
while only storing a single value at a time.
"""

#List Comprehension
print(sum([i * i for i in range(1000)]))

#Generator
print(sum(i * i for i in range(1000000)))

#using map
print(sum(map(lambda i: i*i, range(1000000))))