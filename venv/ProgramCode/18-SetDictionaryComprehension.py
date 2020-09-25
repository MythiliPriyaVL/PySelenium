#The difference from List comprehensions is that set comprehensions make sure the output contains no duplicates.
#Unlike lists, sets don’t guarantee that items will be saved in any particular order.

quote = "life, uh, finds a way"
unique_vowels = {i for i in quote if i in 'aeiou'}
print(unique_vowels)
#O/P: {'a', 'e', 'u', 'i'}


squares = {i: i * i for i in range(10)}
print(squares)
#O/P: {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81}