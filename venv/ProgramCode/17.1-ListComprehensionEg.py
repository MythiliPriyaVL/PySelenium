#Every list comprehension can be rewritten in for loop, but every for loop can’t be rewritten in the form of list comprehension.

#Example 1: Iterating through a string Using for Loop
h_letters = []
for letter in 'human':
    h_letters.append(letter)
print(h_letters)
#O/P: ['h', 'u', 'm', 'a', 'n']

#Example 2: Iterating through a string Using List Comprehension
h_letters = [ letter for letter in 'human' ]
print( h_letters)
#O/P: ['h', 'u', 'm', 'a', 'n']

#Example 3: Using Lambda functions inside List
letters = list(map(lambda x: x, 'human'))
print(letters)
#O/P: ['h','u','m','a','n']

#Example 4: Using if with List Comprehension
number_list = [ x for x in range(20) if x % 2 == 0]
print(number_list)
#O/P: [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]

#Example 5: Nested IF with List Comprehension
num_list = [y for y in range(100) if y % 2 == 0 if y % 5 == 0]
print(num_list)
#O/P: [0, 10, 20, 30, 40, 50, 60, 70, 80, 90]

#Example 6: if...else With List Comprehension
obj = ["Even" if i%2==0 else "Odd" for i in range(10)]
print(obj)
#O/P: ['Even', 'Odd', 'Even', 'Odd', 'Even', 'Odd', 'Even', 'Odd', 'Even', 'Odd']


#Example 7: Transpose of Matrix using Nested Loops
transposed = []
matrix = [[1, 2, 3, 4], [4, 5, 6, 8]]

for i in range(len(matrix[0])):
    transposed_row = []

    for row in matrix:
        transposed_row.append(row[i])
        #print(transposed_row)
    transposed.append(transposed_row)

print(transposed)
#O/P: [[1, 4], [2, 5], [3, 6], [4, 8]]


#Example 8: Transpose of a Matrix using List Comprehension
matrix = [[1, 2], [3,4], [5,6], [7,8]]
transpose = [[row[i] for row in matrix] for i in range(len(matrix[0]))] # Seems tricky, need more insight and practise
print (transpose)
#O/P: [[1, 3, 5, 7], [2, 4, 6, 8]]