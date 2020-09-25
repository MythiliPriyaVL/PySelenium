#List Comprehensions Exercise
"""
Convert the entire string zenPython into a list of words.
Capture the words in the list, words.(Hint: Use split method of strings.)
Print the length of list, words.

Now, remove the word separating characters (such as , . - * ! and space) from each of the word, present in list words.
Store the obtained result again in the list words.(Hint: Use List comprehensions and strip method of strings.)
Print the 3rd indexed element of list, words.

Convert all the words of list words to lower case.
Store the obtained result again in the list words.(Hint: Use list comprehensions and lower method of strings.)
Print the 3rd indexed element of list, words

Determine the unique set of words from the list words.
Store obtained unique words in the list unique_words.(Hint: Use set function)
Print length of list unique_words.

Calculate the frequency of each identified unique word in the list, words and store the result in the dictionary word_frequency.
(Hint: Use dictionary comprehensions and count method of lists.)
Print the frequency of word the

Create the dictionary frequent_words, which filter words having frequency greater than five from word_frequency.
Finally print the length of dictionary frequent_words.(Hint : Use Dictionary comprehensions)
"""
zenPython = ''' 
The Zen of Python, by Tim Peters 

Beautiful is better than ugly. 
Explicit is better than implicit. 
Simple is better than complex. 
Complex is better than complicated. 
Flat is better than nested.
Sparse is better than dense. 
Readability counts. 
Special cases aren't special enough to break the rules. 
Although practicality beats purity. 
Errors should never pass silently. 
Unless explicitly silenced. 
In the face of ambiguity, refuse the temptation to guess. 
There should be one-- and preferably only one --obvious way to do it. 
Although that way may not be obvious at first unless you're Dutch. 
Now is better than never. 
Although never is often better than *right* now. 
If the implementation is hard to explain, it's a bad idea. 
If the implementation is easy to explain, it may be a good idea.
'''

#words1 = zenPython.replace("\n", " ")
words = list(zenPython.split(" "))
print(len(words))
words = [i.strip(",.-*! \n") for i in words] # Using List Comprehensions checking each word and stripping the characters given
print(words[4])
words = [i.lower() for i in words] # Using List Comprehensions converting each word to its lower case
print(words[4])
unique_words = set(words) #Set() gives the unique set of words present in the list
print(len(unique_words))
word_frequency = {w:words.count(w) for w in words} # Creating a Dictionary with Key:Value pair, Word:Word_Count
print(word_frequency["the"])
frequent_words = {w for w in word_frequency if word_frequency[w]>5} # Dictionary Comprehension with conditional statement
print(len(frequent_words))