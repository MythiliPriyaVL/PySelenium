"""
Comprehensions can be nested to create combinations of lists, dictionaries, and sets within a collection.

For example, say a climate laboratory is tracking the high temperature in five different cities for the first week of June.
The perfect data structure for storing this data could be a Python list comprehension nested within a dictionary comprehension.
"""

cities = ['Austin', 'Tacoma', 'Topeka', 'Sacramento', 'Charlotte']
temps = {city: [0 for _ in range(7)] for city in cities}
print(temps)


#Nested lists are a common way to create matrices, which are often used for mathematical purposes.
matrix = [[i for i in range(5)] for _ in range(6)]
print(matrix)


#Flattening nested lists, where the logic arguably makes your code more confusing.
matrix = [[0, 0, 0],[1, 1, 1],[2, 2, 2]]
flat = [num for row in matrix for num in row]
print(flat)

#Use for loops to flatten the same matrix
matrix = [[0, 0, 0],[1, 1, 1],[2, 2, 2]]
flat = []
for row in matrix:
    for num in row:
        flat.append(num)
print(flat)