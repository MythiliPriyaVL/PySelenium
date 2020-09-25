#1.See if a string is a pal-in-drome
strInput = input("Enter the String to check if it is a Palindrome: ")

revString = ""
for i in strInput:
    revString = i + revString

# Printing elements in reverse using slice operation
# slicing - list[start:end:step]
#2. revString = strInput[::-1]

#Reversed function returns the list of characters in reversed order
#Join function joins the list to a single string
#3. revString = ''.join(reversed(strInput))

if(strInput==revString):
    print("Given string is a Palindrome")
else:
    print("Not a Palindrome")
